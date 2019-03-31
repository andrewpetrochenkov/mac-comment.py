#!/usr/bin/env python
"""read/write Finder comment"""
import click
import comment

MODULE_NAME = "comment"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path [comment]' % MODULE_NAME


@click.command()
@click.argument('path', required=True)
@click.argument('srting', required=False)
def _cli(path, srting=None):
    if srting is not None:
        return comment.write(path, srting)
    srting = comment.read(path)
    if srting:
        print(srting)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
