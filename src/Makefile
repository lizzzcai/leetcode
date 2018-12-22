CC = g++

OPT = -O0 -ggdb -std=c++11
WARN = -Wall -Wno-unused-function -finline-functions
INCPATH = -I. -I../ThirdParty/googletest-1.7.0/include
CFLAGS = $(WARN) $(OPT) $(INCPATH)



GTEST = -L../ThirdParty/googletest-1.7.0 -lgtest_main -lgtest -lpthread

# Easy
OBJECTS = \
		  ./001_TwoSum/TwoSum.o \



# Easy
TESTS = \
		TwoSum_test \




all: gtest $(OBJECTS) $(TESTS)

$(OBJECTS): %.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

gtest:
	cmake ../ThirdParty/googletest-1.7.0/CMakeLists.txt
	make -C ../ThirdParty/googletest-1.7.0/


# Individual Tests

# Easy

#helloworld_test: ./0_start/helloworld_test.cc ./0_start/helloworld.o
#	$(CC) $(CFLAGS) $^ $(GTEST) -o $@
TwoSum_test: ./001_TwoSum/TwoSum_test.cpp ./001_TwoSum/TwoSum.o 
	$(CC) $(CFLAGS) $^ $(GTEST) -o $@
ReverseInteger_test: ./007_ReverseInteger/ReverseInteger_test.cpp ./007_ReverseInteger/ReverseInteger.o
	$(CC) $(CFLAGS) $^ $(GTEST) -o $@
RomanToInteger_test: ./013_RomanToInteger/RomanToInteger_test.cpp ./013_RomanToInteger/RomanToInteger.o
	$(CC) $(CFLAGS) $^ $(GTEST) -o $@






clean:
	rm -f */*.o *_test

