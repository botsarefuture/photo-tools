import os
import os.path
import shutil
import exifread
from funcs import calculate_aspect, suunta, format_date, date, suunta_maaritus
from config import VIDEO1_FORMATS, VIDEO_FORMATS, PHOTO_FORMATS, DIRS_PATH, IMAGES, VIDEOS, SUCCESS_COUNT, FAIL_COUNT, DATE_FOR

print("Cleaning formats lists")
for format in VIDEO_FORMATS:
    if not format in VIDEO1_FORMATS:
        VIDEO1_FORMATS.append(format)
print("Video formats ready")
print("Checking paths")
if not os.path.exists(DIRS_PATH):
	os.mkdir(DIRS_PATH)

for img in IMAGES:
    with open(img, "rb") as file:
        tags = exifread.process_file(file, details=False, stop_tag="DateTimeOriginal")
        try:
            
            success = False
            for item in DATE_FOR:
                if not success == True:
                    if f"EXIF {item}" in tags:
                        day, month, year = date(str(tags[f"EXIF {item}"])[:10].replace(":", "."))
                        date_path = format_date(day, month, year)
                        SUCCESS_COUNT += 1
                        success = True

        except:
            print(str(img) + " does not have EXIF tags.")
            FAIL_COUNT += 1
            date_path = "0000"
        y = str(tags["YResolution"])
        x = str(tags["XResolution"])
        suunta_path = suunta_maaritus(date_path, y, x)

    shutil.move(img, DIRS_PATH + date_path + "/"  + suunta_path + "/" + img[-12:])

print("Sorted " + str(SUCCESS_COUNT) + " files.") # Images properly sorted by date taken
print("Failed to sort " + str(FAIL_COUNT) + " files.") # Images sent to 0000