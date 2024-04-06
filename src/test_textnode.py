import unittest
from textnode import TextNode


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

if __name__ == "__main__":
    unittest.main()
