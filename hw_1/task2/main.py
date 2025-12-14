import click
import sys


def print_last_lines(input, n_lines=10):
    lines = input.readlines()

    last_lines = lines[-n_lines:] if len(lines) > n_lines else lines

    for line in last_lines:
        click.echo(line, nl=False)


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
def tail_command(files):
    if not files:
        print_last_lines(sys.stdin, 17)
    elif len(files) == 1:
        try:
            with open(files[0], "r") as f:
                print_last_lines(f)
        except Exception as e:
            click.echo(f"Ошибка чтения файла: {files[0]}: {e}", err=True)
    else:
        for i, filename in enumerate(files):
            if i > 0:
                click.echo()
            click.echo(f"==> {filename} <==")

            try:
                with open(filename, "r") as f:
                    print_last_lines(f)
            except Exception as e:
                click.echo(f"Ошибка чтения файла: {filename}: {e}", err=True)


if __name__ == "__main__":
    tail_command()
