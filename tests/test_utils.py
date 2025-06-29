import unittest
from healthai_core.utils import clean_text, format_response

class TestUtils(unittest.TestCase):

    def test_clean_text_removes_whitespace(self):
        text = "  Hello \n World!  "
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "Hello World!")

    def test_format_response_basic(self):
        response = "Line1\nLine2\n\nLine3"
        formatted = format_response(response)
        self.assertIn("Line1", formatted)
        self.assertIn("Line2", formatted)
        self.assertIn("Line3", formatted)

if __name__ == '__main__':
    unittest.main()
