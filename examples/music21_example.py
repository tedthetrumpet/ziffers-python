from music21 import *
from sardine import *
from ziffers import *


s = to_music21('i v vi vii^dim',time="4/4")

s.show()
s.show('midi')

parsed = zparse('1 2 qr e 124')
s2 = to_music21(parsed,time="4/4")

s2.show()
s2.show('midi')