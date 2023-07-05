import unittest
from executive_assistant_ai.utils import data_cleaner, data_validator, error_handler, logger, ai_enhancer, humanizer

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.data_cleaner = data_cleaner.DataCleaner()
        self.data_validator = data_validator.DataValidator()
        self.error_handler = error_handler.ErrorHandler()
        self.logger = logger.Logger()
        self.ai_enhancer = ai_enhancer.AIEnhancer()
        self.humanizer = humanizer.Humanizer()

    def test_data_cleaner(self):
        dirty_data = {"name": " John Doe ", "email": " johndoe@gmail.com "}
        cleaned_data = self.data_cleaner.clean(dirty_data)
        self.assertEqual(cleaned_data, {"name": "John Doe", "email": "johndoe@gmail.com"})

    def test_data_validator(self):
        valid_data = {"name": "John Doe", "email": "johndoe@gmail.com"}
        self.assertTrue(self.data_validator.validate(valid_data))

    def test_error_handler(self):
        with self.assertRaises(Exception):
            self.error_handler.handle("Test error")

    def test_logger(self):
        self.assertIsNone(self.logger.log("Test log"))

    def test_ai_enhancer(self):
        basic_response = "Hello, how can I assist you today?"
        enhanced_response = self.ai_enhancer.enhance(basic_response)
        self.assertNotEqual(basic_response, enhanced_response)

    def test_humanizer(self):
        basic_response = "Hello, how can I assist you today?"
        humanized_response = self.humanizer.humanize(basic_response)
        self.assertNotEqual(basic_response, humanized_response)

if __name__ == '__main__':
    unittest.main()