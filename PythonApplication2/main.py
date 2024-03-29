from PhysObject import Vector2d, Phys_Rectangle, Phys_Circle
from physics import Velocity, Universe
from geometry import Point2d
from canvas import Canvas
import time
import sdl2.ext
import sdl2
import copy


def main():
    try:
        Universe.left_boundary = 0
        Universe.right_boundary = 640
        Universe.top_boundary = 0
        Universe.bottom_boundary = 480

        sdl2.ext.init()
        canvas = Canvas(640, 480)
        rect_1 = Phys_Rectangle(Point2d(200, 0), Point2d(300, 80))
        circle_1 = Phys_Circle(Point2d(300, 100), radius = 50)
        circle_2 = Phys_Circle(Point2d(100, 100), radius = 20)

        rect_1.velocity.vx = 200
        rect_1.velocity.vy = 100
        circle_1.velocity.vx = 200
        circle_1.velocity.vy = 100
        circle_2.velocity.vx = 100
        circle_2.velocity.vy = 200

        canvas.update()

        running = True
        frames = 0
        dT = 0
        T0 = time.monotonic()
        dt = 0
        while running:
            t0 = time.monotonic()
            events  = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running  = False
                    break

            rect_1.move(dt)
            if (rect_1.bottom_right.y >= Universe.left_boundary and
                Universe.right_boundary and
                rect_1.velocity.vy > 0):
                rect_1.velocity.vy *= -1
            if (rect_1.bottom_right.x >= Universe.top_boundary and
                Universe.bottom_boundary and
                rect_1.velocity.vx > 0):
                rect_1.velocity.vx *= -1
            if (rect_1.top_left.y <= 0 and rect_1.velocity.vy < 0):
                rect_1.velocity.vy *= -1
            if (rect_1.top_left.x <= 0 and rect_1.velocity.vx < 0):
                rect_1.velocity.vx *= -1
            
            circle_1.move(dt)
            if (circle_1.centre.x + circle_1.radius > Universe.right_boundary and
                circle_1.velocity.vx > 0):
                circle_1.velocity.vx *= -1
            if (circle_1.centre.x - circle_1.radius < Universe.left_boundary and
                circle_1.velocity.vx < 0):
                circle_1.velocity.vx *= -1
            if (circle_1.centre.y + circle_1.radius > Universe.bottom_boundary and
                circle_1.velocity.vy > 0):
                circle_1.velocity.vy *= -1
            if (circle_1.centre.y - circle_1.radius < Universe.top_boundary and
                circle_1.velocity.vy < 0):
                circle_1.velocity.vy *= -1
            
            circle_2.move(dt)
            if (circle_2.centre.x + circle_2.radius > Universe.right_boundary and
                circle_2.velocity.vx > 0):
                circle_2.velocity.vx *= -1
            if (circle_2.centre.x - circle_2.radius < Universe.left_boundary and
                circle_2.velocity.vx < 0):
                circle_2.velocity.vx *= -1
            if (circle_2.centre.y + circle_2.radius > Universe.bottom_boundary and
                circle_2.velocity.vy > 0):
                circle_2.velocity.vy *= -1
            if (circle_2.centre.y - circle_2.radius < Universe.top_boundary and
                circle_2.velocity.vy < 0):
                circle_2.velocity.vy *= -1

            canvas.fill(sdl2.ext.color.Color(r=0, g=0, b=0, a=255))

            #canvas.pixel_color(Point2d(20, 50),
            #                   sdl2.ext.color.Color(r=255, g=0, b=0, a=255))
            #canvas.rect_draw(rect_1,
            #                 sdl2.ext.color.Color(r=255, g=165, b=0, a=255))
            canvas.circle_color(circle_1,
                                sdl2.ext.color.Color(r=255, g=0, b=0, a=255))
            canvas.circle_color(circle_2,
                                sdl2.ext.color.Color(r=255, g=0, b=0, a=255))
            #canvas.line_draw(Line(Point2d(80, 90), Point2d(300, 100)),
            #                 sdl2.ext.color.Color(r=255, g=0, b=0, a=255))

            canvas.update()
            frames += 1
            t1 = time.monotonic()
            dt = t1 - t0
            dT = t1 - T0
            if dT > 1:
                canvas.title(f'FPS:{frames/dT}')
                frames = 0
                T0 = t1
    finally:
        sdl2.ext.quit()


#import profile
if __name__ == '__main__':
    #profile.run('main()')
    main()