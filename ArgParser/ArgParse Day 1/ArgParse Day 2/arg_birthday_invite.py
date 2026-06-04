import argparse
parser=argparse.ArgumentParser(description= 'Birthday Greeter')

parser.add_argument('--name', help='Name of the Person To Greet', required=True)
parser.add_argument('--age', help='Age of the person to Greet', required=True)

args_name=input("Enter Name: ")
args_age=input('Enter Age: ')

args=parser.parse_args(['--name', args_name, '--age', args_age])

print(f"Happy Birthday {args.name}! You are {args.age} years old!") 