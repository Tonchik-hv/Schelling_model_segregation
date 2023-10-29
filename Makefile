all: compile_cpp

compile_cpp:
	g++ func.cpp -std=c++11 -O2 -Wall -shared -o mylib.so
clean:
	rm -f *.o
