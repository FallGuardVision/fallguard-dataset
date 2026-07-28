import shutil
from pathlib import Path

# =====================================
# Paths
# =====================================

ROOT = Path(__file__).resolve().parents[2]

UR = ROOT / "UR_Fall" / "keypoints"
LE2I = ROOT / "Le2i" / "keypoints"
IEEE = ROOT / "IEEE_DataPort" / "keypoints"

COMBINED = ROOT / "Combined" / "keypoints"

FALL_OUT = COMBINED / "FALL"
NORMAL_OUT = COMBINED / "NORMAL"

# =====================================
# Clean old combined dataset
# =====================================

if FALL_OUT.exists():
    shutil.rmtree(FALL_OUT)

if NORMAL_OUT.exists():
    shutil.rmtree(NORMAL_OUT)

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

print("\nCopying Le2i Coffee Room...")

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

# =====================================
# IEEE DataPort NORMAL
# =====================================

print("\nCopying IEEE DataPort...")

for file in sorted((IEEE / "NORMAL").glob("*.npy")):

    # ieee_normal_01.npy -> ieee_normal_01.npy
    # Prefix retained for consistency
    new_name = file.name

    shutil.copy(file, NORMAL_OUT / new_name)

print("✓ IEEE DataPort copied.")

# =====================================
# Summary
# =====================================

fall_count = len(list(FALL_OUT.glob("*.npy")))
normal_count = len(list(NORMAL_OUT.glob("*.npy")))

print("\n" + "=" * 50)
print("Combined Dataset Summary")
print("=" * 50)
print(f"FALL sequences   : {fall_count}")
print(f"NORMAL sequences : {normal_count}")
print(f"TOTAL sequences  : {fall_count + normal_count}")
print("=" * 50)

print("\nDone!")