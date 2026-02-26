"""Log"""

import click

@click.command()
def docker():
    """Read log"""
    click.echo("Log")