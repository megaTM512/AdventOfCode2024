nums1, nums2 = [],[]

with open("input.txt", "r") as input_file:
    for line in input_file:
        num1, num2 = map(int, line.split())
        nums1.append(num1)
        nums2.append(num2)

print(sum([abs(x-y) for x,y in zip(sorted(nums1),sorted(nums2))]))
