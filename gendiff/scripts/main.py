from pathlib import Path

from gendiff import generate_diff
from gendiff.documentation import create_parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    file1 = Path(args.first_file)
    file2 = Path(args.second_file)
    result = generate_diff(file1, file2, args.format)
    print(result)


if __name__ == "__main__":
    main()
