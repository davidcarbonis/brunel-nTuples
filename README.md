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
N.B. For some reason I have not been able to get premixing to work correctly on pion - used lxplus machines to submit the Crab jobs and retrieved the final output (i.e. signal files) on pion.

cmsDriver instructions used to create various FCNC files:

pileup:
FCNC script for LHE to AOD:
cmsDriver.py FCNCProd/FastSim/Hadronizer_Generic_cfi.py --mc --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 --filein file:/scratch/data/TopPhysics/FCNC/lhe/TLL_Thadronic_kappa_zct.lhe --filetype LHE --era Run2_2016 --fast -n 2500000 --eventcontent AODSIM --datatier AODSIM -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,HLT:@frozen2016 --python_filename prodLHEtoAOD_ST_TZ_2L_Kappa_Zct.py --pileup 2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput --beamspot Realistic25ns13TeV2016Collision --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring16FSPremix-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-DIGI-RAW" --fileout aod.root --no_exec

Current output dataset DAS URLs: In production

FCNC script for AOD to miniAOD:
To be written ...
Current output dataset DAS URLs: In production

Alexander.
