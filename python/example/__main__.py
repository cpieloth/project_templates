"""Entry point for package."""

import sys

import example.cmdline


def main():
    """
    Execute the CLI entry point.
    """
    return example.cmdline.main()


if __name__ == '__main__':
    sys.exit(main())
