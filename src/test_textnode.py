import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_initialization(self):
        node = TextNode("Sample text", TextType.NORMAL, "https://example.com")
        self.assertEqual(node.text, "Sample text")
        self.assertEqual(node.text_type, TextType.NORMAL)
        self.assertEqual(node.url, "https://example.com")
    
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
    
    def test_repr(self):
        node = TextNode("Test text", TextType.CODE, "https://example.com")
        expected_repr = "TextNode(text='Test text', text_type=<TextType.CODE: 'code'>, url='https://example.com')"
        self.assertEqual(repr(node), expected_repr)
    
    def test_none_url(self):
        node = TextNode("Text without URL", TextType.NORMAL)
        self.assertIsNone(node.url)
    
    def test_neq_different_type(self):
        node = TextNode("Text", TextType.NORMAL)
        self.assertNotEqual(node, "Text")  # Ensures inequality with non-TextNode types

if __name__ == "__main__":
    unittest.main()
