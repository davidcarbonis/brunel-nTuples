#Set up the pat environment
import FWCore.ParameterSet.Config as cms
process = cms.Process("customPAT")

from PhysicsTools.PatAlgos.tools.coreTools import *

#Import the pat configurations
process.load("PhysicsTools.PatAlgos.patSequences_cff")

#Setting up various environmental stuff that makes all of this jazz actually work.

###############################
####### Global Setup ##########
###############################

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.load("RecoBTag.PerformanceDB.BTagPerformanceDB1107")
process.load("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")

process.load("FWCore.Framework.test.cmsExceptionsFatal_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load('Configuration.StandardSequences.Services_cff')

process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.load("Configuration.StandardSequences.MagneticField_cff")

process.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.destinations = ['cerr']
process.MessageLogger.statistics = []
process.MessageLogger.fwkJobReports = []
process.MessageLogger.categories=cms.untracked.vstring('FwkJob'
                                                       ,'FwkReport'
                                                       ,'FwkSummary'
                                                       )

process.MessageLogger.cerr.INFO = cms.untracked.PSet(limit = cms.untracked.int32(0))
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(100)
process.options = cms.untracked.PSet(
                     wantSummary = cms.untracked.bool(True)
                     )

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.globaltag = cms.string('MCRUN2_74_V9')

#There's a bit in here about some btau tags that the code looks for. I don't know if this is significant, however. I'm going to ignore it for now.

#Import jet reco things. Apparently this makes cmsRun crash.
process.load('RecoJets.Configuration.RecoPFJets_cff')


#Now do cool fast jet correction things!

process.ak4PFJets.doRhoFastjet = True

process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlineSlimmedPrimaryVertices'),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(24),
                                           maxd0 = cms.double(2)
                                           )



from PhysicsTools.SelectorUtils.pvSelector_cfi import pvSelector

process.goodOfflinePrimaryVertices = cms.EDFilter(
    "PrimaryVertexObjectFilter",
    filterParams = cms.PSet( minNdof = cms.double( 4. ) ,
                             maxZ = cms.double( 24. ) ,
                             maxRho = cms.double( 2. ) ) ,
    filter = cms.bool( True) ,
    src = cms.InputTag( 'offlineSlimmedPrimaryVertices' ) )

## The iso-based HBHE noise filter ___________________________________________||
process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
process.load('CommonTools.RecoAlgos.HBHENoiseFilter_cfi')

## The CSC beam halo tight filter ____________________________________________||
#process.load('RecoMET.METAnalyzers.CSCHaloFilter_cfi')
process.load('RecoMET.METFilters.CSCTightHaloFilter_cfi')

## The HCAL laser filter _____________________________________________________||
process.load("RecoMET.METFilters.hcalLaserEventFilter_cfi")

## The ECAL dead cell trigger primitive filter _______________________________||
process.load('RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi')

## The EE bad SuperCrystal filter ____________________________________________||
process.load('RecoMET.METFilters.eeBadScFilter_cfi')

## The ECAL laser correction filter
process.load('RecoMET.METFilters.ecalLaserCorrFilter_cfi')

## The tracking failure filter _______________________________________________||
process.load('RecoMET.METFilters.trackingFailureFilter_cfi')

## The tracking POG filters __________________________________________________||
process.load('RecoMET.METFilters.trackingPOGFilters_cff')

process.goodVertices = cms.EDFilter(
      "VertexSelector",
        filter = cms.bool(False),
        src = cms.InputTag("offlineSlimmedPrimaryVertices"),
        cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
      )

process.filtersSeq = cms.Sequence(
    process.HBHENoiseFilterResultProducer *
    process.HBHENoiseFilter *
    process.CSCTightHaloFilter *
    process.hcalLaserEventFilter *
    process.EcalDeadCellTriggerPrimitiveFilter *
    process.goodVertices *
    process.trackingFailureFilter *
    process.eeBadScFilter *
    process.ecalLaserCorrFilter *
    process.trkPOGFilters
    )


