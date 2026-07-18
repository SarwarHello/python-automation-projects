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


def get_category(file_extension):
    """
    Return the folder category for a file extension.

    Files with unknown extensions are placed in the 'Others' folder.
    """
    file_extension = file_extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category

    return "Others"


def create_unique_destination(destination):
    """
    Create a unique destination path if a file with the same name exists.

    Example:
        report.pdf
        report_1.pdf
        report_2.pdf
    """
    if not destination.exists():
        return destination

    counter = 1
    stem = destination.stem
    suffix = destination.suffix

    while True:
        new_destination = destination.with_name(
            f"{stem}_{counter}{suffix}"
        )

        if not new_destination.exists():
            return new_destination

        counter += 1
