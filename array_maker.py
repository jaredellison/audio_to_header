import soundfile as sf

# Max sample value:
# 255 for 8bit
SAMPLE_MAX = 255

# Get samples from aiff file
data, samplerate = sf.read("./chirp.aiff")

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

# Save to output file
f = open('out.txt', 'w')

f.write("-- Start --")

cols = 16
col = 0

for d in data:
    col = col + 1
    f.write(f"{d}, ")
    if (col % cols == 0):
        f.write(f"\n")

f.close()

