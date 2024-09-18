import math
import cairo
import logging
logging.basicConfig(level=logging.INFO)

#set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

#draw the red rectangle
ctx.rectangle(60, 40, 100, 40)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

# Stroke
ctx.rectangle(250, 100, 100, 240)
ctx.set_source_rgb(0, 1, 0)
ctx.set_line_width(5)
ctx.stroke()

# Fill and stroke
ctx.rectangle(400, 100, 100, 240)
ctx.set_source_rgb(0, 0, 1)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

#draw the green rectangle
ctx.rectangle(10, 10, 40, 70)
ctx.set_source_rgb(0, 1, 0)
ctx.fill()

#draw the blue square
ctx.rectangle(350, 300, 50, 50)
ctx.set_source_rgb(0, 0, 1)
ctx.fill()

# Draw a line
ctx.move_to(230, 50)
ctx.line_to(500, 50)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(5)
ctx.stroke()

# Draw an arc
ctx.arc(50,30,150,0, math.pi/2)
ctx.set_source_rgb(1,0,0)
ctx.stroke()

# Draw a small circle
ctx.arc(70,340,50,0, 2*math.pi)
ctx.set_source_rgb(1,0,1)
ctx.set_line_width(10)
ctx.stroke()

#create single bezier curves
ctx.move_to(100,200)
ctx.curve_to(200,100,400,300,500,200)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(10)
ctx.stroke()

#poly curves (bezier)
ctx.move_to(100,100)
ctx.curve_to(200,0,400,200,500,100)
ctx.line_to(500,300)
ctx.curve_to(400,400,200,200,100,300)
ctx.close_path()
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(10)
ctx.stroke()

OUTPUT_DIR = "output_directory/"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    surface.write_to_png(f'{OUTPUT_DIR}new_rectangle.png')
    logging.info('Rectangle was generated successfully')