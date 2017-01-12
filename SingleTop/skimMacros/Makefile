# Adding in a few variables to change up flags etc
CC = g++
CFLAGS = -g -Wall -O2 $(shell root-config --cflags)
LIBS = $(shell root-config --libs) -lboost_filesystem -lboost_system

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
	$(CC) $(CFLAGS) -o skims.exe makeDatasetSkim.o AnalysisEvent.o $(LIBS)
eventCounter.exe: eventCounter.o
	$(CC) $(CFLAGS) -o eventCounter.exe eventCounter.o $(LIBS)

makeDatasetSkim.o: makeDatasetSkim.cpp
	$(CC) $(CFLAGS) -c makeDatasetSkim.cpp $(LIBS)
eventCounter.o: eventCounter.cpp
	$(CC) $(CFLAGS) -c eventCounter.cpp $(LIBS)

AnalysisEvent.o: AnalysisEvent.C AnalysisEvent.h
	$(CC) $(CFLAGS) -c AnalysisEvent.C $(LIBS)

