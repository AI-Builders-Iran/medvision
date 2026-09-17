import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import matplotlib
from medvision.io.loaders.pipeline import PipelineLoader
from medvision.io.writers.png import PNGWriter

matplotlib.use(backend="QtAgg")

# path = examples.get_path("ct")
# image = PipelineLoader(
#     path=path
# ).load()

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
# print(image.metadata.__sizeof__())

# loader = PipelineLoader(
#     path=r"C:\Users\hosse\Downloads\walnut_masked.nii"
# )
# image = loader.load()
#
# writer = NIfTIWriter()
#
# output_path = writer.write(
#     image=image,
#     output_path="example/corrected.nii.gz"
# )
# print(output_path)
#
# loader.path = "example/corrected.nii.gz"
#
# result = loader.load()
# print(loader.path)
# print(result.data.shape)
# print(result.data.dtype)
# print(result.affine)
#
loader = PipelineLoader(
    path=r"D:\AI Source\Projects\list_of_projects\cancer_pictures\brisc2025\classification_task\train\pituitary\brisc2025_train_03550_pi_ax_t1.jpg"
)
# image1 = loader.load()
# writer_jpg = JPGWriter()
# writer_jpg.write(
#     image=image1,
#     output_path="example/picture1.jpg"
# )
# loader.path = "example/picture1.jpg"
# image_loaded = loader.load()
# print(image_loaded)

# # -------------------------------------------------------------------------
loader.path = r"D:\AI Source\Projects\list_of_projects\cancer_pictures\brisc2025\segmentation_task\train\masks\brisc2025_train_00015_gl_ax_t1.png"
image2 = loader.load()

# plt.imshow(image.data, cmap="gray")
# plt.axis("off")
# plt.show()

writer_png = PNGWriter()
out = writer_png.write(image=image2,
                       output_path="example/picture2.png"
                       )

loader.path = "example/picture2.png"
image_loaded2 = loader.load()

print(image_loaded2)
print(out)
