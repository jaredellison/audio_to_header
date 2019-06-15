# aiff_to_header

> Utility script creates c style `.h` header file based on an `.aiff` source

Quick and dirty script for including audio samples in embedded projects.

#### Usage

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

```bash
$ less chirp.h
```

#### Authors

- **Jared Ellison** - [jaredellison.net](http://jaredellison.net/)

#### References

- [SoundFile](https://pypi.org/project/SoundFile/)

