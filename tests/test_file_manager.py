from click.testing import CliRunner
from mini_devops_cli.cli import main


def test_files_copy(tmp_path):
    src = tmp_path / "hello.txt"
    src.write_text("hello world")
    dst = tmp_path / "hello_copy.txt"
    result = CliRunner().invoke(main, ["files", "copy", str(src), str(dst)])
    assert result.exit_code == 0
    assert dst.exists()
    assert "Copied" in result.output


def test_files_copy_not_found(tmp_path):
    result = CliRunner().invoke(main, ["files", "copy", "/fake/src.txt", str(tmp_path / "dst.txt")])
    assert result.exit_code != 0
    assert "does not exist" in result.output


def test_files_backup(tmp_path):
    src = tmp_path / "app.log"
    src.write_text("log data")
    result = CliRunner().invoke(main, ["files", "backup", str(src)])
    assert result.exit_code == 0
    assert "created" in result.output
    backups = list(tmp_path.glob("app.log.*"))
    assert len(backups) == 1


def test_files_find(tmp_path):
    (tmp_path / "a.log").write_text("log1")
    (tmp_path / "b.log").write_text("log2")
    (tmp_path / "c.txt").write_text("not a log")
    result = CliRunner().invoke(main, ["files", "find", str(tmp_path), "*.log"])
    assert result.exit_code == 0
    assert "a.log" in result.output
    assert "b.log" in result.output
    assert "c.txt" not in result.output


def test_files_find_no_match(tmp_path):
    (tmp_path / "readme.txt").write_text("hi")
    result = CliRunner().invoke(main, ["files", "find", str(tmp_path), "*.log"])
    assert result.exit_code == 0
    assert "No matching files" in result.output
