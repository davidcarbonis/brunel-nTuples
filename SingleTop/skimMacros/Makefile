# Adding in a few variables to change up flags etc
CC = g++
CFLAGS = -g -Wall -std=c++0x $(shell root-config --cflags) -I/home/eepgadm/lib/local/include
LIBS = $(shell root-config --libs) -L/home/eepgadm/lib/local/lib -lconfig++ 
ROOTSYS = /cms/cmssw/slc5_amd64_gcc462/lcg/root/5.32.00/

default: build

clean: _cleanall
_cleanall:
	rm -rf *.o
	rm -rf *.exe

all: _all
build: _all
buildall: _all
_all: skims.exe

skims.exe: makeDatasetSkim.o AnalysisEvent.o
	$(CC) $(CFLAGS) $(LIBS) -o skims.exe makeDatasetSkim.o AnalysisEvent.o

makeDatasetSkim.o: makeDatasetSkim.cpp
	$(CC) $(CFLAGS) $(LIBS) -c makeDatasetSkim.cpp

AnalysisEvent.o: AnalysisEvent.C AnalysisEvent.h   
	$(CC) $(CFLAGS) $(LIBS) -c AnalysisEvent.C 

