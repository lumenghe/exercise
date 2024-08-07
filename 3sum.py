"""
3Sum
Medium
Topics
Companies
Hint

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105

"""

from typing import List


class SolutionSlow:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positive, negative, zero = [], [], []
        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                zero.append(num)

        self.ret = set()
        if len(zero) >= 3:
            self.ret.add((0, 0, 0))
        if len(zero) > 0:
            for num in set(positive):
                if -num in set(negative):
                    self.ret.add((-num, 0, num))

        def search(list1, list2):
            for i in range(len(list1)):
                for j in range(i + 1, len(list1)):
                    target = -(list1[i] + list1[j])
                    if target in set(list2):
                        temp = tuple(sorted([list1[i], list1[j], target]))
                        self.ret.add(temp)

        search(positive, negative)
        search(negative, positive)
        return self.ret


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

        # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res


class SolutionSlow:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positive, negative, zeros, self.ret = [], [], [], set()
        nums = sorted(nums)
        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                zeros.append(num)

        if len(zeros) >= 3:
            self.ret.add((0, 0, 0))
        if len(zeros) > 0:
            for num in positive:
                if -1 * num in negative:
                    self.ret.add((num, -num, 0))

        def checktriplets(mylist1, mylist2):
            for i in range(len(mylist1)):
                for j in range(i + 1, len(mylist1)):
                    if -1 * (mylist1[i] + mylist1[j]) in mylist2:
                        self.ret.add((mylist1[i], mylist1[j], -1 * (mylist1[i] + mylist1[j])))

        checktriplets(positive, negative)
        checktriplets(negative, positive)

        return self.ret


class SolutionFasterthanSlow:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positive, negative, zeros, self.ret = [], [], [], set()

        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                zeros.append(num)
        N, P = set(negative), set(positive)
        if len(zeros) >= 3:
            self.ret.add((0, 0, 0))
        if zeros:
            for num in P:
                if -1 * num in N:
                    self.ret.add((-1 * num, 0, num))

        def checktriplets(mylist1, mysetlist):
            for i in range(len(mylist1)):
                for j in range(i + 1, len(mylist1)):
                    target = -1 * (mylist1[i] + mylist1[j])
                    if target in mysetlist:
                        self.ret.add(tuple(sorted([mylist1[i], mylist1[j], target])))

        checktriplets(positive, N)
        checktriplets(negative, P)

        return self.ret


s = Solution()
nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
ret = s.threeSum(nums)
print(len(ret))
