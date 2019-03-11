import argparse

from dump_cleaned_files import create_cleaned_files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('topic', help='The topic.')
    parser.add_argument('--lang', default='en', help='The language. Default: en')
    args = parser.parse_args()

    create_cleaned_files(args.topic, args.lang)


if __name__ == '__main__':
    main()
