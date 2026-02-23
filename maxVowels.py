s = "abciiidef"
k = 3

def maxVowelCounter(s, k):

    vowelCount = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # First window
    for i in range(k):
        if s[i] in vowels:
            vowelCount += 1

    maxVowels = vowelCount

    # Slide the window
    for right in range(k, len(s)):

        # Subtract if left char was vowel
        if s[right - k] in vowels:
            vowelCount -= 1

        # Add if new right char is vowel
        if s[right] in vowels:
            vowelCount += 1

        maxVowels = max(maxVowels, vowelCount)

    return maxVowels

print(maxVowelCounter(s, k))