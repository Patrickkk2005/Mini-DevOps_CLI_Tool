"""System monitor command"""

import click
import time
import psutil

def get_colour(percent:float)->str:
    """Get a colour based on percentage"""
    if percent <60:
        return "green"
    elif percent <85:
        return "yellow"
    return "red"

def show_stats()->None:
    """Show system monitor stats"""
    cpu=psutil.cpu_percent(interval=1)
    mem=psutil.virtual_memory()
    disk=psutil.disk_usage('/')

    click.echo("\n"+"="*40)
    click.echo("System Resource Monitor")
    click.echo("="*40)

    click.echo(click.style(f"CPU Usage: {cpu:.1f}%", fg=get_colour(cpu)))

    mem_used_gb = mem.used / (1024**3)
    mem_total_gb = mem.total / (1024**3)
    click.echo(click.style(f"Memory Usage: {mem_used_gb:.1f} GB / {mem_total_gb:.1f} GB", fg=get_colour(mem.percent)))

    disk_used_gb = disk.used / (1024**3)
    disk_total_gb = disk.total / (1024**3)
    click.echo(click.style(f"Disk Usage: {disk_used_gb:.1f} GB / {disk_total_gb:.1f} GB", fg=get_colour(disk.percent)))

    click.echo("="*40+"\n")

@click.command()
@click.option(
    "--watch", "-w",
    default=0,
    metavar="SECONDS",
    help="Refresh every N seconds. 0 is run once"
)
def monitor(watch: int)->None:
    """Display system monitor"""
    if watch==0:
        show_stats()
    else:
        click.echo(f"Watching every {watch} seconds---press Ctrl+C to exit")
        try:
            while True:
                show_stats()
                time.sleep(watch)
        except KeyboardInterrupt:
            click.echo("\nStopping...")