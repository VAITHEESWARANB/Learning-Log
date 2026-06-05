import argparse
parser =argparse.ArgumentParser(description='PG13 Movie Access Granter')
parser.add_argument('--age', help='Enter your age', required=True)

age =int(input('Enter Your Age: '))
if age>=13:
    args=parser.parse_args(['--age', str(age)])
    print('Access Granted')
else:
    print('You are not old enough for this movie')