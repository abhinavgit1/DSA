import unittest

class Solution:
    def mostFrequentSubstring(self, s: str) -> str:
        i = s[0]
        j= s[1]
        n=len(s)
        mydic={}
        for i in range(len(s)):
            substring = s[i:j+1]
            mydic[substring]=+1

        # TODO: Implement your logic here
        pass


class TestMostFrequentSubstring(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_case(self):
        self.assertEqual(self.sol.mostFrequentSubstring("abab"), "ab")

    def test_single_char(self):
        self.assertEqual(self.sol.mostFrequentSubstring("a"), "a")

    def test_all_unique(self):
        self.assertEqual(self.sol.mostFrequentSubstring("abc"), "a")

    def test_repeated_chars(self):
        self.assertEqual(self.sol.mostFrequentSubstring("aaaa"), "a")

    def test_multiple_max_freq(self):
        self.assertEqual(self.sol.mostFrequentSubstring("abcabc"), "a")

    def test_empty_string(self):
        self.assertEqual(self.sol.mostFrequentSubstring(""), "")

    def test_lexicographic_tiebreaker(self):
        self.assertEqual(self.sol.mostFrequentSubstring("baba"), "a")

    def test_longer_substrings(self):
        self.assertEqual(self.sol.mostFrequentSubstring("ababa"), "aba")

    def test_palindrome(self):
        self.assertEqual(self.sol.mostFrequentSubstring("racecar"), "a")

    def test_complex_case(self):
        self.assertEqual(self.sol.mostFrequentSubstring("abcabcabc"), "a")


if __name__ == "__main__":
    unittest.main()
