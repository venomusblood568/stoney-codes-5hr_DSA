# Question Link -> https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self,tokens: List[str]) -> int:
        st = [] 

        for c in tokens:
            if c  == "+":
                st.append(st.pop()+ st.pop())
            elif c == "-":
                second,first = st.pop(),st.pop()
                st.append(first,second)
            elif c == "*":
                st.append(st.pop() * st.pop())
            elif c == "/":
                second,first = st.pop(),st.pop()
                st.append(int(first/second))
            else:
                st.append(int(c))
        
        return st[0]
            