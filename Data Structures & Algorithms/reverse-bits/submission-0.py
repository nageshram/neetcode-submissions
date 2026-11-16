class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            if n & (1 << i): #the ith bit of n is 1 then append 1 else 0
                binary += "1"
            else:
                binary += "0"

        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= (1 << i)

        return res