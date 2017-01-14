# Adding in a few variables to change up flags etc
CC = g++
CFLAGS = -march=native -mtune=native -pthread -Wextra -O2 \
		$(shell root-config --auxcflags) \
		-Wall \
		-Wextra \
		-Wcast-align \
		-Wcast-qual \
		-Wctor-dtor-privacy \
		-Wformat=2 \
		-Winit-self \
		-Winline \
		-Wlogical-op \
		-Wmissing-include-dirs \
		-Wnoexcept \
		-Wold-style-cast \
		-Woverloaded-virtual \
		-Wredundant-decls \
		-Wshadow \
		-Wstrict-null-sentinel \
		-Wswitch-default \
		-Wuseless-cast \
		-Wnon-virtual-dtor \
		-Wzero-as-null-pointer-constant
INCDIR = -isystem$(shell root-config --incdir)
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
	$(CC) $(CFLAGS) $(INCDIR) -o skims.exe makeDatasetSkim.o AnalysisEvent.o $(LIBS)
eventCounter.exe: eventCounter.o
	$(CC) $(CFLAGS) $(INCDIR) -o eventCounter.exe eventCounter.o $(LIBS)

makeDatasetSkim.o: makeDatasetSkim.cpp
	$(CC) $(CFLAGS) $(INCDIR) -c makeDatasetSkim.cpp $(LIBS)
eventCounter.o: eventCounter.cpp
	$(CC) $(CFLAGS) $(INCDIR) -c eventCounter.cpp $(LIBS)

AnalysisEvent.o: AnalysisEvent.C AnalysisEvent.h
	$(CC) $(CFLAGS) $(INCDIR) -c AnalysisEvent.C $(LIBS)

