import click
from mini_devops_cli import __version__
from mini_devops_cli.commands.log_reader import logs_group
from mini_devops_cli.commands.system_monitor import monitor
from mini_devops_cli.commands.docker_manager import docker_group

@click.group()
@click.version_option(version=__version__, prog_name="mini-devops")
def main():
    """Mini DevOps CLI Tool - A command-line tool for common DevOps tasks."""
    pass

main.add_command(monitor)
main.add_command(docker_group)
main.add_command(logs_group)

if __name__ == "__main__":
    main()