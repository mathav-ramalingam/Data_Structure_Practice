# 1) write a function in python that can reverse a string using stack data structure

from collections import deque

# method 1 (my idealogy)
def reverse_string(string):
    stack = deque()
    res = ""

    for char in string:
        stack.append(char)

    while stack:
        res = res + stack.pop()

    return res

if __name__ == "__main__":
    input_string = input("Enter The Sting: ")
    reverse_str = reverse_string(input_string)
    print(reverse_str)


# method 2 (more optimized)
def reverse_string(string):
    stack = deque(string)
    print(stack)
    res = []

    while stack:
        res.append(stack.pop())

    return ''.join(res)

if __name__ == "__main__":
    input_string = input("Enter the string (optimized res): ")
    reverse_str = reverse_string(input_string)
    print("optimized res :"+ reverse_str)

# ----------------------------------------------------------------------------------------------------------------------------------------------


#2)  Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]".


def is_match(ch1, ch2):
    return (ch1 == "(" and ch2 == ")" ) or (ch1 == "{" and ch2 == "}" ) or (ch1 == "[" and ch2 == "]" )

def is_balanced(string):
    stack = deque()

    for ch in string:
        if ch == "{" or ch == "(" or ch == "[":
            stack.append(ch)
        elif ch == "}" or ch == ")" or ch == "]":
            if not stack or not is_match(stack.pop(), ch):
                return False

    return not stack   # True if empty, else False


if __name__ == "__main__":
    input_string = input("Enter the Expression: ")
    print("Balanced" if is_balanced(input_string) else "Not Balanced")