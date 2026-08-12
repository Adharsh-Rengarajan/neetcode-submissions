class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        need_frequency = {}
        
        for i in t:
            need_frequency[i] = 1 + need_frequency.get(i , 0)
        
        have_frequency = {}
        res, res_len = [-1, -1], float('infinity')
        need = len(need_frequency)
        l = 0
        have = 0

        for r in range(len(s)):
            c = s[r]

            have_frequency[c] = 1 + have_frequency.get(c, 0)

            if c in need_frequency and have_frequency[c] == need_frequency[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l  + 1
                    res = [l, r]

                have_frequency[s[l]] -= 1
                
                if s[l] in need_frequency and have_frequency[s[l]] < need_frequency[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res

        return s[l : r + 1] if res_len != float('infinity') else ""
            