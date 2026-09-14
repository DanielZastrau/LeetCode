class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map: dict[str, int] = {}
        left_pointer = 0
        max_len = 0

        for right_pointer, char in enumerate(s):
            if char in char_map and char_map[char] >= left_pointer:
                left_pointer = char_map[char] + 1
            
            char_map[char] = right_pointer
            # Calculate and update the maximum length
            current_len = right_pointer - left_pointer + 1
            if current_len > max_len:
                max_len = current_len

        return max_len

    def test_cases(self):
        def test_it(string: str, expected: int):
            val = self.lengthOfLongestSubstring(string)
            assert val == expected, f"Failed for '{string}': expected {expected}, got {val}"

        # Standard tests
        test_it('mq', 2)
        test_it('bbbbb', 1)
        test_it('abcabcbb', 3)
        test_it('pwwkew', 3)
        
        # Edge cases
        test_it('', 0)
        test_it('a', 1)
        test_it('au', 2)
        test_it('dvdf', 3)
        test_it('abba', 2)
        test_it('tmmzuxt', 5)

if __name__=='__main__':
    sol = Solution()
    sol.test_cases()
