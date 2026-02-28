"""Task automation"""

import click
import time
import subprocess
from datetime import datetime

@click.group(name="schedule")
def schedule_group():
    """Schedule commands"""
    pass

@schedule_group.command(name="once")
@click.argument("command")
@click.option("--delay", "-d", default=0, type=int, help="Wait n seconds before executing command")
def schedule_once(command: str, delay: int) -> None:
    """Schedule a command once"""
    if delay:
        click.echo(f"Waiting {delay}s before executing....")
        time.sleep(delay)
    timestamp=datetime.now().strftime("%H:%M:%S")
    click.echo(f"[{timestamp}] Running: {command}")
    subprocess.run(command, shell=True, text=True)

@schedule_group.command(name="run")
@click.argument("command")
@click.option("--every", "-e", required=True, type=int, help="Wait n seconds before executing command")
@click.option("--times","-t", required=True, default=0, type=int, help="Number of times to run, 0 = infinite")
def schedule_run(command: str, every: int, times: int) -> None:
    """Schedule a command run"""
    click.echo(f"Scheduling {command}...")
    click.echo(f"Interval: {every}s" + (f", {times} times" if times else ", until Ctrl+C"))
    click.echo("-"*40)
    count=0;
    try:
        while True:
            count+=1
            timestamp=datetime.now().strftime("%H:%M:%S")
            click.echo(f"[{timestamp}] Run #{count}")
            subprocess.run(command, shell=True, text=True)
            if times and count >= times:
                click.echo(click.style(f"Completed {times} run(s)", fg="green"))
                break
            time.sleep(every)
    except KeyboardInterrupt:
        click.echo(click.style(f"Stopped after {count} run(s)", fg="yellow"))