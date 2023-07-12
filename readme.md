![](images/fw_bot_bck.jpeg)

# Digital File Monitoring BOT

The BOT is responsible to Monitor, Retrieve and Process as Source Directory based on a Configuration ini file as the input.
This input is a required to define on the keywords and/or file-type to search on and move the files to respective directories so that they can be given for further analysis.

## Executable

An executable "bot_setup" is provided that is bundled with all dependencies for most of the operating systems. This can be found at <a href="dist/bot_setup#_new">Github: dist</a>.

![Static Badge](https://img.shields.io/badge/python-%3E%3Dv3.10-blue)
![Static Badge](https://img.shields.io/badge/dist-download-pink)
![Static Badge](https://img.shields.io/badge/release-v1.0.0-purple)
![Static Badge](https://img.shields.io/badge/docs-sphinx-purple)
![Static Badge](https://img.shields.io/badge/htmlcov-coverage-yellow)
![Static Badge](https://img.shields.io/badge/test_case-pytest-yellow)
![Static Badge](https://img.shields.io/badge/metrics-radon-yellow)

# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
