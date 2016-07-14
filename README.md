brunel-nTuples
==============

NTupliser for Brunel group

The famous nTupliser passed down from one generation of Brunel phD student to the next. 
All our marks left indelibly on it, if no other reason than that the next guy has no idea what we did.
Needs documentation, cleaning and... I dunno, re-writing?

Enjoy, future students.

//////////////////////////////////


CMSSW_7_6_3 branch contains code from CMSSW_7_4_14 branch which is modified to work for Run 2 miniAOD 76X data and MC.
As data/MC reprocessing taking is using CMSSW_7_6_X, the branch is named CMSSW_7_6_3 as the version which data and MC is currently avaliable for (and which electron VID and MET uncertainities are avlaiable for).
Use CMSSW_7_6_3 branch for Run 2015 and CMSSW_8_0_5 branch for Run 2016.

For EGMSmearing to work, the user will have to execute the following command and compile CMSSW:
git cms-merge-topic -u matteosan1:smearer_76X


To be continued ...

Alexander.

N.B. As Run 2 MC seems to use Pythia 8 for generation, the old status codes have been updated from those used in Pythia 6. This WILL affect the output. Double check generator used if running over old data. 
Status code for gen level is saved. Worth noting that other occasions where status code is checked, these varaibles are not saved to the final root nTuple output. 
