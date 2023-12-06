import parselmouth
import numpy as np
import tts

def pitch(input_words, output):
    per_word_pitch = []
    sound = parselmouth.Sound(output)

    # Calculate pitch
    pitch = sound.to_pitch()
    # print(pitch)

    # Extract pitch values
    pitch_values = pitch.selected_array['frequency']
    pitch = [x for x in pitch_values if x != 0]
    for i in range(len(input_words)):
        # print(f"{input_words[i]} = Pitch: {pitch[i]:.2f}")
        per_word_pitch.append(f'{input_words[i]}: {pitch[i]} Hz')
    # print(per_word_pitch)
    # Calculate the overall average pitch
    overall_average_pitch = np.mean(pitch)

    # Print the overall average pitch value
    # print(f"Overall Pitch: {overall_average_pitch:.2f} Hz")

    return per_word_pitch, overall_average_pitch

# per_word_putch, _ = pitch(input_words, output)
# print(per_word_putch)
