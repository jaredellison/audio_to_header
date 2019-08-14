# audio_to_header

> Utility script creates a c style `.h` header file based on an audio source file

Quick and dirty script for including audio samples in embedded projects.

#### Usage

Install dependencies:

```bash
$ pip install -r requirements.txt
```

Edit `audio_to_header.py` file to specify parameters such as the C number type - the default format is `uint8_t`.

Run script and specify an input file (this has been tested with a a single channel `.aiff` file but may work with others - see soundfile dependency for compatibility):

```bash
$ python aiff_to_header.py chirp.aiff
```

Inspect output header file created with the same name (e.g. `chirp.h`).

```bash
$ less chirp.h
```

#### Authors

- **Jared Ellison** - [jaredellison.net](http://jaredellison.net/)

#### References

- [SoundFile](https://pypi.org/project/SoundFile/)

