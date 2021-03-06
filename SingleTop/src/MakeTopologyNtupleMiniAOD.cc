// -*- C++ -*-
//
// Package:    MakeTopologyNtuple
// Class:      MakeTopologyNtuple
// %
/**\class MakeTopologyNtuple MakeTopologyNtuple.cc
   FreyaAnalysis/MakeTopologyNtuple/src/MakeTopologyNtuplecc Description: <one
   line class summary> Implementation: <Notes on implementation>
*/
//
// Original Author:  Freya Blekman
// Modified by: Duncan Leggat, Alexander Morton
//         Created:  Mon Feb 16 12:53:13 CET 2009
// $Id: MakeTopologyNtuple.cc,v 1.115 2010/12/09 14:23:24 chadwick Exp $
// Modified: Thur April 30 2009
// Vesna --> Add the MC truth information.
//
//

// system include files
#include <boost/numeric/conversion/cast.hpp>
#include <cstdio>
#include <memory>
// user include files
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "PhysicsTools/SelectorUtils/interface/PFJetIDSelectionFunctor.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/PdfInfo.h"
// JEC
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/PhysicsToolsObjects/interface/BinningPointByMap.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "RecoBTag/PerformanceDB/interface/BtagPerformance.h"
#include "RecoBTag/Records/interface/BTagPerformanceRecord.h"
#include "RecoEgamma/EgammaTools/interface/ConversionFinder.h"
#include "RecoEgamma/EgammaTools/interface/ConversionInfo.h"

// includes to make hadron/photonISO varaibles
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"

// Includes for conversion
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"

// Including this for top pt reweighting
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"

// Including this for hit patterns - needed for getting the lost number of
// tracker hits
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/GeometryCommonDetAlgo/interface/Measurement1D.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/METReco/interface/SigInputObj.h"
#include "DataFormats/TrackReco/interface/HitPattern.h"
#include "Math/GenVector/PxPyPzM4D.h"
#include "NTupliser/SingleTop/interface/MakeTopologyNtupleMiniAOD.h"
#include "RecoLocalCalo/EcalRecAlgos/interface/EcalSeverityLevelAlgo.h"
#include "RecoMET/METAlgorithms/interface/significanceAlgo.h"
#include "TClonesArray.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TLorentzVector.h"
#include "TTree.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"

#include <boost/container/vector.hpp>
#include <boost/numeric/conversion/cast.hpp>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <limits>

// relIso stuff
#include "DataFormats/PatCandidates/interface/Isolation.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositDirection.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h"

// Pile-up reweighting
#include "Math/LorentzVector.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

// using namespace reweight;
using boost::numeric_cast;

MakeTopologyNtupleMiniAOD::MakeTopologyNtupleMiniAOD(
    const edm::ParameterSet& iConfig)
    : beamSpotToken_{consumes<reco::BeamSpot>(
          iConfig.getParameter<edm::InputTag>("beamSpotToken"))}
    , trackToken_{consumes<std::vector<pat::PackedCandidate>>(
          iConfig.getParameter<edm::InputTag>("trackToken"))}
    , conversionsToken_{consumes<std::vector<reco::Conversion>>(
          iConfig.getParameter<edm::InputTag>("conversionsToken"))}
    , eleLabel_{mayConsume<pat::ElectronCollection>(
          iConfig.getParameter<edm::InputTag>("electronTag"))}
    , muoLabel_{iConfig.getParameter<edm::InputTag>("muonTag")}
    , jetLabel_{iConfig.getParameter<edm::InputTag>("jetLabel")}
    , genJetsToken_{consumes<reco::GenJetCollection>(
          iConfig.getParameter<edm::InputTag>("genJetToken"))}
    , tauLabel_{iConfig.getParameter<edm::InputTag>("tauTag")}
    , metLabel_{iConfig.getParameter<edm::InputTag>("metTag")}
    , patPhotonsToken_{mayConsume<pat::PhotonCollection>(
          iConfig.getParameter<edm::InputTag>("photonToken"))}
    , patElectronsToken_{mayConsume<pat::ElectronCollection>(
          iConfig.getParameter<edm::InputTag>("electronPFToken"))}
    , tauPFTag_{iConfig.getParameter<edm::InputTag>("tauPFTag")}
    , patMuonsToken_{mayConsume<pat::MuonCollection>(
          iConfig.getParameter<edm::InputTag>("muonPFToken"))}
    , patJetsToken_{consumes<pat::JetCollection>(
          iConfig.getParameter<edm::InputTag>("jetPFToken"))}
    , jetPFRecoTag_{iConfig.getParameter<edm::InputTag>("jetPFRecoTag")}
    , patMetToken_{mayConsume<pat::METCollection>(
          iConfig.getParameter<edm::InputTag>("metPFToken"))}
    // , jetJPTTag_(iConfig.getParameter<edm::InputTag>("jetJPTTag"))
    // , metJPTTag_(iConfig.getParameter<edm::InputTag>("metJPTTag"))
    , trigToken_{consumes<edm::TriggerResults>(
          iConfig.getParameter<edm::InputTag>("triggerToken"))}
    , metFilterToken_{consumes<edm::TriggerResults>(
          iConfig.getParameter<edm::InputTag>("metFilterToken"))}
    , fakeTrigLabelList_{iConfig.getParameter<std::vector<std::string>>(
          "fakeTriggerList")}
    , bTagList_{iConfig.getParameter<std::vector<std::string>>("bTagList")}
    , triggerList_{iConfig.getParameter<std::vector<std::string>>(
          "triggerList")}
    , metFilterList_{iConfig.getParameter<std::vector<std::string>>(
          "metFilterList")}
    , l1TrigLabel_{iConfig.getParameter<edm::InputTag>("l1TriggerTag")}
    , genParticlesToken_{consumes<reco::GenParticleCollection>(
          iConfig.getParameter<edm::InputTag>("genParticles"))}
    , genSimParticlesToken_{consumes<reco::GenParticleCollection>(
          iConfig.getParameter<edm::InputTag>("genSimParticles"))}
    , pvLabel_{consumes<reco::VertexCollection>(
          iConfig.getParameter<edm::InputTag>("primaryVertexToken"))}
    , rhoToken_{consumes<double>(
          iConfig.getParameter<edm::InputTag>("rhoToken"))}
    , effectiveAreaInfo_{(iConfig.getParameter<edm::FileInPath>(
                              "effAreasConfigFile"))
                             .fullPath()}
    , pileupToken_{mayConsume<std::vector<PileupSummaryInfo>>(
          iConfig.getParameter<edm::InputTag>("pileupToken"))}
    , is2016rereco_{iConfig.getParameter<bool>("is2016rereco")}
    , isttbar_{iConfig.getParameter<bool>("isttBar")}
    , ttGenEvent_{iConfig.getParameter<edm::InputTag>("ttGenEvent")}
    , externalLHEToken_{consumes<LHEEventProduct>(
          iConfig.getParameter<edm::InputTag>("externalLHEToken"))}
    , pdfIdStart_{iConfig.getParameter<int>("pdfIdStart")}
    , pdfIdEnd_{iConfig.getParameter<int>("pdfIdEnd")}
    , alphaIdStart_{iConfig.getParameter<int>("alphaIdStart")}
    , alphaIdEnd_{iConfig.getParameter<int>("alphaIdEnd")}
    , pdfInfoToken_{mayConsume<GenEventInfoProduct>(
          iConfig.getParameter<edm::InputTag>("pdfInfoFixingToken"))}
    , generatorToken_{mayConsume<GenEventInfoProduct>(
          iConfig.getParameter<edm::InputTag>("generatorToken"))}
    , btaggingparamnames_{iConfig.getParameter<std::vector<std::string>>(
          "btagParameterizationList")}
    , btaggingparaminputtypes_{iConfig.getParameter<std::vector<std::string>>(
          "btagParameterizationMode")}
    // , eleIDsToNtuple_(
    //       iConfig.getParameter<std::vector<std::string>>("eleIDsToNtuple"))
    , runMCInfo_{iConfig.getParameter<bool>("runMCInfo")}
    , runPUReWeight_{iConfig.getParameter<bool>("runPUReWeight")}
    , doCuts_{iConfig.getParameter<bool>("doCuts")}
    , jetPtCut_{iConfig.getParameter<double>("minJetPt")}
    , jetEtaCut_{iConfig.getParameter<double>("maxJetEta")}
    , runPDFUncertainties_{iConfig.getParameter<bool>("runPDFUncertainties")}
    , useResidualJEC_{iConfig.getParameter<bool>("useResidualJEC")}
    , ignore_emIDtight_{iConfig.getParameter<bool>("ignoreElectronID")}
    , minLeptons_{iConfig.getParameter<int>("minLeptons")}
    , elePtCut_{iConfig.getParameter<double>("minElePt")}
    , eleEtaCut_{iConfig.getParameter<double>("maxEleEta")}
    , eleIsoCut_{iConfig.getParameter<double>("eleRelIso")}
    , muoPtCut_{iConfig.getParameter<double>("minMuonPt")}
    , muoEtaCut_{iConfig.getParameter<double>("maxMuonEta")}
    , muoIsoCut_{iConfig.getParameter<double>("muoRelIso")}
    , metCut_{iConfig.getParameter<double>("metCut")} // met cut
    , check_triggers_{iConfig.getParameter<bool>("checkTriggers")}
    , dREleGeneralTrackMatch_{iConfig.getParameter<double>(
          "dREleGeneralTrackMatchForPhotonRej")}
    , magneticField_{iConfig.getParameter<double>("magneticFieldForPhotonRej")}
    , correctFactor_{iConfig.getParameter<double>("correctFactorForPhotonRej")}
    , maxDist_{iConfig.getParameter<double>("maxDistForPhotonRej")}
    , maxDcot_{iConfig.getParameter<double>("maxDcotForPhotonRej")}
    , isMCatNLO_{iConfig.getParameter<bool>("isMCatNLO")}
    , isLHEflag_{iConfig.getParameter<bool>("isLHEflag")}
    , hasAlphaWeightFlag_{iConfig.getParameter<bool>("hasAlphaWeightFlag")}
    , isrRedHi{1.0}
    , fsrRedHi{1.0}
    , isrRedLo{1.0}
    , fsrRedLo{1.0}
    , isrDefHi{1.0}
    , fsrDefHi{1.0}
    , isrDefLo{1.0}
    , fsrDefLo{1.0}
    , isrConHi{1.0}
    , fsrConHi{1.0}
    , isrConLo{1.0}
    , fsrConLo{1.0}
{
    // now do what ever initialization is needed

    //{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
    // define some histograms using the framework tfileservice. Define the
    // output file name in your .cfg.
    //{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

    //{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
    // histocontainer_ is of type std::map<std::string, TH1D*>. This means you
    // can use it with this syntax:
    // histocontainer_["histname"]->Fill(x);
    // histocontainer_["histname"]->Draw();
    // etc, etc. Essentially you use the histname string to look up a pointer to
    // a TH1D* which you can do everything to you would normally do in ROOT.
    //{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

    //{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
    // here we book new histograms:
    //{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

    filledBIDInfo_ = false;
    histocontainer_["eventcount"] =
        fs->make<TH1D>("eventcount", "events processed", 1, -0.5, +0.5);

    // Putting in a few histograms to debug the loose lepton selection
    // hopefully.
    histocontainer_["tightElectrons"] = fs->make<TH1D>(
        "tightElectrons", "Number of tight electrons in event", 11, -0.5, 10.5);
    histocontainer_["tightMuons"] = fs->make<TH1D>(
        "tightMuons", "Number of tight muons in event", 11, -0.5, 10.5);

    if (isttbar_)
    {
        histocontainer_["topPtWeightSum"] =
            fs->make<TH1D>("topPtWeightSum", "topPtWeightSum", 1, -0.5, 0.5);
    }

    eventCount = 0;
    bookBranches(); // and fill tree
    bTags = 0;
    softTags = 0;

    // Some debugging variables
}

MakeTopologyNtupleMiniAOD::~MakeTopologyNtupleMiniAOD()
{
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)

    mytree_->FlushBaskets();
}

//
// member functions
//
void MakeTopologyNtupleMiniAOD::fillSummaryVariables()
{
    ran_postloop_ = true;
    return;
}
void MakeTopologyNtupleMiniAOD::fillEventInfo(const edm::Event& iEvent,
                                              const edm::EventSetup& /*iSetup*/)
{
    evtRun = iEvent.id().run();
    evtnum = iEvent.id().event();
    evtlumiblock =
        iEvent.luminosityBlock(); // or even: iEvent.luminosityBlock() might
                                  // work, depending on the release)

    // also add pv:
    edm::Handle<reco::VertexCollection> pvHandle;
    iEvent.getByToken(pvLabel_, pvHandle);

    pvX = pvY = pvZ = pvRho = -999999;
    numPv = pvDX = pvDY = pvDZ = 0;
    pvIsFake = pvNdof = pvChi2 = -1;

    if (pvHandle.isValid())
    {
        std::vector<reco::Vertex> pv{*pvHandle};

        numPv = pv.size();
        if (pv.size() > 0)
        {
            pvX = pv[0].x();
            pvY = pv[0].y();
            pvZ = pv[0].z();
            pvDX = pv[0].xError();
            pvDY = pv[0].yError();
            pvDZ = pv[0].zError();
            pvRho = pv[0].position().Rho();
            pvNdof = pv[0].ndof();
            pvIsFake = numeric_cast<int>(pv[0].isFake());
            pvChi2 = pv[0].chi2();
            math::XYZPoint point(pvX, pvY, pvZ);
            vertexPoint_ = point;
        }
    }
}
void MakeTopologyNtupleMiniAOD::fillMissingET(
    const edm::Event& iEvent,
    const edm::EventSetup& /*iSetup*/,
    edm::EDGetTokenT<pat::METCollection> metIn_,
    const std::string& ID)
{
    edm::Handle<pat::METCollection> metHandle;
    iEvent.getByToken(metIn_, metHandle);

    metE[ID] = metHandle->front().energy();
    metEt[ID] = metHandle->front().et();
    metEtRaw[ID] = metHandle->front().et();
    metPhi[ID] = metHandle->front().phi();
    metPt[ID] = metHandle->front().pt();
    metPx[ID] = metHandle->front().px();
    metPy[ID] = metHandle->front().py();
    metPz[ID] = metHandle->front().pz();
    metScalarEt[ID] = metHandle->front().sumEt();
    metEtUncorrected[ID] = metHandle->front().uncorPt();
    metPhiUncorrected[ID] = metHandle->front().uncorPhi();
    metUnclusteredEnUp[ID] =
        metHandle->front().shiftedPt(pat::MET::UnclusteredEnUp);
    metUnclusteredEnDown[ID] =
        metHandle->front().shiftedPt(pat::MET::UnclusteredEnDown);

    if (metHandle->front().isCaloMET())
    {
        metMaxEtEM[ID] = metHandle->front().maxEtInEmTowers();
        metMaxEtHad[ID] = metHandle->front().maxEtInHadTowers();
        metEtFracHad[ID] = metHandle->front().etFractionHadronic();
        metEtFracEM[ID] = metHandle->front().emEtFraction();
        metHadEtHB[ID] = metHandle->front().hadEtInHB();
        metHadEtHO[ID] = metHandle->front().hadEtInHO();
        metHadEtHF[ID] = metHandle->front().hadEtInHF();
        metHadEtHE[ID] = metHandle->front().hadEtInHE();
        metEmEtHF[ID] = metHandle->front().emEtInHF();
        metEmEtEE[ID] = metHandle->front().emEtInEE();
        metEmEtEB[ID] = metHandle->front().emEtInEB();

        metSignificance[ID] = metHandle->front().metSignificance();
        // std::cout << metSignificance << std::endl;
    }
    if (metHandle->front().genMET())
    {
        genMetE[ID] = metHandle->front().genMET()->energy();
        genMetEt[ID] = metHandle->front().genMET()->et();
        genMetPhi[ID] = metHandle->front().genMET()->phi();
        genMetPt[ID] = metHandle->front().genMET()->pt();
        genMetPx[ID] = metHandle->front().genMET()->px();
        genMetPy[ID] = metHandle->front().genMET()->py();
        genMetPz[ID] = metHandle->front().genMET()->pz();
    }
    else
    {
        genMetE[ID] = -999.;
        genMetEt[ID] = -999.;
        genMetPhi[ID] = -999.;
        genMetPt[ID] = -999.;
        genMetPx[ID] = -999.;
        genMetPy[ID] = -999.;
        genMetPz[ID] = -999.;
    }
}
/////////////////////////////////////////////////////////////////////////////////////////////
void MakeTopologyNtupleMiniAOD::fillBeamSpot(const edm::Event& iEvent,
                                             const edm::EventSetup& /*iSetup*/)
{
    if (ran_PV_)
    {
        return;
    }
    ran_PV_ = true;

    reco::BeamSpot beamSpot;

    edm::Handle<reco::BeamSpot> beamSpotHandle;
    iEvent.getByToken(beamSpotToken_, beamSpotHandle);

    if (beamSpotHandle.isValid())
    {
        beamSpot = *beamSpotHandle;
    }
    else
    {
        edm::LogInfo("MyAnalyzer")
            << "No beam spot available from EventSetup \n";
    }
    beamSpotX = beamSpot.x0();
    beamSpotY = beamSpot.y0();
    beamSpotZ = beamSpot.z0();

    math::XYZPoint point(beamSpotX, beamSpotY, beamSpotZ);
    beamSpotPoint_ = point;
}

