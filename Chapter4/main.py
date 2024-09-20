import math
import cairo
import logging
logging.basicConfig(level=logging.INFO)

#set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Relative drawing function
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
# 0.523599 radian equals 30 degrees
ctx.move_to(300, 200)
ctx.line_to(300 + 200*math.cos(0.523599), 200 + 200*math.sin(0.523599))
ctx.stroke()

# Relative drawing function
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
# 0.523599 radian equals 30 degrees
ctx.move_to(100, 150)
ctx.line_to(100 + 200*math.cos(0.523599), 150 + 200*math.sin(0.523599))
ctx.stroke()
#line2
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.move_to(100, 150)
ctx.line_to(100 + 200*math.cos(1.047198), 150 + 200*math.sin(1.047198))
ctx.stroke()
# Draw arc
ctx.arc(100,150 ,200,0.523599, 1.047198)
ctx.set_source_rgb(1,0,0)
ctx.stroke()

#draw arrow function
def arrow(ctx, x, y, width, height, a, b):
    ctx.move_to(x, y + b)  # 1
    ctx.line_to(x, y + height - b)  # 2
    ctx.line_to(x + a, y + height - b)  # 3
    ctx.line_to(x + a, y + height)  # 4
    ctx.line_to(x + width, y + height / 2)  # 5
    ctx.line_to(x + a, y)  # 6
    ctx.line_to(x + a, y + b)  # 7
    ctx.close_path()

OUTPUT_DIR = "output_directory/"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    surface.write_to_png(f'{OUTPUT_DIR}lines.png')
    logging.info('Rectangle was generated successfully')
