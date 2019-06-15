# aiff_to_header

This repo contains a utility script to create a c style `.h` header file from a `.aiff` source for usage in embedded projects.

## Usage

Install dependencies:

```bash
$ pip install -r requirements.txt
```

Edit `aiff_to_header.py` file to specify parameters such as the C number type - the default format is `uint8_t`.

Run script and specify an input file (note this should be a single channel `.aiff` file):

```bash
$ python aiff_to_header.py chirp.aiff
```

Inspect output header file created with the same name (e.g. `chirp.h`).

## Reference

- [SoundFile](https://pypi.org/project/SoundFile/)

