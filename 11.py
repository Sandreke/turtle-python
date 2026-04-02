import turtle
import json
import time

def draw_from_json(json_file, pause=0.0):
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(800, 800)
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.pensize(0)

    with open(json_file) as f:
        regions = json.load(f)

    all_points = [p for r in regions for p in r['contour']]
    min_x = min(p[0] for p in all_points)
    max_x = max(p[0] for p in all_points)
    min_y = min(p[1] for p in all_points)
    max_y = max(p[1] for p in all_points)

    img_w = max_x - min_x
    img_h = max_y - min_y
    scale = min(700 / img_w, 700 / img_h)
    cx = (min_x + max_x) / 2
    cy = (min_y + max_y) / 2

    def to_screen(px, py):
        return (px - cx) * scale, (cy - py) * scale

    total = len(regions)
    print(f"Dibujando {total} regiones...")

    for i, region in enumerate(regions):
        r, g, b = [int(c) for c in region['color']]
        color_hex = f'#{r:02x}{g:02x}{b:02x}'
        t.color(color_hex, color_hex)
        points = region['contour']
        if len(points) < 3:
            continue

        sx, sy = to_screen(points[0][0], points[0][1])
        t.goto(sx, sy)
        t.begin_fill()
        for pt in points[1:]:
            t.goto(*to_screen(pt[0], pt[1]))
        t.goto(sx, sy)
        t.end_fill()

        screen.update()

        if pause > 0:
            time.sleep(pause)

        print(f"  {i+1}/{total}", end='\r')

    print(f"\nDibujo completado")
    screen.mainloop()

if __name__ == "__main__":
    draw_from_json("resources/tulipanes.json", pause=0.2)