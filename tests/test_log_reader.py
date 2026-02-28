from click.testing import CliRunner
from mini_devops_cli.cli import main

def test_log_reader(tmp_path):
    log=tmp_path/"app.log"
    log.write_text("test1\ntest2\ntest3\n")
    result = CliRunner().invoke(main, ["logs", "read", str(log), "--lines", "3"])
    assert result.exit_code == 0
    assert "test1" in result.output
    assert "test2" in result.output
    assert "test3" in result.output

def test_filter_match(tmp_path):
    log=tmp_path/"app.log"
    log.write_text("test1\ntest2\ntest3\n")
    result=CliRunner().invoke(main, ["logs", "filter", str(log), "test2"])
    assert result.exit_code == 0
    assert "test2" in result.output

def test_filter_not_match(tmp_path):
    log=tmp_path/"app.log"
    log.write_text("test1\ntest2\ntest3\n")
    result=CliRunner().invoke(main, ["logs", "filter", str(log), "blabla"])
    assert result.exit_code == 0
    assert "No lines matched" in result.output

def test_filter_ignore_case(tmp_path):
    log=tmp_path/"app.log"
    log.write_text("test1\ntest2\ntest3\n")
    result=CliRunner().invoke(main, ["logs", "filter", str(log), "TEST2", "--ignore-case"])
    assert result.exit_code == 0
    assert "test2" in result.output

def test_logs_read_not_found():
    result=CliRunner().invoke(main, ["logs", "read", "/blalblalbla/path.log"])
    assert result.exit_code != 0
    assert "not found" in result.output