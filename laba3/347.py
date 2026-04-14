nums = [1]
k = 1
d = dict()
for i in set(nums):
    d[i] = nums.count(i)

sorted_tuples = sorted(d.items(), key=lambda item: item[1], reverse=True)
sorted_dict = dict(sorted_tuples)

answ = []
k0 = 0
for j in sorted_dict:
    if k0<k:
        answ.append(j)
        k0+=1
print(answ)
