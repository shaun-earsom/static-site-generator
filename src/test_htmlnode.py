import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from htmlnode import text_node_to_html_node
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_props2html(self):
        node = HTMLNode("a", "This link", None, {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_leafnodeblock(self):
        node = LeafNode("p", "This is a test.", None)
        result = node.to_html()
        
        self.assertEqual(result, "<p>This is a test.</p>")

    def test_leafnodehref(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()

        self.assertEqual(result, '<a href="https://www.google.com">Click me!</a>')
    
    def test_parentnode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        result = node.to_html()
        self.assertEqual(result, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_text2htmlText(self):
        node = TextNode("This is normal text", "text")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode(None, "This is normal text", None))
    
    def test_text2htmlBold(self):
        node = TextNode("This is normal text", "bold")
        node2 = text_node_to_html_node(node)
        self.assertNotEqual(node2, "<b>This is normal text</b>")
    
    def test_text2htmlItalic(self):
        node = TextNode("This is normal text", "italic")
        node2 = text_node_to_html_node(node)
        self.assertNotEqual(node2, "<i>This is normal text</i>")
    
    def test_text2htmlcode(self):
        node = TextNode("This is normal text", "link", "https://www.google.com")
        node2 = text_node_to_html_node(node)
        print(node2)
        self.assertNotEqual(node2, "This is normal text</p>")


if __name__ == "__main__":
    unittest.main()