#include<iostream>
#include<string>
#include<fstream>
#include"AnalysisEvent.h"
#include<sstream>
#include<sys/stat.h>

int main(int argc, char* argv[]){
  
  std::string fileName = argv[1];
  std::string datasetName = argv[2];

  std::ifstream fileList(fileName.c_str());
  std::string line;             


  int fileNum = 0;
  while(getline(fileList,line)){

    std::string numName, numNamePlus;
    std::ostringstream convert, convert1;
    convert << fileNum;
    convert1 << fileNum+2;
    numName = convert.str();
    numNamePlus = convert1.str();
    
    struct stat buffer;
    if (stat(("/scratch/data/tZqSkimsRun2/" + datasetName + "/skimFile"+numNamePlus+".root").c_str(), &buffer) == 0) {
      fileNum++;
      continue;
    }

    TChain * datasetChain = new TChain("makeTopologyNtupleMiniAOD/tree");
    datasetChain->Add(line.c_str());
    
    //    std::cout << line;
    //TFile inFile(line.c_str());
    

    TTree * outTree = datasetChain->CloneTree(0);

    //stupid long conversion between int and string.

    TFile outFile(("/scratch/data/tZqSkimsRun2/" + datasetName + "/skimFile"+numName+".root").c_str(),"RECREATE");
  
    int numberOfEvents = datasetChain->GetEntries();
    AnalysisEvent * event = new AnalysisEvent(false,"",datasetChain);
    for (int i = 0; i < numberOfEvents; i++){
      if (i % 500 < 0.01) std::cerr << i << "/" << numberOfEvents << " (" << 100*float(i)/numberOfEvents << "%)\r";
    
      event->GetEntry(i);
      int numLeps = 0;
      for (int j = 0; j < event->numElePF2PAT; j++){
	if (event->elePF2PATPT[j] < 9) continue;
	if (fabs(event->elePF2PATEta[j]) > 2.7) continue;
	if (event->elePF2PATComRelIsoRho[j]/event->elePF2PATPT[j] > 0.5) continue;
	numLeps++;
      }
      for (int j = 0; j < event->numMuonPF2PAT; j++){
	if (event->muonPF2PATPt[j] < 9) continue;
	if (event->muonPF2PATComRelIsodBeta[j] > 0.5) continue;
	if (fabs(event->muonPF2PATEta[j]) > 2.8) continue;
	numLeps++;
      }
      if (numLeps >= 2) outTree->Fill();
    }
  
    outFile.cd();
    outTree->Write();
    outFile.Write();
    outFile.Close();
    //    inFile.Close();

    delete datasetChain;
    delete event;
    delete outTree;
    fileNum++;
    std::cerr << "" << std::endl;
  }

}

