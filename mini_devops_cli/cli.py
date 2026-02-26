import click
from mini_devops_cli import __version__

@click.group()
@click.version_option(version=__version__, prog_name="mini-devops")
def main():
    """Mini DevOps CLI Tool - A command-line tool for common DevOps tasks."""
    pass

if __name__ == "__main__":
    main()