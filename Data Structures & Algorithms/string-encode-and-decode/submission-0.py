class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            leng = len(string)
            ans+=str(leng)+"#"+string
        return(ans)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Find the separator after the length.
            j = i
            while s[j] != "#":
                j += 1

            # Convert the length field to an integer.
            length = int(s[i:j])

            # Extract the string.
            start = j + 1
            end = start + length
            result.append(s[start:end])

            # Continue from the next encoded piece.
            i = end

        return result
        
