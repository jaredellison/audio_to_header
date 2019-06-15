import soundfile as sf

def get_samples(file_path, SAMPLE_MAX = 255):
    # Max sample value:
    # 255 for 8bit
    # SAMPLE_MAX = 255

    # Get samples from aiff file
    data, samplerate = sf.read(file_path)

    # Find peak to normalize
    max_sample = max(data)
    min_sample = abs(min(data))

    if max_sample > min_sample:
        gain = 1 / max_sample
    else:
        gain = 1 / min_sample

    # Process each sample
    #   Apply gain
    #   Set sample to range between 0 and 1
    #   Scale based on max sample
    #   Cast samples to integer
    data = [int(SAMPLE_MAX * ((d * gain + 1) / 2)) for d in data]

    return data