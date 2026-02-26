"""Docker"""

import click

@click.command()
def docker():
    """Manage Docker"""
    click.echo("Docker")