
numOfNodes = 6
reli = [0.94, 0.91, 0.96, 0.93, 0.92, 0.94, 0.97, 0.91, 0.92, 0.94, 0.90, 0.94, 0.93, 0.96, 0.91]
cost = [10, 25, 10, 20, 30, 10, 10, 25, 20, 20, 40, 10, 20, 10, 30]
	

def main():
	for node in range(5):
		temp = 0
		for i in range(node + 1):
			temp += i

		print ((node+1)*(numOfNodes-1)-temp-1)
		
main()


def nodesReli(node):
	
		
		
	

	# public static double[] nodesReli(int node) {
	# 	double [] nodeReli   = new double [numOfNodes-1];
	# 	int temp = 0;
	# 	for(int i = 0 ; i < node+1; i++) {
	# 		temp += i; 
	# 	}
	# 	int start = (node+1)*(numOfNodes-1)-temp-1;
	# 	while((numOfNodes-1) >0) {
	# 		numOfNodes--;
	# 		nodeReli[numOfNodes-1] = reli[temp];
	# 	}
		
	# 	# int temp = 0;
	# 	# for(int i = 0 ; i < node+1; i++) {
	# 	# 	temp += i; 
	# 	# }
	# 	# int j = 0;
	# 	# int count = node;
		
	# 	# while(count >0) {
	# 	# 	nodeReli[j] = reli[node-1];
	# 	# 	j++;
			
	# 	# }
		
		
	# 	# for(int i = node*numOfNodes-temp ; i < reli.length; i++) {
			
	# 	# }
	# 	return nodeReli;
	# }

