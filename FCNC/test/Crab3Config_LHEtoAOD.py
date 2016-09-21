from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'TT_TopLeptonicDecay_TZ_2L_Kappa_Zct_160920'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'prodLHEtoAOD_TT_TopLeptonicDecay_TZ_2L_Kappa_Zct.py'
config.JobType.maxMemoryMB = 2500
config.JobType.inputFiles = ['/tmp/almorton/TLL_Thadronic_kappa_zct.lhe'] #Required for local files, i.e. for ST gen

config.Data.outputPrimaryDataset = 'TT_TopLeptonicDecay_TZ_2L_Kappa_Zct_160920'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC_TT_TopLeptonicDecay_TZ_2L_Kappa_Zct_160920'

config.Site.storageSite = 'T2_UK_London_Brunel'
