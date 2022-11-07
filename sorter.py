import os
import os.path
import shutil
import exifread
CURRENT_PATH = os.getcwd()
IMAGE_PATH = f"{CURRENT_PATH}/images/"
DIRS_PATH = f"{CURRENT_PATH}/cleaned/"
PHOTO_FORMATS = ["png", "jpg", "jpeg", "raw", "cr2", "nef", "orf", "sr2"]
VIDEO_FORMATS = ["webm", "mkv", "flv", "vob", "ogv", "ogg", "drc", "gif", "gifv", "mng", "avi", "mts", "m2ts", "ts", "mov", "qt", "wmv", "yuv", "rm", "rmvb", "viv", "asf", "amv", "mp4", "m4p", "m4v", "mpg", "mp2", "mpeg", "mpe", "mpv", "mpg", "mpeg", "m2v", "m4v", "svi", "3gp", "3g2", "mxf", "roq", "nsv", "flv*"]
VIDEO1_FORMATS = []
OTHER_FORMATS = []
IMAGES = []
VIDEOS = []
print("Cleaning formats lists")
for format in VIDEO_FORMATS:
    if not format in VIDEO1_FORMATS:
        VIDEO1_FORMATS.append(format)
print("Video formats ready")
print("Checking paths")
if not os.path.exists(DIRS_PATH):
	os.mkdir(DIRS_PATH)
def get_photos(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            for format in PHOTO_FORMATS:
                if f.lower().endswith(format):
                    IMAGES.append(os.path.join(root, f))
            for format in VIDEO1_FORMATS:
                if f.lower().endswith(format):
                    VIDEOS.append(os.path.join(root, f))

fail_count = 0
success_count = 0

for img in IMAGES:
    with open(img, "rb") as file:
        tags = exifread.process_file(file, details=False, stop_tag="DateTimeOriginal")
        try:
            if "EXIF DateTimeOriginal" in tags:
                date_path = str(tags["EXIF DateTimeOriginal"])[:10].replace(":", ".")
                success_count += 1
            if not "EXIF DateTimeOriginal" in tags and "EXIF ModifyDate" in tags:
                date_path = str(tags["EXIF ModifyDate"])[:10].replace(":", ".")
                success_count += 1
        except:
            print(str(img) + " does not have EXIF tags.")
            fail_count += 1
            date_path = "0000"
            y = str(tags["YResolution"])
            x = str(tags["XResolution"])
            if y < x:
                if not os.path.exists(DIRS_PATH + date_path + "vaaka"):
                    os.mkdir(DIRS_PATH + date_path + "vaaka")
            elif x < y:
                if not os.path.exists(DIRS_PATH + date_path + "pysty"):
                    os.mkdir(DIRS_PATH + date_path + "pysty")
            elif x == y:
                if not os.path.exists(DIRS_PATH + date_path + "nelio"):
                    os.mkdir(DIRS_PATH + date_path + "nelio")
	shutil.move(img, dirs_path + date_path + "\\" + img[-12:])

print("Sorted " + str(success_count) + " files.") # Images properly sorted by date taken
print("Failed to sort " + str(fail_count) + " files.") # Images sent to 0000