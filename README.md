brunel-nTuples
==============

ntupliser for brunel group

the famous ntupliser passed down from one generation of brunel phd student to
the next. all our marks left indelibly on it, if no other reason than that the
next guy has no idea what we did.

enjoy, future students.

***

The CMSSW_9_4_8 branch contains code from CMSSW_8_0_25 branch which is modified
to work for Run 2 miniAODv2 94X data and MC. 

This is currently a work in progress left to be completed by the next generation.

Added since last version (8_0_27):
- Muon ID/Iso/etc bools
- Electron VIDs (see below under to be fixed)
- DeepCSV and DeepCMVA added to bTagger list

To be fixed:

- Implement EGM smearing and regression for 94X: 92X required EGM smearing and regression and VID (ie ID cuts) to be added in python
config files and run on top of the miniAOD. The 94X or 2017 and 2016 re-reco miniAODv2s have these already done.
However, using normal accessors such as ele.p4() returns unsmeared values. The correct accessors have been done for the VID for both
2016 and 2017 (set by the is2016rereco flag in the python cfi file), but has not been done for things like energy/momentum smearing.

- Compiling the skimmer: currently fails to compile

- Running MC and Data scripts leads to the following error message which needs to be fixed: 
```bash 
	An exception of category 'ScheduleExecutionFailure' occurred while
	   [0] Calling beginJob
	Exception Message:
	Unrunnable schedule
	Module run order problem found:
	p after makeTopologyNtupleMiniAOD [path p], makeTopologyNtupleMiniAOD consumes TriggerResults, TriggerResults consumes p
	 Running in the threaded framework would lead to indeterminate results.
	 Please change order of modules in mentioned Path(s) to avoid inconsistent module ordering.
	----- End Fatal Exception -------------------------------------------------
```

---

## Additional setup info:

NOTE!!!! YOU DO NOT HAVE TO DO THIS!!!
Only if you want to recreate the EGM regression/smearing corrections that are already in the re-miniAODv2
```bash
git cms-merge-topic cms-egamma:EgammaPostRecoTools_940 #just adds in an extra file to have a setup function to make things easier
git cms-merge-topic cms-egamma:Egamma80XMiniAODV2_946 #adds the c++ changes necessary to enable 2016 scale & smearing corrections
```
---
