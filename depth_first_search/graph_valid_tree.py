def validTree(n, edges):
    # build adj list
    adj_list = [[] for _ in range(n)]
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    visited = [False] * n
    if hasCycle(adj_list,0,visited,-1):
        return False
    
    return all(visited)

def hasCycle(adj_list, node, visited, parent):
    visited[node] = True

    # for the neighbors of the node
    for neighbor in adj_list[node]:
        # if it has already been visited
        # and its not the parent of the current node
        if visited[neighbor] and parent != neighbor:
            return True
        elif not visited[neighbor] and \
            hasCycle(adj_list, neighbor, visited, node):
            # test new node
            return True
    return False
