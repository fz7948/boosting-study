class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        while tokens:
            op = tokens.pop(0)
            if not op in "*+/-":
                s.append(op)
            else:
                n1 = int(s.pop())
                n2 = int(s.pop())
                if op == "+":
                    s.append(n1+n2)
                elif op == "-":
                    s.append(n2-n1)
                elif op == "*":
                    s.append(n1*n2)
                elif op == "/":
                    s.append(n2/n1)
        return int(s[-1])