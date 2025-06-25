from collections import deque


def bus_routes(routes, source, target):
    if source == target:
        return 0
    
    bus_stops = {}
    for i, route in enumerate(routes):
        for stop in route:
            if stop not in bus_stops:
                bus_stops[stop] = []
            bus_stops[stop].append(i)
    
    visited = set()
    queue = deque()

    for bus in bus_stops[source]:
        queue.append((bus,1))
        visited.add(bus)

    while queue:
        curr_bus, num_changes = queue.pop(0)

        # check if target is in current route
        for stop in routes[curr_bus]:
            if stop == target:
                return num_changes
            
        # add neighbors to queue
        for connected_bus in bus_stops[stop]:
            if connected_bus not in visited:
                queue.append((connected_bus, num_changes + 1))
                visited.add(connected_bus)
    
    return -1