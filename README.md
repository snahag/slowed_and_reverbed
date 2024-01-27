# Slowed_and_reverbed

## Overview

This project contains a Python script that applies audio effects such as reverb and delay to MP3 files. It's designed for musicians, sound engineers, or anyone interested in audio processing.

## Features

This script enhances audio files by adding reverb and delay effects, and adjusting the playback speed. The default configuration parameters are as follows:

- **Reverb Effect**:

  - Room Size (Adds depth and space to the audio)
  - Damping (Controls the high-frequency decay)
  - Wet Level (The level of the reverb effect)
  - Dry Level (The level of the original, unprocessed audio)

- **Delay Effect**:

  - Delay Seconds (Creates an echo-like effect)

- **Playback Speed Adjustment**:
  - Slow Factor (Reduces the playback speed for a unique sound)

These settings can be customized as needed to suit different audio processing requirements.

## Getting Started

### Prerequisites

- Python 3.x
- Numpy
- Soundfile
- Pedalboard
- Resampy

You can install these with `pip install -r requirements.txt`.

### Usage

You need to modify the input_song and output_song variables in the script to reflect the paths of their input and output files.

To use the script, run:
python src/slow_feel_and_reverb.py
