# https://docs.python.org/3/howto/argparse.html

import argparse

from .util import human_size


class HumanSize(argparse.Action):
    """Argparse action that parses human readable size into bytes."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __call__(self, parser, namespace, value, option_string=None):
        setattr(namespace, self.dest, human_size(value))


parser = argparse.ArgumentParser()
parser.add_argument("--mode",
                    help="Set the cartridge type",
                    choices=["cv", "gen", "sms", "pce", "tg", "snes"],
                    type=str,
                    default="none")

_readWriteArgs = parser.add_mutually_exclusive_group()
_readWriteArgs.add_argument("--checksum",
                           help="Calculate ROM checksum",
                           action="store_true")

_readWriteArgs.add_argument("--byteswap",
                           nargs=1,
                           help="Reverse the endianness of a file",
                           type=str,
                           metavar=('file to byte swap'))

_readWriteArgs.add_argument("--rd",
                            help="Read from UMD",
                            choices=["rom", "save", "bram", "header", "fid", "sfid", "sf", "sflist", "byte", "word", "sbyte", "sword"],
                            type=str)

_readWriteArgs.add_argument("--wr",
                            help="Write to UMD",
                            choices=["rom", "save", "bram", "sf"],
                            type=str)

_readWriteArgs.add_argument("--clr",
                            help="Clear a memory in the UMD",
                            choices=["rom", "rom2", "save", "bram", "sf"],
                            type=str)

parser.add_argument("--addr",
                    nargs='?',
                    help="Address for current command",
                    type=int,
                    default="0")

parser.add_argument("--size",
                    action=HumanSize,
                    nargs='?',
                    help="Size in bytes for current command",
                    type=str,
                    default="1")

parser.add_argument("--file",
                    help="File path for read/write operations",
                    type=str,
                    default="console")

parser.add_argument("--sfile",
                    help="8.3 filename for UMD's serial flash",
                    type=str)