//////////////////////////////////////////////////////////////////////////////////////////////
void MakeTopologyNtupleMiniAOD::fillElectrons(
    const edm::Event& iEvent,
    const edm::EventSetup& iSetup,
    edm::EDGetTokenT<pat::ElectronCollection> eleIn_,
    const std::string& ID,
    edm::EDGetTokenT<pat::ElectronCollection> eleInOrg_)
{
    // if (ran_eleloop_)
    // {
    //     return;
    // }
    // ran_eleloop_ = true;

    // info for 'default conversion finder
    edm::Handle<std::vector<pat::PackedCandidate>> lostTracks;
    iEvent.getByToken(trackToken_, lostTracks);
    edm::ESHandle<MagneticField> magneticField;
    iSetup.get<IdealMagneticFieldRecord>().get(magneticField);
    // over-ride the magnetic field supplied from the configfile:
    //    double realMagfield=magneticField_;
    //    if(magneticField->inTesla(GlobalPoint(0.,0.,0.)).z()>0) //Accept 0?
    //    realMagfield=magneticField->inTesla(GlobalPoint(0.,0.,0.)).z();
    //  needs beam spot
    fillBeamSpot(iEvent, iSetup);
    // and tracks for photon conversion checks:
    fillGeneralTracks(iEvent, iSetup);

    // note that the fillJets() method needs electrons, due to the fact that we
    // do our own 'cross' cleaning
    edm::Handle<pat::ElectronCollection>
        electronHandle; // changed handle from pat::Electron to
                        // reco::GsfElectron
    iEvent.getByToken(eleIn_, electronHandle);
    const pat::ElectronCollection& electrons{*electronHandle};

    // Original collection used for id-decisions
    edm::Handle<pat::ElectronCollection> electronOrgHandle;
    iEvent.getByToken(eleInOrg_, electronOrgHandle);
    // const pat::ElectronCollection& electronsOrg = *electronOrgHandle;

    // Electron conversions
    edm::Handle<reco::ConversionCollection> Conversions;
    iEvent.getByToken(conversionsToken_, Conversions);

    // Get the rho isolation co-efficient here
    edm::Handle<double> rhoHand_;
    iEvent.getByToken(rhoToken_, rhoHand_);
    rhoIso = *(rhoHand_.product());

    electronEts.clear();
    for (const auto& electron : electrons)
    {
        double et{electron.et()};
        electronEts.emplace_back(et);
    }

    // if (ID == "PF")
    // {
    //     std::cout << "N PF ele: " << electronEts.size() << std::endl;
    // }
    std::vector<size_t> etSortedIndex{
        IndexSorter<std::vector<float>>(electronEts, true)()};

    // Primary vertex
    edm::Handle<reco::VertexCollection> pvHandle;
    iEvent.getByToken(pvLabel_, pvHandle);

    // std::cout << "now starting loop" << std::std::endl;
    // now loop again, in the correct order
    numEle[ID] = 0;

    for (size_t iele{0}; iele < etSortedIndex.size()
                         && numEle[ID] < numeric_cast<int>(NELECTRONSMAX);
         ++iele)
    {
        size_t jele{etSortedIndex[iele]};
        // const pat::Electron& ele = electrons[jele];
        const pat::Electron& ele{(*electronHandle)[jele]};

        pat::ElectronRef refel{electronOrgHandle,
                               numeric_cast<unsigned int>(jele)};

        int photonConversionTag{-1};

        numEle[ID]++;

        // Impact param significance
        if (pvHandle.isValid())
        {
            std::vector<reco::Vertex> pv{*pvHandle};

            edm::ESHandle<TransientTrackBuilder> trackBuilder;
            iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",
                                                   trackBuilder);
            reco::TransientTrack eleTransient{
                trackBuilder->build(ele.gsfTrack())};

            std::pair<bool, Measurement1D> eleImpactTrans{
                IPTools::absoluteTransverseImpactParameter(eleTransient,
                                                           pv[0])};
            std::pair<bool, Measurement1D> eleImpact3D{
                IPTools::absoluteImpactParameter3D(eleTransient, pv[0])};

            if (eleImpactTrans.first)
            {
                electronSortedImpactTransDist[ID][numEle[ID] - 1] =
                    eleImpactTrans.second.value();
                electronSortedImpactTransError[ID][numEle[ID] - 1] =
                    eleImpactTrans.second.error();
                electronSortedImpactTransSignificance[ID][numEle[ID] - 1] =
                    eleImpactTrans.second.significance();
            }
            if (eleImpact3D.first)
            {
                electronSortedImpact3DDist[ID][numEle[ID] - 1] =
                    eleImpact3D.second.value();
                electronSortedImpact3DError[ID][numEle[ID] - 1] =
                    eleImpact3D.second.error();
                electronSortedImpact3DSignificance[ID][numEle[ID] - 1] =
                    eleImpact3D.second.significance();
            }
        }

        const double eleCorrScale{ele.userFloat("ecalTrkEnergyPostCorr")
                                  / ele.p4().energy()};
        const TLorentzVector eleCorr{ele.px() * eleCorrScale,
                                     ele.py() * eleCorrScale,
                                     ele.pz() * eleCorrScale,
                                     ele.energy() * eleCorrScale};

        electronSortedE[ID][numEle[ID] - 1] = eleCorr.E();
        electronSortedEt[ID][numEle[ID] - 1] = eleCorr.Et();
        electronSortedEta[ID][numEle[ID] - 1] = eleCorr.Eta();
        electronSortedPt[ID][numEle[ID] - 1] = eleCorr.Pt();
        electronSortedTheta[ID][numEle[ID] - 1] = eleCorr.Theta();
        electronSortedPhi[ID][numEle[ID] - 1] = eleCorr.Phi();
        electronSortedPx[ID][numEle[ID] - 1] = eleCorr.Px();
        electronSortedPy[ID][numEle[ID] - 1] = eleCorr.Py();
        electronSortedPz[ID][numEle[ID] - 1] = eleCorr.Pz();
        electronSortedCharge[ID][numEle[ID] - 1] = ele.charge();

        if (is2016rereco_)
        {
            electronSortedCutIdVeto[ID][numEle[ID] - 1] =
                ele.electronID("cutBasedElectronID-Fall17-94X-V1-veto");
            electronSortedCutIdLoose[ID][numEle[ID] - 1] =
                ele.electronID("cutBasedElectronID-Fall17-94X-V1-loose");
            electronSortedCutIdMedium[ID][numEle[ID] - 1] =
                ele.electronID("cutBasedElectronID-Fall17-94X-V1-medium");
            electronSortedCutIdTight[ID][numEle[ID] - 1] =
                ele.electronID("cutBasedElectronID-Fall17-94X-V1-tight");
        }
        else
        {
            electronSortedCutIdVeto[ID][numEle[ID] - 1] =
                ele.electronID("cutBasedElectronID-Summer16-80X-V1-veto");
            electronSortedCutIdLoose[ID][numEle[ID] - 1] =
                ele.electronID("cutBasedElectronID-Summer16-80X-V1-loose");
            electronSortedCutIdMedium[ID][numEle[ID] - 1] =
                ele.electronID("cutBasedElectronID-Summer16-80X-V1-medium");
            electronSortedCutIdTight[ID][numEle[ID] - 1] =
                ele.electronID("cutBasedElectronID-Summer16-80X-V1-tight");
        }
        electronSortedChargedHadronIso[ID][numEle[ID] - 1] =
            ele.chargedHadronIso();
        electronSortedNeutralHadronIso[ID][numEle[ID] - 1] =
            ele.neutralHadronIso();
        electronSortedPhotonIso[ID][numEle[ID] - 1] = ele.photonIso();

        electronSortedTrackPt[ID][numEle[ID] - 1] = ele.gsfTrack()->pt();
        electronSortedTrackEta[ID][numEle[ID] - 1] = ele.gsfTrack()->eta();
        electronSortedTrackPhi[ID][numEle[ID] - 1] = ele.gsfTrack()->phi();
        electronSortedTrackChi2[ID][numEle[ID] - 1] = ele.gsfTrack()->chi2();
        electronSortedTrackNDOF[ID][numEle[ID] - 1] = ele.gsfTrack()->ndof();
        electronSortedTrackD0[ID][numEle[ID] - 1] = ele.gsfTrack()->d0();
        electronSortedDBBeamSpotCorrectedTrackD0[ID][numEle[ID] - 1] = ele.dB();
        // electronSortedDBInnerTrackD0[ID][numEle[ID] - 1] =
        //     -1. * (ele.innerTrack()->dxy(beamSpotPoint_));
        electronSortedBeamSpotCorrectedTrackD0[ID][numEle[ID] - 1] =
            -1. * (ele.gsfTrack()->dxy(beamSpotPoint_));
        electronSortedTrackDz[ID][numEle[ID] - 1] = ele.gsfTrack()->dz();
        electronSortedTrackD0PV[ID][numEle[ID] - 1] =
            ele.gsfTrack()->dxy(vertexPoint_);
        electronSortedTrackDZPV[ID][numEle[ID] - 1] =
            ele.gsfTrack()->dz(vertexPoint_);
        electronSortedVtxZ[ID][numEle[ID] - 1] = ele.vertex().z();

        electronSortedIsGsf[ID][numEle[ID] - 1] = ele.gsfTrack().isNonnull();
        electronSortedGsfPx[ID][numEle[ID] - 1] = ele.ecalDrivenMomentum().px();
        electronSortedGsfPy[ID][numEle[ID] - 1] = ele.ecalDrivenMomentum().py();
        electronSortedGsfPz[ID][numEle[ID] - 1] = ele.ecalDrivenMomentum().pz();
        electronSortedGsfE[ID][numEle[ID] - 1] =
            ele.ecalDrivenMomentum().energy();
        electronSortedEcalEnergy[ID][numEle[ID] - 1] = ele.ecalEnergy();

        electronSortedSuperClusterEta[ID][numEle[ID] - 1] =
            ele.superCluster()->eta();
        electronSortedSuperClusterE[ID][numEle[ID] - 1] =
            ele.superCluster()->energy();
        electronSortedSuperClusterPhi[ID][numEle[ID] - 1] =
            ele.superCluster()->phi();
        electronSortedSuperClusterEoverP[ID][numEle[ID] - 1] =
            ele.eSuperClusterOverP();
        electronSortedSuperClusterSigmaEtaEta[ID][numEle[ID] - 1] =
            ele.scSigmaEtaEta();
        electronSortedSuperClusterE1x5[ID][numEle[ID] - 1] = ele.scE1x5();
        electronSortedSuperClusterE2x5max[ID][numEle[ID] - 1] = ele.scE2x5Max();
        electronSortedSuperClusterE5x5[ID][numEle[ID] - 1] = ele.scE5x5();
        electronSortedSuperClusterSigmaIEtaIEta[ID][numEle[ID] - 1] =
            ele.scSigmaIEtaIEta();
        electronSortedSuperClusterSigmaIEtaIEta5x5[ID][numEle[ID] - 1] =
            ele.full5x5_sigmaIetaIeta();

        electronSortedTrackIso04[ID][numEle[ID] - 1] =
            ele.dr04TkSumPt(); // trackIso();
        electronSortedECalIso04[ID][numEle[ID] - 1] =
            ele.dr04EcalRecHitSumEt(); // ecalIso();
        electronSortedTrackIso03[ID][numEle[ID] - 1] =
            ele.dr03TkSumPt(); // trackIso();
        electronSortedECalIso03[ID][numEle[ID] - 1] =
            ele.dr03EcalRecHitSumEt(); // ecalIso();
        electronSortedHCalIso03[ID][numEle[ID] - 1] =
            ele.dr03HcalTowerSumEt(); // ele.hcalIso();
        // electronSortedECalIsoDeposit[ID][numEle[ID] - 1] =
        //     ele.ecalIsoDeposit()->candEnergy();
        // electronSortedHCalIsoDeposit[ID][numEle[ID] - 1] =
        //     ele.hcalIsoDeposit()->candEnergy();
        electronSortedCaloIso[ID][numEle[ID] - 1] = ele.caloIso();

        const reco::GsfElectron::PflowIsolationVariables& pfIso{
            ele.pfIsolationVariables()};

        // calculate comRelIso:
        electronSortedComRelIso[ID][numEle[ID] - 1] =
            electronSortedTrackIso03[ID][numEle[ID] - 1];
        electronSortedComRelIso[ID][numEle[ID] - 1] +=
            electronSortedECalIso03[ID][numEle[ID] - 1];
        electronSortedComRelIso[ID][numEle[ID] - 1] +=
            electronSortedHCalIso03[ID][numEle[ID] - 1];
        electronSortedComRelIso[ID][numEle[ID] - 1] /=
            electronSortedEt[ID][numEle[ID] - 1];
        electronSortedChHadIso[ID][numEle[ID] - 1] = pfIso.sumChargedHadronPt;
        electronSortedNtHadIso[ID][numEle[ID] - 1] = pfIso.sumNeutralHadronEt;
        electronSortedGammaIso[ID][numEle[ID] - 1] = pfIso.sumPhotonEt;
        electronSortedComRelIsodBeta[ID][numEle[ID] - 1] =
            (pfIso.sumChargedHadronPt
             + std::max(0.0, pfIso.sumPhotonEt - 0.5 * pfIso.sumPUPt))
            / ele.pt();

        const float AEff03{effectiveAreaInfo_.getEffectiveArea(
            std::abs(ele.superCluster()->eta()))};
        electronSortedAEff03[ID][numEle[ID] - 1] = AEff03;
        electronSortedRhoIso[ID][numEle[ID] - 1] = rhoIso;

        const double combrelisorho{
            (pfIso.sumChargedHadronPt
             + std::max(0.0,
                        pfIso.sumNeutralHadronEt + pfIso.sumPhotonEt
                            - rhoIso * AEff03))
            / ele.pt()};
        electronSortedComRelIsoRho[ID][numEle[ID] - 1] = combrelisorho;
        // (ele.trackIso() + ele.ecalIso() + ele.hcalIso()) / ele.et();

        // pass electron to photonConversionVeto and see if it comes from photon
        // conversion

        electronSortedMissingInnerLayers[ID][numEle[ID] - 1] =
            ele.gsfTrack()->hitPattern().numberOfLostTrackerHits(
                reco::HitPattern::MISSING_INNER_HITS);

        electronSortedHoverE[ID][numEle[ID] - 1] = ele.hadronicOverEm();
        electronSortedDeltaPhiSC[ID][numEle[ID] - 1] =
            ele.deltaPhiSuperClusterTrackAtVtx();
        electronSortedDeltaEtaSC[ID][numEle[ID] - 1] =
            ele.deltaEtaSuperClusterTrackAtVtx();
        electronSortedDeltaEtaSeedSC[ID][numEle[ID] - 1] =
            (ele.superCluster().isNonnull()
                     && ele.superCluster()->seed().isNonnull()
                 ? ele.deltaEtaSuperClusterTrackAtVtx()
                       - ele.superCluster()->eta()
                       + ele.superCluster()->seed()->eta()
                 : std::numeric_limits<float>::max());
        electronSortedIsBarrel[ID][numEle[ID] - 1] = ele.isEB();

        // calculate dcot and dist using the egamma code...
        // use fixed magnetic field for now:

        // ELECTRON CONVERSIONS

        electronSortedPhotonConversionTag[ID][numEle[ID] - 1] =
            ConversionTools::hasMatchedConversion(
                ele, Conversions, beamSpotPoint_);
        electronSortedPhotonConversionDist[ID][numEle[ID] - 1] = ele.convDist();
        electronSortedPhotonConversionDcot[ID][numEle[ID] - 1] = ele.convDcot();
        electronSortedPhotonConversionVeto[ID][numEle[ID] - 1] =
            ele.passConversionVeto();

        // and using our private code
        if (photonConversionVeto(
                ele,
                electronSortedPhotonConversionDistCustom[ID][numEle[ID] - 1],
                electronSortedPhotonConversionDcotCustom[ID][numEle[ID] - 1]))
        {
            photonConversionTag = 1;
        }
        electronSortedPhotonConversionTagCustom[ID][numEle[ID] - 1] =
            photonConversionTag;

        if (check_triggers_)
        {
            std::vector<pat::TriggerObjectStandAlone> matchedtriggers{
                ele.triggerObjectMatches()};

            if (false)
            { // Debug verboose info if set to 1.
                for (auto& matchedtrigger : matchedtriggers)
                {
                    for (auto it{matchedtrigger.filterLabels().begin()},
                         it_end = matchedtrigger.filterLabels().end();
                         it != it_end;
                         it++)
                    {
                        // std::cout << *it << std::endl;
                    }
                }
            }
            electronSortedTriggerMatch[ID][numEle[ID] - 1] =
                matchedtriggers.size(); // very coarse, probably want to select
                                        // on a filter.
        }

        // if(ele.genParticleRef().ref().isValid()){
        if (!ele.genParticleRef().isNull())
        {
            genElectronSortedPt[ID][numEle[ID] - 1] = ele.genLepton()->pt();
            genElectronSortedEt[ID][numEle[ID] - 1] = ele.genLepton()->et();
            genElectronSortedEta[ID][numEle[ID] - 1] = ele.genLepton()->eta();
            genElectronSortedTheta[ID][numEle[ID] - 1] =
                ele.genLepton()->theta();
            genElectronSortedPhi[ID][numEle[ID] - 1] = ele.genLepton()->phi();
            genElectronSortedPx[ID][numEle[ID] - 1] = ele.genLepton()->px();
            genElectronSortedPy[ID][numEle[ID] - 1] = ele.genLepton()->py();
            genElectronSortedPz[ID][numEle[ID] - 1] = ele.genLepton()->pz();
            genElectronSortedCharge[ID][numEle[ID] - 1] =
                ele.genLepton()->charge();
            genElectronSortedPdgId[ID][numEle[ID] - 1] =
                ele.genLepton()->pdgId();
            genElectronSortedMotherId[ID][numEle[ID] - 1] =
                ele.genLepton()->mother()->pdgId();
            genElectronSortedPromptDecayed[ID][numEle[ID] - 1] =
                ele.genLepton()->isPromptDecayed();
            genElectronSortedPromptFinalState[ID][numEle[ID] - 1] =
                ele.genLepton()->isPromptFinalState();
            genElectronSortedHardProcess[ID][numEle[ID] - 1] =
                ele.genLepton()->isHardProcess();
        }
    }
}

//////////////////////////////////////////////////////////////////////////////////////////////
void MakeTopologyNtupleMiniAOD::fillMuons(
    const edm::Event& iEvent,
    const edm::EventSetup& iSetup,
    edm::EDGetTokenT<pat::MuonCollection> muIn_,
    const std::string& ID)
{
    // ran_muonloop_ = true;
    edm::Handle<pat::MuonCollection> muonHandle;
    iEvent.getByToken(muIn_, muonHandle);
    const pat::MuonCollection& muons = *muonHandle;

    fillBeamSpot(iEvent, iSetup);
    fillGeneralTracks(iEvent, iSetup);

    //   !!!
    // IMPORTANT: DO NOT CUT ON THE OBJECTS BEFORE THEY ARE SORTED, cuts should
    // be applied in the second loop!!!
    //   !!!

    // muons
    muonEts.clear();
    for (const auto& muon : muons)
    {
        double et{muon.et()}; // should already be corrected
        muonEts.emplace_back(et);
    }

    // std::cout << __LINE__ << " : " << __FILE__ << " : nMuons = " <<
    // muons.size()
    //           << std::endl;
    //
    // std::cout << iEvent.id().event() << " " << muons.size() << std::endl;

    if (muonEts.size() == 0)
    { // prevents a crash, the IndexSorter does not know what to do with
      // zero-size vectors
        return;
    }
    std::vector<size_t> etMuonSorted{
        IndexSorter<std::vector<float>>(muonEts, true)()};

    numMuo[ID] = 0;
    // muons:
    for (size_t imuo{0}; imuo < etMuonSorted.size()
                         && numMuo[ID] < numeric_cast<int>(NMUONSMAX);
         ++imuo)
    {
        size_t jmu{etMuonSorted[imuo]};
        // std::cout << imuo << " " << jmu << std::endl;
        const pat::Muon& muo{muons[jmu]};

        numMuo[ID]++;

        // std::cout << muo.pt() << " " << muo.eta() << " " <<
        // muo.isGlobalMuon()
        //           << " " << muo.isTrackerMuon() << " " << muo.isPFMuon()
        //           << std::endl;

        muonSortedE[ID][numMuo[ID] - 1] = muo.energy();
        muonSortedEt[ID][numMuo[ID] - 1] = muo.et();
        muonSortedPt[ID][numMuo[ID] - 1] = muo.pt();
        muonSortedEta[ID][numMuo[ID] - 1] = muo.eta();
        muonSortedTheta[ID][numMuo[ID] - 1] = muo.theta();
        muonSortedPhi[ID][numMuo[ID] - 1] = muo.phi();
        muonSortedPx[ID][numMuo[ID] - 1] = muo.px();
        muonSortedPy[ID][numMuo[ID] - 1] = muo.py();
        muonSortedPz[ID][numMuo[ID] - 1] = muo.pz();
        muonSortedCharge[ID][numMuo[ID] - 1] = muo.charge();

        muonSortedLooseCutId[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::CutBasedIdLoose);
        muonSortedMediumCutId[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::CutBasedIdMedium);
        muonSortedTightCutId[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::CutBasedIdTight);
        muonSortedPfIsoVeryLoose[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::PFIsoVeryLoose);
        muonSortedPfIsoLoose[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::PFIsoLoose);
        muonSortedPfIsoMedium[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::PFIsoMedium);
        muonSortedPfIsoTight[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::PFIsoTight);
        muonSortedPfIsoVeryTight[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::PFIsoVeryTight);
        muonSortedTkIsoLoose[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::TkIsoLoose);
        muonSortedTkIsoTight[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::TkIsoTight);
        muonSortedMvaLoose[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::MvaLoose);
        muonSortedMvaMedium[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::MvaMedium);
        muonSortedMvaTight[ID][numMuo[ID] - 1] =
            muo.passed(reco::Muon::MvaTight);

        muonSortedGlobalID[ID][numMuo[ID] - 1] = muo.isGlobalMuon();
        muonSortedTrackID[ID][numMuo[ID] - 1] = muo.isTrackerMuon();

        if (muo.isTrackerMuon() || muo.isGlobalMuon())
        {
            muonValidFraction[ID][numMuo[ID] - 1] =
                muo.innerTrack()->validFraction();
            muonChi2LocalPosition[ID][numMuo[ID] - 1] =
                muo.combinedQuality().chi2LocalPosition;
            muonTrkKick[ID][numMuo[ID] - 1] = muo.combinedQuality().trkKink;
            muonSegmentCompatibility[ID][numMuo[ID] - 1] =
                muon::segmentCompatibility(muo);
        }

        //----------------------------------------------------------------------------
        if (muo.isTrackerMuon() && muo.isGlobalMuon())
        {
            muonSortedChi2[ID][numMuo[ID] - 1] =
                muo.combinedMuon()->chi2(); // chi2 of the combined muon
            // muonSortedChi2[ID][numMuo[ID] - 1] =
            //     muo.globalTrack()->normalizedChi2();
            //----------------------------------------------------------------------------
            muonSortedD0[ID][numMuo[ID] - 1] =
                muo.combinedMuon()->d0(); // impact parameter
            muonSortedDBBeamSpotCorrectedTrackD0[ID][numMuo[ID] - 1] = muo.dB();
            muonSortedDBInnerTrackD0[ID][numMuo[ID] - 1] =
                -1. * (muo.innerTrack()->dxy(beamSpotPoint_));
            muonSortedBeamSpotCorrectedD0[ID][numMuo[ID] - 1] =
                -1. * (muo.combinedMuon()->dxy(beamSpotPoint_));
            muonSortedNDOF[ID][numMuo[ID] - 1] =
                muo.combinedMuon()->ndof(); // n_d.o.f
            muonSortedTrackNHits[ID][numMuo[ID] - 1] =
                muo.track()
                    ->numberOfValidHits(); // number of valid hits in Tracker
            muonSortedValidHitsGlobal[ID][numMuo[ID] - 1] =
                muo.globalTrack()->hitPattern().numberOfValidMuonHits();

            // Save vertex information.
            muonSortedVertX[ID][numMuo[ID] - 1] = muo.vertex().X();
            muonSortedVertY[ID][numMuo[ID] - 1] = muo.vertex().Y();
            muonSortedVertZ[ID][numMuo[ID] - 1] = muo.vertex().Z();

            // Just some extra stuff.
            muonSortedTkLysWithMeasurements[ID][numMuo[ID] - 1] =
                muo.track()->hitPattern().trackerLayersWithMeasurement();
            muonSortedGlbTkNormChi2[ID][numMuo[ID] - 1] =
                muo.globalTrack()->normalizedChi2();
            muonSortedDBPV[ID][numMuo[ID] - 1] =
                muo.muonBestTrack()->dxy(vertexPoint_);
            muonSortedDZPV[ID][numMuo[ID] - 1] =
                muo.muonBestTrack()->dz(vertexPoint_);
            muonSortedVldPixHits[ID][numMuo[ID] - 1] =
                muo.innerTrack()->hitPattern().numberOfValidPixelHits();
            muonSortedMatchedStations[ID][numMuo[ID] - 1] =
                muo.numberOfMatchedStations();
        }
        //----------------------------------------------------------------------------
        // std::cout << "Gets to the filling bit which says track in it";
        // muonSortedTrackNHits[ID][numMuo[ID] - 1] =
        //     muo.track()->numberOfValidHits(); // number of valid hits in
        // Tracker std::cout << " and fills that bit" << std::endl;
        // muonSortedTrackNHits[ID][numMuo[ID] - 1] =
        //     muo.innerTrack()->numberOfValidHits();
        //----------------------------------------------------------------------------

        muonSortedChargedHadronIso[ID][numMuo[ID] - 1] = muo.chargedHadronIso();
        muonSortedNeutralHadronIso[ID][numMuo[ID] - 1] = muo.neutralHadronIso();
        muonSortedPhotonIso[ID][numMuo[ID] - 1] = muo.photonIso();

        muonSortedTrackIso[ID][numMuo[ID] - 1] =
            muo.isolationR03().sumPt; // muo.trackIso();
        muonSortedECalIso[ID][numMuo[ID] - 1] =
            muo.isolationR03().emEt; // muo.ecalIso();
        muonSortedHCalIso[ID][numMuo[ID] - 1] =
            muo.isolationR03().hadEt; // muo.hcalIso();

        // manually calculating comreliso - ie. muonSortedComRelIsodBeta is with
        // DeltaBeta correction:
        muonSortedComRelIso[ID][numMuo[ID] - 1] =
            muonSortedTrackIso[ID][numMuo[ID] - 1];
        muonSortedComRelIso[ID][numMuo[ID] - 1] +=
            muonSortedECalIso[ID][numMuo[ID] - 1];
        muonSortedComRelIso[ID][numMuo[ID] - 1] +=
            muonSortedHCalIso[ID][numMuo[ID] - 1];
        // Old method of rel iso with beta correction
        // muonSortedComRelIsodBeta[ID][numMuo[ID] - 1] =
        //     (muo.chargedHadronIso()
        //      + std::max(0.0,
        //                 muo.neutralHadronIso() + muo.photonIso()
        //                     - 0.5 * muo.puChargedHadronIso()))
        //     / muo.pt();
        // New Method
        muonSortedComRelIsodBeta[ID][numMuo[ID] - 1] =
            (muo.pfIsolationR04().sumChargedHadronPt
             + std::max(0.0,
                        muo.pfIsolationR04().sumNeutralHadronEt
                            + muo.pfIsolationR04().sumPhotonEt
                            - 0.5 * muo.pfIsolationR04().sumPUPt))
            / muo.pt();
        muonSortedComRelIso[ID][numMuo[ID] - 1] /=
            muonSortedPt[ID][numMuo[ID] - 1];
        muonSortedNumChambers[ID][numMuo[ID] - 1] = muo.numberOfChambers();
        muonSortedNumMatches[ID][numMuo[ID] - 1] = muo.numberOfMatches();
        muonSortedIsPFMuon[ID][numMuo[ID] - 1] = muo.isPFMuon();

        // if (muo.genParticleRef().ref().isValid())
        if (!muo.genParticleRef().isNull())
        {
            genMuonSortedPt[ID][numMuo[ID] - 1] = muo.genLepton()->pt();
            genMuonSortedEt[ID][numMuo[ID] - 1] = muo.genLepton()->et();
            genMuonSortedEta[ID][numMuo[ID] - 1] = muo.genLepton()->eta();
            genMuonSortedTheta[ID][numMuo[ID] - 1] = muo.genLepton()->theta();
            genMuonSortedPhi[ID][numMuo[ID] - 1] = muo.genLepton()->phi();
            genMuonSortedPx[ID][numMuo[ID] - 1] = muo.genLepton()->px();
            genMuonSortedPy[ID][numMuo[ID] - 1] = muo.genLepton()->py();
            genMuonSortedPz[ID][numMuo[ID] - 1] = muo.genLepton()->pz();
            genMuonSortedCharge[ID][numMuo[ID] - 1] = muo.genLepton()->charge();
            genMuonSortedPdgId[ID][numMuo[ID] - 1] = muo.genLepton()->pdgId();
            genMuonSortedMotherId[ID][numMuo[ID] - 1] =
                muo.genLepton()->mother()->pdgId();
            genMuonSortedPromptDecayed[ID][numMuo[ID] - 1] =
                muo.genLepton()->isPromptDecayed();
            genMuonSortedPromptFinalState[ID][numMuo[ID] - 1] =
                muo.genLepton()->isPromptFinalState();
            genMuonSortedHardProcess[ID][numMuo[ID] - 1] =
                muo.genLepton()->isHardProcess();
        }
    }
}
/////////////////////////////
void MakeTopologyNtupleMiniAOD::fillOtherJetInfo(const pat::Jet& jet,
                                                 const size_t jetindex,
                                                 const std::string& ID,
                                                 const edm::Event& iEvent)
{
    jetSortedCorrFactor[ID][jetindex] = jetSortedCorrErrLow[ID][jetindex] =
        jetSortedCorrErrHi[ID][jetindex] = -1;

    if (jet.jecSetsAvailable())
    {
        jetSortedCorrFactor[ID][jetindex] =
            jet.jecFactor("Uncorrected"); // jet.corrStep());

        // jetSortedCorrErrLow[ID][jetindex] = jet.relCorrUncert("DOWN"); //
        // jetSortedCorrErrHi[ID][jetindex] = jet.relCorrUncert("UP");
        jetSortedCorrErrLow[ID][jetindex] = -1.0;
        jetSortedCorrErrHi[ID][jetindex] = -1.0;
    }

    if (false)
    { // very verbose
        std::vector<std::string> corrlabels{jet.availableJECSets()};
        // std::cout << jet.currentJECLevel() << " " << jet.currentJECFlavor()
        //           << " ";
        // for (size_t icorr = 0; icorr < corrlabels.size(); icorr++)
        //     std::cout << corrlabels[icorr] << " ";
        // std::cout << std::endl;
    }
    // Residuals as needed
    float resCor{1.0};
    constexpr float L2L3ResErr{-1.0}; // Temp as uncertainty is missing.

    if (!runMCInfo_)
    {
        resCor = jet.jecFactor("L3Absolute");
    }
    jetSortedCorrResidual[ID][jetindex] = resCor;
    jetSortedL2L3ResErr[ID][jetindex] = L2L3ResErr;

    jetSortedE[ID][jetindex] = jet.energy();
    jetSortedEt[ID][jetindex] = jet.et();
    jetSortedPt[ID][jetindex] = jet.pt();
    jetSortedPtRaw[ID][jetindex] = jet.pt();
    jetSortedUnCorEt[ID][jetindex] = jet.correctedP4("Uncorrected").Et();
    jetSortedUnCorPt[ID][jetindex] = jet.correctedP4("Uncorrected").Pt();
    jetSortedEta[ID][jetindex] = jet.eta();
    jetSortedTheta[ID][jetindex] = jet.theta();
    jetSortedPhi[ID][jetindex] = jet.phi();
    jetSortedPx[ID][jetindex] = jet.px();
    jetSortedPy[ID][jetindex] = jet.py();
    jetSortedPz[ID][jetindex] = jet.pz();
    // jetSortedID[ID][jetindex] = jet.jetID();
    jetSortedNtracksInJet[ID][jetindex] =
        jet.associatedTracks().size(); // Need to fix - not a high priority as
                                       // currently not used in the analysis
    jetSortedN90Hits[ID][jetindex] = jet.jetID().n90Hits;
    jetSortedfHPD[ID][jetindex] = jet.jetID().fHPD;
    jetSortedJetCharge[ID][jetindex] = jet.jetCharge();
    jetSortedNConstituents[ID][jetindex] = jet.numberOfDaughters();

    // Calo & JPT
    if (jet.isCaloJet())
    {
        jetSortedEMEnergyInEB[ID][jetindex] = jet.emEnergyInEB();
        jetSortedEMEnergyInEE[ID][jetindex] = jet.emEnergyInEE();
        jetSortedEMEnergyInHF[ID][jetindex] = jet.emEnergyInHF();
        jetSortedEMEnergyFraction[ID][jetindex] = jet.emEnergyFraction();
        jetSortedHadEnergyInHB[ID][jetindex] = jet.hadEnergyInHB();
        jetSortedHadEnergyInHE[ID][jetindex] = jet.hadEnergyInHE();
        jetSortedHadEnergyInHF[ID][jetindex] = jet.hadEnergyInHF();
        jetSortedHadEnergyInHO[ID][jetindex] = jet.hadEnergyInHO();
        jetSortedN60[ID][jetindex] = jet.n60();
        jetSortedN90[ID][jetindex] = jet.n90();
    }
    else if (jet.isPFJet())
    {
        jetSortedMuEnergy[ID][jetindex] = jet.chargedMuEnergy();
        jetSortedMuEnergyFraction[ID][jetindex] =
            jet.correctedJet("Uncorrected").chargedMuEnergyFraction();
        jetSortedChargedMultiplicity[ID][jetindex] = jet.chargedMultiplicity();
        jetSortedNeutralEmEnergy[ID][jetindex] = jet.neutralEmEnergy();
        jetSortedNeutralHadEnergy[ID][jetindex] = jet.neutralHadronEnergy();
        jetSortedNeutralMultiplicity[ID][jetindex] = jet.neutralMultiplicity();
        jetSortedChargedHadronEnergyFraction[ID][jetindex] =
            jet.correctedJet("Uncorrected").chargedHadronEnergyFraction();
        jetSortedNeutralHadronEnergyFraction[ID][jetindex] =
            jet.correctedJet("Uncorrected").neutralHadronEnergyFraction();
        jetSortedChargedEmEnergyFraction[ID][jetindex] =
            jet.correctedJet("Uncorrected").chargedEmEnergyFraction();
        jetSortedNeutralEmEnergyFraction[ID][jetindex] =
            jet.correctedJet("Uncorrected").neutralEmEnergyFraction();
        jetSortedMuonFraction[ID][jetindex] =
            jet.correctedJet("Uncorrected").muonEnergyFraction();
        jetSortedChargedHadronEnergyFractionCorr[ID][jetindex] =
            jet.chargedHadronEnergyFraction();
        jetSortedNeutralHadronEnergyFractionCorr[ID][jetindex] =
            jet.neutralHadronEnergyFraction();
        jetSortedChargedEmEnergyFractionCorr[ID][jetindex] =
            jet.chargedEmEnergyFraction();
        jetSortedNeutralEmEnergyFractionCorr[ID][jetindex] =
            jet.neutralEmEnergyFraction();
        jetSortedMuonFractionCorr[ID][jetindex] = jet.muonEnergyFraction();
    }
    // else if(jet.isJPTJet()) //This function does not exist in 361, when we
    //  move to 382 reinstate
    else
    {
        //"PF" like branches not compatable with 36X. May not be
        // functional/useful anyway.
        // jetSortedChargedHadronEnergyFraction[ID][jetindex] =
        //     jet.chargedHadronEnergyFraction();
        // jetSortedNeutralHadronEnergyFraction[ID][jetindex] =
        //     jet.neutralHadronEnergyFraction();
        // jetSortedChargedEmEnergyFraction[ID][jetindex] =
        //     jet.chargedEmEnergyFraction();
        // jetSortedNeutralEmEnergyFraction[ID][jetindex] =
        //     jet.neutralEmEnergyFraction();
        jetSortedChargedHadronEnergyFraction[ID][jetindex] = -1.0;
        jetSortedNeutralHadronEnergyFraction[ID][jetindex] = -1.0;
        jetSortedChargedEmEnergyFraction[ID][jetindex] = -1.0;
        jetSortedNeutralEmEnergyFraction[ID][jetindex] = -1.0;

        // Calo collection seems to be empty so get the EMF from oldJetID
        // struct.
        jetSortedEMEnergyFraction[ID][jetindex] = jet.jetID().restrictedEMF;
    }
    // check for triggers:
    if (check_triggers_)
    {
        std::vector<pat::TriggerObjectStandAlone> matchedtriggers{
            jet.triggerObjectMatches()};

        if (false)
        { // very verbose.
            for (auto& matchedtrigger : matchedtriggers)
            {
                for (auto it{matchedtrigger.filterLabels().begin()},
                     it_end = matchedtrigger.filterLabels().end();
                     it != it_end;
                     it++)
                {
                    // std::cout << *it << std::endl;
                }
            }
            jetSortedTriggered[ID][jetindex] =
                matchedtriggers.size(); // very coarse, probably want to select
                                        // on a filter.
        }
    }
    // MC information

    genJetSortedClosestB[ID][jetindex] = -1;
    genJetSortedClosestC[ID][jetindex] = -1;

    if (runMCInfo_)
    {
        edm::Handle<reco::GenParticleCollection> genParticles;
        iEvent.getByToken(genSimParticlesToken_, genParticles);
        if (!genParticles.isValid())
        {
            iEvent.getByToken(genParticlesToken_, genParticles);
        }
        for (size_t k{0}; k < genParticles->size(); k++)
        {
            const reco::Candidate& TCand{(*genParticles)[k]};
            if (std::abs(TCand.pdgId()) == 5 || std::abs(TCand.pdgId()) == 4)
            {
                double deltaR{reco::deltaR(jetSortedEta[ID][jetindex],
                                           jetSortedPhi[ID][jetindex],
                                           TCand.eta(),
                                           TCand.phi())};
                if (std::abs(TCand.pdgId()) == 5
                    && (deltaR < genJetSortedClosestB[ID][jetindex]
                        || genJetSortedClosestB[ID][jetindex] < 0))
                {
                    genJetSortedClosestB[ID][jetindex] = deltaR;
                }
                else if (std::abs(TCand.pdgId()) == 4
                         && (deltaR < genJetSortedClosestC[ID][jetindex]
                             || genJetSortedClosestC[ID][jetindex] < 0))
                {
                    genJetSortedClosestC[ID][jetindex] = deltaR;
                }
            }
        }
    }
    jetSortedPID[ID][jetindex] = jet.partonFlavour();
    // next: only fill if genJet was matched.
}

