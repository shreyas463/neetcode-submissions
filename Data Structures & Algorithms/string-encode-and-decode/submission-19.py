class Solution:

    def encode(self, strs: List[str]) -> str:
        res="" #list of string
        for s in strs:
            res+=str(len(s)) + "#" + s ## store each string as "length#string"
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [],0 #[single string],#i is the first pointer
        while i<len(s):
            j=i #delimiter j
            while s[j]!="#":
                j+=1 #keep moving j
            length=int(s[i:j]) # convert substring s[i:j] into integer (this is the length of the word)
            res.append(s[j+1:j+1+length]) #extract the actual word of that length after '#' we did j+1+length becuase we want until where the word ends
            i=j+1+length #move i forward to the next number, which tells us the length of the next word.
        return res

