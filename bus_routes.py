"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

 

 

Constraints:

    1 <= routes.length <= 500.
    1 <= routes[i].length <= 105
    All the values of routes[i] are unique.
    sum(routes[i].length) <= 105
    0 <= routes[i][j] < 106
    0 <= source, target < 106

"""

from functools import reduce


class SolutionWrong:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stops = set(reduce(lambda x, y: x + y, routes))
        stop_graphs = {i: [] for i in stops}
        bus_graphs = {index: route for index, route in enumerate(routes)}
        print(bus_graphs)
        self.solution = []
        for index, route in enumerate(routes):
            for stop in route:
                stop_graphs[stop].append(index)
        visited_stop = []

        def dfs(stop, target, path):
            if stop == target:
                self.solution.append(path)
                print("path=", path)
                return
            for bus in stop_graphs[stop]:
                if bus not in path:
                    path.append(bus)
                    print("new path=", path)
                    for new_stop in bus_graphs[bus]:
                        dfs(new_stop, target, path + [bus])

        dfs(source, target, [])
        if len(self.solution) == 0:
            return -1
        ret = float("inf")
        for sol in self.solution:
            print(sol)
            ret = min(ret, len(set(sol)))
        return ret
