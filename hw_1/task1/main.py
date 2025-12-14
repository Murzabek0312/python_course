import click
import sys

@click.command()
@click.argument('filename', required=False, type=click.File('r'))
def nl_command(filename):
    input = filename if filename else sys.stdin

    line_number = 1
    for line in input:
        click.echo(f"{line_number:>6}\t{line}", nl=False)
        line_number+=1

    if filename:
        filename.close()


if __name__ == '__main__':
    nl_command()
