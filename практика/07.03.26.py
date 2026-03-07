data =  [0, 1, 0, 3, 12]

def moveZeroes(data):
    
    for i in range(len(data)):
        if data[i] == 0:
            data.pop(i)
            data.append(0)
    return data

print(moveZeroes(data))

nums = [1,2,3,4]
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    return nums

print(runningSum(nums))