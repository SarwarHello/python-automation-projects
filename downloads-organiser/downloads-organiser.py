from pathlib import Path
import shutil


# Windows Downloads folder
DOWNLOADS_FOLDER = Path.home() / "Downloads"


# File categories and their extensions
FILE_CATEGORIES = {
    "Images": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".svg", ".webp", ".tiff"
    },
    "Documents": {
        ".pdf", ".doc", ".docx", ".txt", ".rtf",
        ".odt", ".xls", ".xlsx", ".csv", ".ppt", ".pptx"
    },
    "Videos": {
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm"
    },
    "Audio": {
        ".mp3", ".wav", ".aac", ".flac",
        ".ogg", ".m4a", ".wma"
    },
    "Archives": {
        ".zip", ".rar", ".7z", ".tar",
        ".gz", ".bz2"
    },
    "Applications": {
        ".exe", ".msi", ".apk", ".dmg", ".pkg"
    },
    "Code": {
        ".py", ".js", ".html", ".css", ".java",
        ".cpp", ".c", ".cs", ".php", ".json", ".xml"
    },
    "Ebooks": {
        ".epub", ".mobi", ".azw", ".azw3"
    }
}
