brunel-nTuples
==============

NTupliser for Brunel group

The famous nTupliser passed down from one generation of Brunel phD student to the next. 
All our marks left indelibly on it, if no other reason than that the next guy has no idea what we did.

Enjoy, future students.

//////////////////////////////////


CMSSW_8_0_5 branch contains code from CMSSW_7_6_3 branch which is modified to work for Run 2 miniAOD 80X data and MC.
As data/MC reprocessing taking is using CMSSW_8_0_X, the branch is named CMSSW_8_0_5 as the version which data and MC is currently avaliable for (and which electron VID and MET uncertainities are avlaiable for).
Development is being undertaken in.

For MET Filters not included in HLT collection to work, the following command must be executed:
git cms-merge-topic -u cms-met:CMSSW_8_0_X-METFilterUpdate

For EGM Smearing to work follow the instructions below:
git remote add -f -t ecal_smear_fix_80X emanueledimarco https://github.com/emanueledimarco/cmssw.git
git cms-addpkg EgammaAnalysis/ElectronTools
git checkout -b from-52f192a 52f192a

// download the txt files with the corrections
cd EgammaAnalysis/ElectronTools/data
// corrections calculated with 12.9 fb-1 of 2016 data (ICHEP 16 dataset).
git clone -b ICHEP2016_v2 https://github.com/ECALELFS/ScalesSmearings.git

///

N.B. As Run 2 MC seems to use Pythia 8 for generation, the old status codes have been updated from those used in Pythia 6. This WILL affect the output. Double check generator used if running over old data. 
Status code for gen level is saved. Worth noting that other occasions where status code is checked, these varaibles are not saved to the final root nTuple output. 

///

FCNC Stuff:

Generation of signal samples up till the LHE format: https://twiki.cern.ch/twiki/bin/view/CMS/TopFCNCgenerationSingletop
Rest of instructions follow below ...

cmsDriver instructions used to create various FCNC files:

pileup:
cmsDriver.py MinBias_13TeV_pythia8_TuneCUETP8M1_cfi --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 --fast -n 5000000 --mc --eventcontent FASTPU -s GEN,SIM,RECOBEFMIX --datatier GEN-SIM-RECO --beamspot Realistic25ns13TeV2016Collision --era Run2_2016 --fileout minbias.root --no_exec

Current output dataset DAS URL: https://cmsweb.cern.ch/das/request?input=%2FMinBias%2Falmorton-CRAB3_MC_nTupilisation_PileUp_160905-0e8a9371e45edd808242a5d89d29dcd9%2FUSER&instance=prod%2Fphys03

pileup premixing:
cmsDriver.py SingleNuE10_cfi --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 --pileup_input "dbs:/MinBias/almorton-CRAB3_MC_nTupilisation_PileUp_160905-0e8a9371e45edd808242a5d89d29dcd9/USER instance=prod/phys03" --fast --mc --eventcontent PREMIX -s GEN,SIM,RECOBEFMIX,DIGIPREMIX,L1,DIGI2RAW --era Run2_2016 --beamspot Realistic25ns13TeV2016Collision --datatier GEN-SIM-DIGI-RAW --pileup 2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU -n 5000000 --fileout minbias_premixed.root --no_exec

Current output dataset DAS URL: N/A - not used as minbias input currently

FCNC script for LHE to AOD:
cmsDriver.py FCNCProd/FastSim/Hadronizer_Generic_cfi.py --mc --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 --filein file:/scratch/data/TopPhysics/FCNC/lhe/TLL_Thadronic_kappa_zct.lhe --filetype LHE --era Run2_2016 --fast -n 2500000 --eventcontent AODSIM --datatier AODSIM -s GEN,SIM,RECOBEFMIX,DIGI,L1,L1Reco,RECO,HLT --python_filename prodLHEtoAOD_ST_TZ_2L_Kappa_Zct.py --pileup 2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU --beamspot Realistic25ns13TeV2016Collision --pileup_input "dbs:/MinBias/almorton-CRAB3_MC_nTupilisation_PileUp_160905-0e8a9371e45edd808242a5d89d29dcd9/USER instance=prod/phys03" --fileout aod.root --no_exec

Current output dataset DAS URLs: In production

FCNC script for AOD to miniAOD:
To be written ...
Current output dataset DAS URLs: In production

Alexander.