#Gen Setup - I'm unsure what this does, and I can't actually do it anyway as I don't think TopQuarkAnalysis actually exists? Or I may have to import it. I don't really know what this does. I assume this is related to that bit of global tags that I didn't do, so I might just ignore this for now.
#process.load("TopQuarkAnalysis.TopEventProducers.sequencepfIsolatedMuonsPF2PATs.ttGenEvent_cff")






###############################
###### Electron ID ############
###############################

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)

# define which IDs we want to produce
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Spring15_25ns_nonTrig_V1_cff']

#add them to the VID producer
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)



###############################
#### MET Corrections Setup ####
###############################
#process.load("PhysicsTools.PatUtils.patPFMETCorrections_cff")
#from PhysicsTools.PatUtils.tools.runType1PFMEtUncertainties import runType1PFMEtUncertainties
#runType1PFMEtUncertainties(process,addToPatDefaultSequence=True,
#                           jetCollection="selectedPatJets",
#                           electronCollection="selectedPatElectrons",
#                           muonCollection="selectedPatMuons",
#                           tauCollection="selectedPatTaus",
#                           )


####
# The N-tupliser/cutFlow
####

triggerStringName = 'HLT'

process.load("NTupliser.SingleTop.MakeTopologyNtuple_miniAOD_cfi")
process.makeTopologyNtupleMiniAOD.flavorHistoryTag=cms.bool(False) # change to false at your convenience
process.makeTopologyNtupleMiniAOD.runMCInfo=cms.bool(True) # prevent checking gen info
process.makeTopologyNtupleMiniAOD.runPUReWeight=cms.bool(True) #Run the reweighting for MC. I think I'm doing this right, but I might check anyway.
#process.makeTopologyNtupleMiniAOD.doCuts=cms.bool(True) # if set to false will skip ALL cuts. Z veto still applies electron cuts.
process.makeTopologyNtupleMiniAOD.triggerTag = cms.InputTag("TriggerResults","",triggerStringName) # or HLT, depends on file   

#settings to apply tight selection:
process.makeTopologyNtupleMiniAOD.minJetPt=cms.double(30)
process.makeTopologyNtupleMiniAOD.maxJetEta=cms.double(2.5)
process.makeTopologyNtupleMiniAOD.bDiscCut=cms.double(0.679)
process.makeTopologyNtupleMiniAOD.minEleEt=cms.double(20)
process.makeTopologyNtupleMiniAOD.maxEleEta=cms.double(2.5)
process.makeTopologyNtupleMiniAOD.ignoreElectronID=cms.bool(False)
process.makeTopologyNtupleMiniAOD.eleCombRelIso=cms.double(0.15)
process.makeTopologyNtupleMiniAOD.maxEled0=cms.double(0.04)
process.makeTopologyNtupleMiniAOD.eleInterECALEtaLow=cms.double(1.4442)
process.makeTopologyNtupleMiniAOD.eleInterECALEtaHigh=cms.double(1.5660)
process.makeTopologyNtupleMiniAOD.minEleEtLooseZVeto=cms.double(15)
process.makeTopologyNtupleMiniAOD.minEleEtaLooseZVeto=cms.double(2.5)
process.makeTopologyNtupleMiniAOD.eleCombRelIsoLooseZVeto=cms.double(0.15)
process.makeTopologyNtupleMiniAOD.dREleJetCrossClean=cms.double(0.3)
process.makeTopologyNtupleMiniAOD.maxMuonEta=cms.double(2.4)
process.makeTopologyNtupleMiniAOD.minMuonPt=cms.double(20)
process.makeTopologyNtupleMiniAOD.maxMuonD0=cms.double(0.02)
process.makeTopologyNtupleMiniAOD.muonRelIsoTight=cms.double(0.2)
process.makeTopologyNtupleMiniAOD.muoNormalizedChi2=cms.double(10)
process.makeTopologyNtupleMiniAOD.muoNTrkHits=cms.double(11)
process.makeTopologyNtupleMiniAOD.muonECalIso=cms.double(4)
process.makeTopologyNtupleMiniAOD.muonHCalIso=cms.double(6)
process.makeTopologyNtupleMiniAOD.dREleGeneralTrackMatchForPhotonRej=cms.double(0.3)
process.makeTopologyNtupleMiniAOD.maxDistForPhotonRej=cms.double(0.04)
process.makeTopologyNtupleMiniAOD.maxDcotForPhotonRej=cms.double(0.03)
process.makeTopologyNtupleMiniAOD.fillAll=cms.bool(True)
process.makeTopologyNtupleMiniAOD.processingLoose=cms.bool(False)
#process.makeTopologyNtupleMiniAOD.btagParameterizationList = cms.vstring()
#process.makeTopologyNtupleMiniAOD.btagParameterizationMode = cms.vstring()
process.makeTopologyNtupleMiniAOD.runSwissCross = cms.bool(False)
#Don't actually do cuts
process.makeTopologyNtupleMiniAOD.doCuts = cms.bool(False)
process.makeTopologyNtupleMiniAOD.runCutFlow=cms.double(0)

