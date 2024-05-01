"""
Destination City
Easy
Topics
Companies
Hint

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:

Input: paths = [["A","Z"]]
Output: "Z"

 

Constraints:

    1 <= paths.length <= 100
    paths[i].length == 2
    1 <= cityAi.length, cityBi.length <= 10
    cityAi != cityBi
    All strings consist of lowercase and uppercase English letters and the space character.


"""


def dest_city(paths: list[list[str]]) -> str:
    city_map = {paths[0][0]: 0, paths[0][1]: 1}
    not_visit = paths
    while not_visit:
        path = not_visit.pop(0)
        origin, dest = path[0], path[1]
        if origin in city_map:
            city_map[dest] = city_map[origin] + 1
        elif dest in city_map:
            city_map[origin] = city_map[dest] - 1
        else:
            not_visit.append(path)

    return max(city_map, key=city_map.get)


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

print(dest_city(paths))
