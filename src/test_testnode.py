import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = TextNode("Hello there", TextType.BOLD)
        node2 = TextNode("Hello there", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_elink(self):
        node = TextNode("General Kenobi", TextType.LINK, "www.boot.dev")
        node2 = TextNode("General Kenobi", TextType.LINK, "www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_neqlink(self):
        node = TextNode("Cry", TextType.LINK, "www.boots.dev")
        node2 = TextNode("Cry", TextType.LINK, "www.boot.dev")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
