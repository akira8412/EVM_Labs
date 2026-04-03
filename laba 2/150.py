tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["18"]
nums = []
for n in tokens:
    if n in '+/*-':
        a = int(nums.pop())
        b = int(nums.pop())
        if n == '+':
            nums.append(b+a)
            print(f'{b} + {a}')
        if n == '-':
            nums.append(b-a)
            print(f'{b} - {a}')
        if n == '*':
            nums.append(b*a)
            print(f'{b} * {a}')
        if n == '/':
            nums.append(int(b/a))
            print(f'{b} / {a}')
    else:
        nums.append(n)
print(nums[0])




        