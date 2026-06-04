import argparse
parser = argparse.ArgumentParser(description='Name Parser')
parser.add_argument("--name", help="name to parse", required=True)
args=parser.parse_args(['--name', input("Enter Name: ")])
print(args.name)