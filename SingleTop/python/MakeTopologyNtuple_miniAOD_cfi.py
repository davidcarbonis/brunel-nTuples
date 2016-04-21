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
					   effAreasConfigFile =cms.FileInPath("RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt"),
					   pileupToken	      = cms.InputTag("slimmedAddPileupInfo"),
                                           triggerToken  = cms.InputTag("TriggerResults","","HLT"),
                                           fakeTriggerList = cms.vstring(), # empty. You can add fake triggers that are run on the fly to this list. No check on the process name is made so when duplicates are available only the latest one is added.
					   isLHEflag = cms.bool(True),
					   externalLHEToken = cms.InputTag("externalLHEProducer"),
					   pdfInfoFixingToken = cms.InputTag("pdfInfoFixing"),
					   generatorToken = cms.InputTag("generator"),
                                           
                                           triggerList = cms.vstring(                                                              
	#Updated Triggers - None avaliable for MiniAOD2016v1
        ),
                                           l1TriggerTag = cms.InputTag("gtDigis"),                                    
                                           checkTriggers = cms.bool(True),
                                           genParticles = cms.InputTag("prunedGenParticles"),
					   genSimParticles = cms.InputTag("prunedGenParticles"),
                                           runMCInfo = cms.bool(True), # if set to true will skip MCInfo section
                                           doJERSmear = cms.bool(False), # out of date and done in analysis.
                                           runPUReWeight = cms.bool(False), #Run pile-up reweighting. Don't do if this is data I guess.
                                           doCuts = cms.bool(False), # if set to false will skip ALL cuts. Z veto still applies electron cuts.
                                           # default preselection settings! see https://twiki.cern.ch/twiki/bin/view/CMS/VplusJets for inspiration

                                           #Some jet cuts.
                                           minJetPt = cms.double(0.), #min jet pT in GeV/c
                                           maxJetEta = cms.double(5.), # jet |eta|
                                           isPF = cms.bool(False), #Particle flow or not
                                           jetMinConstituents = cms.double(2),
                                           jetNHEF = cms.double(0.99),	# for jet |eta| <= 3.0
                                           jetHighEtaNHEF = cms.double(0.90),	# for jet |eta| > 3.0			    
					   jetNeutralMultiplicity = cms.double(10), 
                                           jetNEEF = cms.double(0.99),
                                           ecalEndRejectAngle = cms.double(2.4), #Angle before which we care about the charged fraction
                                           jetCEF = cms.double(0.99),
                                           jetCHF = cms.double(0.),
                                           jetNCH = cms.double(0.),
                                           jetPtCutLoose = cms.double(20.),
                                           
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

                                           runSwissCross = cms.bool(True),
                                           runPDFUncertainties = cms.bool(False),
                                           useResidualJEC = cms.bool(False),
                                           electronID = cms.string('eidRobustTight'),
                                           ignoreElectronID = cms.bool(True), # if set to true will save all electrons, also those not passing electronID.
                                           minEleEt = cms.double(0), #  electron ET in GeV
                                           eleMvaCut=cms.double(0.0), #mva minimum. Maximum mva value is hard-coded as 1, as I think that's the highest it can be.
                                           maxEleEta = cms.double(5), #  electron |eta|
                                           eleCombRelIso = cms.double(1.0), # V+jets adviced cut: 0.1. 
                                           maxEled0 = cms.double(500), # D0 (beam spot corrected) in cm, V+jets adviced cut: 0.02 for prompt electrons
                                           eleInterECALEtaLow = cms.double(1.4442),
                                           eleInterECALEtaHigh = cms.double(1.5660),
                                           # electron ID (loose, for Z Veto)
                                           electronIDLooseZVeto = cms.string('eidRobustLoose'),
                                           minEleEtLooseZVeto = cms.double(0),
                                           maxEleEtaLooseZVeto = cms.double(5),
                                           eleCombRelIsoLooseZVeto = cms.double(1.0), # always accept the electron
                                           maxEled0LooseZVeto = cms.double(100.), # always accept the electron
                                           # cross-cleaning parameter (jet is rejected if inside electron cone0
                                           dREleJetCrossClean = cms.double(-1), # cone distance that an electron-jet match needs to have to reject the jet (the electron is always kept)
                                           # muon identification
                                           maxMuonEta = cms.double(5.),
                                           minMuonPt = cms.double(0.),
                                           maxMuonD0 = cms.double(50), # D0 in cm, already corrected for Beam position. V+jets def: 0.02 (for prompt muons)
                                           muoCombRelIso = cms.double(1.), #combined track isolation,
                                           muoNormalizedChi2 = cms.double(5000), #normalized chi2 (Chi2/NDOF)
                                           muoNTrkHits = cms.double(0), # minimal number of track hits
                                           muonECalIso = cms.double(7000),
                                           muonHCalIso = cms.double(7000),
                                           flavorHistoryTag = cms.bool(True),
                                           muoValidHits = cms.double(1), #at least one valid muon hit
                                           muonMatchedStations = cms.double(2),
                                           muonDZCut = cms.double(0.5),
                                           muonDBCut = cms.double(0.2),
                                           muonPixelHits = cms.double(1),#minimum of one
                                           muonTrackLayersWithHits = cms.double(6), # 5 or less is skipped.
                                           muonRelIsoTight = cms.double(0.2),
                                           muonPtLoose = cms.double(10.),
                                           muonEtaLoose = cms.double(2.5),
                                           muoRelIsoLoose = cms.double(0.2),
                                           metCut = cms.double(30.0),
                                           fillAll = cms.bool(False),
                                           # photon rejection:
                                               dREleGeneralTrackMatchForPhotonRej=cms.double(0.3),
                                           magneticFieldForPhotonRej=cms.double(3.8),
                                           correctFactorForPhotonRej=cms.double(-0.003),
                                           maxDistForPhotonRej=cms.double(0),
                                           maxDcotForPhotonRej=cms.double(0),
                                           ebRecHits=cms.InputTag('reducedEcalRecHitsEB'),
                                           eeRecHits=cms.InputTag('reducedEcalRecHitsEE'),
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
                                           runCutFlow = cms.double(0), #0 is no cut flow, 1 is ee, 2 is emu, 3 mumu.
                                           isttBar = cms.bool(False),# This affects reweighting things. If set to false, then has a weight of 1.
                                           ttGenEvent = cms.InputTag("null")
                                           )# end of MakeTopologyNtupleMiniAOD
