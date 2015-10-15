__author__ = 'KoicsD'


"""
def checkio(expression):
    bras = "([{"
    kets = ")]}"
    stack = []
    for ch in expression:
        if ch in bras:
            i = bras.index(ch)
            stack.append(kets[i])
        elif ch in kets:
            if len(stack) == 0 or stack.pop() != ch:
                return False
    return len(stack) == 0
"""


def checkio(expression):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for ch in expression:
        if ch in brackets.keys():
            stack.append(brackets[ch])
        elif ch in brackets.values():
            if len(stack) == 0 or stack.pop() != ch:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("{[(3+1)+2]+}]") == False, "Too many kets"