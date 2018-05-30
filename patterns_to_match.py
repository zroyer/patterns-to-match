def do_something(patterns, paths):
	print patterns
	print paths

if __name__ == "__main__":
	num_patterns = int(raw_input())
	patterns = [raw_input() for n in range(num_patterns)]

	num_paths = int(raw_input())
	paths = [raw_input() for m in range(num_paths)]

	if num_patterns and num_paths:
		do_something(patterns, paths)
