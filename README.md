# Arduino Serial Images

Sends images over serial to an arduino to be displayed on neopixels.

The python serial writer demo requires the library [pySerial](https://pyserial.readthedocs.io/en/latest/index.html) to communicate over serial, and the library [tqdm](https://tqdm.github.io/) to monitor the frame rate.

## Usage

Upload the `serial_frame_reader` sketch to your arduino. Images can be transmitted as follows:
* `[` starts a frame.
* `]` ends a frame - arduino will update the image.
* `>` starts a pixel. The next 3 bytes are the red, green and blue values of the pixel.
* `.` starts 64 pixels. The next 64*3 bytes are the rgb values for the pixels.

An example transmission could be
`
[>rgb>123>abc]
`
, which would be a 3 pixel image. The ASCII values of the letters and numbers would dictate the color of the pixels.
