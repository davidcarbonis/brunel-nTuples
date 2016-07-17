# Adding in a few variables to change up flags etc
CC = g++
CFLAGS = -g -Wall -std=c++0x $(shell root-config --cflags)
LIBS = $(shell root-config --libs)
ROOTSYS = /cms/cmssw/slc5_amd64_gcc462/lcg/root/5.32.00/

#EXECUTABLE_OBJECT_FILES = $(patsubst %.cpp,%.o,${EXECUTABLE_SOURCES})
#EXECUTABLE_SOURCES = $(wildcard *.cpp)
#EXECUTABLES = $(patsubst %.cpp,%.exe,${EXECUTABLE_SOURCES})

default: build

clean: _cleanall
_cleanall:
	rm -rf *.o
	rm -rf *.exe

all: _all
build: _all
buildall: _all
_all: skims.exe eventCounter.exe

skims.exe: makeDatasetSkim.o AnalysisEvent.o
	$(CC) $(CFLAGS) $(LIBS) -o skims.exe makeDatasetSkim.o AnalysisEvent.o
eventCounter.exe: eventCounter.o
	$(CC) $(CFLAGS) $(LIBS) -o eventCounter.exe eventCounter.o

makeDatasetSkim.o: makeDatasetSkim.cpp
	$(CC) $(CFLAGS) $(LIBS) -c makeDatasetSkim.cpp
eventCounter.o: eventCounter.cpp
	$(CC) $(CFLAGS) $(LIBS) -c eventCounter.cpp

AnalysisEvent.o: AnalysisEvent.C AnalysisEvent.h   
	$(CC) $(CFLAGS) $(LIBS) -c AnalysisEvent.C 

