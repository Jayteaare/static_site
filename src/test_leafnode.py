import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_initialization(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph.")
        self.assertIsNone(node.children)
    
    def test_props(self):
        node = LeafNode("p", "Styled text", {"class": "text-muted"})
        self.assertEqual(node.props, {"class": "text-muted"})
    
    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)  # 'value' must not be None
        #with self.assertRaises(ValueError):
        #    LeafNode(None, "Missing tag")  # 'tag' must not be None
    
    def test_children_restriction(self):
        node = LeafNode("p", "No children allowed")
        with self.assertRaises(AttributeError):
            node.children = [HTMLNode("span", "Child")]  # LeafNode cannot have children
    
    def test_to_html(self):
        node = LeafNode("p", "Hello, world!", {"class": "greeting"})
        expected_html = '<p class="greeting">Hello, world!</p>'
        self.assertEqual(node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()