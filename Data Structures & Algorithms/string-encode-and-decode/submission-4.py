class Solution:

    def encode(self, strs):
        l=len(strs)
        out=""
        if l==0:
            return ""
        elif l>100:
            return None
        else:
            for st in strs:
                le=len(st)
                out+=st+"`"
            return out

    def decode(self, s):
        if not s:
            return []
        else:
            start=0
            char=0
            li=[]
            print(s)
            for i in range(len(s)):
                if s[i]=="`":
                    li.append(s[start:start+char])
                    char=0
                    start=i+1
                else:
                    char+=1
        return li  

