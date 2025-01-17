# ASCII-CANVAS
This Python script converts images into ASCII art by mapping pixel brightness to ASCII characters. It allows customizable resolution and output options for terminal display or text file saving. Ideal for creating unique text-based visual representations of images.

---
# Image to ASCII Art Converter

This Python script allows you to convert images into detailed ASCII art by mapping pixel brightness to ASCII characters. It resizes the image, converts it to grayscale, and then replaces each pixel with an ASCII character based on its intensity. The resulting ASCII art can be displayed in the terminal or saved as a text file.

## Features
- Converts images into ASCII art based on pixel brightness.
- Customizable output width for different display sizes.
- Save the generated ASCII art to a text file.

## Requirements
- Python 3.x
- `PIL` (Pillow) library

Install Pillow by running:
```bash
pip install pillow
```

## How It Works
1. **Resizing**: The script resizes the input image to a new width while maintaining the aspect ratio. This ensures the output fits within the terminal.
2. **Grayscale Conversion**: The image is converted to grayscale, where each pixel is represented by a single intensity value between 0 (black) and 255 (white).
3. **Pixel-to-ASCII Mapping**: The script maps each pixel's intensity to an ASCII character. Characters like `@`, `#`, and `8` represent darker pixels, while characters like `.` and ` ` (space) represent lighter pixels.
4. **ASCII Art Output**: The script generates the ASCII art as a string, which can be displayed or saved to a file.


You can watch a demo of the script in action:
[Click here to watch the demo video](src/work.mp4)

## How to Use
1. Place your image in the same directory as the script.
2. Run the script in your terminal:
   ```bash
   python image_to_ascii.py
   ```
3. Enter the image path when prompted.
4. The ASCII art will be displayed in the terminal and saved to a file named `ascii_image.txt`.

Here’s a table that you can add to your README to explain the pixel-to-ASCII mapping:

---

## Pixel Value to ASCII Mapping

Each pixel's value is mapped to a corresponding ASCII character based on its intensity. The formula `pixel // 25` determines which segment the pixel falls into, and then the corresponding character from `ASCII_CHARS` is selected.

| **Pixel Value Range** | **Segment (pixel // 25)** | **ASCII Character** |
|-----------------------|---------------------------|---------------------|
| 0–24                  | 0                         | @                   |
| 25–49                 | 1                         | #                   |
| 50–74                 | 2                         | S                   |
| 75–99                 | 3                         | %                   |
| 100–124               | 4                         | ?                   |
| 125–149               | 5                         | *                   |
| 150–174               | 6                         | +                   |
| 175–199               | 7                         | ;                   |
| 200–224               | 8                         | :                   |
| 225–249               | 9                         | ,                   |
| 250–255               | 10                        | .                   |

### Example Calculation:
Assume a pixel value of 180:
- Perform integer division: `180 // 25 = 7`
- Use this as an index: `ASCII_CHARS[7] = ';'`
- Thus, pixel value 180 maps to the ASCII character `;`.

### Visualization of the Mapping:
If you imagine the pixel-to-character mapping as brightness levels, it would look like this:

| **Brightness (Darkest → Brightest)** | **ASCII Representation** |
|--------------------------------------|---------------------------|
| ██████████                          | @                         |
| ████████                           | #                         |
| ██████                              | S                         |
| ████                                | %                         |
| ███                                 | ?                         |
| ██                                  | *                         |
| █                                   | +                         |
| ;                                   | ;                         |
| :                                   | :                         |
| ,                                   | ,                         |
| .                                   | .                         |

This mapping allows each pixel's intensity to be represented by an ASCII character, producing detailed ASCII art when applied across the entire image.

---

Let me know if you'd like to adjust anything else!
## Explanation of Pixel-to-ASCII Mapping

In the `pixels_to_ascii` function, each pixel's intensity is divided by 16 to categorize it into one of the ASCII characters in the `ASCII_CHARS` list. This list contains a range of characters sorted by their perceived darkness, from the darkest (`@`) to the lightest (` `, space). Here's the mapping breakdown:

- `@` represents the darkest pixels (intensity 0–15).
- `#` represents pixels with slightly higher intensity (16–31).
- `.` represents the lightest pixels (240–255).

The more characters you add to `ASCII_CHARS`, the finer the detail in the resulting ASCII art.


