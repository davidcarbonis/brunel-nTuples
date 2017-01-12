#include "TChain.h"
#include "TTree.h"

#include <stdlib.h>
#include <string>
#include <fstream>
#include <sstream>
#include <regex>
#include <iostream>

#include <boost/range/iterator_range.hpp>
#include <boost/filesystem.hpp>

namespace fs = boost::filesystem;

int main(int argc, char* argv[]) {

  const std::string inDir = argv[1];

  const std::regex mask{".*.root"};
  std::vector<std::string> inFiles;

  for (const auto& file :
          boost::make_iterator_range(fs::directory_iterator{inDir}, {}))
  {
      if (!fs::is_regular_file(file.status())
              || !std::regex_match(file.path().filename(), mask))
      {
          continue;
      }

      inFiles.emplace_back(file.path().string());
  }

  long long unsigned totalEvents{0};
  for (const auto& file : inFiles)
  {

    TChain * datasetChain = new TChain("makeTopologyNtupleMiniAOD/tree");
    datasetChain->Add(file.c_str());

    totalEvents += datasetChain->GetEntries();

    delete datasetChain;
  }

  std::cout << "Found " << totalEvents << " events." << std::endl;

  std::cout << "\nFinished." << std::endl;
}
