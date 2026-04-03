
s = "([)]"

st_open = []
flag = False
def f(s):
    for i in s:
        if i in '([{':
            st_open.append(i)
        else:
            if not st_open:
                flag = False
                break
            a = st_open.pop()
            if (i == ']' and a == '[') or (i == ')' and a == '(') or (i == '}' and a == '{'):
                flag = True
            else:
                flag = False
                break
    if len(st_open)>0:
        return False
    else:
        return flag
print(f(s))