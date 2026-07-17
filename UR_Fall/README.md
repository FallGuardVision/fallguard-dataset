# UR Fall Detection Dataset

## Source
University of Rzeszów Fall Detection Dataset

## Description
This dataset contains RGB frame sequences collected for human fall detection research.

## Contents

- FALL (30 sequences)
- NORMAL / ADL (40 sequences)

## Pose Extraction

- MediaPipe Pose Landmarker (Full)
- 33 landmarks
- x,y,z,visibility

## Keypoint Format

Each NumPy file has shape:

(frames,33,4)

Example

fall_01.npy

Shape

(160,33,4)