"""System monitor command"""

import click

@click.command()
def monitor():
    """Display system monitor"""
    click.echo("System monitor")