import click
from mini_devops_cli import __version__
from mini_devops_cli.commands.system_monitor import monitor

@click.group()
@click.version_option(version=__version__, prog_name="mini-devops")
def main():
    """Mini DevOps CLI Tool - A command-line tool for common DevOps tasks."""
    pass

main.add_command(monitor)

if __name__ == "__main__":
    main()