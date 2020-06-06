from typing import List 
from pathlib import Path 
import shutil

class Parser:
    extensions:List[str] = []
    def valid_extension(self,extension):
        return extension in self.extensions
    def parse(self, path, source, dest):
        raise NotImplementedError
    def read(self,path):
        with path.open() as f:
            return f.read()
    def write(self,path, dest, content,ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with full_path.open() as f:
            f.write(content)
    def copy(self,path, source, dest):
        shutil.copy2(path ,dest / path.relative_to(source))

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css",".html"]

    def parse(self, path, source, dest):
        Parser.copy(path, source, dest)