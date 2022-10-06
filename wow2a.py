from shutil import move


def findDataLocations(locations, movedFrom, movedTo):
    n = len(locations)
    m = len(movedFrom)
    
    movement = {}
    for i in range(m):
        movement[movedFrom[i]] = movedTo[i]
        
    for i in range(n):
        if locations[i] in movement:
            destination = movement[locations[i]]
            movement.pop(locations[i])
            while destination in movement:
                temp = movement[destination]
                movement.pop(destination)
                destination = temp
            locations[i] = destination
    locations.sort()
    return locations

print(findDataLocations([1, 5, 2, 6], [1, 4, 5, 7], [4, 7, 1, 3]))