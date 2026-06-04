import asyncio
import os
import tempfile
from pathlib import Path

from pystarter.utils.file_helper import ensure_folder_exists, is_file_empty


def test_is_file_empty():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("")
        tmp_path = f.name
    try:
        assert is_file_empty(tmp_path) is True
    finally:
        os.unlink(tmp_path)

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("data")
        tmp_path = f.name
    try:
        assert is_file_empty(tmp_path) is False
    finally:
        os.unlink(tmp_path)


def test_ensure_folder_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        folder = Path(tmpdir) / "new_folder"
        asyncio.run(ensure_folder_exists(str(folder)))
        assert folder.exists()
        assert folder.is_dir()
