# Command Line Interface

Command line options for accel

```bash
python -m accel [OPTIONS] input
```

## Options

| Option                | Type | Description                                       | Default    | Choices       |
|-----------------------|------|---------------------------------------------------|------------|---------------|
| `input`               | str  | Path to input (file or folder)                    | *required* | -             |
| `--output`            | str  | Path to output destination                        | *required* | -             |
| `--min_dist`          | int  | Maximum distance between two waypoints            | 25         | -             |
| `--extract_waypoints` | bool | Extract starting points of each track as waypoint | True       | [True, False] |
| `--elevation`         | bool | Include elevation data in waypoints               | True       | [True, False] |


## Examples


### 1. Basic usage

```bash
python -m accel input
```

### 2. With verbose logging

```bash
python -m accel -v input
python -m accel --verbose input
```

### 3. With quiet mode

```bash
python -m accel -q input
python -m accel --quiet input
```

### 4. With min_dist parameter

```bash
python -m accel --min_dist 25 input
```

### 5. With extract_waypoints parameter

```bash
python -m accel --extract_waypoints True input
```

### 6. With elevation parameter

```bash
python -m accel --elevation True input
```