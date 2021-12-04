from unittest import TestCase
from mojibake.tests.common import get_path
from mojibake import compare_diffrences, get_all_files

class TestDiff(TestCase):
    testpath = ""
    expected_fails = 0
    def setUp(self) -> None:
        self.testpath = get_path(__file__, "./test_data/")
        for file in get_all_files(self.testpath):
            # If the file startswith #FAIL than this file should produce
            # output for `compare_diffrences`
            if open(file).readlines()[0].startswith("#FAIL"):
                self.expected_fails += 1

    def test_compare_func(self):
        self.assertEqual(
                self.expected_fails,
                len(list(compare_diffrences(
                    get_path(__file__, "./test_data"), 
                    "utf8", 
                    "Windows-1254"
                ))
            )
        )

    def test_ignored_files(self):
        for file in get_all_files(self.testpath):
            self.assertEqual(
                    False,
                    open(file).readlines()[0].startswith("#Ignore")
            )

