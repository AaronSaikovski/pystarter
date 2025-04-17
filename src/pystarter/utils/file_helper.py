import asyncio
import os
from pathlib import Path

import aiofiles  # type: ignore

# ******************************************************************************** #


def is_file_empty(file_path: str) -> bool:
    """Checks to see if the file is empty

    Args:
        file_path (str): _description_

    Returns:
        bool: _description_
    """
    return os.path.getsize(file_path) == 0


# ******************************************************************************** #


async def write_output_file_async(
    output_file_path: str, output_content: str, logger
) -> bool:
    """Writes an output file - ASync version

    Args:
        output_file_path (str): _description_
        output_content (str): _description_
    """
    try:
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        async with aiofiles.open(output_file_path, "w", encoding="utf-8") as file:
            await file.write(output_content)
        return True
    except Exception as e:
        logger.error("An error occurred while writing the file:", exception=str(e))
        return False


# ******************************************************************************** #


async def delete_output_file_async(file_path: Path, logger) -> None:
    """Deletes a given output file - ASync version

    Args:
        output_file_path (str): _description_
        output_content (str): _description_
    """
    try:
        await asyncio.to_thread(os.remove, file_path)
        logger.info(f"{file_path} deleted successfully.")
    except FileNotFoundError:
        logger.error(f"{file_path} not found.")
    except PermissionError:
        logger.error(f"Permission denied to delete {file_path}.")
    except Exception as e:
        logger.error(f"Error occurred while deleting {file_path}:", exception=str(e))


# ******************************************************************************** #


async def ensure_folder_exists(folder_name: str) -> None:
    """Create a folder if it doesn't exist"""
    folder = Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)


# ******************************************************************************** #
