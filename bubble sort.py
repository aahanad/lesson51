nums=[4,1,5,7,2,3,6,8]

def sort(nums):
    n=len(nums)
    swapped=True
    while swapped==True:
        swapped=False
        for i in range(1,n-1):
            if nums[i-1]>nums[i]:
                temp=nums[i]
                nums[i]=nums[i-1]
                nums[i-1]=temp
                swapped=True
                print(nums)
    return nums
print(sort(nums))            
           
