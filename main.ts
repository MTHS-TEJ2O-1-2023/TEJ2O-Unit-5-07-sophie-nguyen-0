/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: sophie
 * Created on: nov 2023
 * This program moves servo
*/

// variables
const servoNumber1 = robotbit.Servos.S1

// setup
basic.showIcon(IconNames.Heart)

// button A pressed
input.onButtonPressed(Button.A, function () {
  // turns servo to 0 degrees
  robotbit.Servo(servoNumber1, 0)
  basic.clearScreen()
  basic.showString('0')

  // finished turning
  basic.showIcon(IconNames.SmallHeart)
  basic.clearScreen()
  basic.showIcon(IconNames.Heart)
})

// button B pressed
input.onButtonPressed(Button.B, function () {
  // turns servo to 180 degrees
  robotbit.Servo(servoNumber1, 180)
  basic.clearScreen()
  basic.showString('180')

  // finished turning
  basic.showIcon(IconNames.SmallHeart)
  basic.clearScreen()
  basic.showIcon(IconNames.Heart)
})
