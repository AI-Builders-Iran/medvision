import matplotlib
import matplotlib.pyplot as plt
from medvision.io import JPGLoader
matplotlib.use(backend="QtAgg")
loader = JPGLoader()

image = loader.load(
    path=r"D:\AI Source\Projects\list_of_projects\cancer_pictures\brisc2025\classification_task\train\meningioma\brisc2025_train_01149_me_ax_t1.jpg"
)

print(image.affine)
