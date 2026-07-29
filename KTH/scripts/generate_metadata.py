import os
import json
from pathlib import Path
import pandas as pd

# ==========================================
# Paths
# ==========================================

ROOT = Path(__file__).resolve().parents[2]

KEYPOINT_DIR = ROOT / "KTH" / "keypoints" / "NORMAL"
META_DIR = ROOT / "KTH" / "metadata"

META_DIR.mkdir(parents=True, exist_ok=True)

rows = []

# ==========================================
# Read all sequences
# ==========================================

for file in sorted(KEYPOINT_DIR.glob("*.npy")):

    name = file.stem.lower()

    if "walk" in name:
        action = "walking"

    elif "jog" in name:
        action = "jogging"

    elif "run" in name:
        action = "running"

    elif "wave" in name:
        action = "handwaving"

    elif "clap" in name:
        action = "handclapping"

    else:
        action = "unknown"

    rows.append({

        "sequence": file.name,

        "class": "NORMAL",

        "source": "KTH",

        "action": action

    })

labels = pd.DataFrame(rows)

labels.to_csv(

    META_DIR / "labels.csv",

    index=False

)

print("labels.csv generated")

# ==========================================
# Statistics
# ==========================================

stats = labels.groupby("action").size().reset_index(name="count")

stats.to_csv(

    META_DIR / "statistics.csv",

    index=False

)

print("statistics.csv generated")

# ==========================================
# Dataset Information
# ==========================================

info = {

    "dataset": "KTH Action Recognition",

    "version": "1.0",

    "representation": "MediaPipe Pose",

    "landmarks": 33,

    "features_per_landmark": 4,

    "shape": "(Frames,33,4)",

    "total_sequences": len(rows),

    "actions": sorted(labels.action.unique().tolist())

}

with open(

    META_DIR / "dataset_info.json",

    "w"

) as f:

    json.dump(info, f, indent=4)

print("dataset_info.json generated")

print("\n==============================")
print("KTH Dataset Summary")
print("==============================")
print("Total :", len(rows))
print(labels["action"].value_counts())