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

def date(text):
    year = text[0:4]
    month = text[5:7]
    day = text[8:10]
    return day, month, year

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

def format_date(day, month, year):
    return f"{day}.{month}.{year}"

def format_suunta(y, x, suunta_path):
    if y == 720:
        suunta_path += "/720p"
    elif y == 1080 and x == 1920 or x == 1080 and x == 1920:
        suunta_path += "/1080p"
    elif y == 1080 and x == 2048 or x == 1080 and y == 2048:
        suunta_path += "/2k"
    elif y == 2160 and x == 3840 or x == 2160 and y == 3840:
        suunta_path += "/4k"
    else:
        suunta_path = f"/{y}"
    return suunta_path

for img in IMAGES:
    with open(img, "rb") as file:
        tags = exifread.process_file(file, details=False, stop_tag="DateTimeOriginal")
        try:
            if "EXIF DateTimeOriginal" in tags:
                item = "DateTimeOriginal"
                day, month, year = date(str(tags[f"EXIF {item}"])[:10].replace(":", "."))
                date_path = format_date(day, month, year)
                success_count += 1
            if not "EXIF DateTimeOriginal" in tags:
                item = "ModifyDate"
                day, month, year = date(str(tags[f"EXIF {item}"])[:10].replace(":", "."))
                date_path = format_date(day, month, year)
                success_count += 1
        except:
            print(str(img) + " does not have EXIF tags.")
            fail_count += 1
            date_path = "0000"
        y = str(tags["YResolution"])
        x = str(tags["XResolution"])
        if y < x:
            suunta_path = "vaaka"
            if not os.path.exists(DIRS_PATH + date_path + suunta_path):
                os.mkdir(DIRS_PATH + date_path + suunta_path)
            suunta_path = format_suunta(y, x, suunta_path)

        elif x < y:
            suunta_path = "pysty"
            if not os.path.exists(DIRS_PATH + date_path + "pysty" ):
                os.mkdir(DIRS_PATH + date_path + "pysty")
            suunta_path = format_suunta(y, x, suunta_path)
            
        elif x == y:
            suunta_path = "nelio"
            if not os.path.exists(DIRS_PATH + date_path + "nelio"):
                os.mkdir(DIRS_PATH + date_path + "nelio")
            suunta_path = format_suunta(y, x, suunta_path)

    shutil.move(img, DIRS_PATH + date_path + "/"  + suunta_path + "/" + img[-12:])

print("Sorted " + str(success_count) + " files.") # Images properly sorted by date taken
print("Failed to sort " + str(fail_count) + " files.") # Images sent to 0000