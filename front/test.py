import unittest
from unittest.mock import patch

from requests import Timeout

from main import create_account, get_balance, credit, transfer, get_account_data, interest


class CreateAccount(unittest.TestCase):
    @patch('main.requests')
    def test_should_create_normal_account(self, mock_requests):
        mock_requests.post.side_effect = Timeout
        with self.assertRaises(Timeout):
            create_account(1, "normal")
            mock_requests.post.assert_called_once()

    @patch('main.requests')
    def test_should_create_bonus_account(self, mock_requests):
        mock_requests.post.side_effect = Timeout
        with self.assertRaises(Timeout):
            create_account(1, "bonus")
            mock_requests.post.assert_called_once()

    @patch('main.requests')
    def test_should_create_saving_account(self, mock_requests):
        mock_requests.post.side_effect = Timeout
        with self.assertRaises(Timeout):
            create_account(1, "saving")
            mock_requests.post.assert_called_once()


class GetBalance(unittest.TestCase):
    @patch('main.requests')
    def test_get_balance(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_balance(1)
            mock_requests.get.assert_called_once()


class Credit(unittest.TestCase):
    @patch('main.requests')
    def test_credit(self, mock_requests):
        mock_requests.put.side_effect = Timeout
        with self.assertRaises(Timeout):
            credit(1, 10)
            mock_requests.put.assert_called_once()

    @patch('main.requests')
    def test_negative_credit(self, mock_requests):
        mock_requests.put.side_effect = Timeout
        with self.assertRaises(Timeout):
            credit(1, -10)
            mock_requests.put.assert_called_once()

    @patch('main.requests')
    def test_bonus_credit(self, mock_requests):
        mock_requests.put.side_effect = Timeout
        with self.assertRaises(Timeout):
            credit(2, 10)
            mock_requests.put.assert_called_once()


class Transfer(unittest.TestCase):
    @patch('main.requests')
    def test_transfer(self, mock_requests):
        mock_requests.post.side_effect = Timeout
        with self.assertRaises(Timeout):
            transfer(1, 2, 10)
            mock_requests.post.assert_called_once()

    @patch('main.requests')
    def test_negative_transfer(self, mock_requests):
        mock_requests.post.side_effect = Timeout
        with self.assertRaises(Timeout):
            transfer(1, 2, 10)
            mock_requests.post.assert_called_once()

    @patch('main.requests')
    def test_bonus_transfer(self, mock_requests):
        mock_requests.post.side_effect = Timeout
        with self.assertRaises(Timeout):
            transfer(1, 2, 10)
            mock_requests.post.assert_called_once()


class AccountData(unittest.TestCase):
    @patch('main.requests')
    def test_account_data(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_account_data(1)
            mock_requests.get.assert_called_once()


class Interest(unittest.TestCase):
    @patch('main.requests')
    def test_interest(self, mock_requests):
        mock_requests.put.side_effect = Timeout
        with self.assertRaises(Timeout):
            interest(1, 2)
            mock_requests.put.assert_called_once()


if __name__ == '__main__':
    unittest.main()
