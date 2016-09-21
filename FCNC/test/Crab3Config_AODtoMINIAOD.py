from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'TT_TopLeptonicDecay_TZ_2L_Kappa_Zct_RunIISpring16MiniAODv2_160920'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'prodAODtoMINIAOD.py'
config.JobType.maxMemoryMB = 2500

config.Data.inputDataset = '/TT_TopLeptonicDecay_TZ_2L_Kappa_Zct_160919/almorton-CRAB3_MC_TT_TopLeptonicDecay_TZ_2L_Kappa_Zct_160919-58d7b4917a1118d8447b03a0cf3c4041/USER'
config.Data.inputDBS = 'phys03'

config.Data.outputPrimaryDataset = 'TT_TopLeptonicDecay_TZ_2L_Kappa_Zct_RunIISpring16MiniAODv2_160920'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC_TT_TopLeptonicDecay_TZ_2L_Kappa_Zct_RunIISpring16MiniAODv2_160920'

config.Site.storageSite = 'T2_UK_London_Brunel'
