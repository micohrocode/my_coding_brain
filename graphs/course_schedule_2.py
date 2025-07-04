from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    # set up the graph and indegrees
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    # set the neighbors and indegrees
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

    order = []

    while queue:
        # remove the first 0 indegree course
        course = queue.popleft()
        # add the course to the order
        order.append(course)

        # for each neighbor of the course
        for neighbor in graph[course]:
            # decrement their indegree
            in_degree[neighbor] -= 1

            # if the indegree is 0
            # add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == numCourses else []