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


CMSSW_7_6_1 branch contains code from CMSSW_7_4_14 branch which is modified to work for Run 2 miniAOD v2 data and MC.
As data/MC reprocessing taking is using CMSSW_7_6_X, the branch is named CMSSW_7_6_1 as the version which data and MC is currently avaliable for (and which electron VID and MET uncertainities are avlaiable for).
Development is being undertaken in.

git cms-merge-topic ikrav:egm_id_7.4.12_v1 needs to be executed in order for electron Id and MVA to work. (Still the case for 76X?)

This version only works for miniAOD v2 inputs.

To be continued ...

Alexander.

N.B. As Run 2 MC seems to use Pythia 8 for generation, the old status codes have been updated from those used in Pythia 6. This WILL affect the output. Double check generator used if running over old data. 
Status code for gen level is saved. Worth noting that other occasions where status code is checked, these varaibles are not saved to the final root nTuple output. 
