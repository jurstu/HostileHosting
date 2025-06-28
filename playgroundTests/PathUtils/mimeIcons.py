

import mimetypes

from .PathUtils import is_dir
MIME_EMOJI_MAP = {
    # 📄 TEXT FILES & CONFIG
    "text/plain": "📄",
    "text/markdown": "📝",
    "text/html": "🌐",
    "text/css": "🎨",
    "text/javascript": "🧠",
    "application/json": "🗂️",
    "application/xml": "🧾",
    "application/yaml": "🔧",
    "application/x-yaml": "🔧",
    "application/sql": "🛢️",
    "application/rtf": "📃",

    # 🖼 IMAGE FILES
    "image/jpeg": "🖼️",
    "image/png": "🖼️",
    "image/gif": "🖼️",
    "image/svg+xml": "🖌️",
    "image/webp": "🌄",
    "image/bmp": "🖼️",
    "image/tiff": "🖼️",
    "image/heic": "📸",
    "image/avif": "📸",
    "image/vnd.microsoft.icon": "🔳",
    "image/x-icon": "🔳",

    # 🎵 AUDIO FILES
    "audio/mpeg": "🎵",
    "audio/mp3": "🎵",
    "audio/ogg": "🎧",
    "audio/wav": "🔊",
    "audio/x-wav": "🔊",
    "audio/webm": "🎶",
    "audio/flac": "🎼",
    "audio/aac": "🎶",
    "audio/x-aiff": "🎶",
    "audio/x-ms-wma": "🎧",

    # 🎬 VIDEO FILES
    "video/mp4": "🎬",
    "video/mpeg": "📼",
    "video/x-msvideo": "📽️",  # AVI
    "video/x-matroska": "🎞️", # MKV
    "video/webm": "📺",
    "video/ogg": "🎥",
    "video/quicktime": "🎞️",
    "application/vnd.rn-realmedia": "📽️",
    "video/x-ms-wmv": "📽️",
    "video/x-flv": "🌊",
    "application/x-shockwave-flash": "💥",

    # 🗜 ARCHIVES & COMPRESSED
    "application/zip": "🗜️",
    "application/x-tar": "📦",
    "application/x-gzip": "🧷",
    "application/x-bzip2": "🪛",
    "application/x-7z-compressed": "🧳",
    "application/x-rar-compressed": "📦",
    "application/x-xz": "📦",

    # 💻 CODE & SCRIPTS
    "text/x-python": "🐍",
    "application/x-python-code": "🐍",
    "text/x-shellscript": "💻",
    "application/x-sh": "💻",
    "application/javascript": "🧠",
    "application/x-php": "🐘",
    "application/x-ruby": "💎",
    "application/x-perl": "🦪",
    "text/x-c": "👾",
    "text/x-c++": "👾",
    "text/x-java-source": "☕",
    "text/x-go": "🦫",
    "text/x-rustsrc": "🦀",
    "application/x-lua": "🌙",

    # 📚 OFFICE & DOC FILES
    "application/pdf": "📕",
    "application/msword": "📄",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "📘",
    "application/vnd.ms-excel": "📊",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "📊",
    "application/vnd.ms-powerpoint": "📈",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": "📈",
    "application/vnd.oasis.opendocument.text": "📓",
    "application/vnd.oasis.opendocument.spreadsheet": "📗",
    "application/vnd.oasis.opendocument.presentation": "📙",

    # 💾 EXECUTABLES / BINARY
    "application/octet-stream": "📦",
    "application/x-msdownload": "💾",
    "application/x-executable": "⚙️",
    "application/vnd.debian.binary-package": "📦",

    # 📁 DIRECTORY (manually detected)
    "inode/directory": "📁",
}

MIME_EMOJI_MAP.update({
    "video/mp4": "🎬",
    "video/mpeg": "📼",
    "video/x-msvideo": "📽️",  # .avi
    "video/x-matroska": "🎞️", # .mkv
    "video/webm": "📺",
    "video/ogg": "🎥",
    "video/quicktime": "🎞️",  # ✅ .mov files
    "application/vnd.rn-realmedia": "📽️",  # .rm
    "video/x-flv": "🌊",        # .flv (Flash)
    "video/x-ms-wmv": "📽️",    # .wmv
    "application/x-shockwave-flash": "💥", # .swf
})


custom_mime_types = {
    ".md": "text/markdown",
    ".py": "text/x-python",
    ".sh": "text/x-shellscript",
    ".flac": "audio/flac",
    ".mkv": "video/x-matroska",
    ".heic": "image/heic",
    ".avif": "image/avif",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ".mov": "video/quicktime",
}

for ext, mime in custom_mime_types.items():
    mimetypes.add_type(mime, ext)

def get_emoji_for_file(path):
    if is_dir(path):
        return MIME_EMOJI_MAP.get("inode/directory")
    mime_type, _ = mimetypes.guess_type(path)
    return MIME_EMOJI_MAP.get(mime_type, "📦")

