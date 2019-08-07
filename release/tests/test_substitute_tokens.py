from release.scripts.substitute_tokens import *
import unittest

class test_subtitute_tokens(unittest.TestCase):
    def test_subtitute1(self):
        originalText = "$(ep_num) is the best episode"
        changedText = "03 is the best episode"
        swapDict = {"ep_num": "03"}
        self.assertEqual(changedText, substitute(originalText, swapDict))


if __name__ == '__main__':
    unittest.main()