import argparse

def main():
    parser = argparse.ArgumentParser(description="Demo lấy args trong Python")
    parser.add_argument("name", help="Tên của bạn")
    parser.add_argument("--age", type=int, help="Tuổi của bạn", required=False)
    args = parser.parse_args()

    print(f"Xin chào {args.name}")
    if args.age:
        print(f"Tuổi của bạn là {args.age}")
    else:
        print("Chưa nhập tuổi")

if __name__ == "__main__":
    main()
