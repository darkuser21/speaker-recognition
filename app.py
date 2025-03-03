import librosa
import numpy as np
from scipy.spatial.distance import cosine

# Function to extract MFCCs from an audio file
def extract_mfcc(file_path):
    y, sr = librosa.load(file_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)  # Extract MFCC features (13 coefficients)
    mfcc_mean = np.mean(mfcc, axis=1)  # Take the mean to reduce dimensionality
    return mfcc_mean

# Function to compare two audio files using cosine similarity
def compare_audio(file1, file2):
    mfcc1 = extract_mfcc(file1)
    mfcc2 = extract_mfcc(file2)
    
    # Calculate the cosine similarity between the two MFCC feature sets
    similarity = 1 - cosine(mfcc1, mfcc2)
    
    return similarity

# Path to your two audio files (using raw strings)
file1 = r"c:\Users\HP\Downloads\New\audio2.wav"
file2 = r"c:\Users\HP\Downloads\New\audio1.wav"

# Compare the files
similarity = compare_audio(file1, file2)
print(f"Similarity between the two audio files: {similarity}")

# Decide if the audio matches or not (you can set a threshold)
threshold = 0.8
if similarity > threshold:
    print("The audio files match.")
else:
    print("The audio files do not match.")
