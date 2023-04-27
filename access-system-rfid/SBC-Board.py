from gpio import *
from time import *

def main():
	pinMode(1, OUT)
	print("Blinking")
	while True:
		if digitalRead(0) == HIGH:
			customWrite(1, "1,0")
		else:
			customWrite(1, "0,1")
		sleep(1)

if __name__ == "__main__":
	main()
