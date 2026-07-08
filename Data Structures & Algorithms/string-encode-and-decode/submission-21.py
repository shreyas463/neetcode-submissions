from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word

        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0

        while i < len(s):
            # j searches for the "#" delimiter
            j = i

            while s[j] != "#":
                j += 1

            # Everything from i up to j is the word's length
            word_length = int(s[i:j])

            # The actual word starts immediately after "#"
            word_start = j + 1
            word_end = word_start + word_length

            # Extract and store the word
            word = s[word_start:word_end]
            decoded_strings.append(word)

            # Move i to the start of the next encoded word
            i = word_end

        return decoded_strings