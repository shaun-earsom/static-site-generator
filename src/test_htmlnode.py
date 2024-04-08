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
        self.assertEqual(node2, LeafNode("b", "This is normal text"))
    
    def test_text2htmlItalic(self):
        node = TextNode("This is normal text", "italic")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode("i", "This is normal text"))
    
    def test_text2htmlcode(self):
        node = TextNode("This is normal text", "code")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode("code", "This is normal text"))

    def test_text2htmlLink(self):
        node = TextNode("Anchor text here", "link", "https://www.google.com")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode("a", "Anchor text here", {"href": "https://www.google.com"}))

    def test_text2htmlImg(self):
        node = TextNode("cow", "image", "https://www.cows.com/cow.gif")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode("img", "",{"src": "https://www.cows.com/cow.gif", "alt": "cow"}))


if __name__ == "__main__":
    unittest.main()