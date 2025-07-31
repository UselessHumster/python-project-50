from gendiff.documentation import create_parser
from gendiff import generate_diff


def main():
    parser = create_parser()
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == "__main__":
    main()
