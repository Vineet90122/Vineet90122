import sys
import json
import librosa

# 🎸 Step 1: Chord Extraction from audio
def extract_chords(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)

    chords = []
    times = librosa.frames_to_time(range(chroma.shape[1]), sr=sr)
    last_chord = None
    start_time = 0

    for i, t in enumerate(times):
        max_note = chroma[:, i].argmax()
        chord = librosa.midi_to_note(60 + max_note)
        if chord != last_chord:
            if last_chord is not None:
                chords.append({
                    "chord": last_chord,
                    "start": round(start_time, 2),
                    "duration": round(t - start_time, 2),
                    "stringIndex": int(start_time) % 6,
                    "correct": True  # default True for ideal
                })
            last_chord = chord
            start_time = t

    return chords

# 🧠 Step 2: Comparison Logic
def compare_chords(ideal, practice):
    feedback = []
    correct_count = 0

    for i, p_chord in enumerate(practice):
        match = i < len(ideal) and ideal[i]["chord"] == p_chord["chord"]
        if match:
            correct_count += 1
        feedback.append({
            **p_chord,
            "correct": match
        })

    accuracy = round((correct_count / max(len(practice), 1)) * 100, 2)

    if accuracy >= 85:
        level = "Professional"
    elif accuracy >= 60:
        level = "Intermediate"
    else:
        level = "Beginner"

    return feedback, accuracy, level

# 🚀 Entry Point
if __name__ == "__main__":
    if len(sys.argv) == 2:
        # ✅ Only one file — extract ideal chords
        ideal_audio = sys.argv[1]
        chords = extract_chords(ideal_audio)
        print(json.dumps({ "feedback": chords }))
    
    elif len(sys.argv) == 3:
        # ✅ Both files — compare ideal vs practice
        ideal_audio = sys.argv[1]
        practice_audio = sys.argv[2]

        ideal_chords = extract_chords(ideal_audio)
        practice_chords = extract_chords(practice_audio)

        feedback, accuracy, level = compare_chords(ideal_chords, practice_chords)

        print(json.dumps({
            "feedback": feedback,
            "accuracy": f"{accuracy}%",
            "level": level
        }))
    
    else:
        print(json.dumps({ "error": "Invalid number of arguments" }))


'''' ye code ideal or practies audio ka feedback de ta hai required both audio 
import librosa
import json

# Dummy: this should be replaced with real chord extraction logic
def extract_chords(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)

    chords = []
    step = 1.0  # analyze each second
    current = 0
    while current < duration:
        chords.append({
            "chord": "C" if int(current) % 2 == 0 else "G",
            "start": current,
            "duration": step,
            "stringIndex": int(current) % 6,
        })
        current += step
    return chords

def compare_chords(ideal, practice):
    feedback = []
    correct_count = 0

    for i, p_chord in enumerate(practice):
        match = i < len(ideal) and ideal[i]["chord"] == p_chord["chord"]
        if match:
            correct_count += 1
        feedback.append({
            **p_chord,
            "correct": match
        })

    accuracy = round((correct_count / max(len(practice), 1)) * 100, 2)

    if accuracy >= 85:
        level = "Professional"
    elif accuracy >= 60:
        level = "Intermediate"
    else:
        level = "Beginner"

    return feedback, accuracy, level

if __name__ == "__main__":
    import sys
    import os

    ideal_audio = sys.argv[1]
    practice_audio = sys.argv[2]

    ideal_chords = extract_chords(ideal_audio)
    practice_chords = extract_chords(practice_audio)

    feedback, accuracy, level = compare_chords(ideal_chords, practice_chords)

    result = {
        "feedback": feedback,
        "accuracy": accuracy,
        "level": level
    }

    print(json.dumps(result))
'''



''' ye code audio ka feed back de ta hai
 auth-system/python/predict.py
import sys
import json
import librosa

def extract_chords(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)

    chords = []
    times = librosa.frames_to_time(range(chroma.shape[1]), sr=sr)
    last_chord = None
    start_time = 0

    for i, t in enumerate(times):
        max_note = chroma[:, i].argmax()
        chord = librosa.midi_to_note(60 + max_note)
        if chord != last_chord:
            if last_chord is not None:
                chords.append({
                    "chord": last_chord,
                    "start": round(start_time, 2),
                    "duration": round(t - start_time, 2),
                    "correct": True
                })
            last_chord = chord
            start_time = t

    return chords

if __name__ == "__main__":
    audio_path = sys.argv[1]
    result = extract_chords(audio_path)
    print(json.dumps(result))
'''