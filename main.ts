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

input.onButtonPressed(Button.A, function () {
  robotbit.Servo(servoNumber1, 0)
  basic.clearScreen()
  basic.showString('0')
  basic.showIcon(IconNames.SmallHeart)
  basic.clearScreen()
  basic.showIcon(IconNames.Heart)
})

input.onButtonPressed(Button.B, function () {
  robotbit.Servo(servoNumber1, 180)
  basic.clearScreen()
  basic.showString('180')
  basic.showIcon(IconNames.SmallHeart)
  basic.clearScreen()
  basic.showIcon(IconNames.Heart)
})
