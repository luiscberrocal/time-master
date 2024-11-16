import sys
from platform import python_version

import click

from .. import __version__ as current_version


@click.command()
def about() -> None:
    """About Time Master."""
    banner_char = "-"
    app_name = "Time Master"
    display_name = f"{app_name} version {current_version}"
    length = len(display_name) + 4
    click.echo(banner_char * length)
    click.echo(f"{banner_char} {display_name} {banner_char}")
    click.echo(banner_char * length)
    click.echo(f"Operating System: {sys.platform}")
    click.echo(f"Python : {python_version()}")
