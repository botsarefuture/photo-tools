import os
FAIL_COUNT = 0
SUCCESS_COUNT = 0
CURRENT_PATH = os.getcwd()
IMAGE_PATH = f"{CURRENT_PATH}/images/"
DIRS_PATH = f"{CURRENT_PATH}/cleaned/"
PHOTO_FORMATS = ["png", "jpg", "jpeg", "raw", "cr2", "nef", "orf", "sr2"]
VIDEO_FORMATS = ["webm", "mkv", "flv", "vob", "ogv", "ogg", "drc", "gif", "gifv", "mng", "avi", "mts", "m2ts", "ts", "mov", "qt", "wmv", "yuv", "rm", "rmvb", "viv", "asf", "amv", "mp4", "m4p", "m4v", "mpg", "mp2", "mpeg", "mpe", "mpv", "mpg", "mpeg", "m2v", "m4v", "svi", "3gp", "3g2", "mxf", "roq", "nsv", "flv*"]
VIDEO1_FORMATS = []
OTHER_FORMATS = []
IMAGES = []
VIDEOS = []
DATE_FOR = ["DateTimeOriginal", "ModifyDate"]