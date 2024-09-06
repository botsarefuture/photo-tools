import os
import shutil
import exifread
from funcs import calculate_aspect, suunta, format_date, date, suunta_maaritus
from config import VIDEO1_FORMATS, VIDEO_FORMATS, PHOTO_FORMATS, DIRS_PATH, IMAGES, VIDEOS, SUCCESS_COUNT, FAIL_COUNT, DATE_FOR

def update_video_formats():
    """Ensure VIDEO1_FORMATS includes all formats from VIDEO_FORMATS."""
    for format in VIDEO_FORMATS:
        if format not in VIDEO1_FORMATS:
            VIDEO1_FORMATS.append(format)
    print("Video formats updated.")

def ensure_directories_exist():
    """Create the base directory if it does not exist."""
    if not os.path.exists(DIRS_PATH):
        os.mkdir(DIRS_PATH)
    print("Directories checked.")

def process_image(img_path):
    """Process an individual image and move it to the appropriate directory."""
    global SUCCESS_COUNT, FAIL_COUNT
    
    try:
        with open(img_path, "rb") as file:
            tags = exifread.process_file(file, details=False, stop_tag="DateTimeOriginal")

            date_path = extract_date_path(tags)
            suunta_path = calculate_suunta_path(tags, date_path)

            destination = os.path.join(DIRS_PATH, date_path, suunta_path, os.path.basename(img_path))
            shutil.move(img_path, destination)
            SUCCESS_COUNT += 1
            return True
    except Exception as e:
        print(f"{img_path} processing failed: {e}")
        FAIL_COUNT += 1
        return False

def extract_date_path(tags):
    """Extract and format the date path from EXIF tags."""
    for item in DATE_FOR:
        if f"EXIF {item}" in tags:
            date_str = str(tags[f"EXIF {item}"])[:10].replace(":", ".")
            day, month, year = date(date_str)
            return format_date(day, month, year)
    return "0000"

def calculate_suunta_path(tags, date_path):
    """Calculate the suunta path based on EXIF tags."""
    y_res = str(tags.get("YResolution", "0"))
    x_res = str(tags.get("XResolution", "0"))
    return suunta_maaritus(date_path, y_res, x_res)

def main():
    print("Cleaning formats lists")
    update_video_formats()

    print("Checking paths")
    ensure_directories_exist()

    print("Processing images")
    for img in IMAGES:
        process_image(img)

    print(f"Sorted {SUCCESS_COUNT} files.")  # Images properly sorted by date taken
    print(f"Failed to sort {FAIL_COUNT} files.")  # Images sent to 0000

if __name__ == "__main__":
    main()
