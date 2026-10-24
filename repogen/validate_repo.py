"""Run upstream metadata and IPK checks for every registered application."""
import subprocess
import sys
import tempfile
from pathlib import Path


def main():
    for path in sorted(Path('packages').iterdir()):
        if path.name == '.gitkeep':
            continue
        if path.suffix != '.yml':
            raise ValueError(f'Only YAML registrations are supported: {path}')
        subprocess.run([sys.executable, '-m', 'repogen.lintpkg', '-f', str(path)], check=True)
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run([sys.executable, '-m', 'repogen.downloadipk', '-i', str(path),
                            '-o', str(Path(directory, 'package.ipk'))], check=True)


if __name__ == '__main__':
    main()
