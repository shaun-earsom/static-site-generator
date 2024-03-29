import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props2html(self):
        node = HTMLNode("<a>", "This link", None, {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()