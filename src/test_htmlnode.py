import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("a", "visit", None, {"href": "https:www.google.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "visit")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https:www.google.com"})

    def test_repr(self):
        node = HTMLNode("a", "visit", None, {"href": "https:www.google.com"})
        result = """HTMLNode(
    tag:a,
    value:visit,
    children:None,
    props:{'href': 'https:www.google.com'})"""
        self.assertEqual(repr(node), result)

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), result)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_props(self):
        node = LeafNode("a", "Hello", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello</a>')


if __name__ == "__main__":
    unittest.main()
