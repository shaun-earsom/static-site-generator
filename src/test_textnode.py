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

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual([TextNode("This is text with a ", "text"), TextNode("bolded", "bold"), TextNode(" word", "text")], new_nodes)

    def test_delim_bold_double(self):
        node = TextNode("This is text with a **bolded** word and **another**", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual([TextNode("This is text with a ", "text"), TextNode("bolded", "bold"), TextNode(" word and ", "text"), TextNode("another", "bold")], new_nodes)

    def test_delim_bold_multiword(self):
        node = TextNode("This is text with a **bolded word** and **another**", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual([TextNode("This is text with a ", "text"), TextNode("bolded word", "bold"), TextNode(" and ", "text"), TextNode("another", "bold")], new_nodes)

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
