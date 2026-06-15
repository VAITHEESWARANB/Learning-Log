import argparse

def main():
    parser = argparse.ArgumentParser(description= 'Dirbustter Skeleton Structure')

    parser.add_argument('-u', '--url', required=True, help='Enter Target URL')
    parser.add_argument('-w', '--wordlist', required=True, help='Enter Wordlist Path')

    args = parser.parse_args()

    print(f"Target URL: {args.url}")
    print(f"Wordlist Path: {args.wordlist}")
    print('-' *50)

if __name__ == '__main__':
    main()
