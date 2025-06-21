class IntGraphNode:
    def __init__(self, value = 0, neighbors = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    # graph adj list
    adj_list = {}

    def dfs(node):
        # if its already been seen
        # skip it
        if node.value in adj_list:
            return
        
        # set the neighbors for the node
        adj_list[node.value] = [n.value for n in node.neighbors]
        for neighbor in node.neighbors:
            # attempt to find the neighbors
            # of the nodes neighbors
            dfs(neighbor)

    if node:
        dfs(node)
    
    return adj_list