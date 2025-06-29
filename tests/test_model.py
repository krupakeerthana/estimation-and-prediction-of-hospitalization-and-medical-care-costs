import unittest
from unittest.mock import patch
from healthai_core.model import query_model

class TestModel(unittest.TestCase):

    @patch('healthai_core.model.requests.post')
    def test_query_model_success(self, mock_post):
        # Mock a successful API response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{'message': {'content': 'Mocked AI response'}}]
        }
        mock_post.return_value = mock_response

        prompt = "Test prompt"
        response = query_model(prompt)
        self.assertEqual(response, 'Mocked AI response')

    @patch('healthai_core.model.requests.post')
    def test_query_model_failure(self, mock_post):
        # Mock a failed API response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {}
        mock_post.return_value = mock_response

        prompt = "Test prompt"
        response = query_model(prompt)
        self.assertTrue("Error" in response or response is None)

if __name__ == '__main__':
    unittest.main()
