import matplotlib
import matplotlib.pyplot as plt
from pydicom import examples
from medvision.io.loaders.pipeline import PipelineLoader

matplotlib.use(backend="QtAgg")

path = examples.get_path("ct")
image = PipelineLoader(
    path=path
).load()

# volume = image.data
#
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#
# mid_x = volume.shape[0] // 2
# mid_y = volume.shape[1] // 2
# mid_z = volume.shape[2] // 2
#
# axes[0].imshow(volume[mid_x, :, :], cmap="gray")
# axes[0].set_title("Sagittal")
#
# axes[1].imshow(volume[:, mid_y, :], cmap="gray")
# axes[1].set_title("Coronal")
#
# axes[2].imshow(volume[:, :, mid_z], cmap="gray")
# axes[2].set_title("Axial")
#
# for ax in axes:
#     ax.axis("off")
#
# plt.show()

# plt.imshow(image.data, cmap="gray")
# plt.axis("off")
# plt.show()
print(image.metadata.__sizeof__())
