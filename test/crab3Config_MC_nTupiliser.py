from CRABClient.client_utilities import getBasicConfig
config = getBasicConfig()

config.General.requestName = 'MC_nTupiliser_TWJets3l1nu_ScaleUp'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'test/Crab3ConfignTupiliser_cfg.py'

config.Data.inputDataset = '/WZJetsTo3LNu_scaleup_8TeV_TuneZ2Star_madgraph_tauola/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFN = '/store/user/almorton/Crab3/TWJets3l1nu_ScaleUp/'
config.Data.publication = True
config.Data.publishDataName = 'CRAB3_TWJets3l1nu_ScaleUp'

config.Site.storageSite = 'T2_UK_London_Brunel'
