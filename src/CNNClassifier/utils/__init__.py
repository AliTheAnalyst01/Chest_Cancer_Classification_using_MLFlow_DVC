from CNNClassifier.utils.common import (
    read_yaml,
    create_directories,
    load_json,
    save_bin,
    load_bin,
    get_size,
    decode_image,
    encode_image_to_base64
)

# Adding this function for the DataIngestion class
def unzip_file(file_path, extract_path):
    """Unzip a file to the specified path

    Args:
        file_path (Path): Path to the zip file
        extract_path (Path): Path to extract the zip file
    """
    import zipfile
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)