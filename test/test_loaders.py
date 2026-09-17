import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from medvision.io import IOPipeline

io = IOPipeline()

images, loaded_report = io.load(
    input_path=r"D:\AI Source\Projects\list_of_projects\cancer_pictures\brisc2025\classification_task"
)
print(loaded_report.summary())
