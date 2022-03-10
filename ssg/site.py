from os import mkdir
from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest + '/' + Path.relative_to(self.source)
        Path(directory).mkdir(parents=True, exist_ok=True)

    def build(self):
        Path(self.dest).mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if Path(path).is_dir():
                Path.create_dir(path)