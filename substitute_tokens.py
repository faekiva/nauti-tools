def substitute(text: str, substitutions: dict[str, str]) -> str:
    tokenizedsubs = {f"$({key})":value for key, value in substitutions}
    
    for key, value in tokenizedsubs:
        text = text.replace(key, value)
    
    return text

def substitute_file(infile: str, outfile: str, substitutions: dict[str, str]) -> None:
    with open(infile, 'r') as instream:
        with open(outfile, 'w+') as outstream :
            outstream.write(substitute(instream.read(), substitutions))