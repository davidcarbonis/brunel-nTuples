from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'WZJets_ScaleDown_MC_150306'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserMC_cfg.py'

config.Data.inputDataset = '/WZJetsTo3LNu_scaledown_8TeV_TuneZ2Star_madgraph_tauola/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFN = '/store/user/almorton/nTuples/WT/150306/MC/'

#config.Data.outLFN = '/store/user/<subdir>' # or '/store/group/<subdir>'

config.Data.publication = False
config.Data.publishDataName = 'CRAB3_MC_nTupilisation_ScaleDown_150306'

config.Site.storageSite = T2_UK_London_Brunel

