# Photo and Video Processing Tool

## Description

This project is a photo and video processing tool that organizes images and videos based on their format and metadata. It sorts media files into directories based on their resolution and date taken, providing a structured and manageable way to handle large collections of media.

## Features

- **Aspect Ratio Calculation**: Calculates and returns the aspect ratio of images based on width and height.
- **Directory Management**: Creates and organizes directories based on media resolution and date.
- **Metadata Extraction**: Extracts metadata from images to sort them by date and resolution.
- **Format Handling**: Supports various image and video formats for processing.

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- Required Python packages

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mountainland/Photo.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Photo
    ```

3. **Install the required dependencies:**

    ```bash
    python3.7 -m pip install -r requirements.txt
    ```

4. **Set up the project:**

    - Configure paths and formats in the `config.py` file according to your needs.

## Usage

1. **Run the processing script:**

    ```bash
    python process_media.py
    ```

    This script will process images and videos, organizing them based on their metadata and resolution.

2. **Functions Overview:**

    - `calculate_aspect(width: int, height: int) -> str`: Computes the aspect ratio of an image.
    - `get_suunta_path(DIRS_PATH: str, date_path: str, y: int, x: int) -> str`: Determines the directory path based on image resolution.
    - `format_date(day: str, month: str, year: str) -> str`: Formats the date for directory naming.
    - `parse_date(text: str) -> tuple`: Parses a date string into day, month, and year.
    - `get_photos(path: str)`: Scans a directory for photos and videos, adding them to respective lists.
    - `determine_suunta(date_path: str, y: int, x: int) -> str`: Determines the orientation and appropriate directory for the media.

## Configuration

- **`config.py`**: Modify this file to set the paths, formats, and other configuration details.
    - `PHOTO_FORMATS`: List of supported photo file formats.
    - `VIDEO_FORMATS`: List of supported video file formats.
    - `DIRS_PATH`: Path where organized files will be stored.
    - `IMAGES`, `VIDEOS`: Lists to store image and video file paths.
    - `DATE_FOR`: List of EXIF tags used for extracting dates.

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow for contributing:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [Verso](mailto:verso@luova.club).
