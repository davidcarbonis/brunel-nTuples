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


CMSSW_7_4_7 branch contains code from CMSSW_5_3_X branch which is being modified to work for Run 2 data.
As data taking is using CMSSW_7_4_X, the branch is named CMSSW_7_4_7 as the version which data and MC is currently avaliable for (and which electron VID and MET uncertainities are avlaiable for).
Development is currently being undertaken in CMSSW_7_4_7.

git cms-merge-topic ikrav:egm_id_747_v2 needs to be executed in order for electron Id and MVA to work.
git cms-merge-topic -u cms-met:METCorUnc74X needs to be executed in order for MET corrections to work? Not sure ...

This version currently only works for miniAOD inputs.

To be continued ...

Alexander.

