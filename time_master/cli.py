"""Console script for time_master."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("time-master")
    click.echo("=" * len("time-master"))
    click.echo("Time Warrior and Task Warrior simple CLI.")


if __name__ == "__main__":
    main()  # pragma: no cover
