# generate frequency data 
import math

start = 21 # A0
end = 104 #A7

def midiToFreq(note) :
  return (math.pow(2, ((note-69)/12.0)))*440;

if __name__ == "__main__":
	for i in range(start, end):
		print "%f, " % midiToFreq(i) 

