from .loaders.png import PNGLoader
from .loaders.pipeline import PipelineLoader
from .loaders.jpg import JPGLoader
from .loaders.nifti import NIfTILoader

__all__ = [
    "PipelineLoader",
    "PNGLoader",
    "JPGLoader",
    "NIfTILoader"
]