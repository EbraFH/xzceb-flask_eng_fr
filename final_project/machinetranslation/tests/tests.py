import unittest
import translator

class TestE2FTranslator(unittest.TestCase):
    def runTest(self):
        self.assertEqual(translator.english_to_french(
            None), "", "failed to translate correct")
        self.assertEqual(translator.english_to_french('Hello'),
                         "Bonjour", "failed to translate correct")


class TestF2ETranslator(unittest.TestCase):
    def runTest(self):
        self.assertEqual(translator.french_to_english(
            None), "", "failed to translate correct")
        self.assertEqual(translator.french_to_english("Bonjour"),
                         "Hello", "failed to translate correct")


unittest.main()