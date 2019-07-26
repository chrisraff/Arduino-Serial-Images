# Arduino Serial Images

Sends images over serial to an arduino to be displayed on neopixels. The arduino sketch uses the [FastLED library](https://github.com/FastLED/FastLED) to draw to the neopixels as opposed to the Adafruit one, so you'll need to install that if you don't have it. It can be installed from inside the Arduino IDE.

The python serial writer demo requires the library [pySerial](https://pyserial.readthedocs.io/en/latest/index.html) to communicate over serial, and the library [tqdm](https://tqdm.github.io/) to monitor the frame rate.

## Usage

Upload the `serial_frame_reader` sketch to your arduino.

To view an example, run the python demo:
```
python ./serial_frame_writer_demo.py
```
You can specify a port if needed:
```
python ./serial_frame_writer_demo.py COM10
```


### Image transmission
Images are transmitted as follows:
* `[` starts a frame.
* `]` ends a frame - arduino will update the image.
* `>` starts a pixel. The next 3 bytes are the red, green and blue values of the pixel.
* `.` starts 64 pixels. The next 64*3 bytes are the rgb values for the pixels.
* `x` clears the image buffer.

An example transmission could be
`
x[>rgb>123>abc]
`
, which would clear the buffer and then send a 3 pixel image. The ASCII values of the letters and numbers would dictate the color of the pixels.
