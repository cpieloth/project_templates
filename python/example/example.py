"""Entry point for CLI usage."""

import argparse as ag
import sys

import example.sub_commands


def main(argv=sys.argv):
    """
    Start the Example tool.

    :return: 0 on success.
    """
    # Parse arguments
    parser = ag.ArgumentParser(prog=argv[0])
    parser.add_argument('--version', action='version', version='%(prog)s ' + example.__version__)

    subparser = parser.add_subparsers(title='Example Commands', description='Valid example commands.')
    example.sub_commands.HelloCmd.init_subparser(subparser)

    args = parser.parse_args(argv[1:])
    try:
        # Check if a sub-command is given, otherwise print help.
        getattr(args, 'func')
    except AttributeError:
        parser.print_help()
        return 2

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
