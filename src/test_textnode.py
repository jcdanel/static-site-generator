import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_identical_nodes_are_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_nodes_with_different_types_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.text, node2.text)
        self.assertNotEqual(node, node2)

    def test_nodes_with_different_urls_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.pepe.gov")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertEqual(node.text, node2.text)
        self.assertEqual(node.text_type.value, node2.text_type.value)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()