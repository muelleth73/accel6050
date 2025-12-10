# Installation


## 🐍 PyPI

### Install the package from PyPI

Download from [PyPI](https://pypi.org/):

```bash
pip install accel
```

### Run CLI from command line
```bash
accel [OPTIONS] path/to/file
```

### Run GUI from command line
```bash
accel-gui
```

## 🔽 Executable

Download the latest executable:

- [⬇️ Download for Windows](https://github.com/muelleth73/accel/releases/latest/download/installer-win.zip)
- [⬇️ Download for macOS](https://github.com/muelleth73/accel/releases/latest/download/package-macos.zip)


## 👩🏼‍💻 Run from source

### Clone the repository

```bash
git clone
```

### Navigate to the project directory

```bash
cd accel
```

### Install dependencies

```bash
uv venv
uv pip install -e .[dev,docs]
```


### Run with CLI from source

```bash
python -m accel.cli [OPTIONS] path/to/file
```


### Run with GUI from source

```bash
python -m accel.gui
```

