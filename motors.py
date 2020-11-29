import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

H = True
L = False

class Motor:
    def __init__(self, dPin, pPin, t = .005):
        self.dPin = dPin
        self.pPin = pPin
        self.pState = H
        self.dState = H
        GPIO.setup(dPin, GPIO.OUT)
        GPIO.setup(pPin, GPIO.OUT)

        sleep(3*t)
        GPIO.output(dPin, H)
        GPIO.output(pPin, H)
        sleep(3*t)

        GPIO.output(dPin, L)
        sleep(3*t)

        for i in range(3):
                GPIO.output(pPin, L)
                sleep(3*t)
                GPIO.output(pPin, H)
                sleep(3*t)

        GPIO.output(dPin, H)
        sleep(3*t)


    def toggleBit(self, bit):
        if bit == 0:
            bit = 1
        else:
            bit = 0
        return bit

    def halfStep(self):
        self.pState = self.toggleBit(self.pState)
        GPIO.output(self.pPin, self.pState)

    def halfStepIzq(self):
        self.dState = H
        GPIO.output(self.dPin, self.dState)
        self.halfStep()

    def halfStepDer(self):
        self.dState = L
        GPIO.output(self.dPin, self.dState)
        self.halfStep()

    def setDir(self, dir):
        self.dState = L if dir == "izq" else H
        GPIO.output(self.dPin, self.dState)


def main():
    m1 = Motor(19, 6)
    m2 = Motor(5, 13)

    def drawSquare(m1,m2):
        m1.setDir("izq")
        for i in range(400):
            m1.halfStep()
            sleep(.01)
        m2.setDir("izq")
        for i in range(400):
            m2.halfStep()
            sleep(.01)
        m1.setDir("der")
        for i in range(400):
            m1.halfStep()
            sleep(.01)
        m2.setDir("der")
        for i in range(400):
            m2.halfStep()
            sleep(.01)

if __name__ == '__main__':
    main()
