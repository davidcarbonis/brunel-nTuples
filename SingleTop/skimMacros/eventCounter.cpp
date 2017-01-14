#include <iostream>
#include <regex>

#include <boost/range/iterator_range.hpp>
#include <boost/filesystem.hpp>

#include <TChain.h>
#include <TTree.h>


namespace fs = boost::filesystem;


int main(int argc, char* argv[])
{
    const std::string inDir = argv[1];

    const std::regex mask{".*\\.root"};
    std::vector<std::string> inFiles;

    for (const auto& file:
            boost::make_iterator_range(fs::directory_iterator{inDir}, {}))
    {
        if (!fs::is_regular_file(file.status())
                || !std::regex_match(file.path().filename(), mask))
        {
            continue;
        }

        inFiles.emplace_back(file.path().string());
    }

    long long int totalEvents{0};
    for (const auto& file: inFiles)
    {

        TChain datasetChain{"makeTopologyNtupleMiniAOD/tree"};
        datasetChain.Add(file.c_str());

        totalEvents += datasetChain.GetEntries();
    }

    std::cout << "Found " << totalEvents << " events." << std::endl;
    std::cout << "\nFinished." << std::endl;
}
