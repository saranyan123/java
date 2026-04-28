class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return ""
        
        # Create a combined string: original + separator + reverse
        # The separator '#' ensures we don't match across the boundary
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        
        # Build the KMP LPS (Longest Prefix Suffix) table
        n = len(combined)
        lps = [0] * n
        
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
            
        # lps[-1] is the length of the longest prefix of s that is a palindrome
        pal_len = lps[-1]
        
        # Add the reverse of the remaining suffix to the front
        return rev_s[:len(s) - pal_len] + s
