from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DoubleEG_Run2015D_05Oct2015_Golden38T_Data_151202'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserData_miniAOD_cfg.py'

config.Data.inputDataset = '/DoubleEG/Run2015D-05Oct2015-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt'
config.Data.runRange = '256630-258158'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_Data_nTupilisation_DoubleEG_Run2015D_05Oct2015_Golden38T_151202'

config.Site.storageSite = 'T2_UK_London_Brunel'
