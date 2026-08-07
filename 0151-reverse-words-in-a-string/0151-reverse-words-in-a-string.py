class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)

        # Step 1: Reverse the entire list
        self.reverse(chars, 0, n - 1)

        # Step 2: Reverse each word and compact spaces
        write = 0
        i = 0
        while i < n:
            if chars[i] != ' ':
                # Add space between words
                if write > 0:
                    chars[write] = ' '
                    write += 1

                # Copy and track word boundaries
                word_start = write
                while i < n and chars[i] != ' ':
                    chars[write] = chars[i]
                    write += 1
                    i += 1

                # Reverse the word we just wrote
                self.reverse(chars, word_start, write - 1)
            else:
                i += 1

        return ''.join(chars[:write])

    def reverse(self, chars: list, left: int, right: int) -> None:
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1