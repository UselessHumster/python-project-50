from gendiff.documentation import create_parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    print(f'You are trying to check diff from {args.first_file} and {args.second_file}')


if __name__ == "__main__":
    main()
