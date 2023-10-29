cpp_source = func.cpp
compiler = g++
flags = -std=c++11 -O2 -Wall -shared
output = mylib.so

all: compile_cpp

compile_cpp:
	$(compiler) $(cpp_source) $(flags) -o $(output)
clean:
	rm -f *.o
