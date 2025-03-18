import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_initialization(self):
        node = HTMLNode(tag="div", value="Hello, world!", children=[], props={"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})
    
    def test_props_to_html_with_props(self):
        node = HTMLNode(props={"class": "btn", "id": "submit-button"})
        self.assertEqual(node.props_to_html(), ' class="btn" id="submit-button"')
    
    def test_props_to_html_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_repr(self):
        node = HTMLNode(tag="p", value="Test paragraph", children=[HTMLNode()], props={"style": "color: red;"})
        expected_repr = "HTMLNode(tag=p, value=Test paragraph, children=1, props={'style': 'color: red;'})"
        self.assertEqual(repr(node), expected_repr)
    
    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="div")
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
