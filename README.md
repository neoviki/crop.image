## `crop.image`: Crop Image by Coordinates

A utility to crop an image based on user-provided coordinates.

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repo_url>
   cd <repo_folder>
   ```

2. Run the installer:
   ```bash
   ./install.sh
   ```

---

## Usage

```bash
crop.image <image_file> <top_left_x> <top_left_y> <bottom_right_x> <bottom_right_y>
```

**Example:**

```bash
crop.image input.jpg 100 50 400 300
```

This crops a rectangle from the image starting at `(100, 50)` and ending at `(400, 300)`.

---

## How to Find Coordinates

To interactively select an area in an image and get its coordinates, use:

🔗 [https://www.image-map.net/](https://www.image-map.net/)

---

## Tested On

- macOS
