"""An example API module."""


def print_hello_world(name='foo'):
    """
    Print 'Hello <name>!' to stdout.

    :param name: Name to say hello.
    :return: Printed string.
    """
    out = 'Hello {}!'.format(name)
    print(out)
    return out
