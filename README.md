brunel-nTuples
==============

NTupliser for Brunel group

The famous nTupliser passed down from one generation of Brunel phD student to the next. 
All our marks left indelibly on it, if no other reason than that the next guy has no idea what we did.
Needs documentation, cleaning and... I dunno, re-writing?

Stuff that I know needs to be fixed before run2:

-getByLabels need to be changed to consumes

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

# download the txt files with the corrections
cd EgammaAnalysis/ElectronTools/data
# corrections calculated with 12.9 fb-1 of 2016 data (ICHEP 16 dataset).
git clone -b ICHEP2016_v2 https://github.com/ECALELFS/ScalesSmearings.git

///
To be continued ...

Alexander.

N.B. As Run 2 MC seems to use Pythia 8 for generation, the old status codes have been updated from those used in Pythia 6. This WILL affect the output. Double check generator used if running over old data. 
Status code for gen level is saved. Worth noting that other occasions where status code is checked, these varaibles are not saved to the final root nTuple output. 
