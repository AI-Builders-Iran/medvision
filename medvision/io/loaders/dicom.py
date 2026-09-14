from pathlib import Path

from medvision.core.image import MedicalImage
from .base import BaseLoader


class DICOMLoader(BaseLoader):

    def load(self, path: Path | str) -> MedicalImage:
        pass
