from gamelib import *

game = Game(600,384,"Paddle Game")
bk = Animation("background17SpriteSheet.png",8,game,5120/5,768/2,4)
ball = Image("globe.png",game)
ball.resizeBy(-90)
ball.setSpeed(4,60)

paddle1 = Image("paddle.png",game,False)
paddle1.y = game.height - 40
paddle1.score = 0

font = Font(white,40,black,"Comic Sans MS")
while not game.over:
  game.processInput()

  bk.draw()
  ball.move(True)
  paddle1.draw()

  paddle1.x = mouse.x

  if ball.y < 15:
    paddle1.score += 1

  if ball.y > game.height - 20:
    paddle1.health -= 10
    ball.moveTo(game.width / 2, game.height / 2)

  if paddle1.health < 0:
    game.over = True

  if ball.collidedWith(paddle1,"rectangle"):
    ball.changeYSpeed()
    ball.speed += 0.5

  game.drawText(f"Score: {paddle1.score}",10,10, font)
  game.drawText(f"Health: {paddle1.health}",400,10, font)
  
  game.update(60)
game.quit()
