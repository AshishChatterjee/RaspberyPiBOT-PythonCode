import sys
import tty
import termios
UP=0
DOWN=1
RIGHT=2
LEFT=3

def readchar():
    fd=sys.stdin.fileno()
    old_settings=termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch=sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN,old_setting)

    if ch== '0x03':
        raise KeyboardInterrupt
    return ch
def readchar(getchar_fn=None):
    getchar=getchar_fn or readchar
    C1=getchar()
    if ord(C1)!=0x1b:
        return C1
    C2=getchar()
    if ord(C2)!=0x5b:
        return C1
    C3=getchar()
    return ord(C3)-65
#0=UP,1=DOWN,2=RIGHT,3=LEFT arrows
#End of the functions that read your keyboard

speed=30
Pi2go.init()
#Main body of Code this detects your keypress and changes direction dependi $

try:
    while True:
        Keyp=readkey()
        if Keyp=='w' or Keyp==UP:
            Pi2go.forward(speed)
            print 'Forward=',speed
        elif Keyp=='s' or Keyp==DOWN:
            Pi2go.reverse(speed)
            print 'Backward=',speed
            
        elif Keyp=='d' or Keyp==RIGHT:
            Pi2go.spinRight(speed)
            print 'Spin Right=',speed
            
        elif Keyp=='.' or Keyp=='>':
            speed=min(100, speed+10)
            print 'Speed + ',speed
            
        elif Keyp==',' or Keyp=='<':
            speed=max(0, speed-10)
            print 'Speed - ',speed
            
        elif Keyp==' '
            Pi2go.stop()
            print 'Stop'
        elif ord(Keyp)==3:
            break
#When you want to exit -press CTRL +C and it will generate a keyboard interrupts.
except KeyboardInterrupt:
        Pi2go.cleanup()


