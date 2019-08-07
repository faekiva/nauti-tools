from typing import Dict
import argparse


def parse(argv=None):
    p = argparse.ArgumentParser(
        prog="substitute_tokens.py",
        description="a simple utility for performing variable substitutions"
    )

    p.add_argument("infile", help="path to file to perform replacement on")
    p.add_argument("outfile", help="path to file to perform replacement on")
    p.add_argument('-r', "--replace", help="key value pair to replace", nargs=2, action="append")

    return p.parse_args(argv)


def substitute(text: str, substitutions: Dict[str, str]) -> str:
    tokenizedsubs = {f"$({key})": value for key, value in substitutions.items()}
    
    for key, value in tokenizedsubs.items():
        text = text.replace(key, value)
    
    return text


def substitute_file(infile: str, outfile: str, substitutions: Dict[str, str]) -> None:
    with open(infile, 'r') as instream:
        text = instream.read()

    with open(outfile, 'w+') as outstream:
        outstream.write(substitute(text, substitutions))


if __name__ == "__main__":
    args = parse()
    subs = {k: v for k, v in args.replace}
    substitute_file(args.infile, args.outfile, subs)
