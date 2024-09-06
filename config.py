import os

# Constants for file format types
PHOTO_FORMATS = ["png", "jpg", "jpeg", "raw", "cr2", "nef", "orf", "sr2"]

VIDEO_FORMATS = [
    "webm",
    "mkv",
    "flv",
    "vob",
    "ogv",
    "ogg",
    "drc",
    "gif",
    "gifv",
    "mng",
    "avi",
    "mts",
    "m2ts",
    "ts",
    "mov",
    "qt",
    "wmv",
    "yuv",
    "rm",
    "rmvb",
    "viv",
    "asf",
    "amv",
    "mp4",
    "m4p",
    "m4v",
    "mpg",
    "mp2",
    "mpeg",
    "mpe",
    "mpv",
    "m2v",
    "svi",
    "3gp",
    "3g2",
    "mxf",
    "roq",
    "nsv",
    "flv*",
]

VIDEO1_FORMATS = []
OTHER_FORMATS = []
IMAGES = []
VIDEOS = []
DATE_FOR = ["DateTimeOriginal", "ModifyDate"]

# Path constants
CURRENT_PATH = os.getcwd()
IMAGE_PATH = os.path.join(CURRENT_PATH, "images")
DIRS_PATH = os.path.join(CURRENT_PATH, "cleaned")

# Counters
FAIL_COUNT = 0
SUCCESS_COUNT = 0


# Function to add video formats to VIDEO1_FORMATS
def update_video_formats():
    """Ensure VIDEO1_FORMATS includes all formats from VIDEO_FORMATS."""
    for fmt in VIDEO_FORMATS:
        if fmt not in VIDEO1_FORMATS:
            VIDEO1_FORMATS.append(fmt)


# Call this function to initialize VIDEO1_FORMATS
update_video_formats()

print(f"Current image path: {IMAGE_PATH}")
print(f"Current cleaned directory path: {DIRS_PATH}")
print(f"Supported photo formats: {PHOTO_FORMATS}")
print(f"Supported video formats: {VIDEO_FORMATS}")
print(f"Initialized VIDEO1_FORMATS: {VIDEO1_FORMATS}")
