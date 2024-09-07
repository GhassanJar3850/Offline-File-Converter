ICON_COMPRESSED = "./Icons/compressed.png"
ICON_DOC = "./Icons/doc.png"
ICON_DOCX = "./Icons/docx.png"
ICON_IMAGE = "./Icons/image.png"
ICON_MUSIC = "./Icons/music.png"
ICON_PPT = "./Icons/ppt.png"
ICON_PDF = "./Icons/pdf.png"
ICON_SVG = "./Icons/svg.png"
ICON_VIDEO = "./Icons/video.png"
ICON_XLS = "./Icons/xls.png"
ICON_DRAG_N_DROP = "./Icons/dragndrop.png"
ICON_RECORD = "./Icons/record.png"
ICON_CSV = "./Icons/excel.png"
ICON_TXT = "./Icons/txt.png"
ICON_MD = "./Icons/text.png"
ICON_FOLDER = "./Icons/folder.ico"
ICON_APP = "./Icons/app.ico"

file_conversions = {
    "jpg": ["png", "tiff", "gif", "jpeg", "webp", "ico", "bmp"],
    "png": ["jpg", "tiff", "gif", "jpeg", "webp", "ico", "bmp"],
    "tiff": ["jpg", "png", "gif", "jpeg", "webp", "ico", "bmp"],
    "gif": ["jpg", "png", "tiff", "jpeg", "webp", "ico", "bmp"],
    "jpeg": ["png", "tiff", "gif", "jpg", "webp", "ico", "bmp"],
    "webp": ["png", "tiff", "gif", "jpeg", "jpg", "ico", "bmp"],
    "ico": ["png", "tiff", "jpeg", "jpg", "gif", "webp", "bmp"],
    "bmp": ["png", "tiff", "jpeg", "jpg", "ico", "webp", "gif"],
    "svg": ["png", "tiff", "jpeg", "jpg", "ico", "webp", "gif", "bmp"],
    "doc": ["pdf"],
    "docx": ["pdf"],
    "pdf": ["doc", "docx"],
    "xls": ["xlsx", "csv"],
    "xlsx": ["xls", "csv"],
    "csv": ["xls", "xlsx"],
    "ppt": ["pptx", "pdf"],
    "pptx": ["ppt", "pdf"],
    "mp3": ["wav", "flac", "aac", "ogg"],
    "wav": ["mp3", "flac", "aac", "ogg"],
    "flac": ["mp3", "wav", "aac", "ogg"],
    "aac": ["mp3", "wav", "flac", "ogg"],
    "ogg": ["mp3", "wav", "flac", "aac"],
    "mp4": ["avi", "mov", "mkv", "ogv", "webm", "mpeg"],
    "avi": ["mp4", "mov", "mkv", "ogv", "webm", "mpeg"],
    "mov": ["mp4", "avi", "mkv", "ogv", "webm", "mpeg"],
    "mkv": ["mp4", "avi", "mov", "ogv", "webm", "mpeg"],
    "ogv": ["mp4", "avi", "mov", "mkv", "webm", "mpeg"],
    "webm": ["mp4", "avi", "mov", "mkv", "ogv", "mpeg"],
    "mpeg": ["mp4", "avi", "mov", "mkv", "ogv", "webm"],
    "zip": ["rar"],
    "rar": ["zip"],
    "txt": ["md"],
    "md": ["txt"]
}

fileIconMap = {
    "jpg": ICON_IMAGE,
    "png": ICON_IMAGE,
    "tiff": ICON_IMAGE,
    "gif": ICON_IMAGE,
    "jpeg": ICON_IMAGE,
    "webp": ICON_IMAGE,
    "ico": ICON_IMAGE,
    "bmp": ICON_IMAGE,
    "svg": ICON_SVG,
    "doc": ICON_DOC,
    "docx": ICON_DOC,
    "pdf": ICON_PDF,
    "xls": ICON_XLS,
    "xlsx": ICON_XLS,
    "csv": ICON_CSV,
    "ppt": ICON_PPT,
    "pptx": ICON_PPT,
    "mp3": ICON_MUSIC,
    "wav": ICON_MUSIC,
    "flac": ICON_MUSIC,
    "aac": ICON_MUSIC,
    "ogg": ICON_RECORD,
    "mp4": ICON_VIDEO,
    "avi": ICON_VIDEO,
    "mov": ICON_VIDEO,
    "mkv": ICON_VIDEO,
    "ogv": ICON_VIDEO,
    "webm": ICON_VIDEO,
    "mpeg": ICON_VIDEO,
    "zip": ICON_COMPRESSED,
    "rar": ICON_COMPRESSED,
    "txt": ICON_TXT,
    "md": ICON_MD,
}

