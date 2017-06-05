import json
import codecs
import sys
import os
import chardet


def get_encoding(filename: "str") -> "str":
    with open(filename, "rb") as file:
        raw_data = file.read()
    return chardet.detect(raw_data)['encoding']


def load_data(filename: "str") -> "object json":
    try:
        json_data = json.load(codecs.open(filename, 'r', get_encoding(filename)))
    except json.decoder.JSONDecodeError:
        print("file {} contains invalid json data, print stopped".format(filename))
        exit(1)
    else:
        return json_data


def pretty_print_json(json_data: "object json"):
    print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))


def main(filename):
    pretty_print_json(load_data(filename))


if __name__ == '__main__':
    if os.path.isfile(sys.argv[1:][0]):
        main(sys.argv[1:][0])
    else:
        print("invalid path or file name: {}".format(sys.argv[1:][0]))
