# python3
import sys

def check_brackets(text: str):
    stack = []
    
    for i, char in enumerate(text):
        if char in "([{":
            stack.append((char, i + 1))
        elif char in ")]}":
            if not stack:
                return i + 1
            
            top_char, _ = stack.pop()
            if (top_char == '(' and char != ')') or \
               (top_char == '[' and char != ']') or \
               (top_char == '{' and char != '}'):
                return i + 1
                
    if stack:
        # Return 1-based index of the FIRST unmatched opening bracket
        return stack[0][1]
        
    return "Success"

if __name__ == "__main__":
    text = sys.stdin.read().rstrip('\r\n')
    print(check_brackets(text))