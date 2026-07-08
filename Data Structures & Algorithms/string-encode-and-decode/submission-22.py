class Solution:
#length#word
    def encode(self, strs: List[str]) -> str:
        encoded_word= ""
        for word in strs:
            encoded_word += str(len(word)) + "#" + word
        return encoded_word
# 5#Hello5#world -> hello, world
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i=0
        
        while i<len(s):
            j=i

            while s[j]!="#":
                j+=1
            
            word_length=int(s[i:j])
            word_starts=j+1

            word_end=word_starts + word_length

            word=s[word_starts:word_end]

            decoded_string.append(word)

            i=word_end

        return decoded_string