void MakeTopologyNtupleMiniAOD::fillMCJetInfo(const reco::GenJet& jet,
                                              const size_t jetindex,
                                              const std::string& ID,
                                              bool runMC)
{
    if (runMC)
    {
        //    Not every status-1 GEN particle is saved in miniAOD and thus some
        //    of the constituents may be missing. Skip GenConstituent pdgId of
        //    such events.
        edm::Ptr<reco::Candidate> const& constituent{jet.sourceCandidatePtr(
            0)}; // Get pointer to the first genConstituent.

        if (!constituent.isNull() or not constituent.isAvailable())
        {
            genJetSortedPID[ID][jetindex] = constituent->pdgId();
        }
        else
        {
            genJetSortedPID[ID][jetindex] = 0;
        }

        genJetSortedEt[ID][jetindex] = jet.et();
        genJetSortedPt[ID][jetindex] = jet.pt();
        genJetSortedEta[ID][jetindex] = jet.eta();
        genJetSortedTheta[ID][jetindex] = jet.theta();
        genJetSortedPhi[ID][jetindex] = jet.phi();
        genJetSortedPx[ID][jetindex] = jet.px();
        genJetSortedPy[ID][jetindex] = jet.py();
        genJetSortedPz[ID][jetindex] = jet.pz();
        // genJetSortedID[ID][jetindex] = jet.jetID();
    }
    else
    {
        genJetSortedEt[ID][jetindex] = -999.;
        genJetSortedPt[ID][jetindex] = -999.;
        genJetSortedEta[ID][jetindex] = -999.;
        genJetSortedTheta[ID][jetindex] = -999.;
        genJetSortedPhi[ID][jetindex] = -999.;
        genJetSortedPx[ID][jetindex] = -999.;
        genJetSortedPy[ID][jetindex] = -999.;
        genJetSortedPz[ID][jetindex] = -999.;
        // genJetSortedID[ID][jetindex] = 0;
        genJetSortedPID[ID][jetindex] = 0;
        genJetSortedClosestB[ID][jetindex] = -1;
        genJetSortedClosestC[ID][jetindex] = -1;
    }
}

void MakeTopologyNtupleMiniAOD::fillMCJetInfo(int /*empty*/,
                                              const size_t jetindex,
                                              const std::string& ID,
                                              bool /*runMC*/)
{
    genJetSortedEt[ID][jetindex] = -999.;
    genJetSortedPt[ID][jetindex] = -999.;
    genJetSortedEta[ID][jetindex] = -999.;
    genJetSortedTheta[ID][jetindex] = -999.;
    genJetSortedPhi[ID][jetindex] = -999.;
    genJetSortedPx[ID][jetindex] = -999.;
    genJetSortedPy[ID][jetindex] = -999.;
    genJetSortedPz[ID][jetindex] = -999.;
    // genJetSortedID[ID][jetindex] = 0;
    genJetSortedPID[ID][jetindex] = 0;
    genJetSortedClosestB[ID][jetindex] = -1;
    genJetSortedClosestC[ID][jetindex] = -1;
}

void MakeTopologyNtupleMiniAOD::fillBTagInfo(const pat::Jet& jet,
                                             const size_t jetindex,
                                             const std::string& ID)
{
    for (const auto& iBtag : bTagList_)
    {
        bTagRes[iBtag][ID][jetindex] = jet.bDiscriminator(iBtag);
    }

    const reco::SecondaryVertexTagInfo* svTagInfo{jet.tagInfoSecondaryVertex()};
    if (svTagInfo)
    {
        bTags++;
        jetSortedSVX[ID][jetindex] = svTagInfo->secondaryVertex(0).x();
        jetSortedSVY[ID][jetindex] = svTagInfo->secondaryVertex(0).y();
        jetSortedSVZ[ID][jetindex] = svTagInfo->secondaryVertex(0).z();
        jetSortedSVDX[ID][jetindex] = svTagInfo->secondaryVertex(0).xError();
        jetSortedSVDY[ID][jetindex] = svTagInfo->secondaryVertex(0).yError();
        jetSortedSVDZ[ID][jetindex] = svTagInfo->secondaryVertex(0).zError();
    }
}

void MakeTopologyNtupleMiniAOD::fillMCInfo(const edm::Event& iEvent,
                                           const edm::EventSetup& /*iSetup*/)
{
    if (!runMCInfo_)
    {
        return;
    }
    if (ran_mcloop_)
    {
        return;
    }
    ran_mcloop_ = true;
    bool found_b{false};
    int W_hadronic{0};
    int W_leptonic{0};

    // Get the top gen events for top pt reweighting - so I guess this is
    // irrelevant.

    edm::Handle<LHEEventProduct> EventHandle;
    edm::Handle<GenEventInfoProduct> genEventInfo;

    if (isMCatNLO_)
    {
        iEvent.getByToken(pdfInfoToken_, genEventInfo);
    }
    else
    {
        iEvent.getByToken(generatorToken_, genEventInfo);
    }

    if (isLHEflag_)
    {
        iEvent.getByToken(externalLHEToken_, EventHandle);

        origWeightForNorm_ = EventHandle->originalXWGTUP();

        // Weights must be rescaled
        // https://twiki.cern.ch/twiki/bin/viewauth/CMS/LHEReaderCMSSW
        auto rescale_weight = [&](const double w) {
            return w * genEventInfo->weight() / origWeightForNorm_;
        };

        weight_muF0p5_ = rescale_weight(EventHandle->weights()[6].wgt); // muF = 0.5 | muR = 1
        weight_muF2_ = rescale_weight(EventHandle->weights()[3].wgt); // muF = 2 | muR = 1
        weight_muR0p5_ = rescale_weight(EventHandle->weights()[2].wgt); // muF = 1 | muR = 0.5
        weight_muR2_ = rescale_weight(EventHandle->weights()[1].wgt); // muF = 1 | muR = 2
        weight_muF0p5muR0p5_ =
            rescale_weight(EventHandle->weights()[8].wgt); // muF = 0.5 | muR = 0.5
        weight_muF2muR2_ = rescale_weight(EventHandle->weights()[4].wgt); // muF = 2 | muR = 2

        int initialIndex{pdfIdStart_};
        int finalIndex{pdfIdEnd_ + 1};
        int N{finalIndex - initialIndex};
        double pdfSum{0.0};
        double pdfSum2{0.0};

        for (int i{initialIndex}; i != finalIndex; i++)
        {
            for (unsigned int w{0}; w != EventHandle->weights().size(); ++w)
            {
                if (EventHandle->weights()[w].id == std::to_string(i))
                {
                    pdfSum += rescale_weight(EventHandle->weights()[w].wgt);
                }
            }
        }

        double meanObs{(pdfSum) / (double(N))};
        for (int i{initialIndex}; i != finalIndex; i++)
        {
            for (unsigned int w{0}; w != EventHandle->weights().size(); ++w)
            {
                if (EventHandle->weights()[w].id == std::to_string(i))
                {
                    pdfSum2 += (rescale_weight(EventHandle->weights()[w].wgt) - meanObs)
                               * (rescale_weight(EventHandle->weights()[w].wgt) - meanObs);
                }
            }
        }

        double sd{std::sqrt(pdfSum2 / (finalIndex - initialIndex - 1))};
        weight_pdfMax_ = (EventHandle->originalXWGTUP() + sd)
                         / EventHandle->originalXWGTUP();
        weight_pdfMin_ = (EventHandle->originalXWGTUP() - sd)
                         / EventHandle->originalXWGTUP();

        // Debug couts
        // std::cout << "N: " << N << std::endl;
        // std::cout << "pdfSum: " << pdfSum << std::endl;
        // std::cout << "meanObs: " << meanObs << std::endl;
        // std::cout << "evt weight: " << EventHandle->originalXWGTUP()
        //           << std::endl;
        // std::cout << "pdfSum2: " << pdfSum2 << std::endl;
        // std::cout << std::setprecision(10) << std::fixed;
        // std::cout << "sd: " << sd << std::endl;
        //
        // std::cout << (EventHandle->originalXWGTUP() + sd)
        //                  / EventHandle->originalXWGTUP()
        //           << std::endl;
        // std::cout << (EventHandle->originalXWGTUP() - sd)
        //                  / EventHandle->originalXWGTUP()
        //           << std::endl;

        if (hasAlphaWeightFlag_)
        {
            double alphaMax{1.0};
            double alphaMin{1.0};
            for (unsigned int w{0}; w != EventHandle->weights().size(); ++w)
            {
                if (EventHandle->weights()[w].id == alphaIdStart_)
                {
                    alphaMax = rescale_weight(EventHandle->weights()[w].wgt)
                               / EventHandle->originalXWGTUP();
                }
                if (EventHandle->weights()[w].id == alphaIdEnd_)
                {
                    alphaMin = rescale_weight(EventHandle->weights()[w].wgt)
                               / EventHandle->originalXWGTUP();
                }
            }
            weight_alphaMax_ = alphaMax;
            weight_alphaMin_ = alphaMin;
            weight_alphaMax_ = alphaMin;
            weight_alphaMin_ = alphaMax;
        }
        else
        {
            weight_alphaMax_ = 1.0;
            weight_alphaMin_ = 1.0;
        }
    }

    else
    {
        weight_muF0p5_ = -999.0;
        weight_muF2_ = -999.0;
        weight_muR0p5_ = -999.0;
        weight_muR2_ = -999.0;
        weight_muF0p5muR0p5_ = -999.0;
        weight_muF2muR2_ = -999.0;
        origWeightForNorm_ = 0.0;
        weight_pdfMax_ = 1.0;
        weight_pdfMin_ = 1.0;
        weight_alphaMax_ = 1.0;
        weight_alphaMin_ = 1.0;
    }

    if (!is2016rereco_)
    {
        // Perform the recommended rescaling
        // The TWiki says:
        // https://twiki.cern.ch/twiki/bin/viewauth/CMS/LHEReaderCMSSW#Retrieving_the_weights
        // final_weight = nominal_weight * systematic_weight / original_weight
        // but we want to turn these into an easy to use SF
        // sf = final_weight / original_weight
        //    = nominal_weight * systematic_weight / (original_weight ^ 2)
        auto weight_sf = [&](const double w) {
            return w * genEventInfo->weight()
                   / std::pow(EventHandle->originalXWGTUP(), 2);
        };

        for (size_t i{2}; i < genEventInfo->weights().size(); ++i)
        {
            switch (i)
            {
                case 2:
                    isrRedHi = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 3:
                    fsrRedHi = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 4:
                    isrRedLo = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 5:
                    fsrRedLo = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 6:
                    isrDefHi = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 7:
                    fsrDefHi = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 8:
                    isrDefLo = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 9:
                    fsrDefLo = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 10:
                    isrConHi = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 11:
                    fsrConHi = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 12:
                    isrConLo = weight_sf(genEventInfo->weights()[i]);
                    break;
                case 13:
                    fsrConLo = weight_sf(genEventInfo->weights()[i]);
                    break;
                default: break;
            }
        }
    }

    processPtHat_ = genEventInfo->qScale();
    weight_ = genEventInfo->weight();
    processId_ = genEventInfo->signalProcessID();
    edm::Handle<reco::GenParticleCollection> genParticles;
    iEvent.getByToken(genSimParticlesToken_, genParticles);
    if (!genParticles.isValid())
    {
        iEvent.getByToken(genParticlesToken_, genParticles);
    }
    // fillJets(iEvent, iSetup); // needed to do additional MC truth matching.
    nGenPar = 0;

    if (isttbar_)
    {
        double topPt{0.};
        double tBarPt{0.};
        for (size_t k{0}; k < genParticles->size(); k++)
        {
            const reco::Candidate& TCand{(*genParticles)[k]};
            if (TCand.pdgId() == 6)
            {
                topPt = TCand.pt();
            }
            if (TCand.pdgId() == -6)
            {
                tBarPt = TCand.pt();
            }
        }
        // std::cout << topPt << " " << tBarPt << " "
        //           << sqrt(exp(0.0615 - 0.0005 * topPt)
        //                   * exp(0.0615 - 0.0005 * tBarPt))
        //           << std::endl;
        topPtReweight =
            sqrt(exp(0.0615 - 0.0005 * topPt) * exp(0.0615 - 0.0005 * tBarPt));
        histocontainer_["topPtWeightSum"]->Fill(0., topPtReweight);
    }

    for (size_t k{0}; k < genParticles->size(); k++)
    {
        const reco::Candidate& TCand{(*genParticles)[k]};
        // std::cout << "Status: " << TCand.status() << std::endl;
        // std::cout << "pdgId: " << TCand.pdgId() << std::endl;
        // std::cout << "pT: " << TCand.pt() << std::endl;
        // std::cout << "#Mothers: " << TCand.numberOfMothers() << std::endl;
        // std::cout << "#Daughters: " << TCand.numberOfDaughters() <<
        // std::endl;

        // if(TCand.status()==3) // Pythia 6 criteria - MC generators now
        // use Pythia 8 - will store status instead of cutting on it.
        if (std::abs(TCand.pdgId()) <= 18 || std::abs(TCand.pdgId()) == 24
            || std::abs(TCand.pdgId()) == 23)
        {
            // only do this for particles with reasonable pT:
            if (nGenPar < NGENPARMAX)
            {
                // if(TCand.pt()>5. && nGenPar<NGENPARMAX)
                // these are sufficient to fill a lorentz vector, to save space
                // no duplicated information...
                genParEta[nGenPar] = TCand.eta();
                genParPhi[nGenPar] = TCand.phi();
                genParE[nGenPar] = TCand.energy();
                genParPt[nGenPar] = TCand.pt();
                genParId[nGenPar] = TCand.pdgId();
                // ADM Edit 150318
                genParNumMothers[nGenPar] =
                    TCand
                        .numberOfMothers(); // 150318 - ADM - Added so one can
                                            // look for b's from gluon splitting
                                            // - need to know how many parents
                genParMotherId[nGenPar] =
                    TCand.mother()
                        ->pdgId(); // 150318 - ADM - Added so one can
                                   // look for b's from gluon splitting
                                   // - need to know what parent was
                genParNumDaughters[nGenPar] =
                    TCand.numberOfDaughters(); // 150401 - ADM - Added so one
                                               // can look for b's from gluon
                                               // splitting - need to know how
                                               // many daughters
                // End ADM Edit 150318
                // ADM Edit 150927
                genParStatus[nGenPar] =
                    TCand.status(); // 150927 - ADM - Added so that generator
                                    // level status is now saved.
                // End ADM Edit 150927
                genParCharge[nGenPar] = TCand.charge();
                nGenPar++;
            }
        }
        //    }
        if (std::abs(TCand.pdgId()) == 5 || std::abs(TCand.pdgId()) == 4)
        {
            // for (int ijet = 0; ijet < numJet; ijet++)
            // {
            //     float deltaR = reco::deltaR(jetSortedEta[ijet],
            //                                 jetSortedPhi[ijet],
            //                                 TCand.eta(),
            //                                 TCand.phi());
            //     if (std::abs(TCand.pdgId()) == 5
            //         && (deltaR < genJetSortedClosestB[ijet]
            //             || genJetSortedClosestB[ijet] < 0))
            //     {
            //         genJetSortedClosestB[ijet] = deltaR;
            //     }
            //     else if (std::abs(TCand.pdgId()) == 4
            //              && (deltaR < genJetSortedClosestC[ijet]
            //                  || genJetSortedClosestC[ijet] < 0))
            //     {
            //         genJetSortedClosestC[ijet] = deltaR;
            //     }
            // }
        }
        if (TCand.status() == 3
            && std::abs(TCand.pdgId())
                   == 6) // find t or tbar among the genParticles
        {
            if (nT >= NTOPMCINFOSMAX)
            {
                continue;
            }

            if (TCand.numberOfDaughters() >= 2)
            { // check t or tbar has at least 2 daughters
                // std::cout << "The t or tbar candidate has: "
                //           << TCand.numberOfDaughters() << " daughters"
                //           << std::endl;

                for (size_t i_Tdaughter{0};
                     i_Tdaughter < TCand.numberOfDaughters();
                     i_Tdaughter++) // loop over t or tbar daughters
                {
                    const reco::Candidate& TDaughter{
                        *TCand.daughter(i_Tdaughter)};

                    if (TDaughter.status() == 3
                        && std::abs(TDaughter.pdgId()) == 5) // find b
                    {
                        // std::cout << "we found b" << std::endl;
                        found_b = true;

                        if (nb >= NTOPMCINFOSMAX)
                        {
                            continue;
                        }

                        // bMCTruthE[nb] = TDaughter.energy();
                        bMCTruthEt[nb] = TDaughter.et();
                        bMCTruthPx[nb] = TDaughter.px();
                        bMCTruthPy[nb] = TDaughter.py();
                        bMCTruthPz[nb] = TDaughter.pz();

                        nb++;
                    }
                    W_leptonic = W_hadronic = 0;
                    if (TDaughter.status() == 3
                        && std::abs(TDaughter.pdgId()) == 24) // find W
                    {
                        if (TDaughter.numberOfDaughters() >= 2)
                        { // check W has at least 2 daughters

                            for (size_t i_Wdaughter{0};
                                 i_Wdaughter < TDaughter.numberOfDaughters();
                                 i_Wdaughter++)
                            {
                                const reco::Candidate& WDaughter{
                                    *TDaughter.daughter(i_Wdaughter)};
                                if (WDaughter.status() == 3
                                    && std::abs(WDaughter.pdgId()) <= 6
                                    && std::abs(WDaughter.pdgId())
                                           > 0) // W decays in hadronic mode
                                {
                                    if (std::abs(WDaughter.pdgId())
                                        > std::abs(W_hadronic))
                                    {
                                        W_hadronic = WDaughter.pdgId();
                                    }
                                }
                                if (WDaughter.status() == 3
                                    && std::abs(WDaughter.pdgId()) > 10
                                    && std::abs(WDaughter.pdgId()) < 17
                                    && std::abs(WDaughter.pdgId()) % 2
                                           == 1) // W decays in leptonic mode,
                                                 // ele=11, mu=13, tau=15,
                                                 // nuele=12, numu=14, nutau=16
                                {
                                    W_leptonic = WDaughter.pdgId();
                                }
                            }
                        }
                    }

                    if (W_hadronic != 0)
                    {
                        if (nWhadronic >= NTOPMCINFOSMAX)
                        {
                            continue;
                        }
                        W_hadronicMCTruthE[nWhadronic] = TDaughter.energy();
                        // std::cout << "The W hadronic decay energy is: "
                        //           << TDaughter.energy() << std::endl;
                        W_hadronicMCTruthEt[nWhadronic] = TDaughter.et();
                        W_hadronicMCTruthPx[nWhadronic] = TDaughter.px();
                        W_hadronicMCTruthPy[nWhadronic] = TDaughter.py();
                        W_hadronicMCTruthPz[nWhadronic] = TDaughter.pz();
                        W_hadronicMCTruthPID[nWhadronic] = W_hadronic;
                        W_hadronicMCTruthMother[nWhadronic] = nT;
                        nWhadronic++;
                    }

                    else if (W_leptonic != 0)
                    {
                        if (nWleptonic >= NTOPMCINFOSMAX)
                        {
                            continue;
                        }

                        W_leptonicMCTruthE[nWleptonic] = TDaughter.energy();
                        // std::cout << "The W leptonic decay energy is: "
                        //           << TDaughter.energy() << std::endl;
                        W_leptonicMCTruthEt[nWleptonic] = TDaughter.et();
                        W_leptonicMCTruthPx[nWleptonic] = TDaughter.px();
                        W_leptonicMCTruthPy[nWleptonic] = TDaughter.py();
                        W_leptonicMCTruthPz[nWleptonic] = TDaughter.pz();
                        W_leptonicMCTruthPID[nWleptonic] = W_leptonic;
                        W_leptonicMCTruthMother[nWleptonic] = nT;
                        nWleptonic++;
                    }

                    if (found_b
                        && W_hadronic != 0) // now we can keep the top in
                                            // hadronic decay 4-vector
                    {
                        if (nThadronic >= NTOPMCINFOSMAX)
                        {
                            continue;
                        }

                        T_hadronicMCTruthE[nThadronic] = TCand.energy();
                        // std::cout
                        //     << "The initial top (hadronic decay) energy is"
                        //        "then: "
                        //     << TCand.energy() << std::endl;
                        T_hadronicMCTruthEt[nThadronic] = TCand.et();
                        T_hadronicMCTruthPx[nThadronic] = TCand.px();
                        T_hadronicMCTruthPy[nThadronic] = TCand.py();
                        T_hadronicMCTruthPz[nThadronic] = TCand.pz();
                        T_hadronicMotherIndex[nThadronic] = nT;
                        nThadronic++;
                        // std::cout << "test1: " << nThadronic << std::endl;
                    }

                    if (found_b
                        && W_leptonic != 0) // now we can keep the top in
                                            // leptonic decay 4-vector
                    {
                        if (nTleptonic >= NTOPMCINFOSMAX)
                        {
                            continue;
                        }

                        T_leptonicMCTruthE[nTleptonic] = TCand.energy();
                        // std::cout << "The initial top (leptonic decay) energy
                        // "
                        //              "is then: "
                        //           << TCand.energy() << std::endl;
                        T_leptonicMCTruthEt[nTleptonic] = TCand.et();
                        T_leptonicMCTruthPx[nTleptonic] = TCand.px();
                        T_leptonicMCTruthPy[nTleptonic] = TCand.py();
                        T_leptonicMCTruthPz[nTleptonic] = TCand.pz();
                        T_leptonicMotherIndex[nTleptonic] = nT;
                        nTleptonic++;
                        // std::cout << "test2: " << nTleptonic << std::endl;
                    }
                }
            }
            nT++;
        }
    }
    // now check if electron+jets:
    isElePlusJets = 0;
    if (nWleptonic == 1 && std::abs(W_leptonicMCTruthPID[0]) == 11)
    {
        isElePlusJets = 1;
    }

    // PDF info for reweighting!
    // See AN2009/048 for full recipe and description!
    const gen::PdfInfo* pdfInfo{genEventInfo->pdf()};

    if (pdfInfo != nullptr)
    {
        genPDFScale = pdfInfo->scalePDF;
        genPDFx1 = pdfInfo->x.first;
        genPDFx2 = pdfInfo->x.second;
        genPDFf1 = pdfInfo->id.first;
        genPDFf2 = pdfInfo->id.second;
    }

    if (runPDFUncertainties_)
    {
        // CTEQ 6.6 General
        float best_fit{1.0};
        // loop over all (error) pdfs
        // subpdf is the index in the pdf set, 0 = best fit, 1-40 = error pdfs
        // up and down.
        // for (int subpdf = 0; subpdf < LHADPDF::numberPDF(0); subpdf++)
        for (int subpdf{0}; subpdf < 44; subpdf++)
        {
            LHAPDF::usePDFMember(0, subpdf);
            if (subpdf == 0)
            {
                best_fit = LHAPDF::xfx(pdfInfo->x.first,
                                       pdfInfo->scalePDF,
                                       pdfInfo->id.first)
                           * LHAPDF::xfx(pdfInfo->x.second,
                                         pdfInfo->scalePDF,
                                         pdfInfo->id.second);
                genCTEQ66_Weight[subpdf] = best_fit;
            }
            else
            {
                genCTEQ66_Weight[subpdf] =
                    (LHAPDF::xfx(
                         pdfInfo->x.first, pdfInfo->scalePDF, pdfInfo->id.first)
                     * LHAPDF::xfx(pdfInfo->x.second,
                                   pdfInfo->scalePDF,
                                   pdfInfo->id.second)
                     / best_fit);
            }
        }
        // MRST 2006 NLO
        best_fit = 1.0;
        // loop over all (error) pdfs
        // subpdf is the index in the pdf set, 0 = best fit, 1-40 = error pdfs
        // up and down.
        // for (int subpdf = 0; subpdf < LHADPDF::numberPDF(0); subpdf++)
        for (int subpdf{0}; subpdf < 31; subpdf++)
        {
            LHAPDF::usePDFMember(1, subpdf);
            if (subpdf == 0)
            {
                best_fit = LHAPDF::xfx(pdfInfo->x.first,
                                       pdfInfo->scalePDF,
                                       pdfInfo->id.first)
                           * LHAPDF::xfx(pdfInfo->x.second,
                                         pdfInfo->scalePDF,
                                         pdfInfo->id.second);
                genMRST2006nnlo_Weight[subpdf] = best_fit;
            }
            else
            {
                genMRST2006nnlo_Weight[subpdf] =
                    (LHAPDF::xfx(
                         pdfInfo->x.first, pdfInfo->scalePDF, pdfInfo->id.first)
                     * LHAPDF::xfx(pdfInfo->x.second,
                                   pdfInfo->scalePDF,
                                   pdfInfo->id.second)
                     / best_fit);
            }
        }
    }
}

