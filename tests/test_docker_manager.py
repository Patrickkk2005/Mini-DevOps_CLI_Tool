from unittest.mock import MagicMock, patch
from click.testing import CliRunner

import mini_devops_cli
from mini_devops_cli.cli import main

def mock_container(name="testtest", status="Running", image_tag="test:latest", short_id="guerh0jrkj"):
    c=MagicMock()
    c.short_id = short_id
    c.name = name
    c.image.tags = [image_tag]
    c.status = status
    return c

@patch("mini_devops_cli.commands.docker_manager.docker")
def test_docker_ps(mock_docker):
    mock_client=MagicMock()
    mock_docker.from_env.return_value=mock_client
    mock_client.containers.list.return_value=[mock_container("testtest", "running")]
    runner = CliRunner()
    result = runner.invoke(main, ["docker", "ps"])
    assert result.exit_code == 0
    assert "testtest" in result.output

@patch("mini_devops_cli.commands.docker_manager.docker")
def test_docker_ps_empty(mock_docker):
    mock_client=MagicMock()
    mock_docker.from_env.return_value=mock_client
    mock_client.containers.list.return_value=[]
    runner = CliRunner()
    result = runner.invoke(main, ["docker", "ps"])
    assert result.exit_code == 0
    assert "no containers found" in result.output

@patch("mini_devops_cli.commands.docker_manager.docker")
def test_docker_start(mock_docker):
    mock_client=MagicMock()
    mock_docker.from_env.return_value=mock_client
    mock_client.containers.get.return_value= MagicMock()
    runner = CliRunner()
    result = runner.invoke(main, ["docker", "start", "testtest" ])
    assert result.exit_code == 0
    assert "testtest" in result.output


@patch("mini_devops_cli.commands.docker_manager.docker")
def test_docker_stop(mock_docker):
    mock_client=MagicMock()
    mock_docker.from_env.return_value=mock_client
    mock_client.containers.get.return_value= MagicMock()
    runner = CliRunner()
    result = runner.invoke(main, ["docker", "stop", "testtest" ])
    assert result.exit_code == 0
    assert "testtest" in result.output

