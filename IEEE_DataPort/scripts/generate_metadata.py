import os
import json
import numpy as np
import pandas as pd

# ---------------------------------------------------
# Paths
# ---------------------------------------------------

BASE_DIR = r"D:\FYP\fallguard-dataset\IEEE_DataPort"

KEYPOINT_DIR = os.path.join(BASE_DIR, "keypoints")

META_DIR = os.path.join(BASE_DIR, "metadata")

os.makedirs(META_DIR, exist_ok=True)

# ---------------------------------------------------
# Generate labels.csv
# ---------------------------------------------------

labels = []

statistics = []

total_sequences = 0

for class_name in sorted(os.listdir(KEYPOINT_DIR)):

    class_path = os.path.join(KEYPOINT_DIR, class_name)

    if not os.path.isdir(class_path):
        continue

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

# ---------------------------------------------------
# Save labels.csv
# ---------------------------------------------------

labels_df = pd.DataFrame(labels)

labels_df.to_csv(

    os.path.join(META_DIR, "labels.csv"),

    index=False

)

# ---------------------------------------------------
# Save statistics.csv
# ---------------------------------------------------

statistics_df = pd.DataFrame(statistics)

statistics_df.to_csv(

    os.path.join(META_DIR, "statistics.csv"),

    index=False

)

# ---------------------------------------------------
# dataset_info.json
# ---------------------------------------------------

dataset_info = {

    "dataset": "IEEE DataPort",

    "representation": "MediaPipe Pose",

    "landmarks": 33,

    "features_per_landmark": 4,

    "shape": "(Frames, 33, 4)",

    "classes": [

        "NORMAL"

    ],

    "total_sequences": total_sequences

}

with open(

    os.path.join(META_DIR, "dataset_info.json"),

    "w"

) as f:

    json.dump(dataset_info, f, indent=4)

# ---------------------------------------------------
# Done
# ---------------------------------------------------

print("=" * 50)

print("IEEE DataPort metadata generated successfully!")

print("=" * 50)

print(f"Total sequences : {total_sequences}")