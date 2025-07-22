#include <AccelStepper.h>

AccelStepper stepper(AccelStepper::DRIVER, 3, 4); // STEP = 3, DIR = 4

void setup() {
  stepper.setMaxSpeed(1000);     // steps per second
  stepper.setAcceleration(500);  // steps per second^2
  stepper.moveTo(200);           // move one full rotation
}

void loop() {
  if (stepper.distanceToGo() == 0) {
    stepper.moveTo(-stepper.currentPosition()); // reverse direction
  }
  stepper.run(); // Must be called in loop
}