class Solution:
    def compress(self, chars: List[str]) -> int:
        
        s = ""
        l = 0

        while l < len(chars):
            
            r = l + 1
            totalChars = 1

            while r < len(chars) and chars[l] == chars[r]:

                totalChars += 1
                r += 1

            if totalChars == 1:
                s += chars[l]
            else:
                s += chars[l] + str(totalChars)

            l = r

        
        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)