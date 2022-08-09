import sys
from heapq import heapify, heappush, heappop

def dijkstra(graph, src, dest):
	inf = sys.maxsize #place infinite value in variable inf
	node_data = {'A'{'cost':inf, 'pred':[]}, 
	'B'{'cost':inf, 'pred':[]},
	'C'{'cost':inf, 'pred':[]},
	'D'{'cost':inf, 'pred':[]},
	'E'{'cost':inf, 'pred':[]},
	'F'{'cost':inf, 'pred':[]},
	} 
	node_data[src]['cost'] = 0
	visited = []
	temp = src

	for i in range(5):
		if temp not in visited: #TODO: Reassign source
			visited.append(temp)
			min_heap = []
			for j in graph [temp]:
				if j not in visited:
					cost = node_data[temp]['cost']  + graph[temp][j]
					if cost < node_data[j]['cost']: # if cost is lower than previous value in node data, store new node data values 
						node_data[j]['cost'] = cost # new value for cost
						node_data[j]['pred'] = node_data[temp]['pred'] + list(temp) # new value for previous predecessor
					heappush(min_heap, (node_data[j][cost], j)) # put cost and neighbour in min_heap
		heapify(min_heap) # compare cost of neighbour and determine minimum cost
		temp = min_heap[0][1] # save neighbour in temp for next iteration
	print("Shortest Distance: " + str(node_data[dest]['cost']))
	print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))




	if __name__ = "__main__":
		graph = {
		'A': {'B':2, 'C':4},
		'B': {'A':2, 'C':3, 'D':8},
		'C': {'A':4, 'B':3, 'E':5, 'D':2},
		'D': {'B':8, 'C':2, 'E':11, 'F':22},
		'E': {'C':5, 'D':11, 'F':1},
		'F': {'D':22, 'E':1}
		}
		source = 'A'
		destination = 'F'
		dijkstra(graph, source, destination)