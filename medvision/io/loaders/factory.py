from pathlib import Path

from .jpg import JPGLoader
from .png import PNGLoader
from .dicom import DICOMLoader
from .nifti import NIfTILoader
from .base import BaseLoader

class LoaderFactory:

    _loaders:dict = {
        ".png": PNGLoader,
        ".jpg": JPGLoader,
        ".jpeg": JPGLoader,
        ".nii": NIfTILoader,
        ".nii.gz": NIfTILoader,
        ".dcm": DICOMLoader,
    }

    @classmethod
    def create(cls, path: Path | str)-> BaseLoader:

        path = str(path).lower()
        for extension, loader in cls._loaders.items():
            if path.endswith(extension):
                return loader()
        raise ValueError(f"Unsupported image format: {path}")
