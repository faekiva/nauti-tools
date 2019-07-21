import os
import sys
from glob import glob
import substitute_tokens
import VariableYML

ASS_FOLDER = "muxable"
RELEASE_FOLDER = "release"
TEMPLATE_FOLDER = "release_template"
PLACEHOLDER_FILE = "Placeholder"
EPISODE_TOKEN = "ep_num"

def create_folders(ep_num: str, release_path: str, mux_path: str) -> None:
    os.mkdir(ep_num)

    os.mkdir(mux_path)
    os.mknod(os.path.join(mux_path,PLACEHOLDER_FILE))

    os.mkdir(release_path)

def create_deploy_json(release_path: str, mux_path: str):
    VariableYML.save_to_path({"muxable_folders":[mux_path], "release_folder": release_path, "release_name": None})


def main(show_path: str, using_git=True) -> None:
    os.chdir(show_path)
    curr_ep: int = max([int(x) for x in os.listdir() if x.isdigit()])
    next_ep: str = str(curr_ep + 1).zfill(2)
    
    release_path: str = os.path.join(next_ep, RELEASE_FOLDER)
    mux_path: str = os.path.join(next_ep, ASS_FOLDER)

    create_folders(next_ep, release_path, mux_path)

    for file in os.listdir(TEMPLATE_FOLDER):
        infile = os.path.join(os.curdir, TEMPLATE_FOLDER, file)
        outfile = os.path.join(os.curdir, release_path)
        substitute_tokens.substitute_file(infile, outfile, {EPISODE_TOKEN: next_ep})

    create_deploy_json(release_path, mux_path)

    if using_git:
        branch_name: str = f"ep/{next_ep}"
        os.system(f"git checkout -b {branch_name}")
        os.system(f'git commit -m "initial setup for {branch_name}"')
        os.system(f'git push -u origin {branch_name}')
    


if __name__ == "__main__":
    main(sys.argv[1])