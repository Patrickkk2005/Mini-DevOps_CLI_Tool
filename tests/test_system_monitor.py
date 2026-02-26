from click.testing import CliRunner
from mini_devops_cli.cli import main


def test_monitor_runs():
    """Test that it runs"""
    runner = CliRunner()
    result = runner.invoke(main, ["monitor"])
    assert result.exit_code == 0


def test_monitor_shows_cpu():
    """Test that output contains CPU"""
    runner = CliRunner()
    result = runner.invoke(main, ["monitor"])
    assert "CPU" in result.output


def test_monitor_shows_memory():
    """Test that output contains memory"""
    runner = CliRunner()
    result = runner.invoke(main, ["monitor"])
    assert "Memory" in result.output


def test_monitor_shows_disk():
    """Test that output contains disk"""
    runner = CliRunner()
    result = runner.invoke(main, ["monitor"])
    assert "Disk" in result.output


def test_monitor_help():
    """Test that help works."""
    runner = CliRunner()
    result = runner.invoke(main, ["monitor", "--help"])
    assert result.exit_code == 0
    assert "system" in result.output.lower()
