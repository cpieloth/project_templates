"""
Module for command line interface implementation.
"""

import abc
import argparse
import sys

from example import __version__
from example.io import print_hello_world


class SubCommand(abc.ABC):
    """
    Abstract base class for sub commands.

    A new sub command can be added by calling the init_subparser().
    """

    @classmethod
    @abc.abstractmethod
    def _name(cls):
        """
        Return name of the command.

        :return: Command name
        :rtype: str
        """
        raise NotImplementedError()

    @classmethod
    def _help(cls):
        """
        Return help description.

        :return: Help description
        :rtype: str
        """
        return cls.__doc__

    @classmethod
    @abc.abstractmethod
    def _add_arguments(cls, parser):
        """
        Initialize the argument parser and help for the specific sub-command.

        Must be implemented by a sub-command.

        :param parser: A parser.
        :type parser: argparse.ArgumentParser
        :return: void
        """
        raise NotImplementedError()

    @classmethod
    def init_subparser(cls, subparsers):
        """
        Initialize the argument parser and help for the specific sub-command.

        :param subparsers: A subparser.
        :type subparsers: argparse.ArgumentParser
        :return: void
        """
        parser = subparsers.add_parser(cls._name(), help=cls._help())
        cls._add_arguments(parser)
        parser.set_defaults(func=cls.execute)

    @classmethod
    @abc.abstractmethod
    def execute(cls, args):
        """
        Execute the command.

        Must be implemented by a sub-command.

        :param args: argparse arguments.
        :return: 0 on success.
        """
        raise NotImplementedError()


class HelloCmd(SubCommand):
    """Prints a welcome message."""

    @classmethod
    def _name(cls):
        return 'hello'

    @classmethod
    def _add_arguments(cls, parser):
        parser.add_argument('name', help='Name to greet.')
        return parser

    @classmethod
    def execute(cls, args):
        """Execute the command."""
        print_hello_world(args.name)

        return 0


def main(argv=None):
    """
    Start the Example tool.

    :return: 0 on success.
    """
    if not argv:
        argv = sys.argv

    # Parse arguments
    parser = argparse.ArgumentParser(prog=argv[0])
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)

    subparser = parser.add_subparsers(title='Example Commands', description='Valid example commands.')
    HelloCmd.init_subparser(subparser)

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
