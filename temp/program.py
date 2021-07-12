def longestPalindromicSubstring(string):
    # Write your code here
    longest = [0, 1]
    for i in range(1, len(string)):
        odd = getPalindrome(i-1, i+1, string)
        even = getPalindrome(i-1, i, string)
        longestCurrentPalindrome = max(odd, even, key=lambda x: x[1]-x[0])
        longest = max(longest, longestCurrentPalindrome,
                      key=lambda x: x[1]-x[0])
    return string[longest[0]:longest[1]]


def getPalindrome(left, right, string):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1

    return [left + 1, right]
