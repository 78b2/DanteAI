import argparse
import os
from typing import Iterable

ARCHIVE_EXTENSIONS = (
    '.zip', '.rar', '.tar', '.gz', '.bz2', '.7z', '.xz'
)
TEMP_EXTENSIONS = (
    '.tmp', '.temp', '.swp', '.bak', '~'
)

def remove_files(directory: str, extensions: Iterable[str], dry_run: bool = False) -> None:
    """Remove files in ``directory`` that match ``extensions``.

    Parameters
    ----------
    directory: str
        Root directory to scan recursively.
    extensions: Iterable[str]
        File extensions to remove.
    dry_run: bool, optional
        If ``True``, only print files that would be removed.
    """
    for root, _dirs, files in os.walk(directory):
        for name in files:
            if name.lower().endswith(tuple(ext.lower() for ext in extensions)):
                path = os.path.join(root, name)
                if dry_run:
                    print(f"Would remove: {path}")
                else:
                    try:
                        os.remove(path)
                        print(f"Removed: {path}")
                    except OSError as exc:
                        print(f"Failed to remove {path}: {exc}")

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Remove archived (.zip, .rar, .tar, .7z, ...) and temporary files "
            "(.tmp, .temp, .swp, ...)."
        )
    )
    parser.add_argument(
        "directory", nargs="?", default=".",
        help="Directory to clean (default: current directory)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="List files without deleting them"
    )
    args = parser.parse_args()

    remove_files(args.directory, ARCHIVE_EXTENSIONS, args.dry_run)
    remove_files(args.directory, TEMP_EXTENSIONS, args.dry_run)

if __name__ == "__main__":
    main()
