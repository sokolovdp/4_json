import json
import sys
import os
import chardet


def load_decoded_data(filename: "str") -> "str":
    with open(filename, "rb") as file:
        raw_data = file.read()
    encoding = chardet.detect(raw_data)['encoding']
    return raw_data.decode(encoding)


def load_json_data(filename: "str") -> "dict":
    try:
        return json.loads(load_decoded_data(filename))
    except json.decoder.JSONDecodeError:
        print("file {} contains invalid json data".format(filename))


def pretty_print_json(json_data: "object json"):
    print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))


def main(filename):
    pretty_print_json(load_json_data(filename))


if __name__ == '__main__':
    if os.path.isfile(sys.argv[1]):
        main(sys.argv[1])
    else:
        print("invalid path or file name: {}".format(sys.argv[1:][0]))
