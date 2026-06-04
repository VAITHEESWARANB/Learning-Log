Date: 02/06/2026

Today, I started learning 'argparse' library from python for creating Command-Line-Interface based projects. So started with a basic argument parsing program which is below

	import argparse
	parser = argparse.ArgumentParser(description='Name Parser')
	parser.add_argument("--name", help="name to parse", required=True)
	args=parser.parse_args(['--name', input("Enter Name: ")])
	print(args.name)

Line By Line Explanation

Line 1:
	import argparse - import is used to inform python to use the respective predefined functions available in argparse.

Line 2:
	parser = argparse.ArgumentParser(description='Name Parser') - Creating a argument parsing object for our argument to parse through.
	'decription' used for describing the purpose to users.

Line 3:
	parser.add_argument("--name", help="name to parse", required=True) - Here we are adding argument, '--name' is an argument, and help displays when the user doesn't know what to enter n the respective field.
	'required=True' is to mention the field is mandatory and needs a input.

Line 4:
	args=parser.parse_args(['--name', input("Enter Name: ")]) - Here we are getting input for CLI and saving them in variable called 'args' with a tag '--name'.

Line 5:
	print(args.name) - Printing the name received from user input.

Output
	Enter Name: Ann
	Ann

My Experience:
	Since this is the start of 'argparse' library felt had to understand this basic concept but tried to d it by myself without using AI for debugging the code. Also most of the error was due to spelling the keywords and predefined functions wrongly. It was a fun and dizzy 40 minutes experiee f learning this parse argument method. 

	Planning do some little more complicated programs using same concept for grasping the fundamentals.   
