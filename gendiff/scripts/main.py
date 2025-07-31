from gendiff.documentation import create_parser
from gendiff import reader

def main():
    parser = create_parser()
    args = parser.parse_args()
    data1 = reader.get_file_data(args.first_file)
    data2 = reader.get_file_data(args.second_file)

    print(data1)
    print(data2)


if __name__ == "__main__":
    main()
