import heapq
def aStrSearch(maps, heuristics, startCity, goal):
    priorityQ = []
    heapq.heappush(priorityQ, (heuristics[startCity], 0, startCity, [startCity]))
    visited = set()

    while priorityQ:
        _, totalDist, currentCity, path = heapq.heappop(priorityQ)

        if currentCity in visited:
            continue
        
        visited.add(currentCity)
        
        if currentCity == goal:
            return path, totalDist
        
        for neighborCity, dist in maps[currentCity].items():
            if neighborCity in visited:
                continue
            new_totalDist = dist + totalDist
            newData = heuristics[neighborCity] + new_totalDist
            heapq.heappush(priorityQ, (newData, new_totalDist, neighborCity, path + [neighborCity]))

    return None, None


inputPath = "./22301172_SabidMahmud_CSE422_09_Lab_Assignment01_InputFile_Summer2024.txt"
with open(inputPath, 'r') as inputFile:
    readData = inputFile.readlines()

maps = dict() 
heuristics = dict()
for line in readData:
    placeValue = line.strip().split()
    city = placeValue[0]
    huristic = int(placeValue[1])
    heuristics[city] = huristic
    # print(huristic,"\n",heuristics)
    neighbors_dist = dict() # {neighbor city : distatnce}

    for i in range(2, len(placeValue), 2):
        neighbor_ct = placeValue[i]
        dist = int(placeValue[i+1])
        neighbors_dist[neighbor_ct] = dist
    
    # print(neighbors_dist)

    maps[city] = neighbors_dist

# print(heuristics)
# print("Maps:")
# print(maps)

startCity = input("Start City Name: ")
goal = input("Destination City Name: ")

path, totalDistance = aStrSearch(maps, heuristics, startCity, goal)

if path:
    print(f"Path: {' -> '.join(path)}")
    print(f"Total Distance from {startCity} to {goal}: {totalDistance} km")
else:
    print("No Path Found")