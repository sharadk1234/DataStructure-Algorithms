#Intersection are represented as a Dictionary
import math
class GraphEdge(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance

class GraphNode:
    def __init__(self,val, x, y): # X, y => Cordinates
        self.value = val
        self.edges = []
        self.x = x
        self.y = y
        self.g_value = 0
        self.parent = None

    def add_child(self, node, distance):
        for each in self.edges:
            if each.node == node:
                # already exsits in graph
                return -1

        self.edges.append(GraphEdge(node,distance))
        node.edges.append(GraphEdge(self,distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)

class Graph():
    def __init__(self, node_list):
        self.nodes = node_list
        self.node_dict = {node.value for node in self.nodes}

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

class PriorityQueue:

    def __init__(self, queue_list=[]):
        self.queue_list = queue_list

    def append(self, node, priority):
        self.queue_list.append([node , priority])

    def pop(self):
        smallest = float('inf')
        smallest_item = None
        for item in self.queue_list:
            if item[1] < smallest:
                smallest = item[1]
                smallest_item = item
        self.queue_list.remove(smallest_item)
        return smallest_item



def calculate_g_value(current_node_coordinates, next_node_coordinates, current_node, next_node):
    #Euclidean distance base algorithm
    x1 , y1 = current_node_coordinates
    x2 , y2 = next_node_coordinates
    subtract_the_x = x1 - x2
    subtract_the_y = y1 - y2

    distance_value = math.sqrt((subtract_the_x * subtract_the_x) + (subtract_the_y * subtract_the_y))
    g_value = distance_value + current_node.g_value
    return g_value


def calculate_h_value(current_node_cordinates, goal_node_cordinates):
    # Euclidian Distance base algorithm credit to GeeksforGeeks
    x1 , y1 = current_node_cordinates
    x2 , y2 = goal_node_cordinates

    subtract_the_x = x1 - x2
    subtract_the_y = y1 - y2

    h_value = math.sqrt((subtract_the_x * subtract_the_x) + (subtract_the_y * subtract_the_y))
    return h_value

def get_path(goal_node):
    current = goal_node
    shortest_path = [current.value]
    while current.parent:
        current = current.parent
        shortest_path.insert(0, current.value)
    return shortest_path


def find_connected(start_node , checked_nodes):
    for edge in start_node.edges:
        if edge.node not in checked_nodes:
            checked_nodes.add(edge.node)
            find_connected(edge.node, checked_nodes)
    return checked_nodes


def shortest_path(input_map, start_intersection, end_intersection):
    # Converting the Graph into DataStructure for analysis
    intersection_graph_nodes = []
    # if start and  and end node are same
    if start_intersection == end_intersection:
        return[start_intersection]

    for intersection in input_map.intersections.items():
        intersection_node = GraphNode(intersection[0], intersection[1][0], intersection[1][1])
        intersection_graph_nodes.append(intersection_node)
        if start_intersection == intersection[0]:
            start_node = intersection_node
        elif end_intersection == intersection[0]:
            stop_node = intersection_node

    map_graph = Graph(intersection_graph_nodes)

    for intersection_node in map_graph.nodes:
        for destination in input_map.roads[intersection_node.value]:
            distance_between_intersections = calculate_h_value([intersection_node.x, intersection_node.y],
                                                               [input_map.intersections[destination][0],
                                                                input_map.intersections[destination][1]])
            intersection_node.add_child(map_graph.node_dict[destination], distance_between_intersections)

    checked_nodes = set()
    find_connected(start_node, checked_nodes)

    if stop_node not in checked_nodes:
        return "No path between nodes"

    # open_list is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # closed_list is a list of nodes which have been visited
    # and who's neighbors have been inspected

    open_list = PriorityQueue([[start_node, 0]])
    closed_list = set()
    count = 0


    while len(open_list.queue_list) > 0:
        current_location = open_list.pop() #removes smallest item from priority queue, assign to variable
        closed_list.add(current_location[0]) #puts smallest element in closed list - this prevents it from being checked again

        #looks at all edges of item most recently moved to closed list
        for edge in current_location[0].edges:

            location_in_openlist = False

            for item in open_list.queue_list:
                if item[0] == edge.node:
                    location_in_openlist = True
                    open_list_val = item

            if edge.node not in closed_list:
                #if item is not in open list
                if location_in_openlist == False:
                    edge.node.parent = current_location[0]
                    edge.node.g_value = calculate_g_value([current_location[0].x, current_location[0].y], [edge.node.x, edge.node.y], current_location[0], edge.node)
                    open_list.append(edge.node, edge.node.g_value + calculate_h_value([edge.node.x, edge.node.y], [stop_node.x, stop_node.y]))

                #if item is in open list
                elif location_in_openlist == True:
                    if open_list_val[0].g_value > calculate_g_value([current_location[0].x, current_location[0].y], [edge.node.x, edge.node.y], current_location[0], edge.node):
                        edge.node.g_value = calculate_g_value([current_location[0].x, current_location[0].y], [edge.node.x, edge.node.y], current_location[0], edge.node)
                        edge.node.parent = current_location[0]
                        open_list.append(edge.node, calculate_g_value([current_location[0].x, current_location[0].y], [edge.node.x, edge.node.y], current_location[0], edge.node) + calculate_h_value([edge.node.x, edge.node.y], [stop_node.x, stop_node.y]))

    return get_path(stop_node)












