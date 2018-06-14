import FWCore.ParameterSet.Config as cms

makeTopologyNtupleMiniAOD = cms.EDAnalyzer('MakeTopologyNtupleMiniAOD',
					   is2016rereco = cms.bool(False),
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
					   effAreasConfigFile =cms.FileInPath("RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt"),
					   pileupToken	      = cms.InputTag("slimmedAddPileupInfo"),
                                           triggerToken  = cms.InputTag("TriggerResults","","HLT"),
                                           metFilterToken  = cms.InputTag("TriggerResults", "", ""),
                                           fakeTriggerList = cms.vstring(), # empty. You can add fake triggers that are run on the fly to this list. No check on the process name is made so when duplicates are available only the latest one is added.
					   isLHEflag = cms.bool(True),
					   externalLHEToken = cms.InputTag("externalLHEProducer"), # "externalLHEProducer", "source" for THQ 

					   pdfIdStart = cms.int32(10),
					   pdfIdEnd = cms.int32(110),
					   hasAlphaWeightFlag = cms.bool(False),
					   alphaIdStart = cms.int32(2101),
					   alphaIdEnd = cms.int32(2102),

					   pdfInfoFixingToken = cms.InputTag("pdfInfoFixing"),
					   generatorToken = cms.InputTag("generator"),
                                           minLeptons = cms.int32(0),
                                           
                                           bTagList = cms.vstring(
        'pfCombinedInclusiveSecondaryVertexV2BJetTags',        #CombinedSecondaryVertex v2
        'pfDeepCSVJetTags:probudsg',                           #Deep Flavour CSV
        'pfDeepCSVJetTags:probb',                              #Deep Flavour CSV
        'pfDeepCSVJetTags:probc',                              #Deep Flavour CSV
        'pfDeepCSVJetTags:probbb',                             #Deep Flavour CSV
        'pfDeepCSVJetTags:probcc',                             #Deep Flavour CSV
        'pfDeepCMVAJetTags:probudsg',                          #Deep Flavour CMVA
        'pfDeepCMVAJetTags:probb',                             #Deep Flavour CMVA
        'pfDeepCMVAJetTags:probc',                             #Deep Flavour CMVA
        'pfDeepCMVAJetTags:probbb',                            #Deep Flavour CMVA
        'pfDeepCMVAJetTags:probcc',                            #Deep Flavour CMVA
        'pfCombinedCvsLJetTags',                               #Charm vs Light jets
        'pfCombinedCvsBJetTags',                               #Charm vs B jets
        ),
                                           triggerList = cms.vstring(                                                              
	#Updated Triggers for 2017
	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v1',
	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v2',
	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v3',
	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v4',
	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v5',
	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v6',
	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v7',
	'HLT_Ele35_WPTight_Gsf_v1',
	'HLT_Ele35_WPTight_Gsf_v2',
	'HLT_Ele35_WPTight_Gsf_v3',
	'HLT_Ele35_WPTight_Gsf_v4',
	'HLT_Ele35_WPTight_Gsf_v5',
	'HLT_Ele35_WPTight_Gsf_v6',
	'HLT_Ele35_WPTight_Gsf_v7',

	'HLT_IsoMu27_v8' ## All Runs
	'HLT_IsoMu27_v9' ## All Runs
	'HLT_IsoMu27_v10' ## All Runs
	'HLT_IsoMu27_v11' ## All Runs
	'HLT_IsoMu27_v12' ## All Runs
	'HLT_IsoMu27_v13' ## All Runs
	'HLT_IsoMu27_v14' ## All Runs

	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v10', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v11', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v12', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v13', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v14', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v15', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v16', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v17', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v10', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v11', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v12', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v13', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v14', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v15', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v16', ## All Runs
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v17', ## All Runs

	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v8', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v9', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v10', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v11', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v12', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v13', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v14', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v1', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v2', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v3', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v4', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v7', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v8', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v1', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v2', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v3', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v4', ## Runs C onwards

	## All DZ and Mu23Ele12 non-DZ are unprescaled for All Runs
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v2',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v3',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v4',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v5',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v5',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v6',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v8',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v9',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v10',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v11',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v12',
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v13',
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v5',
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v6',
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v8',
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v9',
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v10',
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v11',
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v12',
	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v13',
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v4',
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v6',
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v7',
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v8',
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v9',
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v10',
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v11',

	#Updated MET Triggers for 2017
	# Needs doing ...
        ),
                                           metFilterList = cms.vstring(		
	#MET Filters		
	'Flag_goodVertices',
	'Flag_globalTightHalo2016Filter',
	'Flag_HBHENoiseFilter',
	'Flag_HBHENoiseIsoFilter',
	'Flag_EcalDeadCellTriggerPrimitiveFilter',
	'Flag_BadPFMuonFilter',
	'Flag_BadChargedCandidateFilter',
	'Flag_eeBadScFilter',
	'Flag_ecalBadCalibFilter',
	),	
                                           l1TriggerTag = cms.InputTag("gtDigis"),                                    
                                           checkTriggers = cms.bool(True),
                                           genParticles = cms.InputTag("prunedGenParticles"),
					   genSimParticles = cms.InputTag("prunedGenParticles"),
                                           runMCInfo = cms.bool(True), # if set to true will skip MCInfo section
                                           runPUReWeight = cms.bool(False), #Run pile-up reweighting. Don't do if this is data I guess.
                                           doCuts = cms.bool(False), # if set to false will skip ALL cuts. Z veto still applies electron cuts.
                                           # default preselection settings! see https://twiki.cern.ch/twiki/bin/view/CMS/VplusJets for inspiration

                                           #Some jet cuts.
                                           minJetPt = cms.double(0.), #min jet pT in GeV/c
                                           maxJetEta = cms.double(5.5), # jet |eta|

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
                                           isttBar = cms.bool(True),# This affects reweighting things. If set to false, then has a weight of 1.
                                           ttGenEvent = cms.InputTag("null")
                                           )# end of MakeTopologyNtupleMiniAOD
