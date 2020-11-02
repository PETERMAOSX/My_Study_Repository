def solution(nums):
    left = 0
    right = 0
    while right < len(nums) - 1:
        if nums[left] == 0:
            nums[left:-1] = nums[left+1:]
            nums[-1] = 0
            right += 1
        else:
            right+=1
            left +=1
myList = [0,1,0,3,12]
solution(myList)
print(myList)