P = python3

all: run

runTests : src/ThreeStackTest.py
	$(P) src/ThreeStackTest.py

run : src/ThreeStack.py
	$(P) src/ThreeStack.py