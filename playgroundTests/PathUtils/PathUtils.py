import os
import shutil

from LoggingSetup import getLogger
logger = getLogger(__name__)

def is_dir(path):
    try:
        return os.path.isdir(path)
    except Exception as e:
        logger.error(f"Error checking is path a dir: {e}")


def create_directory(path):
    """Create a directory at the specified path."""
    try:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created: {path}")
    except Exception as e:
        logger.error(f"Error creating directory: {e}")


def delete_directory(path):
    """Delete a directory at the specified path."""
    try:
        shutil.rmtree(path)
        logger.info(f"Directory deleted: {path}")
    except Exception as e:
        logger.error(f"Error deleting directory: {e}")


def list_files_in_directory(path):
    """List all files in the specified directory."""
    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return files
    except Exception as e:
        logger.error(f"Error listing files: {e}")
        return []


def list_directories_in_directory(path):
    """List all directories in the specified directory."""
    try:
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        return directories
    except Exception as e:
        logger.error(f"Error listing directories: {e}")
        return []


def iterate_directory(path):
    """Iterate through all files and directories in the specified path."""
    try:
        for root, dirs, files in os.walk(path):
            print(f"Root: {root}")
            print(f"Directories: {dirs}")
            print(f"Files: {files}")
    except Exception as e:
        logger.error(f"Error iterating directory: {e}")


def delete_file(path):
    """Delete a file at the specified path."""
    try:
        os.remove(path)
        logger.info(f"File deleted: {path}")
    except Exception as e:
        logger.error(f"Error deleting file: {e}")


def create_file(path, content=""):
    """Create a file at the specified path with optional content."""
    try:
        with open(path, "w") as file:
            file.write(content)
        logger.info(f"File created: {path}")
    except Exception as e:
        logger.error(f"Error creating file: {e}")



def exists(path):
    """Check if a file or directory exists at the specified path."""
    return os.path.exists(path)


def get_last_element(path:str):
    return path.split("/")[-1]