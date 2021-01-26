import sys

def get_combinations(coins_dict, target):
	''' 
		Get all the possible coin combinations 
		This is done by looping through each coin and creating a carryover 
		 situation when the coin exceeds the target amount
	'''
	combinations = []
	coins_list = list(coins_dict.values())
	counts = [0 for i in range(len(coins_list))]

	while True:
		total = 0
		incrementLastCoin = True
		
		# Calculate total
		for i, count in enumerate(counts):
			total += count * coins_list[i]

		# Keep coin combination if it matches target
		if total == target:
			combinations.append(counts.copy())

		# Handle coin carryover if it exceeds the max
		for i in range(len(coins_list)-1,-1,-1):
			# if a single coin is greater than target
			if counts[i] * coins_list[i] >= target:
				
				# if last coin exceeds target, it should exit
				if i == 0:
					return combinations

				# increase carryover and zero out current coin
				counts[i] = 0
				counts[i-1] += 1
				incrementLastCoin = False
				break

		# If last coin is reset, don't increment or 0s will not be tested
		if incrementLastCoin:
			counts[len(coins_list)-1] += 1

def get_header_format(curr_dict, type):
	''' 
		Creates the header format based on the length of the header words.
		The main header will be type string (s)
		The data will be type digit (d)
	'''
	l = [ '{:>' + str(len(k)) + type + '}' for k in curr_dict.keys()]
	header_format = ' '.join(l)
	return header_format

def print_combinations(combinations, curr_dict):
	# Print the header with s format
	header_format = get_header_format(curr_dict, 's')
	headers = [k.capitalize() for k in curr_dict.keys()]
	print(header_format.format(*headers))

	# Print the data with d format using lengths from header words
	coins_list = list(curr_dict.values())
	header_format = get_header_format(curr_dict, 'd')
	for c in combinations:
		print(header_format.format(*c))

	print('\nCount: %s\n' % len(combinations))

def parse_string(string):
	''' Takes input string and returns it as a dictionary pair '''
	s_list = string.split(',')
	# Convert to a Pair List
	pairs_list = [[s_list[i], float(s_list[i+1])] for i in range(0, len(s_list), 2)]

	# Sort Pair List and Get the Target number.
	pairs_list.sort(key = lambda x: x[1])
	target = pairs_list[-1][1]

	# Convert List of Lists to List of Dict for later use
	new_pairs_dict = {}
	for p in pairs_list:
		new_pairs_dict[p[0]] = target/p[1]
	return [new_pairs_dict, target]

if __name__ == "__main__":
  print(f"Arguments count: {len(sys.argv)}")
  for i, arg in enumerate(sys.argv):
    print(f"Argument {i:>6}: {arg}")

  # Note* This assumes that the smallest coin value is divisible all the other coin values.

  # Example 1
  string = "Quarter,4,Dime,10,Nickel,20,Penny,100"
  coins_dict, target = parse_string(string)

  combinations = get_combinations(coins_dict, target)
  print_combinations(combinations, coins_dict)

  # Example 2
	# Check to see if argument is passed. If not, use string from assignment details
  if(len(sys.argv) > 1):
    string = sys.argv[1]
  else:
    string = "Coin,1.5,Arrowhead,3,Button,150"

  buttons_dict, target = parse_string(string)

  combinations = get_combinations(buttons_dict, target)
  print_combinations(combinations, buttons_dict)