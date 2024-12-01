# Input Parsing
nums1, nums2 = [],[]
with open("input.txt", "r") as input_file:
    for line in input_file:
        num1, num2 = map(int, line.split())
        nums1.append(num1)
        nums2.append(num2)
        
# Counting the Occurences
similars = {num : 0 for num in nums1}
for num2 in nums2:
    if num2 in similars:
        similars[num2] += 1

# Summing them up!
total = sum(num * count for num, count in similars.items())

print(total)