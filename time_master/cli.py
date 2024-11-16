"""Console script for time_master."""

import click

from time_master.commands.core import about


@click.group()
def main() -> None:
    """Main entrypoint."""
    click.echo("time-master")
    click.echo("=" * len("time-master"))
    click.echo("Time Warrior and Task Warrior simple CLI.")


main.add_command(about)

if __name__ == "__main__":
    main()  # pragma: no cover
