import os
import json
import numpy as np
import pandas as pd

# ===================================================
# Paths
# ===================================================

BASE_DIR = r"D:\FYP\fallguard-dataset\IEEE_DataPort"

KEYPOINT_DIR = os.path.join(BASE_DIR, "keypoints")
META_DIR = os.path.join(BASE_DIR, "metadata")

os.makedirs(META_DIR, exist_ok=True)

# ===================================================
# Generate labels.csv
# ===================================================

labels = []
statistics = []

total_sequences = 0

class_names = sorted([
    d for d in os.listdir(KEYPOINT_DIR)
    if os.path.isdir(os.path.join(KEYPOINT_DIR, d))
])

for class_name in class_names:

    class_path = os.path.join(KEYPOINT_DIR, class_name)

    npy_files = sorted([
        f for f in os.listdir(class_path)
        if f.endswith(".npy")
    ])

    count = 0

    for file in npy_files:

        file_path = os.path.join(class_path, file)

        data = np.load(file_path)

        labels.append({
            "file": file,
            "class": class_name,
            "frames": data.shape[0],
            "shape": str(data.shape)
        })

        count += 1
        total_sequences += 1

    statistics.append({
        "class": class_name,
        "sequences": count
    })

# ===================================================
# Save labels.csv
# ===================================================

labels_df = pd.DataFrame(labels)

labels_df.to_csv(
    os.path.join(META_DIR, "labels.csv"),
    index=False
)

# ===================================================
# Save statistics.csv
# ===================================================

statistics_df = pd.DataFrame(statistics)

statistics_df.to_csv(
    os.path.join(META_DIR, "statistics.csv"),
    index=False
)

# ===================================================
# Dataset Information
# ===================================================

fall_sequences = 0
normal_sequences = 0

for item in statistics:
    if item["class"].upper() == "FALL":
        fall_sequences = item["sequences"]
    elif item["class"].upper() == "NORMAL":
        normal_sequences = item["sequences"]

dataset_info = {

    "dataset": "IEEE DataPort Dataset",

    "version": "2.0",

    "representation": "MediaPipe Pose",

    "landmarks": 33,

    "features_per_landmark": 4,

    "shape": "(Frames, 33, 4)",

    "classes": class_names,

    "fall_sequences": fall_sequences,

    "normal_sequences": normal_sequences,

    "total_sequences": total_sequences
}

with open(
    os.path.join(META_DIR, "dataset_info.json"),
    "w"
) as f:
    json.dump(dataset_info, f, indent=4)

# ===================================================
# Summary
# ===================================================

print("=" * 50)
print("IEEE DataPort metadata generated successfully!")
print("=" * 50)

for item in statistics:
    print(f"{item['class']:<10}: {item['sequences']}")

print("-" * 50)
print(f"TOTAL      : {total_sequences}")
print("=" * 50)