import unittest
from executive_assistant_ai.assistant import Assistant

class TestAssistant(unittest.TestCase):

    def setUp(self):
        self.assistant = Assistant()

    def test_init(self):
        self.assertIsNotNone(self.assistant)

    def test_run(self):
        self.assistant.run()
        self.assertTrue(self.assistant.is_running)

    def test_setup(self):
        self.assistant.setup()
        self.assertTrue(self.assistant.is_setup)

    def test_clean(self):
        self.assistant.clean()
        self.assertTrue(self.assistant.is_clean)

    def test_validate(self):
        self.assistant.validate()
        self.assertTrue(self.assistant.is_valid)

    def test_log(self):
        self.assistant.log("Test log message")
        self.assertIn("Test log message", self.assistant.log_messages)

    def test_enhance(self):
        self.assistant.enhance()
        self.assertTrue(self.assistant.is_enhanced)

    def test_humanize(self):
        self.assistant.humanize()
        self.assertTrue(self.assistant.is_humanized)

if __name__ == '__main__':
    unittest.main()