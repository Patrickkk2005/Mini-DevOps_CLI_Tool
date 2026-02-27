"""Docker"""

import click
import sys

try:
    import docker
    from docker.errors import DockerException, NotFound, APIError
except ImportError:
    docker = None


def get_client():
    if docker is None:
        click.echo(click.style("Error: docker not installed",fg="red"))
        sys.exit(1)
    try:
        client = docker.from_env()
        client.ping()
        return client
    except DockerException:
        click.echo(click.style("Error: cannot connect to docker, is it open?",fg="red"))
        sys.exit(1)


@click.group(name="docker")
def docker_group():
    """Manage Docker containers."""
    pass

@docker_group.command(name="ps")
@click.option("--all", "-a", "all_containers", is_flag=True, default=False, help="List all containers")
def ps(all_containers: bool)->None:
    client = get_client()
    containers=client.containers.list(all=all_containers)

    if not containers:
        click.echo("no containers found")
        return

    click.echo(f"\n {'ID':<12} {'NAME':<25} {'IMAGE':<25} {'STATUS':<15}")
    click.echo("-"*77)

    for c in containers:
        colour = "green" if c.status == "running" else "yellow"
        click.echo(click.style(f"{c.short_id:<12} {c.name:<25} {c.image.tags[0] if c.image.tags else 'none':<25} {c.status:<15}", fg=colour))
    click.echo()

@docker_group.command(name="start")
@click.argument("name")
def start(name: str)->None:
    client = get_client()
    try:
        container=client.containers.get(name)
        container.start()
        click.echo(click.style(f"Started {name}",fg="green"))
    except NotFound:
        click.echo(click.style(f"{name} not found",fg="red"))
    except APIError as err:
        click.echo(click.style(f"API error: {err}",fg="red"))


@docker_group.command(name="stop")
@click.argument("name")
def stop(name: str)->None:
    client = get_client()
    try:
        container=client.containers.get(name)
        container.stop()
        click.echo(click.style(f"Stopped {name}",fg="green"))
    except NotFound:
        click.echo(click.style(f"{name} not found",fg="red"))
    except APIError as err:
        click.echo(click.style(f"API error: {err}",fg="red"))
