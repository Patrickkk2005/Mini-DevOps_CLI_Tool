"""Log"""

import re
import click
from pathlib import Path

def validate_file(path:str)->Path:
    """Return True if path is valid"""
    p=Path(path)
    if not p.exists():
        click.echo(click.style(f"Error: File not found: {path}", fg="red"))
        raise SystemExit(1)
    if not p.is_file():
        click.echo(click.style(f"Error: Not a file: {path}", fg="red"))
        raise SystemExit(1)
    return p

@click.group(name="logs")
def logs_group():
    """Manage logs"""
    pass

@logs_group.command(name="read")
@click.argument("path")
@click.option("--lines", "-n", default=20, help="Number of lines to dsiplay(default: 20)")
def read(path:str, lines:int)->None:
    """Read logs"""
    path=validate_file(path)
    all_lines=path.read_text().splitlines()
    for line in all_lines[-lines:]:
        click.echo(line)

@logs_group.command(name="filter")
@click.argument("path")
@click.argument("keyword")
@click.option("--ignore-case", "-i", is_flag=True, default=False, help="Matching search")
def filter_logs(path:str, keyword:str, ignore_case:bool)->None:
    """Filter logs"""
    path=validate_file(path)
    flags=re.IGNORECASE if ignore_case else 0
    matched=0
    for line in path.read_text().splitlines():
        if re.search(keyword,line,flags):
            click.echo(line)
            matched+=1
    if matched==0:
        click.echo(click.style(f"No lines matched '{keyword}'.", fg="yellow"))


@logs_group.command(name="watch")
@click.argument("path")
def watch(path:str)->None:
    """Watch logs"""
    import time
    path=validate_file(path)
    click.echo(f"Watching {path}  click Ctrl+C to stop")
    with path.open("r") as file:
        file.seek(0,2)
        try:
            while True:
                line=file.readline()
                if line:
                    click.echo(line, nl=False)
                else:
                    time.sleep(1)
        except KeyboardInterrupt:
            click.echo("\n Stopped watching...")