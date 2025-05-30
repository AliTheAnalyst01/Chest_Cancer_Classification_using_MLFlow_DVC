import os
import json
import joblib
import base64
import yaml
from typing import Any, Dict, List, Optional
from CNNClassifier import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): log directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save binary file

    Args:
        data (Any): Data to be saved as binary
        path (Path): Path to binary file
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")



@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary data from file

    Args:
        path (Path): Path to binary file

    Returns:
        Any: Object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Get file size in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: File size in KB, formatted as string
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


def decode_image(img_string: str, file_name: Path) -> None:
    """Decode base64 image data and save to file.

    Args:
        img_string (str): Base64 encoded image string
        file_name (Path): Path to save the decoded image
    """
    img_data = base64.b64decode(img_string)
    with open(file_name, 'wb') as f:
        f.write(img_data)
    # File automatically closed by context manager

def encode_image_to_base64(image_path: Path) -> str:
    """Encode image file to base64 string.

    Args:
        image_path (Path): Path to image file

    Returns:
        str: Base64 encoded image string
    """
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')