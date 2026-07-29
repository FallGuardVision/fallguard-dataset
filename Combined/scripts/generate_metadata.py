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

fall_path = KEYPOINT_DIR / "FALL"
normal_path = KEYPOINT_DIR / "NORMAL"

# ==========================================
# Read FALL sequences
# ==========================================

for file in sorted(fall_path.glob("*.npy")):

    rows.append({
        "sequence": file.name,
        "class": "FALL",
        "source": file.name.split("_")[0]
    })

# ==========================================
# Read NORMAL sequences
# ==========================================

for file in sorted(normal_path.glob("*.npy")):

    rows.append({
        "sequence": file.name,
        "class": "NORMAL",
        "source": file.name.split("_")[0]
    })

# ==========================================
# labels.csv
# ==========================================

labels = pd.DataFrame(rows)

labels.to_csv(
    META_DIR / "labels.csv",
    index=False
)

print("✓ labels.csv generated")

# ==========================================
# statistics.csv
# ==========================================

fall_count = len(list(fall_path.glob("*.npy")))
normal_count = len(list(normal_path.glob("*.npy")))

stats = pd.DataFrame([
    {
        "class": "FALL",
        "count": fall_count
    },
    {
        "class": "NORMAL",
        "count": normal_count
    }
])

stats.to_csv(
    META_DIR / "statistics.csv",
    index=False
)

print("✓ statistics.csv generated")

# ==========================================
# Source statistics
# ==========================================

source_counts = labels["source"].value_counts().to_dict()

# ==========================================
# dataset_info.json
# ==========================================

info = {

    "dataset": "FallGuard Combined Dataset",

    "version": "2.0",

    "sources": [

    "UR Fall Detection Dataset",

    "Le2i Fall Detection Dataset",

    "IEEE DataPort Dataset",

    "KTH Action Recognition Dataset"
],

    "representation": "MediaPipe Pose",

    "landmarks": 33,

    "features_per_landmark": 4,

    "shape": "(Frames, 33, 4)",

    "fall_sequences": fall_count,

    "normal_sequences": normal_count,

    "total_sequences": len(rows),

    "source_distribution": source_counts

}

with open(
    META_DIR / "dataset_info.json",
    "w"
) as f:

    json.dump(info, f, indent=4)

print("✓ dataset_info.json generated")

# ==========================================
# Summary
# ==========================================

print()
print("=" * 50)
print("Combined Dataset Summary")
print("=" * 50)

print(f"FALL sequences   : {fall_count}")
print(f"NORMAL sequences : {normal_count}")
print(f"TOTAL sequences  : {len(rows)}")

print("\nSource Distribution")

for source, count in source_counts.items():
    print(f"  {source:<6}: {count}")

print("=" * 50)