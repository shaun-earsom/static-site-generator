import unittest

from textnode import TextNode
from textnode import text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_nourl(self):
        node = TextNode("This is a test node", "bold")
        self.assertEqual(node.url, None)

    def test_difftext(self):
        node = TextNode("This is normal text", "bold")
        node2 = TextNode("Yet different text", "bold")
        self.assertNotEqual(node, node2)
    
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
