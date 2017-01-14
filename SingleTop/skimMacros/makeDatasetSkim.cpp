#include <array>
#include <iostream>
#include <string>
#include <sys/stat.h>
#include <regex>
#include <vector>

#include <boost/filesystem.hpp>
#include <boost/range/iterator_range.hpp>
#include <boost/progress.hpp>

#include <TChain.h>
#include <TH1I.h>
#include <TFile.h>
#include <TTree.h>

#include "AnalysisEvent.h"


namespace fs = boost::filesystem;


int main(int argc, char* argv[])
{
    const std::string inDir{argv[1]};
    const std::string datasetName{argv[2]};
    const bool isMC{argc >= 4 ? std::stoi(argv[3]) : false};

    const std::regex mask{".*\\.root"};
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

    int fileNum{0};
    for (const auto& file: inFiles)
    {
        const std::string numName{std::to_string(fileNum)};
        const std::string numNamePlus{std::to_string(fileNum + 2)};

        struct stat buffer;
        if (stat(("/scratch/data/tZqSkimsRun2016/" + datasetName + "/skimFile"
                        + numNamePlus + ".root").c_str(), &buffer) == 0)
        {
            fileNum++;
            continue;
        } // ?

        std::array<unsigned int, 14> summedWeights{};
        TH1I weightHisto{"sumNumPosMinusNegWeights",
            "sumNumPosMinusNegWeights", 7, -3.5, 3.5};

        TChain datasetChain{"makeTopologyNtupleMiniAOD/tree"};
        datasetChain.Add(file.c_str());

        // std::cout << file;
        // TFile inFile(file.c_str());

        TTree * const outTree = datasetChain.CloneTree(0);

        std::string outFilePath{"/scratch/data/tZqSkimsRun2016/" + datasetName
            + "/skimFile" + numName + ".root"};
        TFile outFile{outFilePath.c_str(), "RECREATE"};

        // std::cout << outFilePath << std::endl;

        const long long int numberOfEvents{datasetChain.GetEntries()};
        boost::progress_display progress{numberOfEvents, std::cout, outFilePath + "\n"};
        AnalysisEvent event{isMC, "", &datasetChain};

        for (long long int i{0}; i < numberOfEvents; i++)
        {
            ++progress;

            event.GetEntry(i);

#ifndef NO_LHE
            // Get number of positive and negative amc@nlo weights
            if (isMC)
            {
                event.origWeightForNorm >= 0.0   ? summedWeights[0]++
                                                 : summedWeights[1]++;
                event.weight_muF0p5 >= 0.0       ? summedWeights[2]++
                                                 : summedWeights[3]++;
                event.weight_muR0p5 >= 0.0       ? summedWeights[4]++
                                                 : summedWeights[5]++;
                event.weight_muF0p5muR0p5 >= 0.0 ? summedWeights[6]++
                                                 : summedWeights[7]++;
                event.weight_muF2 >= 0.0         ? summedWeights[8]++
                                                 : summedWeights[9]++;
                event.weight_muR2 >= 0.0         ? summedWeights[10]++
                                                 : summedWeights[11]++;
                event.weight_muF2muR2 >= 0.0     ? summedWeights[12]++
                                                 : summedWeights[13]++;
            }
#endif

            int numLeps{0};
            for (int j = 0; j < event.numElePF2PAT; j++)
            {
                if (event.elePF2PATPT[j] < 9
                        || std::abs(event.elePF2PATEta[j]) > 2.7
                        || event.elePF2PATComRelIsoRho[j] > 0.5)
                {
                    continue;
                }
                numLeps++;
            }
            for (int j = 0; j < event.numMuonPF2PAT; j++)
            {
                if (event.muonPF2PATPt[j] < 9
                        || event.muonPF2PATComRelIsodBeta[j] > 0.5
                        || std::abs(event.muonPF2PATEta[j]) > 2.8)
                {
                    continue;
                }
                numLeps++;
            }
            if (numLeps >= 2)
            {
                outTree->Fill();
            }
        }

        if (isMC)
        {
#ifndef NO_LHE
            weightHisto.Fill(0., summedWeights[0] - summedWeights[1]);
            weightHisto.Fill(-1., summedWeights[2] - summedWeights[3]);
            weightHisto.Fill(-2., summedWeights[4] - summedWeights[5]);
            weightHisto.Fill(-3., summedWeights[6] - summedWeights[7]);
            weightHisto.Fill(1., summedWeights[8] - summedWeights[9]);
            weightHisto.Fill(2., summedWeights[10] - summedWeights[11]);
            weightHisto.Fill(3., summedWeights[12] - summedWeights[13]);
#else
            weightHisto.Fill(0., -666.);
            weightHisto.Fill(-1., -666);
            weightHisto.Fill(-2., -666);
            weightHisto.Fill(-3., -666);
            weightHisto.Fill(1., -666);
            weightHisto.Fill(2., -666);
            weightHisto.Fill(3., -666);
#endif
        }

        outFile.cd();
        outTree->Write();
        if (isMC)
        {
            weightHisto.Write();
        }

        outFile.Write();
        outFile.Close();
        // inFile.Close();

        fileNum++;

        std::cout << std::endl;
    }
}
