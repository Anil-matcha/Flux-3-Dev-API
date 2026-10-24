import unittest
from unittest.mock import Mock, patch

from flux3_dev_api import DEFAULT_REQUEST_TIMEOUT, Flux3DevAPI


class RequestTimeoutTests(unittest.TestCase):
    def setUp(self):
        self.client = Flux3DevAPI(api_key="synthetic-test-key")

    @patch("flux3_dev_api.requests.post")
    def test_post_request_uses_client_timeout(self, post):
        post.return_value.json.return_value = {"request_id": "synthetic"}

        result = self.client._post_request("https://example.invalid/task", {"prompt": "synthetic"})

        self.assertEqual(result, {"request_id": "synthetic"})
        self.assertEqual(post.call_args[1]["timeout"], DEFAULT_REQUEST_TIMEOUT)

    @patch("flux3_dev_api.requests.get")
    def test_get_result_uses_explicit_timeout(self, get):
        get.return_value.json.return_value = {"status": "completed"}

        result = self.client.get_result("synthetic-id", timeout=2)

        self.assertEqual(result, {"status": "completed"})
        self.assertEqual(get.call_args[1]["timeout"], 2)

    @patch("flux3_dev_api.time.sleep")
    @patch("flux3_dev_api.time.monotonic", side_effect=[0, 0, 0.75, 1])
    def test_wait_timeout_bounds_request_and_sleep(self, monotonic, sleep):
        self.client.get_result = Mock(return_value={"status": "pending"})

        with self.assertRaises(TimeoutError):
            self.client.wait_for_completion("synthetic-id", poll_interval=5, timeout=1)

        self.assertEqual(self.client.get_result.call_args[1]["timeout"], 1)
        sleep.assert_called_once_with(0.25)

    def test_nonpositive_request_timeout_is_rejected(self):
        with self.assertRaises(ValueError):
            Flux3DevAPI(api_key="synthetic-test-key", request_timeout=0)


if __name__ == "__main__":
    unittest.main()
