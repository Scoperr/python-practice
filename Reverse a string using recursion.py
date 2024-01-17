class reverse_it:
    def reverse_string(self, s, i):
        if i < 0:
            return
        else:
            print(s[i],end="")
            self.reverse_string(s, i-1)
s = input()
ss = reverse_it()
ss.reverse_string(s,len(s)-1)
