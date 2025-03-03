# Speaker Recognition with MFCC and Cosine Similarity

This Python script compares two audio files by extracting their Mel-Frequency Cepstral Coefficients (MFCCs) and calculating the cosine similarity between them. The result is a similarity score that helps determine how similar the two audio files are. If the similarity exceeds a defined threshold, the script determines that the files match.

## Requirements

To run this script, you need to have the following libraries installed:

- **librosa**: Used for audio processing and feature extraction.
- **numpy**: Used for numerical computations.
- **scipy**: Used to calculate cosine similarity.

Install the dependencies with the following command:

```bash
pip install librosa numpy scipy

## Set File Paths
Replace the file1 and file2 variables in the script with the paths to the audio files you want to compare. For example:


file1 = "C:\path\to\your\audio1.wav"
file2 = "C:\path\to\your\audio2.wav" 
```

**Run the Script**
After setting the file paths, run the script in your terminal:
```
python voiceidentify.py
```
 Output
The script will output the similarity score between the two audio files and whether they match or not based on the threshold. The output will look like this:

```
Similarity between the two audio files: 0.85
The audio files match.
```



## Installation
1. Clone the repository:
```bash
 git clone https://github.com/darkuser21/speaker-recognition.git
```

2. Install dependencies:
```bash
pip install librosa numpy scipy
 ```
#**Run the Script**
```bash
python voiceidentify.py
 ```
## Output
```
Similarity between the two audio files: 0.85
The audio files match.
```

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes.
4. Push your branch: `git push origin feature-name`.
5. Create a pull request.

   ## For Further Information feel free to contact
