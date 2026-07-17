import os
import json
from pathlib import Path
import pandas as pd

# ==========================================
# Paths
# ==========================================

ROOT = Path(__file__).resolve().parents[2]

KEYPOINT_DIR = ROOT / "Combined" / "keypoints"
META_DIR = ROOT / "Combined" / "metadata"

META_DIR.mkdir(parents=True, exist_ok=True)

rows = []

# ==========================================
# FALL
# ==========================================

fall_path = KEYPOINT_DIR / "FALL"

for file in sorted(fall_path.glob("*.npy")):
    rows.append({
        "sequence": file.name,
        "class": "FALL",
        "source": file.name.split("_")[0]
    })

# ==========================================
# NORMAL
# ==========================================

normal_path = KEYPOINT_DIR / "NORMAL"

for file in sorted(normal_path.glob("*.npy")):
    rows.append({
        "sequence": file.name,
        "class": "NORMAL",
        "source": file.name.split("_")[0]
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

stats = pd.DataFrame([
    {
        "class": "FALL",
        "count": len(list(fall_path.glob("*.npy")))
    },
    {
        "class": "NORMAL",
        "count": len(list(normal_path.glob("*.npy")))
    }
])

stats.to_csv(
    META_DIR / "statistics.csv",
    index=False
)

print("statistics.csv generated")

# ==========================================
# Dataset Information
# ==========================================

info = {
    "dataset": "FallGuard Combined Dataset",
    "version": "1.0",
    "sources": [
        "UR Fall Detection Dataset",
        "Le2i Fall Detection Dataset"
    ],
    "representation": "MediaPipe Pose",
    "landmarks": 33,
    "features_per_landmark": 4,
    "shape": "(Frames, 33, 4)",
    "fall_sequences": len(list(fall_path.glob("*.npy"))),
    "normal_sequences": len(list(normal_path.glob("*.npy"))),
    "total_sequences": len(rows)
}

with open(
    META_DIR / "dataset_info.json",
    "w"
) as f:
    json.dump(info, f, indent=4)

print("dataset_info.json generated")

print("\n")
print("=" * 40)
print("Combined Dataset Summary")
print("=" * 40)
print(f"Fall   : {len(list(fall_path.glob('*.npy')))}")
print(f"Normal : {len(list(normal_path.glob('*.npy')))}")
print(f"Total  : {len(rows)}")
print("=" * 40)