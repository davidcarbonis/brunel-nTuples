from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'MuonEG_Run2015D_PromptV4_Golden38T_Data_151023'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserData_miniAOD_cfg.py'

config.Data.inputDataset = '/MuonEG/Run2015D-PromptReco-v4/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt'
config.Data.runRange = '258159-258750'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.publishDataName = 'CRAB3_Data_nTupilisation_MuonEG_Run2015D_PromptV4_Golden38T_151023'

config.Site.storageSite = 'T2_UK_London_Brunel'
