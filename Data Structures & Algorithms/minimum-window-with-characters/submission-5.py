class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        res, res_len = [-1, -1], float('infinity')
        need_frequency = {}
        have_frequency = {}
        l = 0

        for i in t:
            need_frequency[i] = 1 + need_frequency.get(i, 0)
        have, need = 0, len(need_frequency)

        for r in range(len(s)):
            c = s[r]
            have_frequency[c] = 1 + have_frequency.get(c, 0)

            if(c in need_frequency and have_frequency[c] == need_frequency[c]):
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                have_frequency[s[l]] -= 1

                if(s[l] in need_frequency and need_frequency[s[l]] > have_frequency[s[l]]):
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l : r + 1] if res_len != float('infinity') else ""