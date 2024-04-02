import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_props2html(self):
        node = HTMLNode("a", "This link", None, {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_leafnodeblock(self):
        node = LeafNode("p", "This is a test.", None)
        result = node.to_html()
        
        self.assertEqual(result, "<p>This is a test.</p>")

    def test_lefnodehref(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()

        self.assertEqual(result, '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()