//////////////////////////////////////////////////////////////////////////////////////////////

void MakeTopologyNtupleMiniAOD::fillJets(
    const edm::Event& iEvent,
    const edm::EventSetup& /*iSetup*/,
    edm::EDGetTokenT<pat::JetCollection> jetIn_,
    const std::string& ID)
{
    // if (ran_jetloop_)
    // {
    //     return;
    // }
    // ran_jetloop_ = true;

    edm::Handle<pat::JetCollection> jetHandle;
    iEvent.getByToken(jetIn_, jetHandle);
    const pat::JetCollection& jets{*jetHandle};

    edm::Handle<reco::GenJetCollection> genJetHandle;
    if (runMCInfo_)
    {
        iEvent.getByToken(genJetsToken_, genJetHandle);
    }

    // check that the electrons are filled, if not do so:
    // if (!ran_eleloop_)
    // {
    //     fillElectrons(iEvent, iSetup);
    // }
    //   !!!
    // IMPORTANT: DO NOT CUT ON THE OBJECTS BEFORE THEY ARE SORTED, cuts should
    // be applied in the second loop!!!
    //   !!!
    correctedJetEts.clear();

    // std::cout << __LINE__ << " : " << __FILE__ << " : nJets = " <<
    // jets.size()
    //           << std::endl;

    for (const auto& jet : jets)
    {
        if (useResidualJEC_) // Correct the Et with residuals first
        {
            if (jet.isCaloJet())
            {
                jecCalo->setJetEta(jet.eta());
                jecCalo->setJetPt(jet.pt());
                correctedJetEts.emplace_back(jet.et()
                                             * jecCalo->getCorrection());
            }
            else if (jet.isPFJet())
            {
                jecPF->setJetEta(jet.eta());
                jecPF->setJetPt(jet.pt());
                correctedJetEts.emplace_back(jet.et() * jecPF->getCorrection());
            }
            // else if (jet_iter->isJPTJet())
            else
            {
                jecJPT->setJetEta(jet.eta());
                jecJPT->setJetPt(jet.pt());
                correctedJetEts.emplace_back(jet.et()
                                             * jecJPT->getCorrection());
            }
        }
        else
        {
            correctedJetEts.emplace_back(jet.et());
        }
    }

    std::vector<size_t> etJetSorted{
        IndexSorter<std::vector<float>>(correctedJetEts, true)()};
    // std::cout << "second jet loop: " << std::endl;

    // jets:
    numJet[ID] = 0;

    boost::container::vector<bool> genJetUsed(
        100,
        false); // index of jets in the gen jet collection - if it's true it
                // means it's already matched and so shouldn't be used again
    for (size_t ijet{0};
         ijet < etJetSorted.size() && numJet[ID] < numeric_cast<int>(NJETSMAX);
         ++ijet)
    {
        size_t jjet{etJetSorted[ijet]};

        const pat::Jet& jet{jets[jjet]};

        // Check our type to match with our electron collection. This will NOT
        // throw errors if it has not been ran yet!
        std::string eleCol;
        if (jet.isCaloJet())
        {
            eleCol = "Calo";
        }
        // else if (jet.isJPTJet())
        // {
        //     eleCol = "Calo";
        // } // JPT only jets
        else if (ID == "AK5PF")
        {
            eleCol = "Calo";
        } // Pass for reco PF jets
        else if (jet.isPFJet())
        {
            eleCol = "PF";
        }
        else
        {
            eleCol = "Calo";
        } // For backup.
        fillOtherJetInfo(jet, numJet[ID], ID, iEvent);
        // Do jet smearing here.
        if (runMCInfo_)
        {
            float delR{9999.};
            reco::GenJet assocJet;
            const reco::GenJetCollection& genJets{*genJetHandle};
            int genJetIndex{0};
            int tempIndex{0};
            for (const auto& genJet : genJets)
            {
                double dphi{jet.phi() - genJet.phi()};
                if (dphi > TMath::Pi())
                {
                    dphi = 2 * TMath::Pi() - dphi;
                }
                if (dphi < -TMath::Pi())
                {
                    dphi = -2 * TMath::Pi() - dphi;
                }
                double dEta{jet.eta() - genJet.eta()};
                double dR{sqrt(dphi * dphi + pow(dEta, 2))};
                if (dR < 0.4 && dR < delR && !genJetUsed[genJetIndex])
                {
                    delR = dR;

                    assocJet = genJet;
                    tempIndex = genJetIndex;
                }
                genJetIndex++;
            }
            if (delR < 999.)
            {
                genJetUsed[tempIndex] = true;
                // Make a fill MC info section here that will fill with the
                // associated jet.
                fillMCJetInfo(assocJet, numJet[ID], ID, true);
            }
            else
            { // if no associated gen jet fill with -999.
                fillMCJetInfo(assocJet, numJet[ID], ID, false);
            }
        }
        else
        {
            fillMCJetInfo(0, numJet[ID], ID, false);
        }

        /////////////////////////////
        // no cuts that remove jets after this!

        numJet[ID]++;

        fillBTagInfo(jet, numJet[ID] - 1, ID);
    }
    metE[ID] = sqrt(pow(metPx[ID], 2) + pow(metPy[ID], 2) + pow(metPz[ID], 2));
    metEt[ID] = sqrt(pow(metPx[ID], 2) + pow(metPy[ID], 2));
    if (numJet[ID] == 0)
    {
        clearjetarrays(ID);
    }

    edm::Handle<double> rhoHand_;
    iEvent.getByToken(rhoToken_, rhoHand_);
    fixedGridRhoFastjetAll[ID] = *(rhoHand_.product());
}

void MakeTopologyNtupleMiniAOD::fillGeneralTracks(
    const edm::Event& iEvent, const edm::EventSetup& /*iSetup*/)
{
    if (ran_tracks_)
    {
        return;
    }
    ran_tracks_ = true;

    edm::Handle<std::vector<pat::PackedCandidate>> lostTracks;
    iEvent.getByToken(trackToken_, lostTracks);

    numGeneralTracks = 0;

    for (auto trit{lostTracks->begin()};
         trit != lostTracks->end()
         && numGeneralTracks < numeric_cast<int>(NTRACKSMAX);
         trit++)
    {
        generalTracksPt[numGeneralTracks] = trit->pt();
        generalTracksEta[numGeneralTracks] = trit->eta();
        generalTracksTheta[numGeneralTracks] = trit->theta();
        generalTracksBeamSpotCorrectedD0[numGeneralTracks] =
            -1. * (trit->dxy(beamSpotPoint_));
        generalTracksPhi[numGeneralTracks] = trit->phi();
        generalTracksCharge[numGeneralTracks] = trit->charge();

        numGeneralTracks++;
    }
}

/////////////////////////////////////
void MakeTopologyNtupleMiniAOD::clearTauArrays(const std::string& ID)
{
    ntaus[ID] = 0;
    tau_e[ID].clear();
    tau_phi[ID].clear();
    tau_eta[ID].clear();
    tau_pt[ID].clear();
}
void MakeTopologyNtupleMiniAOD::clearPhotonArrays(const std::string& ID)
{
    nphotons[ID] = 0;
    photon_e[ID].clear();
    photon_phi[ID].clear();
    photon_eta[ID].clear();
    photon_pt[ID].clear();
}
void MakeTopologyNtupleMiniAOD::clearelectronarrays(const std::string& ID)
{
    numEle[ID] = 0;

    nzcandidates[ID] = 0;
    zcandidatesvector[ID].clear();

    electronEts.clear(); // just used for sorting
    std::vector<float> tempVector;

    electronSortedE[ID].clear();
    electronSortedEt[ID].clear();
    electronSortedEta[ID].clear();
    electronSortedPt[ID].clear();
    electronSortedTheta[ID].clear();
    electronSortedPhi[ID].clear();
    electronSortedPx[ID].clear();
    electronSortedPy[ID].clear();
    electronSortedPz[ID].clear();
    electronSortedCharge[ID].clear();

    electronSortedCutIdVeto[ID].clear();
    electronSortedCutIdLoose[ID].clear();
    electronSortedCutIdMedium[ID].clear();
    electronSortedCutIdTight[ID].clear();

    electronSortedChargedHadronIso[ID].clear();
    electronSortedNeutralHadronIso[ID].clear();
    electronSortedPhotonIso[ID].clear();
    electronSortedTrackPt[ID].clear();
    electronSortedTrackEta[ID].clear();
    electronSortedTrackPhi[ID].clear();
    electronSortedTrackChi2[ID].clear();
    electronSortedTrackNDOF[ID].clear();
    electronSortedTrackD0[ID].clear();
    electronSortedDBBeamSpotCorrectedTrackD0[ID].clear();

    // electronSortedDBInnerTrackD0[ID].clear();

    electronSortedBeamSpotCorrectedTrackD0[ID].clear();
    electronSortedTrackDz[ID].clear();
    electronSortedTrackD0PV[ID].clear();
    electronSortedTrackDZPV[ID].clear();
    electronSortedVtxZ[ID].clear();
    electronSortedBeamSpotCorrectedTrackDz[ID].clear();
    electronSortedIsGsf[ID].clear();
    electronSortedGsfPx[ID].clear();
    electronSortedGsfPy[ID].clear();
    electronSortedGsfPz[ID].clear();
    electronSortedGsfE[ID].clear();
    electronSortedEcalEnergy[ID].clear();

    electronSortedSuperClusterEta[ID].clear();
    electronSortedSuperClusterE[ID].clear();
    electronSortedSuperClusterPhi[ID].clear();
    electronSortedSuperClusterEoverP[ID].clear();
    electronSortedSuperClusterSigmaEtaEta[ID].clear();
    electronSortedSuperClusterE1x5[ID].clear();
    electronSortedSuperClusterE2x5max[ID].clear();
    electronSortedSuperClusterE5x5[ID].clear();
    electronSortedSuperClusterSigmaIEtaIEta[ID].clear();
    electronSortedSuperClusterSigmaIEtaIEta5x5[ID].clear();
    electronSortedTrackIso04[ID].clear();
    electronSortedECalIso04[ID].clear();
    electronSortedHCalIso04[ID].clear();
    electronSortedTrackIso03[ID].clear();
    electronSortedECalIso03[ID].clear();
    electronSortedHCalIso03[ID].clear();
    electronSorteddr04EcalRecHitSumEt[ID].clear();
    electronSorteddr03EcalRecHitSumEt[ID].clear();
    electronSortedECalIsoDeposit[ID].clear();
    electronSortedHCalIsoDeposit[ID].clear();
    electronSortedCaloIso[ID].clear();
    electronSortedTriggerMatch[ID].clear();
    electronSortedJetOverlap[ID].clear();
    electronSortedComRelIso[ID].clear();
    electronSortedComRelIsodBeta[ID].clear();
    electronSortedComRelIsoRho[ID].clear();
    electronSortedChHadIso[ID].clear();
    electronSortedNtHadIso[ID].clear();
    electronSortedGammaIso[ID].clear();
    electronSortedRhoIso[ID].clear();
    electronSortedAEff03[ID].clear();
    electronSortedMissingInnerLayers[ID].clear();
    electronSortedHoverE[ID].clear();
    electronSortedDeltaPhiSC[ID].clear();
    electronSortedDeltaEtaSC[ID].clear();
    electronSortedDeltaEtaSeedSC[ID].clear();
    electronSortedIsBarrel[ID].clear();
    electronSortedPhotonConversionTag[ID].clear();
    electronSortedPhotonConversionTagCustom[ID].clear();
    electronSortedPhotonConversionDcot[ID].clear();
    electronSortedPhotonConversionDist[ID].clear();
    electronSortedPhotonConversionVeto[ID].clear();
    electronSortedPhotonConversionDcotCustom[ID].clear();
    electronSortedPhotonConversionDistCustom[ID].clear();

    electronSortedImpactTransDist[ID].clear();
    electronSortedImpactTransError[ID].clear();
    electronSortedImpactTransSignificance[ID].clear();
    electronSortedImpact3DDist[ID].clear();
    electronSortedImpact3DError[ID].clear();
    electronSortedImpact3DSignificance[ID].clear();

    // electronSortedIDResults_[ID].clear();

    genElectronSortedPt[ID].clear();
    genElectronSortedEt[ID].clear();
    genElectronSortedEta[ID].clear();
    genElectronSortedTheta[ID].clear();
    genElectronSortedPhi[ID].clear();
    genElectronSortedPx[ID].clear();
    genElectronSortedPy[ID].clear();
    genElectronSortedCharge[ID].clear();
    genElectronSortedPdgId[ID].clear();
    genElectronSortedMotherId[ID].clear();
    genElectronSortedPromptDecayed[ID].clear();
    genElectronSortedPromptFinalState[ID].clear();
    genElectronSortedHardProcess[ID].clear();
}

void MakeTopologyNtupleMiniAOD::clearmuonarrays(const std::string& ID)
{
    // std::cout << "clearmuonarrays CHECK" << std::endl;
    numMuo[ID] = 0;
    muonEts.clear(); // just used for sorting

    muonSortedE[ID].clear();
    muonSortedEt[ID].clear();
    muonSortedPt[ID].clear();
    muonSortedEta[ID].clear();
    muonSortedTheta[ID].clear();
    muonSortedPhi[ID].clear();
    muonSortedPx[ID].clear();
    muonSortedPy[ID].clear();
    muonSortedPz[ID].clear();
    muonSortedCharge[ID].clear();

    muonSortedLooseCutId[ID].clear();
    muonSortedMediumCutId[ID].clear();
    muonSortedTightCutId[ID].clear();
    muonSortedPfIsoVeryLoose[ID].clear();
    muonSortedPfIsoLoose[ID].clear();
    muonSortedPfIsoMedium[ID].clear();
    muonSortedPfIsoTight[ID].clear();
    muonSortedPfIsoVeryTight[ID].clear();
    muonSortedTkIsoLoose[ID].clear();
    muonSortedTkIsoTight[ID].clear();
    muonSortedMvaLoose[ID].clear();
    muonSortedMvaMedium[ID].clear();
    muonSortedMvaTight[ID].clear();

    muonSortedGlobalID[ID].clear();
    muonSortedTrackID[ID].clear();

    muonValidFraction[ID].clear();
    muonChi2LocalPosition[ID].clear();
    muonTrkKick[ID].clear();
    muonSegmentCompatibility[ID].clear();

    muonSortedChi2[ID].clear();
    muonSortedD0[ID].clear();
    muonSortedDBBeamSpotCorrectedTrackD0[ID].clear();

    muonSortedDBInnerTrackD0[ID].clear();

    muonSortedBeamSpotCorrectedD0[ID].clear();
    muonSortedTrackNHits[ID].clear();
    muonSortedValidHitsGlobal[ID].clear();
    muonSortedNDOF[ID].clear(); // n_d.o.f

    muonSortedVertX[ID].clear();
    muonSortedVertY[ID].clear();
    muonSortedVertZ[ID].clear();

    muonSortedTkLysWithMeasurements[ID].clear();
    muonSortedGlbTkNormChi2[ID].clear();
    muonSortedDBPV[ID].clear();
    muonSortedDZPV[ID].clear();
    muonSortedVldPixHits[ID].clear();
    muonSortedMatchedStations[ID].clear();

    muonSortedChargedHadronIso[ID].clear();
    muonSortedNeutralHadronIso[ID].clear();
    muonSortedPhotonIso[ID].clear();

    muonSortedTrackIso[ID].clear();
    muonSortedECalIso[ID].clear();
    muonSortedHCalIso[ID].clear();
    muonSortedComRelIso[ID].clear();
    muonSortedComRelIsodBeta[ID].clear();
    muonSortedIsPFMuon[ID].clear();
    muonSortedNumChambers[ID].clear();
    muonSortedNumMatches[ID].clear();

    genMuonSortedPt[ID].clear();
    genMuonSortedEt[ID].clear();
    genMuonSortedEta[ID].clear();
    genMuonSortedTheta[ID].clear();
    genMuonSortedPhi[ID].clear();
    genMuonSortedPx[ID].clear();
    genMuonSortedPy[ID].clear();
    genMuonSortedPz[ID].clear();
    genMuonSortedCharge[ID].clear();
    genMuonSortedPdgId[ID].clear();
    genMuonSortedMotherId[ID].clear();
    genMuonSortedPromptDecayed[ID].clear();
    genMuonSortedPromptFinalState[ID].clear();
    genMuonSortedHardProcess[ID].clear();
}

void MakeTopologyNtupleMiniAOD::clearMetArrays(const std::string& ID)
{
    // std::cout << "clearMetArrays CHECK" << std::endl;
    metE[ID] = -99999.0;
    metEt[ID] = -99999.0;
    metEtRaw[ID] = -99999.0;
    metPhi[ID] = -99999.0;
    metPt[ID] = -99999.0;
    metPx[ID] = -99999.0;
    metPy[ID] = -99999.0;
    metPz[ID] = -99999.0;
    metSignificance[ID] = -99999.0;
    metScalarEt[ID] = -99999.0;
    metEtUncorrected[ID] = -99999.0;
    metPhiUncorrected[ID] = -99999.0;
    metUnclusteredEnUp[ID] = -99999.0;
    metUnclusteredEnDown[ID] = -99999.0;
    metMaxEtEM[ID] = -99999.0;
    metMaxEtHad[ID] = -99999.0;
    metEtFracHad[ID] = -99999.0;
    metEtFracEM[ID] = -99999.0;
    metHadEtHB[ID] = -99999.0;
    metHadEtHO[ID] = -99999.0;
    metHadEtHE[ID] = -99999.0;
    metEmEtEE[ID] = -99999.0;
    metEmEtEB[ID] = -99999.0;
    metEmEtHF[ID] = -99999.0;
    metHadEtHF[ID] = -99999.0;
    genMetE[ID] = -99999.0;
    genMetEt[ID] = -99999.0;
    genMetPhi[ID] = -99999.0;
    genMetPt[ID] = -99999.0;
    genMetPx[ID] = -99999.0;
    genMetPy[ID] = -99999.0;
    genMetPz[ID] = -99999.0;
}
/////////////////////////////////////
void MakeTopologyNtupleMiniAOD::clearMCarrays()
{
    // electronTruthEts.clear(); // just used for sorting
    // std::cout << "clearMCarrays CHECK" << std::endl;
    nT = 0;
    nThadronic = 0;
    nTleptonic = 0;
    nb = 0;
    nWhadronic = 0;
    nWleptonic = 0;
    VQQBosonAbsId = -999;

    for (size_t i{0}; i < NTOPMCINFOSMAX; i++)
    {
        T_hadronicMCTruthE[i] = 0;
        T_hadronicMCTruthEt[i] = 0;
        T_hadronicMCTruthPx[i] = 0;
        T_hadronicMCTruthPy[i] = 0;
        T_hadronicMCTruthPz[i] = 0;
        T_hadronicMotherIndex[i] = -1;

        T_leptonicMCTruthE[i] = 0;
        T_leptonicMCTruthEt[i] = 0;
        T_leptonicMCTruthPx[i] = 0;
        T_leptonicMCTruthPy[i] = 0;
        T_leptonicMCTruthPz[i] = 0;
        T_leptonicMotherIndex[i] = -1;

        bMCTruthE[i] = 0;
        bMCTruthEt[i] = 0;
        bMCTruthPx[i] = 0;
        bMCTruthPy[i] = 0;
        bMCTruthPz[i] = 0;
        bMCTruthMother[i] = -1;

        W_hadronicMCTruthE[i] = 0;
        W_hadronicMCTruthEt[i] = 0;
        W_hadronicMCTruthPx[i] = 0;
        W_hadronicMCTruthPy[i] = 0;
        W_hadronicMCTruthPz[i] = 0;
        W_hadronicMCTruthPID[i] = 0;
        W_hadronicMCTruthMother[i] = -1;

        W_leptonicMCTruthE[i] = 0;
        W_leptonicMCTruthEt[i] = 0;
        W_leptonicMCTruthPx[i] = 0;
        W_leptonicMCTruthPy[i] = 0;
        W_leptonicMCTruthPz[i] = 0;
        W_leptonicMCTruthPID[i] = 0;
        W_leptonicMCTruthMother[i] = -1;

        // remainingEnergy[i] = 0;
    }
    // PDF Reweighting
    genPDFScale = -1;
    genPDFx1 = -1;
    genPDFx2 = -1;
    genPDFf1 = 9999;
    genPDFf2 = 9999;
    if (runPDFUncertainties_)
    {
        for (float& i : genCTEQ66_Weight)
        {
            i = -1;
        }
        for (float& i : genMRST2006nnlo_Weight)
        {
            i = -1;
        }
    }

    topPtReweight = 1.;
}

