import unittest
from unittest.mock import patch

from crawler import command_line, crawl
from storage import storage_stack


class TestCrawl(unittest.TestCase):
    @patch('requests.get')
    def test_crawl(self, mock_get):
        
        with self.subTest('When crawl is successful'):
            mock_get.return_value.text = """
            <html>
                <body>
                    <a href="/link1">Link 1</a>
                    <img src="/image1" />
                    <a href="/link2">Link 2</a>
                    <img src="/image2" />
                </body>
            </html>"""

            crawl('http://example.com', 0, 2)
            result = storage_stack.stack
            self.assertEqual(result, [
                {'imageURL': '/image1', 'sourceURL': 'http://example.com', 'depth': 1},
                {'imageURL': '/image2', 'sourceURL': 'http://example.com', 'depth': 1},
                {'imageURL': '/image1', 'sourceURL': '/link1', 'depth': 2},
                {'imageURL': '/image2', 'sourceURL': '/link1', 'depth': 2},
                {'imageURL': '/image1', 'sourceURL': '/link2', 'depth': 2},
                {'imageURL': '/image2', 'sourceURL': '/link2', 'depth': 2},
            ])
        
        with self.subTest('When crawl is not successful'):
            # Empty the previous result and make new requests
            storage_stack.stack = []
            mock_get.side_effect = Exception("Request failed")
            crawl('http://example.com', 0, 2)
            result = storage_stack.stack
            self.assertEqual(result, [])

    @patch('crawler.crawl')
    @patch('sys.argv', ['crawler.py', 'http://example.com', '2'])
    def test_command_line(self, mock_crawl):
        command_line()
        mock_crawl.assert_called_with('http://example.com', -1, 2)
        self.assertEqual(storage_stack.stack, [])


if __name__ == '__main__':
    unittest.main()
