import cairo
import logging
logging.basicConfig(level=logging.INFO)

#set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

#draw the image
ctx.rectangle(150, 100, 100, 240)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

#draw the green rectangle
ctx.rectangle(300, 100, 100, 240)
ctx.set_source_rgb(0, 1, 0)
ctx.fill()

#draw the blue square
ctx.rectangle(300, 100, 100, 240)
ctx.set_source_rgb(0, 1, 0)
ctx.fill()

OUTPUT_DIR = "output_directory/"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    surface.write_to_png(f'{OUTPUT_DIR}new_rectangle.png')
    logging.info('Rectangle was generated successfully')