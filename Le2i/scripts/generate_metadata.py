import os
import json
import pandas as pd

ROOT = os.path.dirname(os.path.abspath(__file__))

KEYPOINT_DIR = os.path.join(ROOT, "keypoints")
META_DIR = os.path.join(ROOT, "metadata")

os.makedirs(META_DIR, exist_ok=True)

rows = []

for scene in sorted(os.listdir(KEYPOINT_DIR)):
    scene_path = os.path.join(KEYPOINT_DIR, scene)

    if not os.path.isdir(scene_path):
        continue

    for file in sorted(os.listdir(scene_path)):
        if file.endswith(".npy"):
            rows.append({
                "sequence": file,
                "scene": scene,
                "label": "Fall"
            })

labels = pd.DataFrame(rows)
labels.to_csv(
    os.path.join(META_DIR, "labels.csv"),
    index=False
)

stats = []

for scene in sorted(os.listdir(KEYPOINT_DIR)):
    scene_path = os.path.join(KEYPOINT_DIR, scene)

    if not os.path.isdir(scene_path):
        continue

    count = len([
        f for f in os.listdir(scene_path)
        if f.endswith(".npy")
    ])

    stats.append({
        "scene": scene,
        "sequences": count
    })

statistics = pd.DataFrame(stats)
statistics.to_csv(
    os.path.join(META_DIR, "statistics.csv"),
    index=False
)

dataset_info = {
    "dataset": "Le2i Fall Detection",
    "representation": "MediaPipe Pose",
    "landmarks": 33,
    "features_per_landmark": 4,
    "shape": "(Frames, 33, 4)",
    "total_sequences": len(labels),
    "scenes": sorted(os.listdir(KEYPOINT_DIR))
}

with open(
    os.path.join(META_DIR, "dataset_info.json"),
    "w"
) as f:
    json.dump(dataset_info, f, indent=4)

print("Metadata generated successfully!")
print(f"Total sequences: {len(labels)}")