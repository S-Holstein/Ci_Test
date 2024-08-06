import argparse


def message_to_the_world(text: str) -> bool:
    if isinstance(text, str):
        print(text)
        return True
    else:
        return False


def add(n_1: int, n_2: int) -> int:
    if isinstance(n_1, int) and isinstance(n_2, int):
        return n_1 + n_2
    else:
        raise ValueError("Both arguments have to be integers.")


def main():
    parser = argparse.ArgumentParser(description='Process some text.')
    parser.add_argument('text', nargs='?', type=str, help='Text to be processed')
    args = parser.parse_args()

    if args.text:
        message_to_the_world(args.text)
    else:
        print("No text provided.")


if __name__ == "__main__":

    main()

    print("Hello")
