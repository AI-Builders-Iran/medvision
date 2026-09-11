# medvision

**A modular Python library for detecting and correcting medical image artifacts — before they reach your model.**

Built on [MONAI](https://monai.io/) and [OpenCV](https://opencv.org/), `medvision` targets the artifacts that quietly degrade medical imaging pipelines: **noise, bias field, poor contrast, and motion**. Instead of discovering these problems after a model underperforms, `medvision` detects and corrects them as an explicit preprocessing stage, with every step measurable and reproducible.

---

## Why medvision

Medical imaging datasets are rarely clean. Scanner noise, intensity inhomogeneity (bias field), inconsistent contrast, and patient motion are common — and most computer vision pipelines either ignore them or handle them with ad-hoc scripts that aren't reusable, testable, or explainable.

`medvision` treats artifact handling as a first-class engineering problem:

- **Detect before you correct.** Every artifact type has a dedicated detector that reports *what* it found and *how confident* it is — nothing is corrected blindly.
- **Every step is inspectable.** Detection and correction results are structured objects, not side effects, so you always know what changed and why.
- **Format-agnostic by design.** DICOM, NIfTI, PNG, and JPG are all normalized into the same internal representation before any processing happens.
- **Built to be extended.** New artifact types, new file formats, or new correction algorithms plug into fixed interfaces without touching the rest of the codebase.

---

## How it works

`medvision` moves an image through four stages, all speaking the same data language:

```
   Loader              Detector             Corrector             Writer
(any format)  ───▶  (per artifact)  ───▶  (per artifact)  ───▶  (any format)
     │                    │                     │                    │
     ▼                    ▼                     ▼                    ▼
MedicalImage      DetectionResult      CorrectionResult        MedicalImage
```

- **`MedicalImage`** is the single unit of data used everywhere in the library — the pixel/voxel array plus whatever spatial metadata the source format provides (affine, header, etc.). No module ever passes around a bare array.
- **`DetectionResult`** is what a detector returns: whether an artifact was found, how confident the detector is, and an optional raw score. Detectors only *report* — they never modify the image.
- **`CorrectionResult`** is what a corrector returns: a new `MedicalImage` plus whether anything actually changed. Correctors never mutate the input in place.
- **`PipelineResult`** ties a full run together — the original image, the final image, and every detection and correction that happened along the way.

Full details on these contracts, and the rules every module must follow, live in [`core-architecture.md`](./core-architecture.md) — required reading before contributing a loader, detector, or corrector.

Because every module speaks through these same contracts, any loader, detector, or corrector can be swapped, added, or removed without breaking the rest of the pipeline.

---

## Project structure

```
medvision/
├── core/            # Shared data contracts (MedicalImage, DetectionResult, CorrectionResult, PipelineResult)
├── io/
│   ├── loaders/     # Format-specific loaders (PNG, JPG, DICOM, NIfTI) behind a common factory
│   └── writers/     # Format-specific writers, mirroring the loaders
├── detectors/       # One detector per artifact type (noise, bias_field, contrast, motion)
├── correctors/      # One corrector per artifact type
├── utils/           # Metrics and visualization helpers
├── exceptions/      # Library-specific exception types
└── pipeline.py      # Orchestration layer: wires loaders → detectors → correctors → writers
```

Every detector implements a common `BaseDetector.detect()` interface; every corrector implements a common `BaseCorrector.correct()` interface. This is what lets `pipeline.py` treat all artifact types uniformly, regardless of the algorithm behind each one.

---

## Status

`medvision` is under active development. The architecture and data contracts are fixed; individual components are being implemented incrementally, one module at a time, against the contracts above. Check the source directly for the current state of any given loader, detector, or corrector — this README describes the design, not a snapshot of what's finished.

---

## Installation

`medvision` isn't published as a package yet. Until then, install directly from source:

```bash
git clone https://github.com/HosseinHeydari2004/medvision.git
cd medvision
pip install -r requirements.txt
```

## Usage

```python
from medvision.io import LoaderFactory

loader = LoaderFactory.create("scan.png")
image = loader.load("scan.png")

print(image.data.shape, image.format)
```

As detectors, correctors, and the pipeline are implemented, this section will grow into a full detect → correct → write workflow example.

---

## Contributing

Before opening a PR that adds or modifies a loader, detector, or corrector:

1. Read [`core-architecture.md`](./core-architecture.md) — it defines the contracts every module must follow.
2. Implement against the relevant base class (`BaseDetector`, `BaseCorrector`, `BaseLoader`) rather than inventing a new interface.
3. Don't change the shape of `MedicalImage`, `DetectionResult`, `CorrectionResult`, or `PipelineResult` without proposing it first — the rest of the pipeline depends on their current shape.

## Tech stack

Python · [MONAI](https://monai.io/) · [OpenCV](https://opencv.org/) · NumPy · SciPy · scikit-image · NiBabel · pydicom · Pillow · Pydantic

## License

Not yet specified — check the repository for the current license before use.

---

Part of **Versa** — open-source, production-grade AI engineering.
