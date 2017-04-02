"""Module for CLI command implementations."""

import abc

__author__ = 'christof.pieloth'


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
    def _add_arguments(cls, subparsers):
        """
        Initialize the argument parser and help for the specific sub-command.

        Must be implemented by a sub-command.

        :param subparsers: A subparser.
        :type subparsers: argparse.ArgumentParser
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
        parser.set_defaults(func=cls.exec)

    @classmethod
    @abc.abstractmethod
    def exec(cls, args):
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
    def exec(cls, args):
        """Execute the command."""
        from example.io import print_hello_world

        print_hello_world(args.name)

        return 0
