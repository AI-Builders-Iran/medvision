from pathlib import Path

from medvision.core.image import MedicalImage
from .base import BaseLoader


class NIfTILoader(BaseLoader):

    def load(self, path: Path | str) -> MedicalImage:
        pass