/////////////////////////////////////
void MakeTopologyNtupleMiniAOD::clearjetarrays(const std::string& ID)
{
    // std::cout << "clearjetarrays CHECK" << std::endl;
    numJet[ID] = 0;
    correctedJetEts.clear();

    jetSortedE[ID].clear();
    jetSortedEt[ID].clear();
    jetSortedPt[ID].clear();
    jetSortedPtRaw[ID].clear();
    jetSortedUnCorEt[ID].clear();
    jetSortedUnCorPt[ID].clear();
    jetSortedEta[ID].clear();
    jetSortedTheta[ID].clear();
    jetSortedPhi[ID].clear();
    jetSortedPx[ID].clear();
    jetSortedPy[ID].clear();
    jetSortedPz[ID].clear();
    // jetSortedID[ID].clear();
    jetSortedClosestLepton[ID].clear();
    jetSortedNtracksInJet[ID].clear();
    jetSortedJetCharge[ID].clear();
    jetSortedfHPD[ID].clear();
    jetSortedCorrFactor[ID].clear();
    jetSortedCorrResidual[ID].clear();
    jetSortedL2L3ResErr[ID].clear();
    jetSortedCorrErrLow[ID].clear();
    jetSortedCorrErrHi[ID].clear();
    jetSortedN90Hits[ID].clear();
    jetSortedBtagSoftMuonPtRel[ID].clear();
    jetSortedBtagSoftMuonQuality[ID].clear();
    jetSortedTriggered[ID].clear();
    jetSortedSVX[ID].clear();
    jetSortedSVY[ID].clear();
    jetSortedSVZ[ID].clear();
    jetSortedSVDX[ID].clear();
    jetSortedSVDY[ID].clear();
    jetSortedSVDZ[ID].clear();
    jetSortedBIDParams_[ID].clear();
    jetSortedNConstituents[ID].clear();
    bidParamsDiscCut_[ID] = -1.0;

    for (const auto& iBtag : bTagList_)
    {
        bTagRes[iBtag][ID].clear();
    }

    // Calo specific
    jetSortedEMEnergyInEB[ID].clear();
    jetSortedEMEnergyInEE[ID].clear();
    jetSortedEMEnergyFraction[ID].clear();
    jetSortedEMEnergyInHF[ID].clear();
    jetSortedHadEnergyInHB[ID].clear();
    jetSortedHadEnergyInHE[ID].clear();
    jetSortedHadEnergyInHF[ID].clear();
    jetSortedHadEnergyInHO[ID].clear();
    jetSortedN60[ID].clear();
    jetSortedN90[ID].clear();
    // PF specific
    jetSortedNeutralMultiplicity[ID].clear();
    jetSortedChargedMultiplicity[ID].clear();
    jetSortedMuEnergy[ID].clear();
    jetSortedMuEnergyFraction[ID].clear();
    jetSortedNeutralHadEnergy[ID].clear();
    jetSortedNeutralEmEnergy[ID].clear();
    jetSortedChargedHadronEnergyFraction[ID].clear();
    jetSortedNeutralHadronEnergyFraction[ID].clear();
    jetSortedChargedEmEnergyFraction[ID].clear();
    jetSortedNeutralEmEnergyFraction[ID].clear();
    jetSortedMuonFraction[ID].clear();
    jetSortedChargedHadronEnergyFractionCorr[ID].clear();
    jetSortedNeutralHadronEnergyFractionCorr[ID].clear();
    jetSortedChargedEmEnergyFractionCorr[ID].clear();
    jetSortedNeutralEmEnergyFractionCorr[ID].clear();
    jetSortedMuonFractionCorr[ID].clear();

    genJetSortedEt[ID].clear();
    genJetSortedPt[ID].clear();
    genJetSortedEta[ID].clear();
    genJetSortedTheta[ID].clear();
    genJetSortedPhi[ID].clear();
    genJetSortedPx[ID].clear();
    genJetSortedPy[ID].clear();
    genJetSortedPz[ID].clear();
    // genJetSortedID[ID].clear();
    jetSortedPID[ID].clear();
    genJetSortedPID[ID].clear();
    genJetSortedClosestB[ID].clear();
    genJetSortedClosestC[ID].clear();

    fixedGridRhoFastjetAll[ID] = -999.0f;
}

/////////////////////////////////////
void MakeTopologyNtupleMiniAOD::clearGeneralTracksarrays()
{
    // std::cout << "clearGeneralTracksarrays CHECK" << std::endl;
    numGeneralTracks = 0;

    for (size_t i{0}; i < NTRACKSMAX; i++)
    {
        generalTracksPt[i] = -1.;
        generalTracksEta[i] = 9999;
        generalTracksTheta[i] = 9999;
        generalTracksBeamSpotCorrectedD0[i] = -9999;
        generalTracksPhi[i] = 9999;
        generalTracksCharge[i] = 0;
    }
}

/////////////////////////////////////
void MakeTopologyNtupleMiniAOD::cleararrays()
{
    // reset the bookkeeping bools;
    // std::cout << "cleararrays CHECK" << std::endl;
    // std::cout << "before FALSE: " << ran_postloop_ << std::endl;
    ran_jetloop_ = ran_eleloop_ = ran_muonloop_ = ran_PV_ = ran_tracks_ =
        ran_mcloop_ = ran_postloop_ = ran_photonTau_ = false;
    // std::cout << "psot FALSE: " << ran_postloop_ << std::endl;

    for (size_t iTrig{0}; iTrig < triggerList_.size(); iTrig++)
    {
        triggerRes[iTrig] = -99;
    }
    for (size_t iMetFilter{0}; iMetFilter < metFilterList_.size(); iMetFilter++)
    {
        metFilterRes[iMetFilter] = -99;
    }

    for (int& HLT_fakeTriggerValue : HLT_fakeTriggerValues)
    {
        HLT_fakeTriggerValue = -99;
    }
    for (size_t ii{0}; ii < 200; ii++)
    {
        TriggerBits[ii] = -99;
    }

    clearjetarrays("Calo");
    clearelectronarrays("Calo");
    clearmuonarrays("Calo");
    clearMetArrays("Calo");
    clearTauArrays("Calo");
    clearPhotonArrays("Calo");

    clearjetarrays("PF");
    clearelectronarrays("PF");
    clearmuonarrays("PF");
    clearMetArrays("PF");
    clearTauArrays("PF");

    clearjetarrays("AK5PF");

    clearjetarrays("JPT");
    clearMetArrays("JPT");

    clearMCarrays();
    clearGeneralTracksarrays();

    mhtSignif = -1;
    mhtPx = -9999.;
    mhtPy = -9999.;
    mhtPhi = -9999.;
    mhtSumEt = -1;
    mhtPt = -1;

    // metSignificance = -9999.; // metHandle->front().metSignificance();
    // metScalarEt = -9999.; // metHandle->front().sumEt();
    // metEtUncorrected = -9999.; // metHandle->front().uncorrectedPt();
    // metPhiUncorrected = -9999.; // metHandle->front().uncorrectedPhi();

    topo_sphericity = -1;
    topo_aplanarity = -1;
    topo_ht = -1;
    topo_sqrts = -1;
    // and same but including the electron.
    topo_sphericitye = -1;
    topo_aplanaritye = -1;
    topo_hte = -1;
    topo_sqrtse = -1;
    flavorHistory = 999;

    // clear zcandidates;

    beamSpotX = beamSpotY = beamSpotZ = 0;
    math::XYZPoint point(beamSpotX, beamSpotY, beamSpotZ);
    beamSpotPoint_ = point;

    evtRun = 0;
    evtnum = 0;
    evtlumiblock = 0.;
}

// ------------ method called to for each event  ------------
void MakeTopologyNtupleMiniAOD::analyze(const edm::Event& iEvent,
                                        const edm::EventSetup& iSetup)
{
    using namespace edm;
    // std::cout << iEvent.id().run() << " " << iEvent.luminosityBlock() << " "
    //           << iEvent.id().event()
    //           << std::endl; // Run pile-up reweighting here
    numVert = 0;
    if (runPUReWeight_)
    {
        edm::Handle<std::vector<PileupSummaryInfo>> pileupSummaryInfo_;
        iEvent.getByToken(
            pileupToken_,
            pileupSummaryInfo_); // miniAODv1 uses "addPileupInfo", miniAODv2
                                 // uses "slimmedAddPileupInfo"

        std::vector<PileupSummaryInfo>::const_iterator PVI;

        float Tnpv{-1};
        for (PVI = pileupSummaryInfo_->begin();
             PVI != pileupSummaryInfo_->end();
             PVI++)
        {
            int BX{PVI->getBunchCrossing()};

            if (BX == 0)
            {
                Tnpv = pileupSummaryInfo_->begin()->getTrueNumInteractions();
                continue;
            }
        }
        numVert = Tnpv;
    }

    histocontainer_["eventcount"]->Fill(0.0);

    // std::cout << "now in loop" << std::endl;
    // std::cout << "cleared arrays." << std::endl;

    cleararrays();

    fillEventInfo(iEvent, iSetup);
    fillTriggerData(iEvent);
    fillBeamSpot(iEvent, iSetup);

    // std::cout << "done with trigger and beam spot" << std::endl;

    // Here I am taking out the Calo and JPT stuff. I don't think this should
    // matter, as I'm only using PF things. If it turns out to be a problem I
    // can add them back in later.

    // fillMuons(iEvent, iSetup, muoLabel_, "Calo");
    fillMuons(iEvent, iSetup, patMuonsToken_, "PF");
    fillElectrons(iEvent, iSetup, patElectronsToken_, "PF", eleLabel_);

    // fillJets(iEvent, iSetup, jetLabel_, "Calo");
    // Putting MET info before jets so it can be used for jet smearing.
    fillMissingET(iEvent, iSetup, patMetToken_, "PF");

    fillJets(iEvent, iSetup, patJetsToken_, "PF");

    // fillJets(iEvent, iSetup, jetPFRecoTag_, "AK5PF");
    // fillJets(iEvent, iSetup, jetJPTTag_, "JPT");
    //
    // std::cout << "done with jets" << std::endl;
    fillGeneralTracks(iEvent, iSetup);

    // fillElectrons(iEvent, iSetup, eleLabel_, "Calo");
    fillMCInfo(iEvent, iSetup);
    // fillMissingET(iEvent, iSetup, metLabel_, "Calo");
    //
    // fillMissingET(iEvent, iSetup, metJPTTag_, "JPT");
    // fillGeneralTracks(iEvent, iSetup);

    fillSummaryVariables();

    // std::cout << "done with topology, now filling tree..." << std::endl;
    // std::cout << numEle["PF"] << std::endl;
    // Run the cut flow code. This involves event selections and seeing how many
    // events containing things we get. Eventually this will require me putting
    // in different selections for the different channels, but for now just
    // double electron.

    if (!doCuts_)
    {
        mytree_->Fill(); // If not doing cuts, fill up EVERYTHING
    }
    else
    { // If doing cuts, ensure that we have at least x leptons which meet
      // minimum sensible criteria

        int numLeps{0};
        numLeps = numEle["PF"] + numMuo["PF"];

        for (int j{0}; j < numEle["PF"]; j++)
        {
            if (electronSortedPt["PF"][0] < elePtCut_)
            {
                continue;
            }
            if (std::abs(electronSortedEta["PF"][0]) > eleEtaCut_)
            {
                continue;
            }
            if (electronSortedComRelIsoRho["PF"][0] > eleIsoCut_)
            {
                continue;
            }
            numLeps++;
        }

        for (int j{0}; j < numMuo["PF"]; j++)
        {
            if (muonSortedPt["PF"][0] < muoPtCut_)
            {
                continue;
            }
            if (std::abs(muonSortedEta["PF"][0]) > muoEtaCut_)
            {
                continue;
            }
            if (muonSortedComRelIsodBeta["PF"][0] > muoIsoCut_)
            {
                continue;
            }
            numLeps++;
        }

        if (numLeps >= minLeptons_)
        {
            mytree_->Fill();
        }
    }

    // fill debugging histograms.
    histocontainer_["tightElectrons"]->Fill(numEle["PF"]);
    histocontainer_["tightMuons"]->Fill(numMuo["PF"]);
}

void MakeTopologyNtupleMiniAOD::bookBranches()
{
    // std::cout << "bookBranches CHECK" << std::endl;
    TTree::SetMaxTreeSize(std::numeric_limits<Long64_t>::max());
    mytree_ = new TTree("tree", "tree");
    mytree_->SetAutoSave(-std::numeric_limits<Long64_t>::max());

    // bookElectronBranches("Calo", "Calo");
    // bookMuonBranches("Calo", "Calo");
    // bookJetBranches("Calo", "Calo");
    // bookMETBranches("Calo", "Calo");
    // bookTauBranches("Calo", "Calo");

    bookElectronBranches("PF", "PF2PAT");
    bookMuonBranches("PF", "PF2PAT");
    bookJetBranches("PF", "PF2PAT");
    bookPFJetBranches("PF", "PF2PAT");
    bookMETBranches("PF", "PF2PAT");
    bookTauBranches("PF", "PF2PAT");

    // bookJetBranches("AK5PF", "AK5PF");
    // bookPFJetBranches("AK5PF", "AK5PF");
    // bookJetBranches("JPT", "JPT");
    // bookMETBranches("JPT", "TC");

    bookGeneralTracksBranches();
    if (runMCInfo_)
    {
        bookMCBranches();
    }

    mytree_->Branch("processId", &processId_, "processId/I");
    mytree_->Branch("processPtHat", &processPtHat_, "processPtHat/F");
    mytree_->Branch("processMCWeight", &weight_, "processMCWeight/D");

    mytree_->Branch("beamSpotX", &beamSpotX, "beamSpotX/F");
    mytree_->Branch("beamSpotY", &beamSpotY, "beamSpotY/F");
    mytree_->Branch("beamSpotZ", &beamSpotZ, "beamSpotZ/F");

    mytree_->Branch("numPv", &numPv, "numPv/I");
    mytree_->Branch("pvX", &pvX, "pvX/F");
    mytree_->Branch("pvY", &pvY, "pvY/F");
    mytree_->Branch("pvZ", &pvZ, "pvZ/F");
    mytree_->Branch("pvDX", &pvDX, "pvDX/F");
    mytree_->Branch("pvDY", &pvDY, "pvDY/F");
    mytree_->Branch("pvDZ", &pvDZ, "pvDZ/F");
    mytree_->Branch("pvRho", &pvRho, "pvRho/F");
    mytree_->Branch("pvIsFake", &pvIsFake, "pvIsFake/I");
    mytree_->Branch("pvNdof", &pvNdof, "pvNdof/F");
    mytree_->Branch("pvChi2", &pvChi2, "pvChi2/F");

    mytree_->Branch("mhtPt", &mhtPt, "mhtPt/F");
    mytree_->Branch("mhtPy", &mhtPy, "mhtPy/F");
    mytree_->Branch("mhtPx", &mhtPx, "mhtPx/F");
    mytree_->Branch("mhtPhi", &mhtPhi, "mhtPhi/F");
    mytree_->Branch("mhtSumEt", &mhtSumEt, "mhtSumEt/F");
    mytree_->Branch("mhtSignif", &mhtSignif, "mhtSignif/F");

    mytree_->Branch("nTriggerBits", &nTriggerBits, "nTriggerBits/I");
    mytree_->Branch("TriggerBits", TriggerBits, "TriggerBits[nTriggerBits]/I");

    mytree_->Branch("numVert", &numVert, "numVert/I");

    mytree_->Branch("weight_muF0p5", &weight_muF0p5_, "weight_muF0p5/D");
    mytree_->Branch("weight_muF2", &weight_muF2_, "weight_muF2/D");
    mytree_->Branch("weight_muR0p5", &weight_muR0p5_, "weight_muR0p5/D");
    mytree_->Branch("weight_muR2", &weight_muR2_, "weight_muR2/D");
    mytree_->Branch(
        "weight_muF0p5muR0p5", &weight_muF0p5muR0p5_, "weight_muF0p5muR0p5/D");
    mytree_->Branch("weight_muF2muR2", &weight_muF2muR2_, "weight_muF2muR2/D");
    mytree_->Branch(
        "origWeightForNorm", &origWeightForNorm_, "origWeightForNorm/D");
    mytree_->Branch("weight_pdfMax", &weight_pdfMax_, "weight_pdfMax/D");
    mytree_->Branch("weight_pdfMin", &weight_pdfMin_, "weight_pdfMin/D");
    mytree_->Branch("weight_alphaMax", &weight_alphaMax_, "weight_alphaMax/D");
    mytree_->Branch("weight_alphaMin", &weight_alphaMin_, "weight_alphaMin/D");

    mytree_->Branch("isrRedHi", &isrRedHi, "isrRedHi/D");
    mytree_->Branch("fsrRedHi", &fsrRedHi, "fsrRedHi/D");
    mytree_->Branch("isrRedLo", &isrRedLo, "isrRedLo/D");
    mytree_->Branch("fsrRedLo", &fsrRedLo, "fsrRedLo/D");
    mytree_->Branch("isrDefHi", &isrDefHi, "isrDefHi/D");
    mytree_->Branch("fsrDefHi", &fsrDefHi, "fsrDefHi/D");
    mytree_->Branch("isrDefLo", &isrDefLo, "isrDefLo/D");
    mytree_->Branch("fsrDefLo", &fsrDefLo, "fsrDefLo/D");
    mytree_->Branch("isrConHi", &isrConHi, "isrConHi/D");
    mytree_->Branch("fsrConHi", &fsrConHi, "fsrConHi/D");
    mytree_->Branch("isrConLo", &isrConLo, "isrConLo/D");
    mytree_->Branch("fsrConLo", &fsrConLo, "fsrConLo/D");

    while (HLT_fakeTriggerValues.size() < fakeTrigLabelList_.size())
    {
        HLT_fakeTriggerValues.emplace_back(-99);
    }
    for (size_t ii{0}; ii < fakeTrigLabelList_.size(); ii++)
    {
        TString name{"HLTFake_"};
        name += fakeTrigLabelList_[ii];
        name.ReplaceAll(" ", "");
        TString name2{name};
        name2 += "/I";
        std::cout << "making fake trigger branch " << name << std::endl;
        mytree_->Branch(name, &HLT_fakeTriggerValues[ii], name2);
    }

    // Dynamic trigger list
    // for (auto iTrig = triggerList_.begin(); iTrig != triggerList_.end();
    //      iTrig++)
    while (triggerRes.size() < triggerList_.size())
    {
        triggerRes.emplace_back(-99);
    }
    while (metFilterRes.size() < metFilterList_.size())
    {
        metFilterRes.emplace_back(-99);
    }
    for (size_t iTrig{0}; iTrig < triggerList_.size(); iTrig++)
    {
        std::cout << "Booking trigger branch: " << triggerList_[iTrig]
                  << std::endl;
        mytree_->Branch(triggerList_[iTrig].c_str(),
                        &triggerRes[iTrig],
                        (triggerList_[iTrig] + "/I").c_str());
    }
    for (size_t iMetFilter{0}; iMetFilter < metFilterList_.size(); iMetFilter++)
    {
        std::cout << "Booking MET filter branch: " << metFilterList_[iMetFilter]
                  << std::endl;
        mytree_->Branch(metFilterList_[iMetFilter].c_str(),
                        &metFilterRes[iMetFilter],
                        (metFilterList_[iMetFilter] + "/I").c_str());
    }

    // generator level information
    //  mytree_->Branch("myProcess", &genMyProcId, "myProcess/I");
    if (runMCInfo_)
    {
        mytree_->Branch("nGenPar", &nGenPar, "nGenPar/I");
        mytree_->Branch("genParEta", genParEta, "genParEta[nGenPar]/F");
        mytree_->Branch("genParPhi", genParPhi, "genParPhi[nGenPar]/F");
        mytree_->Branch("genParE", genParE, "genParE[nGenPar]/F");
        mytree_->Branch("genParPt", genParPt, "genParPt[nGenPar]/F");
        mytree_->Branch("genParId", genParId, "genParId[nGenPar]/I");
        mytree_->Branch("genParNumMothers",
                        genParNumMothers,
                        "genParNumMothers[nGenPar]/I");
        mytree_->Branch(
            "genParMotherId", genParMotherId, "genParMotherId[nGenPar]/I");
        mytree_->Branch("genParNumDaughters",
                        genParNumDaughters,
                        "genParNumDaughters[nGenPar]/I");
        mytree_->Branch(
            "genParCharge", genParCharge, "genParCharge[nGenPar]/I");
    }

    mytree_->Branch("eventRun", &evtRun, "eventRun/I");
    mytree_->Branch("eventNum", &evtnum, "eventNum/I");
    mytree_->Branch("eventLumiblock", &evtlumiblock, "eventLumiblock/F");
}

