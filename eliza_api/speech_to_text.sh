
# Install DeepSpeech
pip3 install deepspeech

# Download pre-trained English model files
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/deepspeech-0.8.1-models.pbmm
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/deepspeech-0.8.1-models.scorer

# Download example audio files
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/audio-0.8.1.tar.gz
tar xvf audio-0.8.1.tar.gz

# Transcribe an audio file
deepspeech --model deepspeech-0.8.1-models.pbmm --scorer deepspeech-0.8.1-models.scorer --audio audio/2830-3980-0043.wav