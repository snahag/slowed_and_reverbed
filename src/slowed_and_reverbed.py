import numpy as np
import soundfile as sf
from pedalboard import Pedalboard, Reverb, Delay
from math import trunc
import resampy



#def slow_feel_and_reverb(input_path, output_path, room_size=0.75, damping=0.5, wet_level=0.08, dry_level=0.2, delay_seconds=2, slowfactor=0.08):
def slow_feel_and_reverb(input_path, output_path, room_size, damping, wet_level, dry_level, delay_seconds, slowfactor):
    # Load the audio file
    audio, sample_rate = sf.read(input_path, dtype=np.float32)
    original_sample_rate = sample_rate
    sample_rate -= trunc(sample_rate * slowfactor)

    # Add reverb
    reverb = Reverb(room_size=room_size, damping=damping, wet_level=wet_level, dry_level=dry_level)
    
    # Add delay effect
    delay_effect = Delay(delay_seconds=delay_seconds, mix=1.0)

    # Create a pedalboard with the effects
    board = Pedalboard([reverb, delay_effect])

    # Process the audio with the effects
    effected = board(audio, sample_rate=sample_rate)

    # Resample to original sample rate for MP3 compatibility
    effected_resampled = resampy.resample(effected, sample_rate, original_sample_rate, axis=0)

    # Save the processed audio to a new file
    sf.write(output_path, effected_resampled, original_sample_rate)

if __name__ == "__main__":
        # Configuration parameters
    room_size = 0.85
    damping = 0.9
    wet_level = 0.05
    dry_level = 0.15
    delay_seconds = 1
    slowfactor = 0.20

    # Input and output paths
    input_song = "/slowed and reverb/sample.mp3"
    
    # Construct the output file name with configuration parameters
    output_song = "/slowed and reverb/sample_rs{room_size}_damp{damping}_wet{wet_level}_dry{dry_level}_delay{delay_seconds}_slow{slowfactor}.mp3"

    # Call the function to process the audio
    slow_feel_and_reverb(input_song, output_song, room_size, damping, wet_level, dry_level, delay_seconds, slowfactor)
