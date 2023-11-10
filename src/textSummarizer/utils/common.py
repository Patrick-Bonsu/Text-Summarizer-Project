import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox.

    Args:
        path_to_yaml (str): Path to the YAML file.

    Raises:
        ValueError: if yaml file is empty
        FileNotFoundError: If the YAML file is not found
        BoxValueError: If there is an issue with Box
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml,'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Content of YAML file {path_to_yaml}: {content}")
            if not content:
                raise ValueError("YAML file is empty")
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            print(type(content))
            return ConfigBox(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file not found at: {path_to_yaml}")
    except BoxValueError:
        raise ValueError("Failed to create ConfigBox. YAML file may be empty or malformed.")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    
