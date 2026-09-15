from pathlib import Path

from .dicom import DICOMLoader
from .jpg import JPGLoader
from .nifti import NIfTILoader
from .png import PNGLoader


class PipelineLoader:
    _loaders: dict = {
        ".png": PNGLoader,
        ".jpg": JPGLoader,
        ".jpeg": JPGLoader,
        ".nii": NIfTILoader,
        ".nii.gz": NIfTILoader,
        ".dcm": DICOMLoader,
    }

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def load(self):
        path_str = str(self.path).lower()
        extension = path_str
        for extension, loader_cls in self._loaders.items():
            if path_str.endswith(extension):
                return loader_cls().load(self.path)
        raise ValueError(f"Unsupported image format: {self.path}")