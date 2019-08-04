import json
import typing
import unittest

def load_string(input: str) -> typing.Dict[str, str] :
    raw_json = json.loads(input)
    output = dict()
    # for pair in raw_json["variables"]:
    #     output[pair["name"]] = pair["value"]

    return {pair["name"]:pair["value"] for pair in raw_json["variables"]}

def load_path(inputPath: str) -> typing.Dict[str, str]:
    with open(inputPath, 'r') as inputfile:
        return load_string(inputfile.read())

def save_to_path(inputFile: typing.Dict[str, str], outputPath: str ) -> None:
    with open(outputPath, 'w+') as outputStream:
        outputStream.write()

def to_string(input: typing.Dict[str, str]) -> str:
    output = list()
    for k,v in input.items():
        output.append({"name":k, "value":v})
    return json.dumps({"variables": output})


class _Tests(unittest.TestCase):
    def test_load_string(self):
        self.assertEqual(load_string('{"variables":[{"name":"bop","value":"beep"}]}'), {"bop": "beep"})

    def test_to_string(self):
        self.assertEqual(to_string(load_string('{"variables":[{"name":"bop","value":"beep"}]}')), '{"variables": [{"name": "bop", "value": "beep"}]}')

if __name__ == '__main__':
    unittest.main()