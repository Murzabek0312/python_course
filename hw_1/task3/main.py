import sys

import click


def count_stats(input):
    lines_count = 0
    words_count = 0
    bytes_count = 0

    for line in input:
        lines_count += 1
        words_count += len(line.split())
        bytes_count += len(line.encode('utf-8'))
    return lines_count, words_count, bytes_count


def print_stats(lines, words, bytes, filename=None):
    if filename:
        click.echo(f"{lines:8}{words:8}{bytes:8} {filename}")
    else:
        click.echo(f"{lines:8}{words:8}{bytes:8}")


@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def wc_command(files):
    if not files:
        lines, words, bytes = count_stats(sys.stdin)
        print_stats(lines, words, bytes)
    elif len(files) == 1:
        with open(files[0], 'r') as f:
            lines, words, bytes = count_stats(f)
            print_stats(lines, words, bytes, files[0])
    else:
        total_lines = 0
        total_words = 0
        total_bytes = 0

        for file in files:
            with open(file, 'r') as f:
                lines, words, bytes = count_stats(f)
                print_stats(lines, words, bytes, file)

                total_lines += lines
                total_words += words
                total_bytes += bytes
        print_stats(total_lines, total_words, total_bytes, "total")


if __name__ == "__main__":
    wc_command()
