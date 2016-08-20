from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DoubleEG_Run2016B_PromptReco_Golden38T_Data_160820'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserData_miniAOD_cfg.py'

config.Data.inputDataset = '/DoubleEG/Run2016B-PromptReco-v2/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.lumiMask = '/afs/cern.ch/user/j/jfernan/public/TOPtriggerJSONS2016/TOP_Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_NoL1T_UnprescaledPaths.txt'

# Golden JSON: /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt
# NoL1T Unprescaled (for Single + Double EG): /afs/cern.ch/user/j/jfernan/public/TOPtriggerJSONS2016/TOP_Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_NoL1T_UnprescaledPaths.txt

config.Data.runRange = '272007-275376' #Run2016B 272007-275376; Run2016C 275657-276283; Run2016D 276315-276811; Run2016E 276831-277420; Run2016F 277772-278808; Run2016G 278820-;
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_Data_nTupilisation_DoubleEG_Run2016B_PromptReco_Golden38T_160820'

config.Site.storageSite = 'T2_UK_London_Brunel'
