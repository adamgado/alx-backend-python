#!/usr/bin/env python3
""" Parameterize and patch as decorators
"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test Org Client"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, name, mock):
        """test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(name)
        test_class.org()
        mock.called_with_once(test_class.ORG_URL.format(org=name))

    def test_public_repos_url(self):
        """unit-test GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "something"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test the list of repos from the chosen payload"""
        payloads = [{"name": "google"}, {"name": "Twitter"}]
        mock_json.return_value = payloads

        with patch('client.GithubOrgClient._public_repos_url') as mock_public:
            mock_public.return_value = "test"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            correct = [a["name"] for a in payloads]
            self.assertEqual(result, correct)

            mock_json.called_with_once()
            mock_public.called_with_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, correct):
        """unit-test GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license)
        self.assertEqual(result, correct)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integeration test for Fixtures
    """
    @classmethod
    def setUpClass(a):
        """return example payloads found in the fixtures"""
        config = {"return_value.json.side_effect": [
            a.org_payload, a.repos_payload,
            a.org_payload, a.repos_payload
        ]}

        a.get_patcher = patch('requests.get', **config)
        a.mock = a.get_patcher.start()

    @classmethod
    def tearDownClass(a):
        """stop the patcher"""
        a.get_patcher.stop()
