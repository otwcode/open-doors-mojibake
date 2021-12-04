from unittest import TestCase
from mojibake.tests.common import get_path
from mojibake import detect_encodings_in_dir

class TestDetector(TestCase):
    testpath = ""
    def setUp(self) -> None:
        self.testpath = get_path(__file__, "./test_data/")

    def test_detector_result_num(self):
        self.assertTrue(
            len(detect_encodings_in_dir(self.testpath)) > 1 
        )

