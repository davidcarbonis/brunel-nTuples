from CRABClient.client_utilities import getBasicConfig
config = getBasicConfig()

config.General.requestName = 'MC_nTupiliser_TWJets3l1nu_MatchingUp'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'test/nTupliserData_cfg.py'

config.Data.inputDataset = '/WZJetsTo3LNu_matchingup_8TeV_TuneZ2Star_madgraph_tauola/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFN = '/store/user/almorton/TWJets3l1nu_MatchingUp_1/'
config.Data.publication = True
config.Data.publishDataName = 'CRAB3_nTupiliser_TWJets3l1nu_MatchingUp_1'

config.Site.storageSite = 'T2_UK_London_Brunel'
