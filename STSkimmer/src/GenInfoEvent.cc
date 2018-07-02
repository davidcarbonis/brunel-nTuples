#define GenInfoEvent_cxx
#include "NTupliser/STSkimmer/interface/GenInfoEvent.h"

#include <TCanvas.h>
#include <TH2.h>
#include <TStyle.h>

void GenInfoEvent::Loop()
{
    //   In a ROOT session, you can do:
    //      Root > .L GenInfoEvent.C
    //      Root > GenInfoEvent t
    //      Root > t.GetEntry(12); // Fill t data members with entry number 12
    //      Root > t.Show();       // Show values of entry 12
    //      Root > t.Show(16);     // Read and show values of entry 16
    //      Root > t.Loop();       // Loop on all entries
    //

    //     This is the loop skeleton where:
    //    jentry is the global entry number in the chain
    //    ientry is the entry number in the current Tree
    //  Note that the argument to GetEntry must be:
    //    jentry for TChain::GetEntry
    //    ientry for TTree::GetEntry and TBranch::GetEntry
    //
    //       To read only selected branches, Insert statements like:
    // METHOD1:
    //    fChain->SetBranchStatus("*",0);  // disable all branches
    //    fChain->SetBranchStatus("branchname",1);  // activate branchname
    // METHOD2: replace line
    //    fChain->GetEntry(jentry);       //read all branches
    // by  b_branchname->GetEntry(ientry); //read only this branch
    if (fChain == nullptr)
    {
        return;
    }

    Long64_t nentries = fChain->GetEntriesFast();

    Long64_t nbytes = 0;
    Long64_t nb = 0;
    for (Long64_t jentry = 0; jentry < nentries; jentry++)
    {
        Long64_t ientry = LoadTree(jentry);
        if (ientry < 0)
        {
            break;
        }
        nb = fChain->GetEntry(jentry);
        nbytes += nb;
        // if (Cut(ientry) < 0) continue;
    }
}

float GenInfoEvent::getEventWeight(Long64_t /*entry*/)
{
    return 1.;
}
