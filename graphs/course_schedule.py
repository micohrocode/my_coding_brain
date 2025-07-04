from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    # set the graph neighbor lists
    graph = defaultdict(list)
    # set to track indegrees
    in_degree = [0] * numCourses

    # set neigbors and indegrees
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    # set queue for currently 0 indegree courses
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

    courses_taken = 0

    while queue:
        # take the left most course
        course = queue.popleft()
        # add it to the courses taken
        courses_taken += 1

        # for all neighbors of that course
        for neighbor in graph[course]:
            # lower their indegree
            in_degree[neighbor] -= 1
            # if its zero add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # check if all courses have been taken
    return courses_taken == numCourses