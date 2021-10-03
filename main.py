def on_up_pressed():
    john.vy += 0 - paddle_speed
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    nico.vy += paddle_speed
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    nico.vy += 0 - paddle_speed
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_down_released():
    john.vy += 0 - paddle_speed
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_on_overlap(sprite, otherSprite):
    if sprite == nico:
        otherSprite.vx = ball_speed * -1
    else:
        otherSprite.vx = ball_speed
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_a_released():
    nico.vy += paddle_speed
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_up_released():
    john.vy += paddle_speed
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    john.vy += paddle_speed
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_b_released():
    nico.vy += 0 - paddle_speed
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

paddle_speed = 0
ball_speed = 0
john: Sprite = None
nico: Sprite = None
nico = sprites.create(img("""
        . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . .
    """),
    SpriteKind.player)
nico.set_position(148, 53)
nico.set_stay_in_screen(True)
john = sprites.create(img("""
        . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . . 
            . . . . . . . 3 3 . . . . . . .
    """),
    SpriteKind.player)
john.set_stay_in_screen(True)
john.set_position(2, 51)
ball = sprites.create(img("""
        . . . . 9 9 9 9 9 9 9 . . . . 
            . . 9 9 9 9 9 9 9 9 9 9 9 . . 
            . 9 9 9 9 9 9 9 9 9 9 9 9 9 . 
            . 9 9 9 9 9 9 9 9 9 9 9 9 9 . 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            . 9 9 9 9 9 9 9 9 9 9 9 9 9 . 
            . 9 9 9 9 9 9 9 9 9 9 9 9 9 . 
            . . 9 9 9 9 9 9 9 9 9 9 9 . . 
            . . . . 9 9 9 9 9 9 9 . . . .
    """),
    SpriteKind.projectile)
ball_speed = 50
ball.set_velocity(ball_speed, ball_speed)
ball.set_bounce_on_wall(True)
paddle_speed = 100