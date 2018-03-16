import time

values = [360, 83, 59, 130, 431, 67, 230, 52, 93,
            125, 670, 892, 600, 38, 48, 147, 78, 256,
            63, 17, 120, 164, 432, 35, 92, 110, 22,
            42, 50, 323, 514, 28, 87, 73, 78, 15,
            26, 78, 210, 36, 85, 189, 274, 43, 33,
            10, 19, 389, 276, 312]

weights = [7, 0, 30, 22, 80, 94, 11, 81, 70,
              64, 59, 18, 0, 36, 3, 8, 15, 42,
              9, 0, 42, 47, 52, 32, 26, 48, 55,
              6, 29, 84, 2, 4, 18, 56, 7, 29,
              93, 44, 71, 3, 86, 66, 31, 65, 0,
              79, 20, 65, 52, 13]

capacities = [850]
	 

def greedy(values, weights, capacities):
	knapsack = []
	value_weight = dict(zip(values, weights))
	weightlimit = 0
	capacity = capacities[0]

	while True:
		knapsack.append(values.pop(values.index(max(values))))
		weight_of_object = value_weight.get(knapsack[-1])
		weightlimit += weight_of_object 
		if weightlimit > capacity:
			newknapsack = knapsack[:-1]
			weightlimit -= weight_of_object
# 			
			exceeded = 1
			break
# 		
			
		
			
	if exceeded == 1:
		print("value of items", newknapsack)
		print("Weight of the knapsack", weightlimit)
	else:
		print("value of items", knapsack)
		print("Weight of the knapsack", weightlimit)

start_time = time.time()		
greedy(values, weights, capacities)
end_time = time.time()

print("The calculation took", end_time - start_time, "seconds")
				
	

			
			
			