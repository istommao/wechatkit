"""Resource test module."""

from unittest import TestCase
from unittest.mock import patch

from wechatkit.resource import ResourceAPI


class ResourceAPITest(TestCase):
    """ResourceAPITest test case."""

    def setUp(self):
        """Init setup."""

    def tearDown(self):
        """Tear down."""

    @patch('wechatkit.utils.RequestUtil.upload')
    def test_upload(self, mock_data):
        """Test upload method."""
        data = {
            'type': 'python',
            'media': '1123456789',
            'created_at': '1234567890'
        }
        mock_data.return_value = data
        resp = ResourceAPI.upload(
            './tests/test_resource.py', 'token', 'python')

        self.assertEqual(resp, data)

    def test_upload_no_media(self):
        """Test upload meida not exists."""
        resp = ResourceAPI.upload('None', 'token', 'python')

        self.assertFalse(resp)

    def test_upload_no_support(self):
        """Test not support upload type."""
        resp = ResourceAPI.upload(
            './tests/test_resource.py', 'token', 'ptyhon', 'test')

        self.assertFalse(resp)
