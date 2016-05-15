from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'MuonEG_Run2015C_16Dec2015_Golden38T_Data_160508'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserData_miniAOD_cfg.py'

config.Data.inputDataset = '/MuonEG/Run2015C_25ns-16Dec2015-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt'
config.Data.runRange = '254227-255031' #Run2015C 254227-255031; Run2015D 256630-260627; Run2015D without bad beamspot reco runs 256630-259625,259627-259635,259638-259680,259684,259686-260627
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_Data_nTupilisation_MuonEG_Run2015C_16Dec2015_Golden38T_160508'

config.Site.storageSite = 'T2_UK_London_Brunel'
