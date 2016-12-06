from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DoubleEG_Run2016G_23Sep2016_Golden38T_Data_161201'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserData_miniAOD_cfg.py'

config.Data.inputDataset = '/DoubleEG/Run2016G_23Sep2016-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.lumiMask = '/afs/cern.ch/user/j/jfernan/public/TOPtriggerJSONS2016/7Oct/LSfor_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_withLowestSeed_L1_DoubleEG_22_10.json'

## ICHEP
# Golden JSON: /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt
# NoL1T Unprescaled (for Single + Double EG): /afs/cern.ch/user/j/jfernan/public/TOPtriggerJSONS2016/TOP_Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_NoL1T_UnprescaledPaths.txt

## Full year
# Golden JSON: /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
# NoL1T Unprescaled (for Single + Double EG): https://twiki.cern.ch/twiki/pub/CMS/TopTrigger/LSfor_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_withLowestSeed_L1_DoubleEG_22_10.json

config.Data.runRange = '278820-280385' #Run2016B 272007-275376; Run2016C 275657-276283; Run2016D 276315-276811; Run2016E 276831-277420; Run2016F 277772-278808; Run2016G 278820-280385; Run2016H 280919-284044;
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_Data_nTupilisation_DoubleEG_Run2016G_23Sep2016_Golden38T_161201'

config.Site.storageSite = 'T2_UK_London_Brunel'
