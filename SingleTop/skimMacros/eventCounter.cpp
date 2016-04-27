#include "TChain.h"
#include "TTree.h"

#include <stdlib.h> 
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>

int main(int argc, char* argv[]) {

  std::string fileName = argv[1];

  std::ifstream fileList(fileName.c_str());
  std::string line;             
  uint totalEvents(0);

  while(getline(fileList,line)){

    TChain * datasetChain = new TChain("makeTopologyNtupleMiniAOD/tree");
    datasetChain->Add(line.c_str());
    
    uint numberOfEvents = datasetChain->GetEntries();
    totalEvents += numberOfEvents;

    delete datasetChain;
  }

  std::cout << "Found " << totalEvents << " events." << std::endl;

  std::cout << "\nFinished." << std::endl;
}
