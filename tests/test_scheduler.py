from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from mini_devops_cli.cli import main


@patch("mini_devops_cli.commands.scheduler.subprocess")
def test_schedule_once(mock_subprocess):
    mock_subprocess.run.return_value = MagicMock(returncode=0)
    result = CliRunner().invoke(main, ["schedule", "once", "echo hello"])
    assert result.exit_code == 0
    mock_subprocess.run.assert_called_once()


@patch("mini_devops_cli.commands.scheduler.time")
@patch("mini_devops_cli.commands.scheduler.subprocess")
def test_schedule_once_delay(mock_subprocess, mock_time):
    mock_subprocess.run.return_value = MagicMock(returncode=0)
    result = CliRunner().invoke(main, ["schedule", "once", "echo hello", "--delay", "5"])
    assert result.exit_code == 0
    mock_time.sleep.assert_called_once_with(5)


@patch("mini_devops_cli.commands.scheduler.subprocess")
def test_schedule_run_times(mock_subprocess):
    mock_subprocess.run.return_value = MagicMock(returncode=0)
    result = CliRunner().invoke(main, ["schedule", "run", "echo hello", "--every", "0", "--times", "3"])
    assert result.exit_code == 0
    assert mock_subprocess.run.call_count == 3
    assert "Completed 3 run(s)" in result.output
