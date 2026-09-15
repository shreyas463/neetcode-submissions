class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            j = i

            # Move j until it finds #
            while s[j] != "#":
                j += 1

            # Get the number before #
            word_length = int(s[i:j])

            # Word starts after #
            word_start = j + 1

            # Word ends after word_length characters
            word_end = word_start + word_length

            # Extract the word
            word = s[word_start:word_end]

            decoded_string.append(word)

            # Move i to the next encoded word
            i = word_end

        return decoded_string