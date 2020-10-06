import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing a Face")

arcade.set_background_color(arcade.color.GHOST_WHITE)

arcade.start_render()

# Draw the face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# Draw the right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the right eyeball
x = 370
y = 350
radius = 10
arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE)

# Draw the left eye
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left eyeball
x = 230
y = 350
radius = 10
arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE)

# Draw the smile
x = 300
y = 260
width = 120
height = 100
start_angle = 180
end_angle = 360
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 20)

arcade.finish_render()

arcade.run()
arcade.close_window()




