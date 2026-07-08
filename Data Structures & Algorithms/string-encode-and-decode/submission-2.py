class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str((len(i))) + "#"
            encoded += i
        print(encoded)
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        ind = 0
        while ind < len(s):
            end_ind = ind
            while s[end_ind] != "#":
                end_ind +=1
            length = int(s[ind:end_ind])
            decoded.append(s[(end_ind +1):(length + end_ind + 1)])
            ind = end_ind + 1 + length
            print(ind)
        return decoded