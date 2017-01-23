import FWCore.ParameterSet.Config as cms

makeTopologyNtupleMiniAOD = cms.EDAnalyzer('MakeTopologyNtupleMiniAOD',
                                           # "Calo"
					   beamSpotToken = cms.InputTag("offlineBeamSpot"),
                                           trackToken  = cms.InputTag("lostTracks"),
                                           conversionsToken = cms.InputTag("reducedEgamma", "reducedConversions"),
                                           electronTag = cms.InputTag("slimmedElectrons"),
                                           tauTag      = cms.InputTag("slimmedTaus"),
                                           muonTag     = cms.InputTag("slimmedMuons"),
                                           jetLabel    = cms.InputTag("slimmedJets"),
                                           genJetToken = cms.InputTag("slimmedGenJets"),
                                           photonToken = cms.InputTag("slimmedPhotons"),
                                           metTag      = cms.InputTag("patMETs"),
                                           # PF
                                           electronPFToken = cms.InputTag("slimmedElectrons"),
                                           tauPFTag      = cms.InputTag("slimmedTaus"),
                                           muonPFToken   = cms.InputTag("slimmedMuons"),
                                           jetPFToken    = cms.InputTag("slimmedJets"),
                                           jetPFRecoTag  = cms.InputTag("slimmedJets"),
                                           #                                    photonPFTag   = cms.InputTag("slimmedPhotons"), 
                                           metPFToken      = cms.InputTag("slimmedMETs"),
                                           # JPT
                                           #jetJPTTag         = cms.InputTag("selectedPatJetsAK4JPT"),
                                           #metJPTTag      = cms.InputTag("patMETsTC"),
                                           primaryVertexToken = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                           rhoToken           = cms.InputTag("fixedGridRhoFastjetAll"),
					   effAreasConfigFile =cms.FileInPath("RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt"),
					   pileupToken	      = cms.InputTag("slimmedAddPileupInfo"),
                                           triggerToken  = cms.InputTag("TriggerResults","","HLT"),
                                           metFilterToken  = cms.InputTag("TriggerResults", "", ""),
                                           fakeTriggerList = cms.vstring(), # empty. You can add fake triggers that are run on the fly to this list. No check on the process name is made so when duplicates are available only the latest one is added.
					   isLHEflag = cms.bool(True),
					   externalLHEToken = cms.InputTag("externalLHEProducer"), # "externalLHEProducer", "source" for THQ 
					   pdfInfoFixingToken = cms.InputTag("pdfInfoFixing"),
					   generatorToken = cms.InputTag("generator"),
                                           minLeptons = cms.int32(2),
					   ebrechits = cms.InputTag("reducedEgamma","reducedEBRecHits"),
                                           
                                           triggerList = cms.vstring(                                                              
	#Updated Triggers for 2016
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v3',         #DoubleElectron
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v4',         #DoubleElectron
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v5',         #DoubleElectron
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v6',         #DoubleElectron
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v7',         #DoubleElectron
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v8',         #DoubleElectron
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v9',         #DoubleElectron

	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v2', 		#DoubleMuon
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v3', 		#DoubleMuon
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v4', 		#DoubleMuon
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v5', 		#DoubleMuon
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v6', 		#DoubleMuon
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v7', 		#DoubleMuon
	'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v2', 		#DoubleMuon
	'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v3', 		#DoubleMuon
	'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v4', 		#DoubleMuon
	'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v5', 		#DoubleMuon
	'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v6', 		#DoubleMuon

	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v3', #MuonEG Unprescaled for Runs B,C,D 
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v4', #MuonEG Unprescaled for Runs B,C,D 
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v5', #MuonEG Unprescaled for Runs B,C,D 
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v6', #MuonEG Unprescaled for Runs B,C,D 
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v7', #MuonEG Unprescaled for Runs B,C,D 
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v8', #MuonEG Unprescaled for Runs B,C,D 
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v9', #MuonEG Unprescaled for Runs B,C,D 
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v3', 	#Muon+Electron Unprescaled for Runs B,C,D
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v4', 	#Muon+Electron Unprescaled for Runs B,C,D
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v5', 	#Muon+Electron Unprescaled for Runs B,C,D
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v6', 	#Muon+Electron Unprescaled for Runs B,C,D
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v7', 	#Muon+Electron Unprescaled for Runs B,C,D
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v8', 	#Muon+Electron Unprescaled for Runs B,C,D
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v9', 	#Muon+Electron Unprescaled for Runs B,C,D

	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v1', #MuonEG
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v2', #MuonEG
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v3', #MuonEG
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v4', #MuonEG
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v1', #MuonEG
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v2', #MuonEG
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v3', #MuonEG
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v4', #MuonEG

	#Updated MET Triggers for 2016
	'HLT_MET250_v1',
	'HLT_MET250_v2',
	'HLT_MET250_v3',
	'HLT_MET250_v4',
	'HLT_MET250_v5',
	'HLT_PFMET120_PFMHT120_IDTight_v2',
	'HLT_PFMET120_PFMHT120_IDTight_v3',
	'HLT_PFMET120_PFMHT120_IDTight_v4',
	'HLT_PFMET120_PFMHT120_IDTight_v5',
	'HLT_PFMET120_PFMHT120_IDTight_v6',
	'HLT_PFMET120_PFMHT120_IDTight_v7',
	'HLT_PFMET120_PFMHT120_IDTight_v8',
	'HLT_PFMET170_HBHECleaned_v2',
	'HLT_PFMET170_HBHECleaned_v3',
	'HLT_PFMET170_HBHECleaned_v4',
	'HLT_PFMET170_HBHECleaned_v5',
	'HLT_PFMET170_HBHECleaned_v6',
	'HLT_PFMET170_HBHECleaned_v7',
	'HLT_PFMET170_HBHECleaned_v8',
	'HLT_PFMET170_HBHECleaned_v9',
	'HLT_PFHT800_v2',
	'HLT_PFHT800_v3',
	'HLT_PFHT800_v4',
	'HLT_PFHT800_v5',
	'HLT_PFHT900_v4',
	'HLT_PFHT900_v5',
	'HLT_PFHT900_v6',
	'HLT_PFHT750_4JetPt50_v3',
	'HLT_PFHT750_4JetPt50_v4',
	'HLT_PFHT750_4JetPt50_v5',
	'HLT_PFHT750_4JetPt50_v6',
	'HLT_PFHT750_4JetPt70_v1',
	'HLT_PFHT750_4JetPt70_v2',
        'HLT_PFHT750_4JetPt80_v2',
	'HLT_PFHT300_PFMET100_v1',
	'HLT_PFHT300_PFMET100_v2',
	'HLT_PFHT300_PFMET100_v3',
	'HLT_PFHT300_PFMET100_v4',
	'HLT_PFHT300_PFMET110_v4',
	'HLT_PFHT300_PFMET110_v5',
	'HLT_PFHT300_PFMET110_v6',
        ),
                                           metFilterList = cms.vstring(		
	#MET Filters		
	'Flag_HBHENoiseFilter',		
	'Flag_HBHENoiseIsoFilter',
	'Flag_globalTightHalo2016Filter',
	'Flag_EcalDeadCellTriggerPrimitiveFilter',		
	'Flag_goodVertices',		
	'Flag_eeBadScFilter',
	'Flag_ecalLaserCorrFilter',
	'Flag_chargedHadronTrackResolutionFilter',
	'Flag_muonBadTrackFilter',
	),	
                                           l1TriggerTag = cms.InputTag("gtDigis"),                                    
                                           checkTriggers = cms.bool(True),
                                           genParticles = cms.InputTag("prunedGenParticles"),
					   genSimParticles = cms.InputTag("prunedGenParticles"),
                                           runMCInfo = cms.bool(True), # if set to true will skip MCInfo section
                                           runPUReWeight = cms.bool(False), #Run pile-up reweighting. Don't do if this is data I guess.
                                           doCuts = cms.bool(True), # if set to false will skip ALL cuts. Z veto still applies electron cuts.
                                           # default preselection settings! see https://twiki.cern.ch/twiki/bin/view/CMS/VplusJets for inspiration

                                           #Some jet cuts.
                                           minJetPt = cms.double(0.), #min jet pT in GeV/c
                                           maxJetEta = cms.double(5.5), # jet |eta|

                                           #electron triggering MVA ID (tight, for analysis)

                                           eleTrigMediumIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring15-25ns-Trig-V1-wp90"),
                                           eleTrigTightIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring15-25ns-Trig-V1-wp80"),
                                           trigMvaValuesMap = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
                                           trigMvaCategoriesMap = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),

                                           #electron non-triggering MVA ID (tight, for analysis)

                                           eleNonTrigMediumIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring15-25ns-nonTrig-V1-wp90"),
                                           eleNonTrigTightIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring15-25ns-nonTrig-V1-wp80"),
                                           nonTrigMvaValuesMap = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
                                           nonTrigMvaCategoriesMap = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),

                                           #electron cut based ID
					   eleCutIdVetoMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-veto"),
					   eleCutIdLooseMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-loose"),
					   eleCutIdMediumMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-medium"),
					   eleCutIdTightMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-tight"),

                                           runSwissCross = cms.bool(True),
                                           runPDFUncertainties = cms.bool(False),
                                           useResidualJEC = cms.bool(False),
                                           ignoreElectronID = cms.bool(True), # if set to true will save all electrons, also those not passing electronID.
                                           minElePt = cms.double(9.0), #  electron pT in GeV
                                           maxEleEta = cms.double(2.70), #  electron |eta|
					   eleRelIso = cms.double(0.50), # electron combined rel track iso with rho corrections
                                           # muon identification
                                           minMuonPt = cms.double(9.0),
                                           maxMuonEta = cms.double(2.80),
                                           muoRelIso = cms.double(0.50), # muon combined track isolation with delta beta corrections
                                           metCut = cms.double(0.0),
                                           # photon rejection:
                                               dREleGeneralTrackMatchForPhotonRej=cms.double(0.3),
                                           magneticFieldForPhotonRej=cms.double(3.8),
                                           correctFactorForPhotonRej=cms.double(-0.003),
                                           maxDistForPhotonRej=cms.double(0),
                                           maxDcotForPhotonRej=cms.double(0),
                                           isMCatNLO=cms.bool(False),
                                           #New B-tagging info
                                           bDiscCut=cms.double(-1.0),
                                           bDiscName=cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
					   cVsLDiscName=cms.string('pfCombinedCvsLJetTags'), 
					   cVsBDiscName=cms.string('pfCombinedCvsBJetTags'),

                                           # Btagging algorithms: "pfJetProbabilityBJetTags","pfCombinedInclusiveSecondaryVertexV2BJetTags", "pfCombinedMVAV2BJetTags"
					   # Ctagging algorithms: "pfCombinedCvsLJetTags", "pfCombinedCvsBJetTags"

                                           # Btagging parameterizations to look at (the vectors btagParameterizationList and btagParameterizationMode are coupled!). Documentation on algo names (go in btagParamerizationList) and parameterizations (go in btagParameterizationMode) are available on this twiki:
                                               # https://twiki.cern.ch/twiki/bin/view/CMS/BtagOctober09ExerciseUsePayload
                                           btagParameterizationList = cms.vstring(
        #MC Measurements
        "MCCaloSSVHPTb","MCCaloSSVHPTc","MCCaloSSVHPTl",
        "MCCaloSSVHEMb","MCCaloSSVHEMc","MCCaloSSVHEMl",
        "MCCaloSSVHETb","MCCaloSSVHETc","MCCaloSSVHETl",
        "MCCaloTCHELb","MCCaloTCHELc","MCCaloTCHELl",
        "MCCaloTCHEMb","MCCaloTCHEMc","MCCaloTCHEMl",
        "MCCaloTCHETb","MCCaloTCHETc","MCCaloTCHETl",
        #MC Measurements Errors
        "MCCaloSSVHPTb","MCCaloSSVHPTc","MCCaloSSVHPTl",
        "MCCaloSSVHEMb","MCCaloSSVHEMc","MCCaloSSVHEMl",
        "MCCaloSSVHETb","MCCaloSSVHETc","MCCaloSSVHETl",
        "MCCaloTCHELb","MCCaloTCHELc","MCCaloTCHELl",
        "MCCaloTCHEMb","MCCaloTCHEMc","MCCaloTCHEMl",
        "MCCaloTCHETb","MCCaloTCHETc","MCCaloTCHETl",
        #Mistag fall10
        "MISTAGSSVHEM", "MISTAGSSVHEM", "MISTAGSSVHEM", "MISTAGSSVHEM",
        "MISTAGSSVHPT", "MISTAGSSVHPT", "MISTAGSSVHPT", "MISTAGSSVHPT",
        "MISTAGTCHEL", "MISTAGTCHEL", "MISTAGTCHEL", "MISTAGTCHEL",
        "MISTAGTCHEM", "MISTAGTCHEM", "MISTAGTCHEM", "MISTAGTCHEM"
        ),
                                           btagParameterizationMode = cms.vstring(
        "BTAGBEFF", "BTAGCEFF", "BTAGLEFF",
        "BTAGBEFF", "BTAGCEFF", "BTAGLEFF",
        "BTAGBEFF", "BTAGCEFF", "BTAGLEFF",
        "BTAGBEFF", "BTAGCEFF", "BTAGLEFF",
        "BTAGBEFF", "BTAGCEFF", "BTAGLEFF",
        "BTAGBEFF", "BTAGCEFF", "BTAGLEFF",
        "BTAGBERR", "BTAGCERR", "BTAGLERR",
        "BTAGBERR", "BTAGCERR", "BTAGLERR",
        "BTAGBERR", "BTAGCERR", "BTAGLERR",
        "BTAGBERR", "BTAGCERR", "BTAGLERR",
        "BTAGBERR", "BTAGCERR", "BTAGLERR",
        "BTAGBERR", "BTAGCERR", "BTAGLERR",
        #Mistag fall10
        "BTAGLEFF", "BTAGLERR", "BTAGLEFFCORR", "BTAGLERRCORR",
        "BTAGLEFF", "BTAGLERR", "BTAGLEFFCORR", "BTAGLERRCORR",
        "BTAGLEFF", "BTAGLERR", "BTAGLEFFCORR", "BTAGLERRCORR",
        "BTAGLEFF", "BTAGLERR", "BTAGLEFFCORR", "BTAGLERRCORR"
        ),
                                           isttBar = cms.bool(False),# This affects reweighting things. If set to false, then has a weight of 1.
                                           ttGenEvent = cms.InputTag("null")
                                           )# end of MakeTopologyNtupleMiniAOD
