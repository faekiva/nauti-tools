from torf import Torrent
import argparse

DEFAULT_TRACKERS = ["http://nyaa.tracker.wf:7777/announce"]


def parse(argv=None):
    p = argparse.ArgumentParser(prog="create_torrent.py", description="simple script for creating torrents")

    p.add_argument("resource", help="path to resource for torrent")
    p.add_argument("torrent", help="path to save torrent file to")
    p.add_argument('-t', "--tracker", help="add tracker to torrent", action="append", default=DEFAULT_TRACKERS)
    p.add_argument('-n', "--name", help="override the metadata name of the torrent (not the file)")
    p.add_argument('-c', "--comment", help="add comment to torrent")

    return p.parse_args(argv)


def create_torrent(resource, torrent, trackers, name=None, comment=""):
    t = Torrent(
        path=resource,
        trackers=trackers,
        comment=comment,
        name=name,
    )
    t.generate()
    t.write(torrent)


if __name__ == "__main__":
    args = parse()
    create_torrent(
        resource=args.resource,
        torrent=args.torrent,
        trackers=args.tracker,
        name=args.name,
        comment=args.comment,
    )
