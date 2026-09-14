from pathlib import Path

from PIL import Image
from numpy import array

from medvision.core.image import MedicalImage
from medvision.exceptions.errro import ImageLoadError
from .base import BaseLoader


class PNGLoader(BaseLoader):

    def load(self, path: Path | str) -> MedicalImage:
        path = Path(path)
        try:
            image = Image.open(Path)
            data = array(image)
        except FileNotFoundError:
            raise ImageLoadError(
                f"Image file not found: '{path}'"
            )
        except Exception as ex:
            raise ImageLoadError(
                f"Failed to load PNG image: '{path}'"
            ) from ex

        return MedicalImage(
            data=data,
            path=path,
            format="png",
            metadata={
                "mode": image.mode
            }
        )
