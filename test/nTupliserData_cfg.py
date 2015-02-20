#Set up the pat environment
from PhysicsTools.PatAlgos.patTemplate_cfg import *

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
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.destinations = ['cerr']
process.MessageLogger.statistics = []
process.MessageLogger.fwkJobReports = []
process.MessageLogger.categories=cms.untracked.vstring('FwkJob'
                                                       ,'FwkReport'
                                                       ,'FwkSummary'
                                                       )

process.MessageLogger.cerr.INFO = cms.untracked.PSet(limit = cms.untracked.int32(0))
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)
process.options = cms.untracked.PSet(
                     wantSummary = cms.untracked.bool(True)
                     )

process.GlobalTag.globaltag = cms.string('START53_V19::All')

#There's a bit in here about some btau tags that the code looks for. I don't know if this is significant, however. I'm going to ignore it for now.


#Import jet reco things. Apparently this makes cmsRun crash.
process.load('RecoJets.Configuration.RecoPFJets_cff')

#Now do cool fast jet correction things!

process.kt6PFJets.doRhoFastjet = True

process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
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
    src = cms.InputTag( 'offlinePrimaryVertices' ) )

## The iso-based HBHE noise filter ___________________________________________||
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
        src = cms.InputTag("offlinePrimaryVertices"),
        cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
      )

