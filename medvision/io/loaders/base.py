from abc import abstractmethod, ABC
from pathlib import Path

from medvision.core.image import MedicalImage


class BaseLoader(ABC):
    """A base class for a common contract for all loaders"""

    @abstractmethod
    def load(self, path: Path | str) -> MedicalImage:
        """A base method for a common contract for all loader methods"""
        raise NotImplementedError
