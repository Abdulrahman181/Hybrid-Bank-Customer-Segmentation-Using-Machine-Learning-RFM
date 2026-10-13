import unittest
from pathlib import Path

from scripts.validate_notebook import NOTEBOOK, validate_notebook


class NotebookStaticValidationTest(unittest.TestCase):
    def test_notebook_exists(self):
        self.assertTrue(Path(NOTEBOOK).is_file())

    def test_notebook_is_portable_and_syntax_valid(self):
        self.assertEqual(validate_notebook(), [])


if __name__ == "__main__":
    unittest.main()
