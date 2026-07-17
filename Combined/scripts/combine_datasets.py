import shutil
from pathlib import Path

# =====================================
# Paths
# =====================================

ROOT = Path(__file__).resolve().parents[2]

UR = ROOT / "UR_Fall" / "keypoints"
LE2I = ROOT / "Le2i" / "keypoints"

COMBINED = ROOT / "Combined" / "keypoints"

FALL_OUT = COMBINED / "FALL"
NORMAL_OUT = COMBINED / "NORMAL"

FALL_OUT.mkdir(parents=True, exist_ok=True)
NORMAL_OUT.mkdir(parents=True, exist_ok=True)

print("=" * 50)
print("Combining datasets...")
print("=" * 50)

# =====================================
# UR FALL
# =====================================

print("\nCopying UR Fall dataset...")

for file in sorted((UR / "FALL").glob("*.npy")):

    new_name = file.name.replace("fall_", "ur_fall_")

    shutil.copy(file, FALL_OUT / new_name)

for file in sorted((UR / "NORMAL").glob("*.npy")):

    new_name = file.name.replace("adl_", "ur_adl_")

    shutil.copy(file, NORMAL_OUT / new_name)

print("✓ UR Fall copied.")

# =====================================
# LE2I Coffee Room
# =====================================

print("Copying Le2i Coffee Room...")

for file in sorted((LE2I / "Coffee_room").glob("*.npy")):

    number = file.stem.split("_")[-1]

    new_name = f"le2i_coffee_{number}.npy"

    shutil.copy(file, FALL_OUT / new_name)

# =====================================
# LE2I Home
# =====================================

print("Copying Le2i Home...")

for file in sorted((LE2I / "Home").glob("*.npy")):

    number = file.stem.split("_")[-1]

    new_name = f"le2i_home_{number}.npy"

    shutil.copy(file, FALL_OUT / new_name)

# =====================================
# LE2I Lecture Room
# =====================================

print("Copying Le2i Lecture Room...")

for file in sorted((LE2I / "Lecture_room").glob("*.npy")):

    number = file.stem.split("_")[-1]

    new_name = f"le2i_lecture_{number}.npy"

    shutil.copy(file, FALL_OUT / new_name)

# =====================================
# LE2I Office
# =====================================

print("Copying Le2i Office...")

for file in sorted((LE2I / "Office").glob("*.npy")):

    number = file.stem.split("_")[-1]

    new_name = f"le2i_office_{number}.npy"

    shutil.copy(file, FALL_OUT / new_name)

print("✓ Le2i copied.")

print("\nDone!")