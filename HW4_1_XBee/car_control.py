import time
import serial
import sys,tty,termios
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get():
    d1 = input()
    d2 = input()
    direction = input()
    t1 = (float(d1) + 7)/5.8
    t2 = (float(d2) + 6)/5.8

    s.write("/goStraight/run -30 \n".encode())
    time.sleep(t2)
    s.write("/stop/run \n".encode())
    time.sleep(1.5)

    if direction[0] == 'e':
        s.write("/turn/run -30 0.05 \n".encode())
        time.sleep(2.65)
        s.write("/stop/run \n".encode())
    elif direction[0] == 'w':
        s.write("/turn/run -30 -0.05 \n".encode())
        time.sleep(4)
        s.write("/stop/run \n".encode())
    time.sleep(1.5)

    s.write("/goStraight/run -30 \n".encode())
    time.sleep(t1)
    s.write("/stop/run \n".encode())
    time.sleep(1.5)

s = serial.Serial(sys.argv[1])
get()
#18cm/s