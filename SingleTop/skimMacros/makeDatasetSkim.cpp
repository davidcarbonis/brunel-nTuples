#include<iostream>
#include<string>
#include<fstream>
#include"AnalysisEvent.h"
#include<sstream>
#include<sys/stat.h>

int main(int argc, char* argv[]){
  
  std::string fileName = argv[1];
  std::string outFileName = argv[2];

  std::ifstream fileList(fileName.c_str());
  std::string line;             


  TChain * datasetChain = new TChain("tree");

  //Fill chain with provided files
  while(getline(fileList,line)){
    datasetChain->Add(line.c_str());
  }
   
  //Make the output skim tree
  TTree * outTree = datasetChain->CloneTree(0);

  //Make the output file
  TFile outFile(outFileName.c_str(),"RECREATE");
  
  int numberOfEvents = datasetChain->GetEntries();
  AnalysisEvent * event = new AnalysisEvent(false,"",datasetChain);
  for (int i = 0; i < numberOfEvents; i++){
    //Simple status bar to see how far through we are
    if (i % 500 < 0.01) std::cerr << i << "/" << numberOfEvents << " (" << 100*float(i)/numberOfEvents << "%)\r";
    
    event->GetEntry(i);
    int numLeps = 0;
    //Make some electron cuts
    for (int j = 0; j < event->numElePF2PAT; j++){
      if (event->elePF2PATPT[j] < 9) continue;
      if (fabs(event->elePF2PATEta[j]) > 2.7) continue;
      if (event->elePF2PATComRelIsoRho[j]/event->elePF2PATPT[j] > 0.5) continue;
      if (event->elePF2PATMVA[j] < 0.) continue;
      numLeps++;
    }
    //Make some muon cuts
    for (int j = 0; j < event->numMuonPF2PAT; j++){
      if (event->muonPF2PATPt[j] < 9) continue;
      if (event->muonPF2PATComRelIsodBeta[j] > 0.5) continue;
      if (fabs(event->muonPF2PATEta[j]) > 2.8) continue;
      numLeps++;
    }
    //Fill output tree
    if (numLeps >= 2) outTree->Fill();
  }
  
  //write output tree
  outFile.cd();
  outTree->Write();
  outFile.Write();
  outFile.Close();
  //    inFile.Close();

  delete datasetChain;
  delete event;
  delete outTree;
}