process.filtersSeq = cms.Sequence(
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
#process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")





###############################
####### PF2PAT Setup ##########
###############################

# Default PF2PAT with AK5 jets. Make sure to turn ON the L1fastjet stuff.
from PhysicsTools.PatAlgos.tools.pfTools import *
postfix = "PF2PAT"
usePF2PAT(process,runPF2PAT=True, jetAlgo="AK5", runOnMC=False, postfix=postfix, pvCollection=cms.InputTag('goodOfflinePrimaryVertices'), typeIMetCorrections=True)


getattr(process,"pfNoPileUp"  +postfix).enable = True
getattr(process,"pfNoMuon"    +postfix).enable = False
getattr(process,"pfNoElectron"+postfix).enable = False
getattr(process,"pfNoTau"     +postfix).enable = False
getattr(process,"pfNoJet"     +postfix).enable = False

#process.patJetsPF2PAT.discriminatorSources = cms.VInputTag(
#            cms.InputTag("combinedSecondaryVertexBJetTagsAODPF2PAT"),
#            cms.InputTag("combinedSecondaryVertexMVABJetTagsAODPF2PAT"),
#            )



#Gsf Electrons
#useGsfElectrons(process, postfix, "03")

#process.pfIsolatedMuonsPF2PAT.doDeltaBetaCorrection = True
process.pfIsolatedMuonsPF2PAT.isolationCut = cms.double(9999.)
process.pfIsolatedMuonsPF2PAT.combinedIsolationCut = cms.double(9999.)
#process.pfSelectedMuonsPF2PAT.cut = cms.string('pt > 10. && abs(eta) < 2.5')
process.pfIsolatedMuonsPF2PAT.isolationValueMapsCharged = cms.VInputTag(cms.InputTag("muPFIsoValueCharged04PF2PAT"))
process.pfIsolatedMuonsPF2PAT.deltaBetaIsolationValueMap = cms.InputTag("muPFIsoValuePU04PF2PAT")
process.pfIsolatedMuonsPF2PAT.isolationValueMapsNeutral = cms.VInputTag(cms.InputTag("muPFIsoValueNeutral04PF2PAT"), cms.InputTag("muPFIsoValueGamma04PF2PAT"))

process.pfIsolatedElectronsPF2PAT.isolationCut = cms.double(9999.)
process.pfIsolatedElectronsPF2PAT.combinedIsolationCut = cms.double(9999.)
#process.pfIsolatedElectronsPF2PAT.doDeltaBetaCorrection = True
#process.pfSelectedElectronsPF2PAT.cut = cms.string('pt > 15. && abs(eta) < 2.5')
process.pfIsolatedElectronsPF2PAT.isolationValueMapsCharged = cms.VInputTag(cms.InputTag("elPFIsoValueCharged03PFIdPF2PAT"))
process.pfIsolatedElectronsPF2PAT.deltaBetaIsolationValueMap = cms.InputTag("elPFIsoValuePU03PFIdPF2PAT")
process.pfIsolatedElectronsPF2PAT.isolationValueMapsNeutral = cms.VInputTag(cms.InputTag("elPFIsoValueNeutral03PFIdPF2PAT"), cms.InputTag("elPFIsoValueGamma03PFIdPF2PAT"))


#I don't think I need these right now, but it can't hurt to include them. Unless it breaks my code. Which is entirely possible. It did! I knew it!
process.patElectronsPF2PAT.isolationValues = cms.PSet(
    pfChargedHadrons = cms.InputTag("elPFIsoValueCharged03PFIdPF2PAT"),
    pfChargedAll = cms.InputTag("elPFIsoValueChargedAll03PFIdPF2PAT"),
    pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU03PFIdPF2PAT"),
    pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral03PFIdPF2PAT"),
    pfPhotons = cms.InputTag("elPFIsoValueGamma03PFIdPF2PAT")
    )

#process.patElectronsPF2PAT.electronIDSources.mvaTrigV0    = cms.InputTag("mvaTrigV0")
#process.patElectronsPF2PAT.electronIDSources.mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0")
#process.patPF2PATSequencePF2PAT.replace( process.patElectronsPF2PAT, process.eidMVASequence * process.patElectronsPF2PAT )

#Now do a bit of JEC
process.patJetCorrFactorsPF2PAT.payload = 'AK5PFchs'
process.patJetCorrFactorsPF2PAT.levels = cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual'])
process.pfPileUpPF2PAT.checkClosestZVertex = False



###############################
###### Electron ID ############
###############################


process.load('EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi')
process.eidMVASequence = cms.Sequence( process.mvaTrigV0 + process.mvaNonTrigV0 )



#process.load('EGamma.EGammaAnalysisTools.electronIdMVAProducer_cfi')
process.load('EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi')
process.eidMVASequence = cms.Sequence(  process.mvaTrigV0 + process.mvaNonTrigV0 )
#Electron ID
process.patElectronsPF2PAT.electronIDSources.mvaTrigV0	 = cms.InputTag("mvaTrigV0")
process.patElectronsPF2PAT.electronIDSources.mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0") 
process.patPF2PATSequencePF2PAT.replace( process.patElectronsPF2PAT, process.eidMVASequence * process.patElectronsPF2PAT )


#Convesion Rejection
# this should be your last selected electron collection name since currently index is used to match with electron later. We can fix this using reference pointer.
process.patConversionsPF2PAT = cms.EDProducer("PATConversionProducer",
                                             electronSource = cms.InputTag("selectedPatElectronsPF2PAT")      
                                             )
					     
process.patPF2PATSequencePF2PAT += process.patConversionsPF2PAT




###############################
###### Bare KT 0.6 jets ####### Because why not?
###############################

#from RecoJets.JetProducers.kt4PFJets_cfi import kt4PFJets
# For electron (effective area) isolation
#process.kt6PFJetsForIsolation = kt4PFJets.clone( rParam = 0.6, doRhoFastjet = True )
#mprocess.kt6PFJetsForIsolation.Rho_EtaMax = cms.double(2.5)

###############################
#### Selections Setup #########
###############################

# AK5 Jets
#   PF
process.selectedPatJetsPF2PAT.cut = cms.string("pt > 5.0")

# Flavor history stuff - don't really know what this is, but it was in the other one too so I guess I need to include it.
#process.load("PhysicsTools.HepMCCandAlgos.flavorHistoryPaths_cfi")
#process.flavorHistoryFilter.pathToSelect = cms.int32(-1)



#Letting pat run
process.patseq = cms.Sequence(
  #  process.kt6PFJetsForIsolation*
    process.goodOfflinePrimaryVertices*
    process.primaryVertexFilter * #removes events with no good pv (but if cuts to determine good pv change...)
    process.filtersSeq *
    getattr(process,"patPF2PATSequence"+postfix) # main PF2PAT
#   * process.flavorHistorySeq
    )

####
# The N-tupliser/cutFlow
####

triggerStringName = 'HLT'

process.load("NTupliser.SingleTop.MakeTopologyNtuple_cfi")
process.makeTopologyNtuple.flavorHistoryTag=cms.bool(False) # change to false at your convenience
process.makeTopologyNtuple.runMCInfo=cms.bool(False) # prevent checking gen info
process.makeTopologyNtuple.doJERSmear=cms.bool(False)
#process.makeTopologyNtuple.doCuts=cms.bool(True) # if set to false will skip ALL cuts. Z veto still applies electron cuts.
process.makeTopologyNtuple.triggerTag = cms.InputTag("TriggerResults","",triggerStringName) # or HLT, depends on file   

#settings to apply tight selection:
process.makeTopologyNtuple.minJetPt=cms.double(30)
process.makeTopologyNtuple.maxJetEta=cms.double(2.5)
process.makeTopologyNtuple.bDiscCut=cms.double(0.679)
process.makeTopologyNtuple.minEleEt=cms.double(20)
process.makeTopologyNtuple.maxEleEta=cms.double(2.5)
process.makeTopologyNtuple.ignoreElectronID=cms.bool(False)
process.makeTopologyNtuple.eleCombRelIso=cms.double(0.15)
process.makeTopologyNtuple.maxEled0=cms.double(0.04)
process.makeTopologyNtuple.eleInterECALEtaLow=cms.double(1.4442)
process.makeTopologyNtuple.eleInterECALEtaHigh=cms.double(1.5660)
process.makeTopologyNtuple.minEleEtLooseZVeto=cms.double(15)
process.makeTopologyNtuple.minEleEtaLooseZVeto=cms.double(2.5)
process.makeTopologyNtuple.eleCombRelIsoLooseZVeto=cms.double(0.15)
process.makeTopologyNtuple.dREleJetCrossClean=cms.double(0.3)
process.makeTopologyNtuple.maxMuonEta=cms.double(2.4)
process.makeTopologyNtuple.minMuonPt=cms.double(20)
process.makeTopologyNtuple.maxMuonD0=cms.double(0.02)
process.makeTopologyNtuple.muonRelIsoTight=cms.double(0.2)
process.makeTopologyNtuple.muoNormalizedChi2=cms.double(10)
process.makeTopologyNtuple.muoNTrkHits=cms.double(11)
process.makeTopologyNtuple.muonECalIso=cms.double(4)
process.makeTopologyNtuple.muonHCalIso=cms.double(6)
process.makeTopologyNtuple.dREleGeneralTrackMatchForPhotonRej=cms.double(0.3)
process.makeTopologyNtuple.maxDistForPhotonRej=cms.double(0.04)
process.makeTopologyNtuple.maxDcotForPhotonRej=cms.double(0.03)
process.makeTopologyNtuple.fillAll=cms.bool(True)
process.makeTopologyNtuple.processingLoose=cms.bool(False)
#process.makeTopologyNtuple.btagParameterizationList = cms.vstring()
#process.makeTopologyNtuple.btagParameterizationMode = cms.vstring()
process.makeTopologyNtuple.runSwissCross = cms.bool(False)
#Don't actually do cuts
process.makeTopologyNtuple.doCuts = cms.bool(False)
process.makeTopologyNtuple.runCutFlow=cms.double(0)

#Make the inputs for the n-tupliser right.
process.makeTopologyNtuple.electronPFTag = cms.InputTag("selectedPatElectronsPF2PAT")
process.makeTopologyNtuple.tauPFTag = cms.InputTag("selectedPatTausPF2PAT")
process.makeTopologyNtuple.muonPFTag = cms.InputTag("selectedPatMuonsPF2PAT")
process.makeTopologyNtuple.jetPFTag = cms.InputTag("selectedPatJetsPF2PAT")
process.makeTopologyNtuple.metPFTag = cms.InputTag("patType1CorrectedPFMetPF2PAT")                                                                                  
#For now this is just the patseq, but soon this will also involve the ntupliser. And then minor corrections for the data version which will include more filters and such.
process.p = cms.Path(
    process.patseq
*    process.makeTopologyNtuple
    )

process.source.fileNames = [
<<<<<<< HEAD
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/06A911BC-3CBB-E311-9AFD-00266CFACC38.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/087BD118-47BB-E311-B826-848F69FD28AD.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/08A01B54-4CBB-E311-93E0-7845C4FC35E1.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/104B816B-3FBB-E311-95CE-7845C4FC3A70.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/12CE7CDA-4ABB-E311-A13E-848F69FD2949.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/189D8048-5EBB-E311-9141-7845C4F91495.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/18EDB36F-45BB-E311-8ECA-7845C4FC3B0F.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/207E3046-5EBB-E311-94DC-F04DA275BFEC.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/225EBD28-1CBB-E311-AA15-7845C4F92E7F.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/2292B8F8-3FBB-E311-9FBD-00A0D1EE8ECC.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/22C7D925-3FBB-E311-8CD7-008CFA001D7C.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/26BCBD6B-3ABB-E311-9860-848F69FD4592.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/2A5E3AA2-09BB-E311-BBA9-00266CF9157C.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/34691666-45BB-E311-BD48-7845C4FC3779.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/36D893E5-3BBB-E311-9261-00266CF9BED8.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/38EA4C79-44BB-E311-AB81-848F69FD2D6F.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/3AAB7DED-45BB-E311-96C6-008CFA001D7C.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/3EABE8DA-48BB-E311-9555-7845C4FC3C65.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/40CCD4B6-3ABB-E311-9B95-7845C4FC36D7.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/42797B27-38BB-E311-BE02-008CFA001EE4.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/4ADE56A0-62BB-E311-A122-848F69FD2892.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/4C541CC7-49BB-E311-8C1E-848F69FD28E3.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/54D04F31-41BB-E311-8932-848F69FD2D6F.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/566FDC45-5EBB-E311-A7B5-848F69FD2943.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/58B42E40-48BB-E311-96DE-180373FF8D6A.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/58E9FF36-41BB-E311-9B65-7845C4FC379D.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/5A9B371D-47BB-E311-8EDB-848F69FD2949.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/5AF41F9A-42BB-E311-B3DC-008CFA002FF4.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/5C01C77E-3EBB-E311-8900-7845C4FC3B0C.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/5EB7F8D6-29BB-E311-9498-848F69FD46C1.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/66123E54-5EBB-E311-9C31-F04DA275C007.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/72635D00-31BB-E311-9FD2-848F69FD4C76.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/767EC9BE-4BBB-E311-96B6-008CFA008DB4.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/76E97E78-49BB-E311-A28D-00A0D1EE8E94.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/7A2EA09C-42BB-E311-8C50-848F69FD2D6F.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/80070815-47BB-E311-9177-7845C4FC37B5.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/821A0550-5EBB-E311-915F-7845C4F92F7B.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/82C7B8C6-40BB-E311-B9AB-848F69FD47A5.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/82D867FF-42BB-E311-BA22-00A0D1EE8A14.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/84AA4D95-43BB-E311-ACAE-001D09FDD7EC.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/8C1D849A-32BB-E311-BDDD-848F69FD4C76.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/8CDE46E0-40BB-E311-BBB5-7845C4FC3A61.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/90D61D0C-42BB-E311-9D1C-00A0D1EE8EB4.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/90FE9CB1-45BB-E311-BE5C-7845C4FC3B6F.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/920E675E-21BB-E311-AAFB-7845C4FC3C56.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/9452F74B-44BB-E311-95B2-00266CFAE228.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/98D08517-45BB-E311-82A5-008CFA001DB8.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/98D934A7-43BB-E311-B272-00266CF23C94.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/A0024081-46BB-E311-8BA4-00A0D1EE95AC.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/A04047E7-45BB-E311-96DD-001D09FDD7C8.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/A08338A6-2FBB-E311-88A5-7845C4FC3758.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/A61C7CDC-43BB-E311-9637-7845C4FC39AD.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/A68C3A48-5EBB-E311-8E13-7845C4FC3C6B.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/A8E5FB94-4ABB-E311-8D33-001D09FDD831.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/AC29A878-68BB-E311-A535-848F69FD2892.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/B611C5F5-40BB-E311-97F8-00A0D1EE8A14.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/B6763070-41BB-E311-836A-7845C4FC3641.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/B6C3E1A5-3FBB-E311-A80B-848F69FD2D6F.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/B8DFE16F-02BB-E311-8AF6-848F69FD29AF.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/BA864C97-35BB-E311-885E-7845C4FC3A4C.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/BA9F1B6C-14BB-E311-9BD7-7845C4FC371F.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/BC162BF6-47BB-E311-B440-00A0D1EE8A14.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/BC563250-42BB-E311-B9A4-848F69FD3048.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/BE490CC2-3DBB-E311-9427-7845C4FC35C9.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/BEC4F75E-3FBB-E311-AA7E-008CFA008D4C.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/BED96B1D-34BB-E311-AB0F-F04DA275BFC2.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/C03040C3-42BB-E311-BBCE-848F69FD2823.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/C260BAE4-3DBB-E311-A0D1-F04DA275C007.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/C819EA7A-45BB-E311-8F5F-7845C4FC3C65.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/C8991B47-5EBB-E311-A30A-F04DA275BF8C.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/CAA0629E-43BB-E311-BEB9-00266CF97FF4.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/D0EAAB72-49BB-E311-BD88-848F69FD2943.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/DA4C2102-38BB-E311-AE41-00266CF9AEA4.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/DC82F112-42BB-E311-A44C-848F69FD4CB2.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/DCB9D477-36BB-E311-A466-008CFA001EE4.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/E0ABB951-0EBB-E311-BCF8-7845C4FC3620.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/E2DEA3B7-3DBB-E311-BDFB-848F69FD2D6F.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/E84F7B3B-34BB-E311-80B7-848F69FD4C76.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/EC7D6D47-5EBB-E311-8D88-001D09FDD6A5.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/F0E6CC6E-24BB-E311-8791-848F69FD4667.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/F22AB345-44BB-E311-B358-7845C4FC399E.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/F813AF85-46BB-E311-A42D-7845C4FC35F6.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/FA007B0F-39BB-E311-B5E1-848F69FD28AA.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/FAA2519E-3BBB-E311-9D24-F04DA275C007.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/FCA2F43C-48BB-E311-BC70-008CFA0025A4.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/FCA56011-77BC-E311-BA4E-00A0D1EEE5CC.root',
	'root://xrootd.unl.edu//store/mc/Summer12_DR53X/WZJetsTo3LNu_matchingdown_8TeV_TuneZ2Star_madgraph_tauola/AODSIM/PU_S10_START53_V19-v1/00000/FE218665-3FBB-E311-8176-00A0D1EEE0C0.root',
	
=======
    #Danny's selection
#    "file:/afs/cern.ch/work/l/leggat/FA8766A2-38EA-E111-9624-001A92811738.root",
#    "file:eeMetDump/res/pickevents_1_1_NM8.root",
    "file:synchFiles/data1.root",
    "file:synchFiles/data2.root",
    "file:synchFiles/data3.root"
#    "file:synchFiles/synch1.root",
#    "file:synchFiles/synch2.root",
#    "file:synchFiles/synch3.root",
#    "file:synchFiles/synch4.root",
#    "file:synchFiles/synch5.root",
#    "file:synchFiles/synch6.root"
#        "file:/afs/cern.ch/work/j/jandrea/public/147DB408-446A-E311-8E63-00259073E32A.root"
>>>>>>> 87fbdd9b1645cce8fd6b42d2f9ffa884f7aa14cc
    ]

process.maxEvents.input = cms.untracked.int32(-1)

from PhysicsTools.PatAlgos.patEventContent_cff import *
process.out.outputCommands += patEventContent
process.out.outputCommands += patTriggerEventContent
process.out.outputCommands += patExtraAodEventContent
process.out.outputCommands += cms.untracked.vstring('keep *_flavorHistoryFilter_*_*','keep *_TriggerResults_*_*','keep *_selectedPat*_*_*', 'keep *_*goodOfflinePrimaryVertices*_*_*','keep double_*_rho_*', 'keep patMuons_*_*_*', 'keep *MET*_*_*_*', 'keep *_*MET*_*_*')

#PAT output and various other outpath stuff which is a bit dumb coz I'm probably not even gonna use the outpath. Nevermind.
process.out.fileName = cms.untracked.string('Data_out.root')

#NTuple output
process.TFileService = cms.Service("TFileService", fileName = cms.string('MatchingDown_out.root') )
process.options.wantSummary = False
process.out.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p'))

#To run with pat output:
#process.Fin = cms.EndPath(process.out)
#process.schedule = cms.Schedule(process.p, process.Fin)

#Removing pat output (coz we really don't need it now)
del process.out
del process.outpath

process.schedule = cms.Schedule(process.p)
