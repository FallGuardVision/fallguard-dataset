import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]

KEYPOINT_DIR = ROOT / "MCFD" / "keypoints"
META_DIR = ROOT / "MCFD" / "metadata"

META_DIR.mkdir(parents=True, exist_ok=True)

rows = []

fall_path = KEYPOINT_DIR / "FALL"

for file in sorted(fall_path.glob("*.npy")):

    rows.append({
        "sequence": file.name,
        "class": "FALL",
        "source": "MCFD"
    })

labels = pd.DataFrame(rows)

labels.to_csv(
    META_DIR / "labels.csv",
    index=False
)

stats = pd.DataFrame([
    {
        "class": "FALL",
        "count": len(rows)
    }
])

stats.to_csv(
    META_DIR / "statistics.csv",
    index=False
)

info = {

    "dataset": "Multicam Fall Dataset",

    "version": "1.0",

    "representation": "MediaPipe Pose",

    "landmarks": 33,

    "features_per_landmark": 4,

    "shape": "(Frames,33,4)",

    "fall_sequences": len(rows),

    "total_sequences": len(rows)
}

with open(
    META_DIR / "dataset_info.json",
    "w"
) as f:

    json.dump(info, f, indent=4)

print("Metadata generated.")