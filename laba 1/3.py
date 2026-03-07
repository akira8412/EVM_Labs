s = " "

k = ''
cnt = 0
for char in s: 
    if char not in k:
        k += char
    else:
        cnt = max(cnt, len(k))
        idx = k.index(char)
        k = k[idx + 1:] + char
max_len = max(cnt, len(k))

print(max_len)
