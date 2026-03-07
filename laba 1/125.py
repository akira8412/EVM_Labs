s = "A man, a plan, a canal: Panama"
s = s.replace(' ', '').lower()
s1 = ''
for i in range(len(s)):
    if 97<= ord(s[i]) <=122 or (48<= ord(s[i]) <=57):
        s1+=s[i]

if s1 == s1[::-1]:
    print('true')
else:
    print('false')
