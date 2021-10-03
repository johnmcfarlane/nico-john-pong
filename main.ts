controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    john.vy += 0 - paddle_speed
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    nico.vy += paddle_speed
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    nico.vy += 0 - paddle_speed
})
controller.down.onEvent(ControllerButtonEvent.Released, function on_down_released() {
    john.vy += 0 - paddle_speed
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    if (sprite == nico) {
        otherSprite.vx = ball_speed * -1
    } else {
        otherSprite.vx = ball_speed
    }
    
})
controller.A.onEvent(ControllerButtonEvent.Released, function on_a_released() {
    nico.vy += paddle_speed
})
controller.up.onEvent(ControllerButtonEvent.Released, function on_up_released() {
    john.vy += paddle_speed
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    john.vy += paddle_speed
})
controller.B.onEvent(ControllerButtonEvent.Released, function on_b_released() {
    nico.vy += 0 - paddle_speed
})
let paddle_speed = 0
let ball_speed = 0
let john : Sprite = null
let nico : Sprite = null
nico = sprites.create(img`
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
    `, SpriteKind.Player)
nico.setPosition(148, 53)
nico.setStayInScreen(true)
john = sprites.create(img`
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
    `, SpriteKind.Player)
john.setStayInScreen(true)
john.setPosition(2, 51)
let ball = sprites.create(img`
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
    `, SpriteKind.Projectile)
ball_speed = 50
ball.setVelocity(ball_speed, ball_speed)
ball.setBounceOnWall(true)
paddle_speed = 100
