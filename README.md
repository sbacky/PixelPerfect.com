# Pixel Perfect

Click on the image to get the color hex. Open an image from your computer or drag and drop an image in the canvas to get started.

## Installation

Clone this repository to get started:

```bash
git clone https://github.com/sbacky/PixelPerfect.com.git
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run main.py:

```bash
python main.py
```

## Guide

Images are scaled down by default to a maximum width of 1024 pixels and a maximum height of 768 pixels. This can be changed in shared_config.py to your desired width and height.

```python
# image_handling.py
class SharedConfig:
    _instance: Union[Type['SharedConfig'], None] = None
    def __new__(cls: Type['SharedConfig']) -> 'SharedConfig':
            if cls._instance is None:
                cls._instance = super(SharedConfig, cls).__new__(cls)
                # Other settings ...
                cls._instance.max_size = (1024, 768) # <--- Edit this line (width, height)
            return cls._instance
```

Color history contains the last 5 colors previewed along with the color hex.

## Future Updates

This section contains any features I want to add. The order the features are listed are roughly the order they will be implemented. I will release updates when I can, but this project is a hobby.

### PixelPreview

Enter a hex and preview the color. Provide a complimentary color for the selected color, a lighter shade of the selected color, and a darker shade of the selected color. The color will also have its associated hex.

### Update pixel selector in PixelPerfect

On hover, bring up a zoomed in version of the picture, estimating what pixel is being selected. This will give more control over what color is being selected from the image.