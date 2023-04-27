from gpio import *
from time import *

def main():
	pinMode(1, OUT)
	print("on")
	while True:
		if digitalRead("""your port""") == HIGH:
			customWrite("""your port""", "1,0")
		else:
			customWrite("""your port""", "0,1")
		sleep(1)

if __name__ == "__main__":
	main()
