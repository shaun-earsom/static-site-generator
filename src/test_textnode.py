import unittest

from textnode import TextNode
from textnode import text_node_to_html_node
from textnode import split_nodes_delimiter
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Test of eq Override.", "bold")
        node2 = TextNode("Test of eq Override.", "bold")
        self.assertEqual(node, node2)
    
    def test_nourl(self):
        node = TextNode("Test of no url", "bold")
        self.assertEqual(node.url, None)

    def test_difftext(self):
        node = TextNode("Test of different text", "bold")
        node2 = TextNode("And yet, text is different text", "bold")
        self.assertNotEqual(node, node2)
    
    def test_text2htmlText(self):
        node = TextNode("Test of text to HTML", "text")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode(None, "Test of text to HTML", None))
    
    def test_text2htmlBold(self):
        node = TextNode("Test of bold text", "bold")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode("b", "Test of bold text"))
    
    def test_text2htmlItalic(self):
        node = TextNode("Test of Italic text.", "italic")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode("i", "Test of Italic text."))
    
    def test_text2htmlcode(self):
        node = TextNode("Test of text code.", "code")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode("code", "Test of text code."))

    def test_text2htmlLink(self):
        node = TextNode("Test of HTML link", "link", "https://www.google.com")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode("a", "Test of HTML link", {"href": "https://www.google.com"}))

    def test_text2htmlImg(self):
        node = TextNode("cow", "image", "https://www.cows.com/cow.gif")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2, LeafNode("img", "",{"src": "https://www.cows.com/cow.gif", "alt": "cow"}))
    
    def test_splitNodeDelimBld(self):
        node = TextNode("This is **bold** text.", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(new_nodes, [TextNode("This is ", "text"), TextNode("bold", "bold"), TextNode(" text.", "text")])

if __name__ == "__main__":
    unittest.main()