#Make the inputs for the n-tupliser right.
process.makeTopologyNtupleMiniAOD.electronPFTag = cms.InputTag("slimmedElectrons")
process.makeTopologyNtupleMiniAOD.tauPFTag = cms.InputTag("slimmedTaus")
process.makeTopologyNtupleMiniAOD.muonPFTag = cms.InputTag("slimmedMuons")
process.makeTopologyNtupleMiniAOD.jetPFToken = cms.InputTag("slimmedJets")
process.makeTopologyNtupleMiniAOD.metPFTag = cms.InputTag("slimmedMETs")
process.makeTopologyNtupleMiniAOD.rho = cms.InputTag("fixedGridRhoAll")                                                                          

##electronIdMva Stuff.
#process.makeTopologyNtupleMiniAOD.eleLooseIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring15-25ns-nonTrig-V1-wp90")
#process.makeTopologyNtupleMiniAOD.eleTightIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring15-25ns-nonTrig-V1-wp80")
#process.makeTopologyNtupleMiniAOD.mvaValuesMap = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values")
#process.makeTopologyNtupleMiniAOD.mvaCategoriesMap = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories")

## Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring()
)

## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.source.fileNames = [
	#'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/06A911BC-3CBB-E311-9AFD-00266CFACC38.root',
        #'root://xrootd.unl.edu//store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/02E34918-E717-E511-AD0A-001E675A6630.root',
    'root://xrootd.unl.edu//store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/008E7FBF-9218-E511-81E0-001E675A5244.root',
#        'root://xrootd.unl.edu//store/mc/RunIISpring15DR74/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v1/00000/006A97CE-D301-E511-8072-0025905A60A6.root',
        ]

from PhysicsTools.PatAlgos.patEventContent_cff import *
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('patTuple.root'),
                               ## save only events passing the full path
                               #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               ## save PAT output; you need a '*' to unpack the list of commands
                               outputCommands = cms.untracked.vstring('drop *', *patEventContentNoCleaning )
                               )

process.out.outputCommands += patEventContent
process.out.outputCommands += patTriggerEventContent
process.out.outputCommands += patExtraAodEventContent
process.out.outputCommands += cms.untracked.vstring('keep *_flavorHistoryFilter_*_*','keep *_TriggerResults_*_*','keep *_selectedPat*_*_*', 'keep *_*goodOfflinePrimaryVertices*_*_*','keep double_*_rho_*', 'keep patMuons_*_*_*', 'keep *MET*_*_*_*', 'keep *_*MET*_*_*')


#PAT output and various other outpath stuff which is a bit dumb coz I'm probably not even gonna use the outpath. Nevermind.
process.out.fileName = cms.untracked.string('Data_out.root')

#NTuple output
process.TFileService = cms.Service("TFileService", fileName = cms.string('Data_output.root') )
process.options.wantSummary = False
process.out.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p'))

#Removing pat output (coz we really don't need it now)
#del process.out

process.p = cms.Path(
    process.goodOfflinePrimaryVertices*
    process.primaryVertexFilter * #removes events with no good pv (but if cuts to determine good pv change...)
#    process.filtersSeq *
#    process.producePatPFMETCorrections *
    process.egmGsfElectronIDSequence *
    process.makeTopologyNtupleMiniAOD
    )

process.schedule = cms.Schedule( process.p )

process.outpath = cms.EndPath( process.out )
