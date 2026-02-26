"""Task automation"""

import click

@click.command()
def schedule():
    """Schedule tasks"""
    click.echo("Scheduler")