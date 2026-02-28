"""File management"""

import click
import shutil
from pathlib import Path
from datetime import datetime

@click.group(name="files")
def files_group():
    """Manage Files"""
    pass

@files_group.command(name="copy")
@click.argument("src")
@click.argument("dst")
def copy(src:str, dst:str)->None:
    """Copy a file"""
    source=Path(src)
    if not source.exists():
        click.echo(click.style(f"Source {src} does not exist", fg="red"))
        raise SystemExit(1)
    if source.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)
    click.echo(click.style(f"Copied {src} to {dst}", fg="green"))


@files_group.command(name="backup")
@click.argument("path")
def backup(path:str)->None:
    """Backup a file"""
    backup=Path(path)
    if not backup.exists():
        click.echo(click.style(f"Backup {path} does not exist", fg="red"))
        raise SystemExit(1)
    if not backup.is_file():
        click.echo(click.style(f"Backup {path} not a file", fg="yellow"))
        raise SystemExit(1)
    timestamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    backup_path=Path(f"{path}.{timestamp}")
    shutil.copy2(backup, backup_path)
    click.echo(click.style(f"Backup {backup_path} created", fg="green"))


@files_group.command(name="find")
@click.argument("directory")
@click.argument("pattern")
def find(directory:str, pattern:str)->None:
    """Find files in a directory"""
    d=Path(directory)
    if not d.is_dir():
        click.echo(click.style(f"Directory {directory} does not exist", fg="red"))
        raise SystemExit(1)
    matches=list(d.rglob(pattern))
    if not matches:
        click.echo(click.style(f"No matching files", fg="yellow"))
        return
    for match in sorted(matches):
        click.echo(match)