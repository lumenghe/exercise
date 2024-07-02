"""
Task Scheduler
Medium
Topics
Companies
Hint

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

    1 <= tasks.length <= 104
    tasks[i] is an uppercase English letter.
    0 <= n <= 100

"""
from typing import List

class Solution1:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1

        freq.sort()
        chunk = freq[25] - 1
        idle = chunk * n
        print(idle)
        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)
        
class SolutionWrong:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        idle_nb = 0
        rest = 0
        for c, v in task_counter.most_common():
            if idle_nb == 0:
                idle_nb = n * (v-1)
                most_common = v
            else:

                rest += v
        print(idle_nb, rest)
        return len(tasks) if idle_nb < rest else most_common+idle_nb
        


        
        
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        print(task_counter)
        c = task_counter.most_common(1)[0]
        print(c)
        
s= Solution()
tasks=["A","A","A","B","B","B"]
res = s.leastInterval(tasks=tasks, n=2)