void MakeTopologyNtupleMiniAOD::bookTauBranches(const std::string& ID,
                                                const std::string& name)
{
    ntaus[ID] = 0;

    std::vector<float> tempVecF(NTAUSMAX);
    tau_e[ID] = tempVecF;
    tau_phi[ID] = tempVecF;
    tau_eta[ID] = tempVecF;
    tau_pt[ID] = tempVecF;

    mytree_->Branch(("numTau" + name).c_str(),
                    &ntaus[ID],
                    ("numTau" + name + "/I").c_str());

    std::string prefix{"tau" + name};
    mytree_->Branch((prefix + "E").c_str(),
                    &tau_e[ID][0],
                    (prefix + "E[numTau" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Pt").c_str(),
                    &tau_pt[ID][0],
                    (prefix + "Pt[numTau" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Phi").c_str(),
                    &tau_phi[ID][0],
                    (prefix + "Phi[numTau" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Eta").c_str(),
                    &tau_eta[ID][0],
                    (prefix + "Eta[numTau" + name + "]/F").c_str());
}

// book electron branches:
void MakeTopologyNtupleMiniAOD::bookElectronBranches(const std::string& ID,
                                                     const std::string& name)
{
    // Initialise maps so ROOT wont panic
    std::vector<float> tempVecF(NELECTRONSMAX);
    std::vector<int> tempVecI(NELECTRONSMAX);
    boost::container::vector<bool> tempVecB(NELECTRONSMAX);

    numEle[ID] = -1;

    electronSortedCharge[ID] = tempVecI;

    electronSortedIsBarrel[ID] = tempVecI;
    electronSortedPhotonConversionTag[ID] = tempVecI;
    electronSortedPhotonConversionTagCustom[ID] = tempVecI;
    electronSortedMissingInnerLayers[ID] = tempVecI;

    electronSortedE[ID] = tempVecF;
    electronSortedEt[ID] = tempVecF;
    electronSortedEta[ID] = tempVecF;
    electronSortedPt[ID] = tempVecF;
    electronSortedTheta[ID] = tempVecF;
    electronSortedPhi[ID] = tempVecF;
    electronSortedPx[ID] = tempVecF;
    electronSortedPy[ID] = tempVecF;
    electronSortedPz[ID] = tempVecF;

    electronSortedCutIdVeto[ID] = tempVecI;
    electronSortedCutIdLoose[ID] = tempVecI;
    electronSortedCutIdMedium[ID] = tempVecI;
    electronSortedCutIdTight[ID] = tempVecI;

    electronSortedChargedHadronIso[ID] = tempVecF;
    electronSortedNeutralHadronIso[ID] = tempVecF;
    electronSortedPhotonIso[ID] = tempVecF;

    electronSortedTrackPt[ID] = tempVecF;
    electronSortedTrackEta[ID] = tempVecF;
    electronSortedTrackPhi[ID] = tempVecF;
    electronSortedTrackChi2[ID] = tempVecF;
    electronSortedTrackNDOF[ID] = tempVecF;
    electronSortedTrackD0[ID] = tempVecF;
    electronSortedDBBeamSpotCorrectedTrackD0[ID] = tempVecF;

    // electronSortedDBInnerTrackD0[ID] = tempVecF;

    electronSortedBeamSpotCorrectedTrackD0[ID] = tempVecF;
    electronSortedTrackDz[ID] = tempVecF;
    electronSortedTrackD0PV[ID] = tempVecF;
    electronSortedTrackDZPV[ID] = tempVecF;
    electronSortedVtxZ[ID] = tempVecF;
    electronSortedBeamSpotCorrectedTrackDz[ID] = tempVecF;
    electronSortedIsGsf[ID] = tempVecI;
    electronSortedGsfPx[ID] = tempVecF;
    electronSortedGsfPy[ID] = tempVecF;
    electronSortedGsfPz[ID] = tempVecF;
    electronSortedGsfE[ID] = tempVecF;
    electronSortedEcalEnergy[ID] = tempVecF;

    electronSortedSuperClusterEta[ID] = tempVecF;
    electronSortedSuperClusterE[ID] = tempVecF;
    electronSortedSuperClusterPhi[ID] = tempVecF;
    electronSortedSuperClusterEoverP[ID] = tempVecF;
    electronSortedSuperClusterSigmaEtaEta[ID] = tempVecF;
    electronSortedSuperClusterE1x5[ID] = tempVecF;
    electronSortedSuperClusterE2x5max[ID] = tempVecF;
    electronSortedSuperClusterE5x5[ID] = tempVecF;
    electronSortedSuperClusterSigmaIEtaIEta[ID] = tempVecF;
    electronSortedSuperClusterSigmaIEtaIEta5x5[ID] = tempVecF;
    electronSortedTrackIso04[ID] = tempVecF;
    electronSortedECalIso04[ID] = tempVecF;
    electronSortedHCalIso04[ID] = tempVecF;
    electronSortedTrackIso03[ID] = tempVecF;
    electronSortedECalIso03[ID] = tempVecF;
    electronSortedHCalIso03[ID] = tempVecF;
    electronSorteddr04EcalRecHitSumEt[ID] = tempVecF;
    electronSorteddr03EcalRecHitSumEt[ID] = tempVecF;
    electronSortedECalIsoDeposit[ID] = tempVecF;
    electronSortedHCalIsoDeposit[ID] = tempVecF;
    electronSortedCaloIso[ID] = tempVecF;
    electronSortedTriggerMatch[ID] = tempVecF;
    electronSortedJetOverlap[ID] = tempVecF;
    electronSortedComRelIso[ID] = tempVecF;
    electronSortedComRelIsodBeta[ID] = tempVecF;
    electronSortedComRelIsoRho[ID] = tempVecF;
    electronSortedChHadIso[ID] = tempVecF;
    electronSortedNtHadIso[ID] = tempVecF;
    electronSortedGammaIso[ID] = tempVecF;
    electronSortedRhoIso[ID] = tempVecF;
    electronSortedAEff03[ID] = tempVecF;
    electronSortedHoverE[ID] = tempVecF;
    electronSortedDeltaPhiSC[ID] = tempVecF;
    electronSortedDeltaEtaSC[ID] = tempVecF;
    electronSortedDeltaEtaSeedSC[ID] = tempVecF;
    electronSortedPhotonConversionDcot[ID] = tempVecF;
    electronSortedPhotonConversionDist[ID] = tempVecF;
    electronSortedPhotonConversionVeto[ID] = tempVecI;
    electronSortedPhotonConversionDcotCustom[ID] = tempVecF;
    electronSortedPhotonConversionDistCustom[ID] = tempVecF;
    electronSortedImpactTransDist[ID] = tempVecF;
    electronSortedImpactTransError[ID] = tempVecF;
    electronSortedImpactTransSignificance[ID] = tempVecF;
    electronSortedImpact3DDist[ID] = tempVecF;
    electronSortedImpact3DError[ID] = tempVecF;
    electronSortedImpact3DSignificance[ID] = tempVecF;

    genElectronSortedPt[ID] = tempVecF;
    genElectronSortedEt[ID] = tempVecF;
    genElectronSortedEta[ID] = tempVecF;
    genElectronSortedTheta[ID] = tempVecF;
    genElectronSortedPhi[ID] = tempVecF;
    genElectronSortedPx[ID] = tempVecF;
    genElectronSortedPy[ID] = tempVecF;
    genElectronSortedPz[ID] = tempVecF;
    genElectronSortedCharge[ID] = tempVecI;
    genElectronSortedPdgId[ID] = tempVecI;
    genElectronSortedMotherId[ID] = tempVecI;
    genElectronSortedPromptDecayed[ID] = tempVecI;
    genElectronSortedPromptFinalState[ID] = tempVecI;
    genElectronSortedHardProcess[ID] = tempVecI;

    std::string prefix{"ele" + name};
    mytree_->Branch(("numEle" + name).c_str(),
                    &numEle[ID],
                    ("numEle" + name + "/I").c_str());

    // Dynamic ID's

    mytree_->Branch((prefix + "E").c_str(),
                    &electronSortedE[ID][0],
                    (prefix + "E[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "ET").c_str(),
                    &electronSortedEt[ID][0],
                    (prefix + "ET[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "PX").c_str(),
                    &electronSortedPx[ID][0],
                    (prefix + "PX[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "PY").c_str(),
                    &electronSortedPy[ID][0],
                    (prefix + "PY[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "PZ").c_str(),
                    &electronSortedPz[ID][0],
                    (prefix + "PZ[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Phi").c_str(),
                    &electronSortedPhi[ID][0],
                    (prefix + "Phi[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Theta").c_str(),
                    &electronSortedTheta[ID][0],
                    (prefix + "Theta[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Eta").c_str(),
                    &electronSortedEta[ID][0],
                    (prefix + "Eta[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "PT").c_str(),
                    &electronSortedPt[ID][0],
                    (prefix + "PT[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Charge").c_str(),
                    &electronSortedCharge[ID][0],
                    (prefix + "Charge[numEle" + name + "]/I").c_str());

    mytree_->Branch((prefix + "CutIdVeto").c_str(),
                    &electronSortedCutIdVeto[ID][0],
                    (prefix + "CutIdVeto[numEle" + name + "]/I").c_str());
    mytree_->Branch((prefix + "CutIdLoose").c_str(),
                    &electronSortedCutIdLoose[ID][0],
                    (prefix + "CutIdLoose[numEle" + name + "]/I").c_str());
    mytree_->Branch((prefix + "CutIdMedium").c_str(),
                    &electronSortedCutIdMedium[ID][0],
                    (prefix + "CutIdMedium[numEle" + name + "]/I").c_str());
    mytree_->Branch((prefix + "CutIdTight").c_str(),
                    &electronSortedCutIdTight[ID][0],
                    (prefix + "CutIdTight[numEle" + name + "]/I").c_str());

    mytree_->Branch((prefix + "ImpactTransDist").c_str(),
                    &electronSortedImpactTransDist[ID][0],
                    (prefix + "ImpactTransDist[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "ImpactTransError").c_str(),
        &electronSortedImpactTransError[ID][0],
        (prefix + "ImpactTransError[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "ImpactTransSignificance").c_str(),
        &electronSortedImpactTransSignificance[ID][0],
        (prefix + "ImpactTransSignificance[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Impact3DDist").c_str(),
                    &electronSortedImpact3DDist[ID][0],
                    (prefix + "Impact3DDist[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Impact3DError").c_str(),
                    &electronSortedImpact3DError[ID][0],
                    (prefix + "Impact3DError[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "Impact3DSignificance").c_str(),
        &electronSortedImpact3DSignificance[ID][0],
        (prefix + "Impact3DSignificance[numEle" + name + "]/F").c_str());

    mytree_->Branch(
        (prefix + "ChargedHadronIso").c_str(),
        &electronSortedChargedHadronIso[ID][0],
        (prefix + "ChargedHadronIso[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "NeutralHadronIso").c_str(),
        &electronSortedNeutralHadronIso[ID][0],
        (prefix + "NeutralHadronIso[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "PhotonIso").c_str(),
                    &electronSortedPhotonIso[ID][0],
                    (prefix + "PhotonIso[numEle" + name + "]/F").c_str());

    mytree_->Branch((prefix + "TrackPt").c_str(),
                    &electronSortedTrackPt[ID][0],
                    (prefix + "TrackPt[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrackPhi").c_str(),
                    &electronSortedTrackPhi[ID][0],
                    (prefix + "TrackPhi[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrackEta").c_str(),
                    &electronSortedTrackEta[ID][0],
                    (prefix + "TrackEta[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrackChi2").c_str(),
                    &electronSortedTrackChi2[ID][0],
                    (prefix + "TrackChi2[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrackNDOF").c_str(),
                    &electronSortedTrackNDOF[ID][0],
                    (prefix + "TrackNDOF[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrackD0").c_str(),
                    &electronSortedTrackD0[ID][0],
                    (prefix + "TrackD0[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrackDBD0").c_str(),
                    &electronSortedDBBeamSpotCorrectedTrackD0[ID][0],
                    (prefix + "TrackDBD0[numEle" + name + "]/F").c_str());

    // mytree_->Branch((prefix + "DBInnerTrackD0").c_str(),
    //                 &electronSortedDBInnerTrackD0[ID][0],
    //                 (prefix + "DBInnerTrackD0[numEle" + name +
    //                 "]/F").c_str());

    mytree_->Branch(
        (prefix + "BeamSpotCorrectedTrackD0").c_str(),
        &electronSortedBeamSpotCorrectedTrackD0[ID][0],
        (prefix + "BeamSpotCorrectedTrackD0[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrackDz").c_str(),
                    &electronSortedTrackDz[ID][0],
                    (prefix + "TrackDz[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "D0PV").c_str(),
                    &electronSortedTrackD0PV[ID][0],
                    (prefix + "D0PV[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "DZPV").c_str(),
                    &electronSortedTrackDZPV[ID][0],
                    (prefix + "DZPV[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "VtxZ").c_str(),
                    &electronSortedVtxZ[ID][0],
                    (prefix + "VtxZ[numEle" + name + "]/F").c_str());

    mytree_->Branch((prefix + "IsGsf").c_str(),
                    &electronSortedIsGsf[ID][0],
                    (prefix + "IsGsf[numEle" + name + "]/I").c_str());

    mytree_->Branch((prefix + "GsfPx").c_str(),
                    &electronSortedGsfPx[ID][0],
                    (prefix + "GsfPx[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "GsfPy").c_str(),
                    &electronSortedGsfPy[ID][0],
                    (prefix + "GsfPy[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "GsfPz").c_str(),
                    &electronSortedGsfPz[ID][0],
                    (prefix + "GsfPz[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "GsfE").c_str(),
                    &electronSortedGsfE[ID][0],
                    (prefix + "GsfE[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "EcalEnergy").c_str(),
                    &electronSortedEcalEnergy[ID][0],
                    (prefix + "EcalEnergy[numEle" + name + "]/F").c_str());

    mytree_->Branch((prefix + "SCEta").c_str(),
                    &electronSortedSuperClusterEta[ID][0],
                    (prefix + "SCEta[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SCE").c_str(),
                    &electronSortedSuperClusterE[ID][0],
                    (prefix + "SCE[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SCPhi").c_str(),
                    &electronSortedSuperClusterPhi[ID][0],
                    (prefix + "SCPhi[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SCEoverP").c_str(),
                    &electronSortedSuperClusterEoverP[ID][0],
                    (prefix + "SCEoverP[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SCSigmaEtaEta").c_str(),
                    &electronSortedSuperClusterSigmaEtaEta[ID][0],
                    (prefix + "SCSigmaEtaEta[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SCSigmaIEtaIEta").c_str(),
                    &electronSortedSuperClusterSigmaIEtaIEta[ID][0],
                    (prefix + "SCSigmaIEtaIEta[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "SCSigmaIEtaIEta5x5").c_str(),
        &electronSortedSuperClusterSigmaIEtaIEta5x5[ID][0],
        (prefix + "SCSigmaIEtaIEta5x5[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SCE1x5").c_str(),
                    &electronSortedSuperClusterE1x5[ID][0],
                    (prefix + "SCE1x5[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SCE5x5").c_str(),
                    &electronSortedSuperClusterE5x5[ID][0],
                    (prefix + "SCE5x5[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SCE2x5max").c_str(),
                    &electronSortedSuperClusterE2x5max[ID][0],
                    (prefix + "SCE2x5max[numEle" + name + "]/F").c_str());

    mytree_->Branch((prefix + "TrackIso04").c_str(),
                    &electronSortedTrackIso04[ID][0],
                    (prefix + "TrackIso04[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "EcalIso04").c_str(),
                    &electronSortedECalIso04[ID][0],
                    (prefix + "EcalIso04[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "HcalIso04").c_str(),
                    &electronSortedHCalIso04[ID][0],
                    (prefix + "HcalIso04[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrackIso03").c_str(),
                    &electronSortedTrackIso03[ID][0],
                    (prefix + "TrackIso03[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "EcalIso03").c_str(),
                    &electronSortedECalIso03[ID][0],
                    (prefix + "EcalIso03[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "HcalIso03").c_str(),
                    &electronSortedHCalIso03[ID][0],
                    (prefix + "HcalIso03[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "dr04EcalRecHitSumEt").c_str(),
        &electronSorteddr04EcalRecHitSumEt[ID][0],
        (prefix + "dr04EcalRecHitSumEt[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "dr03EcalRecHitSumEt").c_str(),
        &electronSorteddr03EcalRecHitSumEt[ID][0],
        (prefix + "dr03EcalRecHitSumEt[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "EcalIsoDeposit").c_str(),
                    &electronSortedECalIsoDeposit[ID][0],
                    (prefix + "EcalIsoDeposit[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "HcalIsoDeposit").c_str(),
                    &electronSortedHCalIsoDeposit[ID][0],
                    (prefix + "HcalIsoDeposit[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "ComRelIso").c_str(),
                    &electronSortedComRelIso[ID][0],
                    (prefix + "ctronComRelIso[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "ComRelIsodBeta").c_str(),
        &electronSortedComRelIsodBeta[ID][0],
        (prefix + "ctronComRelIsodBeta[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "ComRelIsoRho").c_str(),
        &electronSortedComRelIsoRho[ID][0],
        (prefix + "ctronComRelIsoRho[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "ChHadIso").c_str(),
                    &electronSortedChHadIso[ID][0],
                    (prefix + "ChHadIso[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "NtHadIso").c_str(),
                    &electronSortedNtHadIso[ID][0],
                    (prefix + "NtHadIso[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "GammaIso").c_str(),
                    &electronSortedGammaIso[ID][0],
                    (prefix + "GammaIso[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "RhoIso").c_str(),
                    &electronSortedRhoIso[ID][0],
                    (prefix + "RhoIso[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "AEff03").c_str(),
                    &electronSortedAEff03[ID][0],
                    (prefix + "AEff03[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "MissingInnerLayers").c_str(),
        &electronSortedMissingInnerLayers[ID][0],
        (prefix + "MissingInnerLayers[numEle" + name + "]/I").c_str());
    mytree_->Branch((prefix + "HoverE").c_str(),
                    &electronSortedHoverE[ID][0],
                    (prefix + "HoverE[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "DeltaPhiSC").c_str(),
                    &electronSortedDeltaPhiSC[ID][0],
                    (prefix + "DeltaPhiSC[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "DeltaEtaSC").c_str(),
                    &electronSortedDeltaEtaSC[ID][0],
                    (prefix + "DeltaEtaSC[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "DeltaEtaSeedSC").c_str(),
                    &electronSortedDeltaEtaSeedSC[ID][0],
                    (prefix + "DeltaEtaSeedSC[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "IsBarrel").c_str(),
                    &electronSortedIsBarrel[ID][0],
                    (prefix + "IsBarrel[numEle" + name + "]/I").c_str());
    mytree_->Branch(
        (prefix + "PhotonConversionTag").c_str(),
        &electronSortedPhotonConversionTag[ID][0],
        (prefix + "PhotonConversionTag[numEle" + name + "]/I").c_str());
    mytree_->Branch(
        (prefix + "PhotonConversionDist").c_str(),
        &electronSortedPhotonConversionDist[ID][0],
        (prefix + "PhotonConversionDist[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "PhotonConversionDcot").c_str(),
        &electronSortedPhotonConversionDcot[ID][0],
        (prefix + "PhotonConversionDcot[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "PhotonConversionVeto").c_str(),
        &electronSortedPhotonConversionVeto[ID][0],
        (prefix + "PhotonConversionVeto[numEle" + name + "]/I").c_str());
    mytree_->Branch(
        (prefix + "PhotonConversionTagCustom").c_str(),
        &electronSortedPhotonConversionTagCustom[ID][0],
        (prefix + "PhotonConversionTagCustom[numEle" + name + "]/I").c_str());
    mytree_->Branch(
        (prefix + "PhotonConversionDistCustom").c_str(),
        &electronSortedPhotonConversionDistCustom[ID][0],
        (prefix + "PhotonConversionDistCustom[numEle" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "PhotonConversionDcotCustom").c_str(),
        &electronSortedPhotonConversionDcotCustom[ID][0],
        (prefix + "PhotonConversionDcotCustom[numEle" + name + "]/F").c_str());

    mytree_->Branch((prefix + "TriggerMatch").c_str(),
                    &electronSortedTriggerMatch[ID][0],
                    (prefix + "TriggerMatch[numEle" + name + "]/F").c_str());
    mytree_->Branch((prefix + "JetOverlap").c_str(),
                    &electronSortedJetOverlap[ID][0],
                    (prefix + "JetOverlap[numEle" + name + "]/F").c_str());

    if (runMCInfo_)
    {
        mytree_->Branch(
            ("genEle" + name + "PT").c_str(),
            &genElectronSortedPt[ID][0],
            ("genEle" + name + "ElePT[numEle" + name + "]/F").c_str());
        mytree_->Branch(
            ("genEle" + name + "ET").c_str(),
            &genElectronSortedEt[ID][0],
            ("genEle" + name + "EleET[numEle" + name + "]/F").c_str());
        mytree_->Branch(
            ("genEle" + name + "PX").c_str(),
            &genElectronSortedPx[ID][0],
            ("genEle" + name + "ElePx[numEle" + name + "]/F").c_str());
        mytree_->Branch(
            ("genEle" + name + "PY").c_str(),
            &genElectronSortedPy[ID][0],
            ("genEle" + name + "ElePy[numEle" + name + "]/F").c_str());
        mytree_->Branch(
            ("genEle" + name + "PZ").c_str(),
            &genElectronSortedPz[ID][0],
            ("genEle" + name + "ElePz[numEle" + name + "]/F").c_str());
        mytree_->Branch(
            ("genEle" + name + "Phi").c_str(),
            &genElectronSortedPhi[ID][0],
            ("genEle" + name + "ElePhi[numEle" + name + "]/F").c_str());
        mytree_->Branch(
            ("genEle" + name + "Theta").c_str(),
            &genElectronSortedTheta[ID][0],
            ("genEle" + name + "EleTheta[numEle" + name + "]/F").c_str());
        mytree_->Branch(
            ("genEle" + name + "Eta").c_str(),
            &genElectronSortedEta[ID][0],
            ("genEle" + name + "EleEta[numEle" + name + "]/F").c_str());
        mytree_->Branch(
            ("genEle" + name + "Charge").c_str(),
            &genElectronSortedCharge[ID][0],
            ("genEle" + name + "EleCharge[numEle" + name + "]/I").c_str());
        mytree_->Branch(
            ("genEle" + name + "PdgId").c_str(),
            &genElectronSortedPdgId[ID][0],
            ("genEle" + name + "ElePdgId[numEle" + name + "]/I").c_str());
        mytree_->Branch(
            ("genEle" + name + "MotherId").c_str(),
            &genElectronSortedMotherId[ID][0],
            ("genEle" + name + "EleMotherId[numEle" + name + "]/I").c_str());
        mytree_->Branch(
            ("genEle" + name + "PromptDecayed").c_str(),
            &genElectronSortedPromptDecayed[ID][0],
            ("genEle" + name + "ElePromptDecayed[numEle" + name + "]/I")
                .c_str());
        mytree_->Branch(
            ("genEle" + name + "PromptFinalState").c_str(),
            &genElectronSortedPromptFinalState[ID][0],
            ("genEle" + name + "ElePromptFinalState[numEle" + name + "]/I")
                .c_str());
        mytree_->Branch(
            ("genEle" + name + "HardProcess").c_str(),
            &genElectronSortedHardProcess[ID][0],
            ("genEle" + name + "ElePromptHardProcess[numEle" + name + "]/I")
                .c_str());
    }

    // Also handle z candidates
    nzcandidates[ID] = 0;
    zcandidatesvector[ID] = tempVecF;
}
// book muon branches:
void MakeTopologyNtupleMiniAOD::bookMuonBranches(const std::string& ID,
                                                 const std::string& name)
{
    // Initialise maps to prevent root panicing.
    std::vector<float> tempVecF(NMUONSMAX);
    std::vector<int> tempVecI(NMUONSMAX);

    muonSortedE[ID] = tempVecF;
    muonSortedEt[ID] = tempVecF;
    muonSortedPt[ID] = tempVecF;
    muonSortedEta[ID] = tempVecF;
    muonSortedTheta[ID] = tempVecF;
    muonSortedPhi[ID] = tempVecF;
    muonSortedPx[ID] = tempVecF;
    muonSortedPy[ID] = tempVecF;
    muonSortedPz[ID] = tempVecF;
    muonSortedCharge[ID] = tempVecI;
    muonSortedLooseCutId[ID] = tempVecI;
    muonSortedMediumCutId[ID] = tempVecI;
    muonSortedTightCutId[ID] = tempVecI;
    muonSortedPfIsoVeryLoose[ID] = tempVecI;
    muonSortedPfIsoLoose[ID] = tempVecI;
    muonSortedPfIsoMedium[ID] = tempVecI;
    muonSortedPfIsoTight[ID] = tempVecI;
    muonSortedPfIsoVeryTight[ID] = tempVecI;
    muonSortedTkIsoLoose[ID] = tempVecI;
    muonSortedTkIsoTight[ID] = tempVecI;
    muonSortedMvaLoose[ID] = tempVecI;
    muonSortedMvaMedium[ID] = tempVecI;
    muonSortedMvaTight[ID] = tempVecI;

    muonSortedGlobalID[ID] = tempVecF;
    muonSortedTrackID[ID] = tempVecF;

    muonValidFraction[ID] = tempVecF;
    muonChi2LocalPosition[ID] = tempVecF;
    muonTrkKick[ID] = tempVecF;
    muonSegmentCompatibility[ID] = tempVecF;

    muonSortedChi2[ID] = tempVecF;
    muonSortedD0[ID] = tempVecF;
    muonSortedDBBeamSpotCorrectedTrackD0[ID] = tempVecF;

    muonSortedDBInnerTrackD0[ID] = tempVecF;

    muonSortedBeamSpotCorrectedD0[ID] = tempVecF;
    muonSortedTrackNHits[ID] = tempVecI;
    muonSortedValidHitsGlobal[ID] = tempVecI;
    muonSortedNDOF[ID] = tempVecF; // n_d.o.f

    muonSortedVertX[ID] = tempVecF;
    muonSortedVertY[ID] = tempVecF;
    muonSortedVertZ[ID] = tempVecF;

    muonSortedTkLysWithMeasurements[ID] = tempVecI;
    muonSortedGlbTkNormChi2[ID] = tempVecF;
    muonSortedDBPV[ID] = tempVecF;
    muonSortedDZPV[ID] = tempVecF;
    muonSortedVldPixHits[ID] = tempVecI;
    muonSortedMatchedStations[ID] = tempVecI;

    muonSortedChargedHadronIso[ID] = tempVecF;
    muonSortedNeutralHadronIso[ID] = tempVecF;
    muonSortedPhotonIso[ID] = tempVecF;

    muonSortedTrackIso[ID] = tempVecF;
    muonSortedECalIso[ID] = tempVecF;
    muonSortedHCalIso[ID] = tempVecF;
    muonSortedComRelIso[ID] = tempVecF;
    muonSortedComRelIsodBeta[ID] = tempVecF;
    muonSortedIsPFMuon[ID] = tempVecI;
    muonSortedNumChambers[ID] = tempVecI;
    muonSortedNumMatches[ID] = tempVecI;

    genMuonSortedPt[ID] = tempVecF;
    genMuonSortedEt[ID] = tempVecF;
    genMuonSortedEta[ID] = tempVecF;
    genMuonSortedTheta[ID] = tempVecF;
    genMuonSortedPhi[ID] = tempVecF;
    genMuonSortedPx[ID] = tempVecF;
    genMuonSortedPy[ID] = tempVecF;
    genMuonSortedPz[ID] = tempVecF;
    genMuonSortedCharge[ID] = tempVecI;
    genMuonSortedPdgId[ID] = tempVecI;
    genMuonSortedMotherId[ID] = tempVecI;
    genMuonSortedPromptDecayed[ID] = tempVecI;
    genMuonSortedPromptFinalState[ID] = tempVecI;
    genMuonSortedHardProcess[ID] = tempVecI;

    mytree_->Branch(("numMuon" + name).c_str(),
                    &numMuo[ID],
                    ("numMuon" + name + "/I").c_str());
    std::string prefix{"muon" + name};
    mytree_->Branch((prefix + "E").c_str(),
                    &muonSortedE[ID][0],
                    (prefix + "E[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "ET").c_str(),
                    &muonSortedEt[ID][0],
                    (prefix + "ET[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Pt").c_str(),
                    &muonSortedPt[ID][0],
                    (prefix + "Pt[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "PX").c_str(),
                    &muonSortedPx[ID][0],
                    (prefix + "PX[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "PY").c_str(),
                    &muonSortedPy[ID][0],
                    (prefix + "PY[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "PZ").c_str(),
                    &muonSortedPz[ID][0],
                    (prefix + "PZ[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Phi").c_str(),
                    &muonSortedPhi[ID][0],
                    (prefix + "Phi[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Theta").c_str(),
                    &muonSortedTheta[ID][0],
                    (prefix + "Theta[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Eta").c_str(),
                    &muonSortedEta[ID][0],
                    (prefix + "Eta[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Charge").c_str(),
                    &muonSortedCharge[ID][0],
                    (prefix + "Charge[numMuon" + name + "]/I").c_str());

    mytree_->Branch((prefix + "LooseCutId").c_str(),
                    &muonSortedLooseCutId[ID][0],
                    (prefix + "LooseCutId[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "MediumCutId").c_str(),
                    &muonSortedMediumCutId[ID][0],
                    (prefix + "MediumCutId[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "TightCutId").c_str(),
                    &muonSortedTightCutId[ID][0],
                    (prefix + "TightCutId[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "PfIsoVeryLoose").c_str(),
                    &muonSortedPfIsoVeryLoose[ID][0],
                    (prefix + "PfIsoVeryLoose[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "PfIsoLoose").c_str(),
                    &muonSortedPfIsoLoose[ID][0],
                    (prefix + "PfIsoLoose[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "PfIsoMedium").c_str(),
                    &muonSortedPfIsoMedium[ID][0],
                    (prefix + "PfIsoMedium[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "PfIsoTight").c_str(),
                    &muonSortedPfIsoTight[ID][0],
                    (prefix + "PfIsoTight[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "PfIsoVeryTight").c_str(),
                    &muonSortedPfIsoVeryTight[ID][0],
                    (prefix + "PfIsoVeryTight[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "TkIsoLoose").c_str(),
                    &muonSortedTkIsoLoose[ID][0],
                    (prefix + "TkIsoLoose[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "TkIsoTight").c_str(),
                    &muonSortedTkIsoTight[ID][0],
                    (prefix + "TkIsoTight[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "MvaLoose").c_str(),
                    &muonSortedMvaLoose[ID][0],
                    (prefix + "MvaLoose[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "MvaMedium").c_str(),
                    &muonSortedMvaMedium[ID][0],
                    (prefix + "MvaMedium[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "MvaTight").c_str(),
                    &muonSortedMvaTight[ID][0],
                    (prefix + "MvaTight[numMuon" + name + "]/I").c_str());

    mytree_->Branch((prefix + "GlobalID").c_str(),
                    &muonSortedGlobalID[ID][0],
                    (prefix + "GlobalID[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrackID").c_str(),
                    &muonSortedTrackID[ID][0],
                    (prefix + "TrackID[numMuon" + name + "]/F").c_str());

    mytree_->Branch((prefix + "Chi2").c_str(),
                    &muonSortedChi2[ID][0],
                    (prefix + "Chi2[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "D0").c_str(),
                    &muonSortedD0[ID][0],
                    (prefix + "D0[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrackDBD0").c_str(),
                    &muonSortedDBBeamSpotCorrectedTrackD0[ID][0],
                    (prefix + "TrackDBD0[numMuon" + name + "]/F").c_str());

    mytree_->Branch((prefix + "DBInnerTrackD0").c_str(),
                    &muonSortedDBInnerTrackD0[ID][0],
                    (prefix + "DBInnerTrackD0[numMuon" + name + "]/F").c_str());

    mytree_->Branch(
        (prefix + "BeamSpotCorrectedD0").c_str(),
        &muonSortedBeamSpotCorrectedD0[ID][0],
        (prefix + "BeamSpotCorrectedD0[numMuon" + name + "]/F").c_str());

    mytree_->Branch((prefix + "TrackNHits").c_str(),
                    &muonSortedTrackNHits[ID][0],
                    (prefix + "TrackNHits[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "MuonNHits").c_str(),
                    &muonSortedValidHitsGlobal[ID][0],
                    (prefix + "MuonNHits[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "NDOF").c_str(),
                    &muonSortedNDOF[ID][0],
                    (prefix + "NDOF[numMuon" + name + "]/F").c_str());

    mytree_->Branch((prefix + "VertX").c_str(),
                    &muonSortedVertX[ID][0],
                    (prefix + "VertX[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "VertY").c_str(),
                    &muonSortedVertY[ID][0],
                    (prefix + "VertY[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "VertZ").c_str(),
                    &muonSortedVertZ[ID][0],
                    (prefix + "VertZ[numMuon" + name + "]/F").c_str());

    mytree_->Branch(
        (prefix + "TkLysWithMeasurements").c_str(),
        &muonSortedTkLysWithMeasurements[ID][0],
        (prefix + "TkLysWithMeasurements[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "GlbTkNormChi2").c_str(),
                    &muonSortedGlbTkNormChi2[ID][0],
                    (prefix + "GlbTkNormChi2[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "DBPV").c_str(),
                    &muonSortedDBPV[ID][0],
                    (prefix + "DBPV[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "DZPV").c_str(),
                    &muonSortedDZPV[ID][0],
                    (prefix + "DZPV[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "VldPixHits").c_str(),
                    &muonSortedVldPixHits[ID][0],
                    (prefix + "VldPixHits[numMuon" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "MatchedStations").c_str(),
        &muonSortedMatchedStations[ID][0],
        (prefix + "MatchedStations[numMuon" + name + "]/F").c_str());

    mytree_->Branch(
        (prefix + "ChargedHadronIso").c_str(),
        &muonSortedChargedHadronIso[ID][0],
        (prefix + "ChargedHadronIso[numMuon" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "NeutralHadronIso").c_str(),
        &muonSortedNeutralHadronIso[ID][0],
        (prefix + "NeutralHadronIso[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "PhotonIso").c_str(),
                    &muonSortedPhotonIso[ID][0],
                    (prefix + "PhotonIso[numMuon" + name + "]/F").c_str());

    mytree_->Branch((prefix + "TrackIso").c_str(),
                    &muonSortedTrackIso[ID][0],
                    (prefix + "TrackIso[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "EcalIso").c_str(),
                    &muonSortedECalIso[ID][0],
                    (prefix + "EcalIso[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "HcalIso").c_str(),
                    &muonSortedHCalIso[ID][0],
                    (prefix + "HcalIso[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "ComRelIso").c_str(),
                    &muonSortedComRelIso[ID][0],
                    (prefix + "ComRelIso[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "ComRelIsodBeta").c_str(),
                    &muonSortedComRelIsodBeta[ID][0],
                    (prefix + "ComRelIsodBeta[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "IsPFMuon").c_str(),
                    &muonSortedIsPFMuon[ID][0],
                    (prefix + "IsPFMuon[numMuon" + name + "]/I").c_str());

    mytree_->Branch((prefix + "NChambers").c_str(),
                    &muonSortedNumChambers[ID][0],
                    (prefix + "NChambers[numMuon" + name + "]/I").c_str());
    mytree_->Branch((prefix + "NMatches").c_str(),
                    &muonSortedNumMatches[ID][0],
                    (prefix + "NMatches[numMuon" + name + "]/I").c_str());

    mytree_->Branch((prefix + "ValidFraction").c_str(),
                    &muonValidFraction[ID][0],
                    (prefix + "ValidFraction[numMuon" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "Chi2LocalPosition").c_str(),
        &muonChi2LocalPosition[ID][0],
        (prefix + "Chi2LocalPosition[numMuon" + name + "]/F").c_str());
    mytree_->Branch((prefix + "TrkKick").c_str(),
                    &muonTrkKick[ID][0],
                    (prefix + "TrkKick[numMuon" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "SegmentCompatibility").c_str(),
        &muonSegmentCompatibility[ID][0],
        (prefix + "SegmentCompatibility[numMuon" + name + "]/F").c_str());

    if (runMCInfo_)
    {
        prefix = "genMuon" + name;
        mytree_->Branch((prefix + "PT").c_str(),
                        &genMuonSortedPt[ID][0],
                        (prefix + "PT[numMuon" + name + "]/F").c_str());
        mytree_->Branch((prefix + "ET").c_str(),
                        &genMuonSortedEt[ID][0],
                        (prefix + "ET[numMuon" + name + "]/F").c_str());
        mytree_->Branch((prefix + "PX").c_str(),
                        &genMuonSortedPx[ID][0],
                        (prefix + "PX[numMuon" + name + "]/F").c_str());
        mytree_->Branch((prefix + "PY").c_str(),
                        &genMuonSortedPy[ID][0],
                        (prefix + "PY[numMuon" + name + "]/F").c_str());
        mytree_->Branch((prefix + "PZ").c_str(),
                        &genMuonSortedPz[ID][0],
                        (prefix + "PZ[numMuon" + name + "]/F").c_str());
        mytree_->Branch((prefix + "Phi").c_str(),
                        &genMuonSortedPhi[ID][0],
                        (prefix + "Phi[numMuon" + name + "]/F").c_str());
        mytree_->Branch((prefix + "Theta").c_str(),
                        &genMuonSortedTheta[ID][0],
                        (prefix + "Theta[numMuon" + name + "]/F").c_str());
        mytree_->Branch((prefix + "Eta").c_str(),
                        &genMuonSortedEta[ID][0],
                        (prefix + "Eta[numMuon" + name + "]/F").c_str());
        mytree_->Branch((prefix + "Charge").c_str(),
                        &genMuonSortedCharge[ID][0],
                        (prefix + "Charge[numMuon" + name + "]/I").c_str());
        mytree_->Branch((prefix + "PdgId").c_str(),
                        &genMuonSortedPdgId[ID][0],
                        (prefix + "PdgId[numMuon" + name + "]/I").c_str());
        mytree_->Branch((prefix + "MotherId").c_str(),
                        &genMuonSortedMotherId[ID][0],
                        (prefix + "MotherId[numMuon" + name + "]/I").c_str());
        mytree_->Branch(
            (prefix + "PromptDecayed").c_str(),
            &genMuonSortedPromptDecayed[ID][0],
            (prefix + "PromptDecayed[numMuon" + name + "]/I").c_str());
        mytree_->Branch(
            (prefix + "PromptFinalState").c_str(),
            &genMuonSortedPromptFinalState[ID][0],
            (prefix + "PromptFinalState[numMuon" + name + "]/I").c_str());
        mytree_->Branch(
            (prefix + "HardProcess").c_str(),
            &genMuonSortedHardProcess[ID][0],
            (prefix + "HardProcess[numMuon" + name + "]/I").c_str());
    }
}

void MakeTopologyNtupleMiniAOD::bookMETBranches(const std::string& ID,
                                                const std::string& name)
{
    // std::cout << "bookMETBranches CHECK" << std::endl;
    metE[ID] = -1.0;
    metEt[ID] = -1.0;
    metEtRaw[ID] = -1.0;
    metPhi[ID] = -99999;
    metPt[ID] = -99999;
    metPx[ID] = -99999;
    metPy[ID] = -99999;
    metPz[ID] = -99999;
    metScalarEt[ID] = -1.0;
    metEtUncorrected[ID] = -1.0;
    metPhiUncorrected[ID] = -99999;
    metUnclusteredEnUp[ID] = -99999;
    metUnclusteredEnDown[ID] = -99999;
    genMetE[ID] = -1.0;
    genMetEt[ID] = -1.0;
    genMetPhi[ID] = -99999;
    genMetPt[ID] = -99999;
    genMetPx[ID] = -99999;
    genMetPy[ID] = -99999;
    genMetPz[ID] = -99999;

    std::string prefix{"met" + name};
    mytree_->Branch(
        (prefix + "E").c_str(), &metE[ID], (prefix + "E/D").c_str());
    mytree_->Branch(
        (prefix + "Et").c_str(), &metEt[ID], (prefix + "Et/D").c_str());
    mytree_->Branch((prefix + "EtRaw").c_str(),
                    &metEtRaw[ID],
                    (prefix + "EtRaw/D").c_str());
    mytree_->Branch(
        (prefix + "Phi").c_str(), &metPhi[ID], (prefix + "Phi/D").c_str());
    mytree_->Branch(
        (prefix + "Pt").c_str(), &metPt[ID], (prefix + "Pt/D").c_str());
    mytree_->Branch(
        (prefix + "Px").c_str(), &metPx[ID], (prefix + "Px/D").c_str());
    mytree_->Branch(
        (prefix + "Py").c_str(), &metPy[ID], (prefix + "Py/D").c_str());
    mytree_->Branch(
        (prefix + "Pz").c_str(), &metPz[ID], (prefix + "Pz/D").c_str());
    mytree_->Branch((prefix + "ScalarEt").c_str(),
                    &metScalarEt[ID],
                    (prefix + "ScalarEt/F").c_str());
    mytree_->Branch((prefix + "EtUncorrected").c_str(),
                    &metEtUncorrected[ID],
                    (prefix + "EtUncorrected/F").c_str());
    mytree_->Branch((prefix + "PhiUncorrected").c_str(),
                    &metPhiUncorrected[ID],
                    (prefix + "PhiUncorrected/F").c_str());
    mytree_->Branch((prefix + "UnclusteredEnUp").c_str(),
                    &metUnclusteredEnUp[ID],
                    (prefix + "UnclusteredEnUp/F").c_str());
    mytree_->Branch((prefix + "UnclusteredEnDown").c_str(),
                    &metUnclusteredEnDown[ID],
                    (prefix + "UnclusteredEnDown/F").c_str());

    prefix = "genMet" + name;
    if (runMCInfo_)
    {
        mytree_->Branch(
            (prefix + "E").c_str(), &genMetE, (prefix + "E/F").c_str());
        mytree_->Branch(
            (prefix + "Et").c_str(), &genMetEt, (prefix + "Et/F").c_str());
        mytree_->Branch(
            (prefix + "Phi").c_str(), &genMetPhi, (prefix + "Phi/F").c_str());
        mytree_->Branch(
            (prefix + "Pt").c_str(), &genMetPt, (prefix + "Pt/F").c_str());
        mytree_->Branch(
            (prefix + "Px").c_str(), &genMetPx, (prefix + "Px/F").c_str());
        mytree_->Branch(
            (prefix + "Py").c_str(), &genMetPy, (prefix + "Py/F").c_str());
        mytree_->Branch(
            (prefix + "Pz").c_str(), &genMetPz, (prefix + "Pz/F").c_str());
    }
}
// book MC branches:
void MakeTopologyNtupleMiniAOD::bookMCBranches()
{
    // std::cout << "bookMCBranches CHECK" << std::endl;
    // mytree_->Branch("nT", &nT, "nT/I");
    //
    // mytree_->Branch("nThadronic", &nThadronic, "nThadronic/I");
    // mytree_->Branch("T_hadronicMCTruthE",
    //                 T_hadronicMCTruthE,
    //                 "T_hadronicMCTruthE[nThadronic]/F");
    // mytree_->Branch("T_hadronicMCTruthEt",
    //                 T_hadronicMCTruthEt,
    //                 "T_hadronicMCTruthEt[nThadronic]/F");
    // mytree_->Branch("T_hadronicMCTruthPx",
    //                 T_hadronicMCTruthPx,
    //                 "T_hadronicMCTruthPx[nThadronic]/F");
    // mytree_->Branch("T_hadronicMCTruthPy",
    //                 T_hadronicMCTruthPy,
    //                 "T_hadronicMCTruthPy[nThadronic]/F");
    // mytree_->Branch("T_hadronicMCTruthPz",
    //                 T_hadronicMCTruthPz,
    //                 "T_hadronicMCTruthPz[nThadronic]/F");
    // mytree_->Branch("T_hadronicMCMotherIndex",
    //                 T_hadronicMotherIndex,
    //                 "T_hadronicMCMotherIndex[nThadronic]/I");
    //
    // mytree_->Branch("nTleptonic", &nTleptonic, "nTleptonic/I");
    // mytree_->Branch("T_leptonicMCTruthE",
    //                 T_leptonicMCTruthE,
    //                 "T_leptonicMCTruthE[nTleptonic]/F");
    // mytree_->Branch("T_leptonicMCTruthEt",
    //                 T_leptonicMCTruthEt,
    //                 "T_leptonicMCTruthEt[nTleptonic]/F");
    // mytree_->Branch("T_leptonicMCTruthPx",
    //                 T_leptonicMCTruthPx,
    //                 "T_leptonicMCTruthPx[nTleptonic]/F");
    // mytree_->Branch("T_leptonicMCTruthPy",
    //                 T_leptonicMCTruthPy,
    //                 "T_leptonicMCTruthPy[nTleptonic]/F");
    // mytree_->Branch("T_leptonicMCTruthPz",
    //                 T_leptonicMCTruthPz,
    //                 "T_leptonicMCTruthPz[nTleptonic]/F");
    // mytree_->Branch("T_leptonicMCMotherIndex",
    //                 T_leptonicMotherIndex,
    //                 "T_leptonicMCMotherIndex[nTleptonic]/I");
    //
    // mytree_->Branch("nb", &nb, "nb/I");
    // mytree_->Branch("bMCTruthE", bMCTruthE, "bMCTruthE[nb]/F");
    // mytree_->Branch("bMCTruthEt", bMCTruthEt, "bMCTruthEt[nb]/F");
    // mytree_->Branch("bMCTruthPx", bMCTruthPx, "bMCTruthPx[nb]/F");
    // mytree_->Branch("bMCTruthPy", bMCTruthPy, "bMCTruthPy[nb]/F");
    // mytree_->Branch("bMCTruthPz", bMCTruthPz, "bMCTruthPz[nb]/F");
    // mytree_->Branch("bMCTruthMother", bMCTruthMother,
    // "bMCTruthMother[nb]/I");
    //
    // mytree_->Branch("nWhadronic", &nWhadronic, "nWhadronic/I");
    // mytree_->Branch("W_hadronicMCTruthE",
    //                 W_hadronicMCTruthE,
    //                 "W_hadronicMCTruthE[nWhadronic]/F");
    // mytree_->Branch("W_hadronicMCTruthEt",
    //                 W_hadronicMCTruthEt,
    //                 "W_hadronicMCTruthEt[nWhadronic]/F");
    // mytree_->Branch("W_hadronicMCTruthPx",
    //                 W_hadronicMCTruthPx,
    //                 "W_hadronicMCTruthPx[nWhadronic]/F");
    // mytree_->Branch("W_hadronicMCTruthPy",
    //                 W_hadronicMCTruthPy,
    //                 "W_hadronicMCTruthPy[nWhadronic]/F");
    // mytree_->Branch("W_hadronicMCTruthPz",
    //                 W_hadronicMCTruthPz,
    //                 "W_hadronicMCTruthPz[nWhadronic]/F");
    // mytree_->Branch("W_hadronicMCTruthPID",
    //                 W_hadronicMCTruthPID,
    //                 "W_hadronicMCTruthPID[nWhadronic]/I");
    // mytree_->Branch("W_hadronicMCTruthMother",
    //                 W_hadronicMCTruthMother,
    //                 "W_hadronicMCTruthMother[nWhadronic]/I");
    //
    // mytree_->Branch("nWleptonic", &nWleptonic, "nWleptonic/I");
    // mytree_->Branch("W_leptonicMCTruthE",
    //                 W_leptonicMCTruthE,
    //                 "W_leptonicMCTruthE[nWleptonic]/F");
    // mytree_->Branch("W_leptonicMCTruthEt",
    //                 W_leptonicMCTruthEt,
    //                 "W_leptonicMCTruthEt[nWleptonic]/F");
    // mytree_->Branch("W_leptonicMCTruthPx",
    //                 W_leptonicMCTruthPx,
    //                 "W_leptonicMCTruthPx[nWleptonic]/F");
    // mytree_->Branch("W_leptonicMCTruthPy",
    //                 W_leptonicMCTruthPy,
    //                 "W_leptonicMCTruthPy[nWleptonic]/F");
    // mytree_->Branch("W_leptonicMCTruthPz",
    //                 W_leptonicMCTruthPz,
    //                 "W_leptonicMCTruthPz[nWleptonic]/F");
    // mytree_->Branch("W_leptonicMCTruthPID",
    //                 W_leptonicMCTruthPID,
    //                 "W_leptonicMCTruthPID[nWleptonic]/I");
    // mytree_->Branch("W_leptonicMCTruthMother",
    //                 W_leptonicMCTruthMother,
    //                 "W_leptonicMCTruthMother[nWleptonic]/I");

    mytree_->Branch("isElePlusJets", &isElePlusJets, "isElePlusJets/I");
    // mytree_->Branch("VQQBosonAbsId", &VQQBosonAbsId, "VQQBosonAbsId/I");

    mytree_->Branch("genPDFScale", &genPDFScale, "genPDFScale/F");
    mytree_->Branch("genPDFx1", &genPDFx1, "genPDFx1/F");
    mytree_->Branch("genPDFx2", &genPDFx2, "genPDFx2/F");
    mytree_->Branch("genPDFf1", &genPDFf1, "genPDFf1/I");
    mytree_->Branch("genPDFf2", &genPDFf2, "genPDFf2/I");

    if (runPDFUncertainties_)
    {
        mytree_->Branch(
            "genCTEQ66_Weight", genCTEQ66_Weight, "genCTEQ66_Weight[44]/F");
        mytree_->Branch("genMRST2006nnlo_Weight",
                        genMRST2006nnlo_Weight,
                        "genMRST2006nnlo_Weight[31]/F");
    }

    // Book in the ttbar top pt reweighting information.
    mytree_->Branch("topPtReweight", &topPtReweight, "topPtReweight/D");
}

// book jet branches:
void MakeTopologyNtupleMiniAOD::bookPFJetBranches(const std::string& ID,
                                                  const std::string& name)
{
    // std::cout << "bookPFJetBranches CHECK" << std::endl;
    // Initialise the maps so ROOT wont panic
    std::vector<float> tempVecF(NJETSMAX);
    std::vector<int> tempVecI(NJETSMAX);

    jetSortedNeutralMultiplicity[ID] = tempVecI;
    jetSortedChargedMultiplicity[ID] = tempVecI;

    jetSortedMuEnergy[ID] = tempVecF;
    jetSortedMuEnergyFraction[ID] = tempVecF;
    jetSortedNeutralHadEnergy[ID] = tempVecF;
    jetSortedNeutralEmEnergy[ID] = tempVecF;
    jetSortedChargedHadronEnergyFraction[ID] = tempVecF;
    jetSortedNeutralHadronEnergyFraction[ID] = tempVecF;
    jetSortedChargedEmEnergyFraction[ID] = tempVecF;
    jetSortedNeutralEmEnergyFraction[ID] = tempVecF;
    jetSortedMuonFraction[ID] = tempVecF;
    jetSortedChargedHadronEnergyFractionCorr[ID] = tempVecF;
    jetSortedNeutralHadronEnergyFractionCorr[ID] = tempVecF;
    jetSortedChargedEmEnergyFractionCorr[ID] = tempVecF;
    jetSortedNeutralEmEnergyFractionCorr[ID] = tempVecF;
    jetSortedMuonFractionCorr[ID] = tempVecF;

    std::string prefix{"jet" + name};
    mytree_->Branch((prefix + "MuEnergy").c_str(),
                    &jetSortedMuEnergy[ID][0],
                    (prefix + "MuEnergy[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "MuEnergyFraction").c_str(),
        &jetSortedMuEnergyFraction[ID][0],
        (prefix + "MuEnergyFraction[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "NeutralHadEnergy").c_str(),
        &jetSortedNeutralHadEnergy[ID][0],
        (prefix + "NeutralHadEnergy[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "NeutralEmEnergy").c_str(),
                    &jetSortedNeutralEmEnergy[ID][0],
                    (prefix + "NeutralEmEnergy[numJet" + name + "]/F").c_str());

    mytree_->Branch(
        (prefix + "ChargedHadronEnergyFraction").c_str(),
        &jetSortedChargedHadronEnergyFraction[ID][0],
        (prefix + "ChargedHadronEnergyFraction[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "NeutralHadronEnergyFraction").c_str(),
        &jetSortedNeutralHadronEnergyFraction[ID][0],
        (prefix + "NeutralHadronEnergyFraction[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "ChargedEmEnergyFraction").c_str(),
        &jetSortedChargedEmEnergyFraction[ID][0],
        (prefix + "ChargedEmEnergyFraction[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "NeutralEmEnergyFraction").c_str(),
        &jetSortedNeutralEmEnergyFraction[ID][0],
        (prefix + "NeutralEmEnergyFraction[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "MuonFraction").c_str(),
                    &jetSortedMuonFraction[ID][0],
                    (prefix + "MuonFraction[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "ChargedHadronEnergyFractionCorr").c_str(),
        &jetSortedChargedHadronEnergyFractionCorr[ID][0],
        (prefix + "ChargedHadronEnergyFractionCorr[numJet" + name + "]/F")
            .c_str());
    mytree_->Branch(
        (prefix + "NeutralHadronEnergyFractionCorr").c_str(),
        &jetSortedNeutralHadronEnergyFractionCorr[ID][0],
        (prefix + "NeutralHadronEnergyFractionCorr[numJet" + name + "]/F")
            .c_str());
    mytree_->Branch(
        (prefix + "ChargedEmEnergyFractionCorr").c_str(),
        &jetSortedChargedEmEnergyFractionCorr[ID][0],
        (prefix + "ChargedEmEnergyFractionCorr[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "NeutralEmEnergyFractionCorr").c_str(),
        &jetSortedNeutralEmEnergyFractionCorr[ID][0],
        (prefix + "NeutralEmEnergyFractionCorr[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "MuonFractionCorr").c_str(),
        &jetSortedMuonFractionCorr[ID][0],
        (prefix + "MuonFractionCorr[numJet" + name + "]/F").c_str());

    mytree_->Branch(
        (prefix + "NeutralMultiplicity").c_str(),
        &jetSortedNeutralMultiplicity[ID][0],
        (prefix + "NeutralMultiplicity[numJet" + name + "]/I").c_str());
    mytree_->Branch(
        (prefix + "ChargedMultiplicity").c_str(),
        &jetSortedChargedMultiplicity[ID][0],
        (prefix + "ChargedMultiplicity[numJet" + name + "]/I").c_str());
}

void MakeTopologyNtupleMiniAOD::bookJetBranches(const std::string& ID,
                                                const std::string& name)
{
    // std::cout << "bookJetBranches CHECK" << std::endl;
    // Initialise the maps so ROOT wont panic
    std::vector<float> tempVecF(NJETSMAX);
    std::vector<int> tempVecI(NJETSMAX);
    std::vector<double> tempVecD(NJETSMAX);

    numJet[ID] = -1;

    jetSortedNtracksInJet[ID] = tempVecI;
    jetSortedPID[ID] = tempVecI;
    jetSortedNConstituents[ID] = tempVecI;
    genJetSortedPID[ID] = tempVecI;

    jetSortedE[ID] = tempVecD;
    jetSortedEt[ID] = tempVecD;
    jetSortedPt[ID] = tempVecD;
    jetSortedPtRaw[ID] = tempVecD;
    jetSortedUnCorEt[ID] = tempVecD;
    jetSortedUnCorPt[ID] = tempVecD;
    jetSortedEta[ID] = tempVecD;
    jetSortedTheta[ID] = tempVecD;
    jetSortedPhi[ID] = tempVecD;
    jetSortedPx[ID] = tempVecD;
    jetSortedPy[ID] = tempVecD;
    jetSortedPz[ID] = tempVecD;
    // jetSortedID[ID] = tempVecI;
    jetSortedClosestLepton[ID] = tempVecD;
    jetSortedJetCharge[ID] = tempVecF;
    jetSortedfHPD[ID] = tempVecF;
    jetSortedCorrFactor[ID] = tempVecF;
    jetSortedCorrResidual[ID] = tempVecF;
    jetSortedL2L3ResErr[ID] = tempVecF;
    jetSortedCorrErrLow[ID] = tempVecF;
    jetSortedCorrErrHi[ID] = tempVecF;
    jetSortedN90Hits[ID] = tempVecF;
    jetSortedBtagSoftMuonPtRel[ID] = tempVecF;
    jetSortedBtagSoftMuonQuality[ID] = tempVecF;
    jetSortedTriggered[ID] = tempVecF;
    jetSortedSVX[ID] = tempVecF;
    jetSortedSVY[ID] = tempVecF;
    jetSortedSVZ[ID] = tempVecF;
    jetSortedSVDX[ID] = tempVecF;
    jetSortedSVDY[ID] = tempVecF;
    jetSortedSVDZ[ID] = tempVecF;

    for (size_t iBtag{0}; iBtag < bTagList_.size(); iBtag++)
    {
        bTagRes[bTagList_[iBtag]][ID] = tempVecF;
    }

    genJetSortedEt[ID] = tempVecF;
    genJetSortedPt[ID] = tempVecF;
    genJetSortedEta[ID] = tempVecF;
    genJetSortedTheta[ID] = tempVecF;
    genJetSortedPhi[ID] = tempVecF;
    genJetSortedPx[ID] = tempVecF;
    genJetSortedPy[ID] = tempVecF;
    genJetSortedPz[ID] = tempVecF;
    // genJetSortedID[ID] = tempVecI;
    genJetSortedClosestB[ID] = tempVecF;
    genJetSortedClosestC[ID] = tempVecF;

    std::string prefix{"jet" + name};
    mytree_->Branch(("numJet" + name).c_str(),
                    &numJet[ID],
                    ("numJet" + name + "/I").c_str());

    mytree_->Branch((prefix + "E").c_str(),
                    &jetSortedE[ID][0],
                    (prefix + "E[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "Et").c_str(),
                    &jetSortedEt[ID][0],
                    (prefix + "Et[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "Pt").c_str(),
                    &jetSortedPt[ID][0],
                    (prefix + "Pt[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "PtRaw").c_str(),
                    &jetSortedPtRaw[ID][0],
                    (prefix + "PtRaw[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "UnCorEt").c_str(),
                    &jetSortedUnCorEt[ID][0],
                    (prefix + "UnCorEt[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "UnCorPt").c_str(),
                    &jetSortedUnCorPt[ID][0],
                    (prefix + "UnCorPt[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "Eta").c_str(),
                    &jetSortedEta[ID][0],
                    (prefix + "Eta[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "Theta").c_str(),
                    &jetSortedTheta[ID][0],
                    (prefix + "Theta[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "Phi").c_str(),
                    &jetSortedPhi[ID][0],
                    (prefix + "Phi[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "Px").c_str(),
                    &jetSortedPx[ID][0],
                    (prefix + "Px[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "Py").c_str(),
                    &jetSortedPy[ID][0],
                    (prefix + "Py[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "Pz").c_str(),
                    &jetSortedPz[ID][0],
                    (prefix + "Pz[numJet" + name + "]/D").c_str());
    // mytree_->Branch((prefix + "ID").c_str(),
    //                 &jetSortedID[ID][0],
    //                 (prefix + "ID[numJet" + name + "]/I").c_str());
    mytree_->Branch((prefix + "dRClosestLepton").c_str(),
                    &jetSortedClosestLepton[ID][0],
                    (prefix + "ClosestLepton[numJet" + name + "]/D").c_str());
    mytree_->Branch((prefix + "NtracksInJet").c_str(),
                    &jetSortedNtracksInJet[ID][0],
                    (prefix + "NtracksInJet[numJet" + name + "]/I").c_str());
    mytree_->Branch((prefix + "JetCharge").c_str(),
                    &jetSortedJetCharge[ID][0],
                    (prefix + "JetCharge[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "fHPD").c_str(),
                    &jetSortedfHPD[ID][0],
                    (prefix + "fHPD[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "BtagSoftMuonPtRel").c_str(),
        &jetSortedBtagSoftMuonPtRel[ID][0],
        (prefix + "BtagSoftMuonPtRel[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "BtagSoftMuonQuality").c_str(),
        &jetSortedBtagSoftMuonQuality[ID][0],
        (prefix + "BtagSoftMuonQuality[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "CorrFactor").c_str(),
                    &jetSortedCorrFactor[ID][0],
                    (prefix + "CorrFactor[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "CorrResidual").c_str(),
                    &jetSortedCorrResidual[ID][0],
                    (prefix + "CorrResidual[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "L2L3ResErr").c_str(),
                    &jetSortedL2L3ResErr[ID][0],
                    (prefix + "L2L3ResErr[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "CorrErrLow").c_str(),
                    &jetSortedCorrErrLow[ID][0],
                    (prefix + "CorrErrLow[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "CorrErrHi").c_str(),
                    &jetSortedCorrErrHi[ID][0],
                    (prefix + "CorrErrHi[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "N90Hits").c_str(),
                    &jetSortedN90Hits[ID][0],
                    (prefix + "N90Hits[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "Triggered").c_str(),
                    &jetSortedTriggered[ID][0],
                    (prefix + "Triggered[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SVX").c_str(),
                    &jetSortedSVX[ID][0],
                    (prefix + "SVX[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SVY").c_str(),
                    &jetSortedSVY[ID][0],
                    (prefix + "SVY[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SVZ").c_str(),
                    &jetSortedSVZ[ID][0],
                    (prefix + "SVZ[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SVDX").c_str(),
                    &jetSortedSVDX[ID][0],
                    (prefix + "SVDX[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SVDY").c_str(),
                    &jetSortedSVDY[ID][0],
                    (prefix + "SVDY[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "SVDZ").c_str(),
                    &jetSortedSVDZ[ID][0],
                    (prefix + "SVDZ[numJet" + name + "]/F").c_str());
    mytree_->Branch((prefix + "NConstituents").c_str(),
                    &jetSortedNConstituents[ID][0],
                    (prefix + "NConstituents[numJet" + name + "]/I").c_str());

    for (size_t iBtag{0}; iBtag < bTagList_.size(); iBtag++)
    {
        std::cout << "Booking bTag disc branch: " << bTagList_[iBtag]
                  << std::endl;
        mytree_->Branch(
            (prefix + bTagList_[iBtag]).c_str(),
            &bTagRes[bTagList_[iBtag]][ID][0],
            (prefix + bTagList_[iBtag] + "[numJet" + name + "]/F").c_str());
    }

    // generator information
    mytree_->Branch((prefix + "PID").c_str(),
                    &jetSortedPID[ID][0],
                    (prefix + "PID[numJet" + name + "]/I").c_str());
    mytree_->Branch(
        (prefix + "ClosestBPartonDeltaR").c_str(),
        &genJetSortedClosestB[ID][0],
        (prefix + "ClosestBPartonDeltaR[numJet" + name + "]/F").c_str());
    mytree_->Branch(
        (prefix + "ClosestCPartonDeltaR").c_str(),
        &genJetSortedClosestC[ID][0],
        (prefix + "ClosestCPartonDeltaR[numJet" + name + "]/F").c_str());

    prefix = "genJet" + name;
    if (runMCInfo_)
    {
        mytree_->Branch((prefix + "ET").c_str(),
                        &genJetSortedEt[ID][0],
                        (prefix + "ET[numJet" + name + "]/F").c_str());
        mytree_->Branch((prefix + "PT").c_str(),
                        &genJetSortedPt[ID][0],
                        (prefix + "PT[numJet" + name + "]/F").c_str());
        mytree_->Branch((prefix + "PX").c_str(),
                        &genJetSortedPx[ID][0],
                        (prefix + "PX[numJet" + name + "]/F").c_str());
        mytree_->Branch((prefix + "PY").c_str(),
                        &genJetSortedPy[ID][0],
                        (prefix + "PY[numJet" + name + "]/F").c_str());
        mytree_->Branch((prefix + "PZ").c_str(),
                        &genJetSortedPz[ID][0],
                        (prefix + "PZ[numJet" + name + "]/F").c_str());
        // mytree_->Branch((prefix + "ID").c_str(),
        //                 &genJetSortedID[ID][0],
        //                 (prefix + "ID[numJet" + name + "]/I").c_str());
        mytree_->Branch((prefix + "Phi").c_str(),
                        &genJetSortedPhi[ID][0],
                        (prefix + "Phi[numJet" + name + "]/F").c_str());
        mytree_->Branch((prefix + "Theta").c_str(),
                        &genJetSortedTheta[ID][0],
                        (prefix + "Theta[numJet" + name + "]/F").c_str());
        mytree_->Branch((prefix + "Eta").c_str(),
                        &genJetSortedEta[ID][0],
                        (prefix + "Eta[numJet" + name + "]/F").c_str());
        mytree_->Branch((prefix + "PID").c_str(),
                        &genJetSortedPID[ID][0],
                        (prefix + "PID[numJet" + name + "]/I").c_str());
    }

    mytree_->Branch("fixedGridRhoFastjetAll",
                    &fixedGridRhoFastjetAll[ID],
                    "fixedGridRhoFastjetAll]/F");

    bookBIDInfoBranches(ID, name);
}

void MakeTopologyNtupleMiniAOD::bookBIDInfoBranches(const std::string& /*ID*/,
                                                    const std::string& /*name*/)
{
    // std::cout << "bookBIDInfoHistos CHECK" << std::endl;
    // for all parameterizations:
    btaggingparamtype_["BTAGBEFF"] = PerformanceResult::BTAGBEFF;
    btaggingparamtype_["BTAGBERR"] = PerformanceResult::BTAGBERR;
    btaggingparamtype_["BTAGCEFF"] = PerformanceResult::BTAGCEFF;
    btaggingparamtype_["BTAGCERR"] = PerformanceResult::BTAGCERR;
    btaggingparamtype_["BTAGLEFF"] = PerformanceResult::BTAGLEFF;
    btaggingparamtype_["BTAGLERR"] = PerformanceResult::BTAGLERR;
    btaggingparamtype_["BTAGNBEFF"] = PerformanceResult::BTAGNBEFF;
    btaggingparamtype_["BTAGNBERR"] = PerformanceResult::BTAGNBERR;
    btaggingparamtype_["BTAGBEFFCORR"] = PerformanceResult::BTAGBEFFCORR;
    btaggingparamtype_["BTAGBERRCORR"] = PerformanceResult::BTAGBERRCORR;
    btaggingparamtype_["BTAGCEFFCORR"] = PerformanceResult::BTAGCEFFCORR;
    btaggingparamtype_["BTAGCERRCORR"] = PerformanceResult::BTAGCERRCORR;
    btaggingparamtype_["BTAGLEFFCORR"] = PerformanceResult::BTAGLEFFCORR;
    btaggingparamtype_["BTAGLERRCORR"] = PerformanceResult::BTAGLERRCORR;
    btaggingparamtype_["BTAGNBEFFCORR"] = PerformanceResult::BTAGNBEFFCORR;
    btaggingparamtype_["BTAGNBERRCORR"] = PerformanceResult::BTAGNBERRCORR;
    btaggingparamtype_["BTAGNBERRCORR"] = PerformanceResult::BTAGNBERRCORR;
    btaggingparamtype_["MUEFF"] = PerformanceResult::MUEFF;
    btaggingparamtype_["MUERR"] = PerformanceResult::MUERR;
    btaggingparamtype_["MUFAKE"] = PerformanceResult::MUFAKE;
    btaggingparamtype_["MUEFAKE"] = PerformanceResult::MUEFAKE;
}

void MakeTopologyNtupleMiniAOD::bookGeneralTracksBranches()
{
    // std::cout << "bookGeneralTrackBranches CHECK" << std::endl;
    mytree_->Branch(
        "numGeneralTracks", &numGeneralTracks, "numGeneralTracks/I");
    mytree_->Branch("generalTracksPt",
                    generalTracksPt,
                    "generalTracksPt[numGeneralTracks]/F");
    mytree_->Branch("generalTracksEta",
                    generalTracksEta,
                    "generalTracksEta[numGeneralTracks]/F");
    mytree_->Branch("generalTracksTheta",
                    generalTracksTheta,
                    "generalTracksTheta[numGeneralTracks]/F");
    mytree_->Branch("generalTracksBeamSpotCorrectedD0",
                    generalTracksBeamSpotCorrectedD0,
                    "generalTracksBeamSpotCorrectedD0[numGeneralTracks]/F");
    mytree_->Branch("generalTracksPhi",
                    generalTracksPhi,
                    "generalTracksPhi[numGeneralTracks]/F");
    mytree_->Branch("generalTracksCharge",
                    generalTracksCharge,
                    "generalTracksCharge[numGeneralTracks]/I");
}

// ------------ method called once each job just before starting event loop
// ------------
void
    // MakeTopologyNtupleMiniAOD::beginJob(const edm::EventSetup&
    // #<{(|unused|)}>#)
    MakeTopologyNtupleMiniAOD::beginJob()
{
    if (runPDFUncertainties_)
    {
        // Setup the PDFs
        // CTEQ 6.6
        initPDFSet(0, "cteq66", LHAPDF::LHGRID, 0);
        initPDFSet(1, "MRST2006nnlo", LHAPDF::LHGRID, 0);
    }
}

// ------------ method called once each job just after ending the event loop
// ------------
void MakeTopologyNtupleMiniAOD::endJob()
{
    std::cout << "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+="
              << std::endl;
    std::cout << "\n\nJOB Summary:" << std::endl;
    std::cout << "number of events processed: "
              << histocontainer_["eventcount"]->GetEntries() << std::endl;
    std::cout << "number of events added to tree: " << mytree_->GetEntries()
              << std::endl;
    std::cout << "\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+="
              << std::endl;
}
void MakeTopologyNtupleMiniAOD::fillTriggerData(const edm::Event& iEvent)
{
    // std::cout << "fillTriggerData CHECK" << std::endl;
    for (int& TriggerBit : TriggerBits)
    { // size hard-coded in MakeTopologyNtuple.h!!!
        TriggerBit = -999;
    }

    if (!check_triggers_)
    {
        std::cout << "not checking triggers! " << std::endl;
        return;
    }
    edm::Handle<edm::TriggerResults> hltResults;
    iEvent.getByToken(trigToken_, hltResults);

    if (hltResults.product()->wasrun())
    {
        const edm::TriggerNames& triggerNames{iEvent.triggerNames(*hltResults)};

        // HLTBits_Size = hltResults.product()->size();
        nTriggerBits = 0;

        hltnames_ = triggerNames.triggerNames();

        for (int itrig{0}; itrig < (int)hltnames_.size(); ++itrig)
        {
            const bool accept{hltResults->accept(itrig)};
            // if (histocontainer_["eventcount"]->GetBinContent(0.0) < 2)
            // {
            //     std::cout << "TRIGGER BIT:" << itrig
            //               << ", NAME:" << hltnames_[itrig]
            //               << " FIRED:" << accept << std::endl;
            // }
            int trigbit{0};
            if (accept)
            {
                trigbit = 1;
            }
            if (!hltResults->wasrun(itrig))
                trigbit = -1;
            if (hltResults->error(itrig))
                trigbit = -2;

            for (size_t iTrigList{0}; iTrigList < triggerList_.size();
                 iTrigList++)
            {
                if (triggerList_[iTrigList] == hltnames_[itrig])
                {
                    // if (mytree_->GetEntries() < 1)
                    // {
                    //     std::cout << "found 'standard' trigger bit "
                    //               << triggerList_[iTrigList] << std::endl;
                    // }
                    triggerRes[iTrigList] = trigbit;
                }
            }
        }
    } // hltResults.wasRun()

    edm::Handle<edm::TriggerResults> metFilterResults;
    iEvent.getByToken(metFilterToken_, metFilterResults);

    if (metFilterResults.product()->wasrun())
    {
        const edm::TriggerNames& metFilterNames{
            iEvent.triggerNames(*metFilterResults)};
        // HLTBits_Size = metFilterResults.product()->size();

        metFilterNames_ = metFilterNames.triggerNames();
        for (int iFilter{0}; iFilter < (int)metFilterNames_.size(); ++iFilter)
        {
            const bool accept(metFilterResults->accept(iFilter));
            // if (histocontainer_["eventcount"]->GetBinContent(0.0) < 2)
            // {
            //     if (metFilterNames_[iFilter] == "Flag_noBadMuons")
            //     {
            //         std::cout << "TRIGGER BIT:" << iFilter
            //                   << ", NAME:" << metFilterNames_[iFilter]
            //                   << " FIRED:" << accept << std::endl;
            //     }
            // }
            int filterbit{0};
            if (accept)
            {
                filterbit = 1;
            }
            if (!metFilterResults->wasrun(iFilter))
                filterbit = -1;
            if (metFilterResults->error(iFilter))
                filterbit = -2;
            for (size_t iMetFilterList{0};
                 iMetFilterList < metFilterList_.size();
                 iMetFilterList++)
            {
                if (metFilterList_[iMetFilterList] == metFilterNames_[iFilter])
                {
                    metFilterRes[iMetFilterList] = filterbit;
                }
            }
        }
    } // metFilterResults.wasRun()

    // collect the fake trigger information:
    if (fakeTrigLabelList_.size() > 0)
    {
        edm::Handle<edm::TriggerResults> fakeResults;
        // gettnig the default TriggerResults, which is (by definition) the
        // latest one produced.
        iEvent.getByLabel(edm::InputTag("TriggerResults"), fakeResults);

        const edm::TriggerNames& triggerNamesFake{
            iEvent.triggerNames(*fakeResults)};
        for (size_t ii{0}; ii < fakeTrigLabelList_.size(); ++ii)
        {
            // std::cout << "looking for path " << fakeTrigLabelList_[ii]
            //           << std::endl;
            size_t pathIndex{
                triggerNamesFake.triggerIndex(fakeTrigLabelList_[ii])};
            HLT_fakeTriggerValues[ii] = -99;
            // if (pathIndex >= 0 && pathIndex < triggerNamesFake.size())
            if (pathIndex < triggerNamesFake.size())
            {
                // std::cout << "found it! " << std::endl;
                int trigbit{0};
                if (fakeResults->accept(pathIndex))
                    trigbit = 1;
                if (!fakeResults->wasrun(pathIndex))
                    trigbit = -1;
                if (fakeResults->error(pathIndex))
                    trigbit = -2;
                HLT_fakeTriggerValues[ii] = trigbit;
                if (mytree_->GetEntries() <= 2)
                    std::cout << "fake trigger bit: " << fakeTrigLabelList_[ii]
                              << " TRIGGERED: " << HLT_fakeTriggerValues[ii]
                              << std::endl;
            }
        }
    }
}

/////////////
// identification functions!
/////////////

bool MakeTopologyNtupleMiniAOD::photonConversionVeto(
    const pat::Electron& electron, float& dist, float& Dcot)
{
    // return true if object is good (so not a conversion)
    // std::cout << "photonConversionVeto CHECK" << std::endl;

    float local_dcot{};
    float local_dist{};
    float TrackWithinConeRho[200]{}; // curvature of tracks within the cone
    float TrackWithinConeRx[200]{}; // circule coordinate formed by the track in
                                    // the phi plane
    float TrackWithinConeRy[200]{};
    float TrackWithinConeCharge[200]{}; // charges of tracks
    float TrackWithinConeTheta[200]{}; // thetas of tracks

    int numTrackWithinCone{0};
    bool CONV{false}; // use to tag electron if it comes from photon conversion

    // calculate the deltaR between the track and the isolated electron, if
    // deltaR<0.3, this track is close to the electron, this track is saved as
    // the candidate to calculate the photon conversion,

    // loop over all the generalTrack collections
    for (int nGeneral{0}; nGeneral < numGeneralTracks; nGeneral++)
    {
        // eta and phi of both generalTrack and electron are the angles measured
        // in vertex
        float DR{reco::deltaR(generalTracksEta[nGeneral],
                              generalTracksPhi[nGeneral],
                              electron.eta(),
                              electron.phi())};

        if (DR > dREleGeneralTrackMatch_)
        {
            continue;
        }

        numTrackWithinCone++;
        // as the arrays are fixed to 200 break loop if more than that:
        if (numTrackWithinCone > 200)
        {
            break;
        }

        /*       C*B*e
            rho= _________

                     Pt    , where C=-0.003, B=3.8T, e is charge of the track in
           unit of positron, Pt the transverse momentum of the track
        */

        TrackWithinConeRho[numTrackWithinCone - 1] =
            correctFactor_ * magneticField_ * generalTracksCharge[nGeneral]
            / generalTracksPt[nGeneral];
        /* rx=(1/rho-d0)sin(phi), ry=-(1/rho-d0)cos(phi)*/
        TrackWithinConeRx[numTrackWithinCone - 1] =
            (1 / TrackWithinConeRho[numTrackWithinCone - 1]
             - generalTracksBeamSpotCorrectedD0[nGeneral])
            * sin(generalTracksPhi[nGeneral]);
        TrackWithinConeRy[numTrackWithinCone - 1] =
            -1.
            * (1 / TrackWithinConeRho[numTrackWithinCone - 1]
               - generalTracksBeamSpotCorrectedD0[nGeneral])
            * cos(generalTracksPhi[nGeneral]);
        TrackWithinConeTheta[numTrackWithinCone - 1] =
            generalTracksTheta[nGeneral];
        TrackWithinConeCharge[numTrackWithinCone - 1] =
            generalTracksCharge[nGeneral];
    }

    if (numTrackWithinCone > 0)
    {
        for (int nTrack{0}; nTrack < numTrackWithinCone; nTrack++)
        {
            // loop over generalTracks collection again
            for (int i{0}; i < numGeneralTracks; i++)
            {
                // try to find the second track with opposite charege, do not
                // need to match this track with the electron
                if (TrackWithinConeCharge[nTrack] == generalTracksCharge[i])
                {
                    continue;
                }
                double SecondTrackRho{correctFactor_ * magneticField_
                                      * generalTracksCharge[i]
                                      / generalTracksPt[i]};
                double SecondTrackRx{
                    (1. / SecondTrackRho - generalTracksBeamSpotCorrectedD0[i])
                    * sin(generalTracksPhi[i])};
                double SecondTrackRy{-1.
                                     * (1. / SecondTrackRho
                                        - generalTracksBeamSpotCorrectedD0[i])
                                     * cos(generalTracksPhi[i])};
                float SecondTrackTheta{generalTracksTheta[i]};

                /*  dist=|vector(r1)-vector(r2)|-|1/rho1|-|1/rho2|         */

                local_dist =
                    sqrt((TrackWithinConeRx[nTrack] - SecondTrackRx)
                             * (TrackWithinConeRx[nTrack] - SecondTrackRx)
                         + (TrackWithinConeRy[nTrack] - SecondTrackRy)
                               * (TrackWithinConeRy[nTrack] - SecondTrackRy))
                    - 1 / std::abs(TrackWithinConeRho[nTrack])
                    - 1 / std::abs(SecondTrackRho);

                /*  Delta Cot(theta)=1/tan(theta1)-1/tan(theta2)     */

                local_dcot = 1 / tan(TrackWithinConeTheta[nTrack])
                             - 1 / tan(SecondTrackTheta);
                if (std::abs(local_dist) < std::abs(dist)
                    && std::abs(local_dcot) < std::abs(Dcot))
                {
                    dist = local_dist;
                    Dcot = local_dcot;
                }
                if (std::abs(local_dist) <= maxDist_
                    && std::abs(local_dcot) < maxDcot_)
                {
                    CONV = true;
                } // tag electron from photon conversion, immediately leave loop
                  // to save time.
            }
        }
    }
    return (!CONV);
}

// define this as a plug-in
DEFINE_FWK_MODULE(MakeTopologyNtupleMiniAOD);
