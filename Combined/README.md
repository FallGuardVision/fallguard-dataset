# FallGuard Combined Pose Keypoint Dataset

## Overview

This directory contains the standardized **Combined Pose Keypoint Dataset** used for the FallGuard project.

The dataset was created by merging two publicly available fall detection datasets:

- **UR Fall Detection Dataset**
- **Le2i Fall Detection Dataset**

All video/image sequences were processed using **MediaPipe Pose** to extract human skeletal keypoints. The combined dataset is intended for training and evaluating deep learning models for vision-based fall detection.

---

# Dataset Structure

```
Combined/
│
├── keypoints/
│   ├── FALL/
│   └── NORMAL/
│
├── metadata/
│   ├── labels.csv
│   ├── statistics.csv
│   └── dataset_info.json
│
├── scripts/
│   ├── combine_datasets.py
│   └── generate_metadata.py
│
└── README.md
```

---

# Pose Representation

Each sequence is stored as a NumPy (`.npy`) file.

Each frame contains:

- 33 MediaPipe body landmarks

Each landmark contains:

- x
- y
- z
- visibility

Sequence shape:

```
(Frames, 33, 4)
```

---

# Dataset Statistics

| Class | Number of Sequences |
|-------|--------------------:|
| FALL | 220 |
| NORMAL | 40 |
| **TOTAL** | **260** |

---

# Dataset Sources

## UR Fall Detection Dataset

Contributes:

- Fall sequences
- Activities of Daily Living (ADL)

Files are renamed as:

```
ur_fall_01.npy
ur_adl_01.npy
```

---

## Le2i Fall Detection Dataset

Contributes:

- Coffee Room
- Home
- Lecture Room
- Office

Files are renamed as:

```
le2i_coffee_01.npy
le2i_home_01.npy
le2i_lecture_01.npy
le2i_office_01.npy
```

---

# Preprocessing Pipeline

The following preprocessing steps were performed:

1. Raw datasets were organized.
2. Human pose landmarks were extracted using MediaPipe Pose.
3. One `.npy` file was generated for each sequence.
4. Files were standardized using a unified naming convention.
5. Keypoint sequences from multiple datasets were merged.
6. Metadata files were automatically generated.

---

# Scripts

## combine_datasets.py

Copies and merges the standardized keypoint datasets into a single Combined dataset.

## generate_metadata.py

Automatically generates:

- labels.csv
- statistics.csv
- dataset_info.json

---

# Naming Convention

Examples:

```
ur_fall_01.npy
ur_adl_15.npy

le2i_coffee_08.npy
le2i_home_21.npy
le2i_lecture_05.npy
le2i_office_18.npy
```

Each filename uniquely identifies:

- Source dataset
- Scene / Activity
- Sequence number

---

# Metadata Files

### labels.csv

Contains:

- sequence filename
- class label
- source dataset

---

### statistics.csv

Contains the number of sequences available for each class.

---

### dataset_info.json

Contains dataset configuration, dataset sources, sequence counts, and pose representation information.

---

# Notes

- Original videos and images are **not included** in this repository.
- Only extracted MediaPipe Pose keypoints are provided.
- The original datasets must be obtained from their respective official sources.

---

# Project

This dataset was created as part of the **FallGuard** Final Year Project.

The combined dataset provides a unified representation for training deep learning models for automatic human fall detection using pose estimation.