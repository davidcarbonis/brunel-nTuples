// -*- C++ -*-
//
// Package:    TopTools
// Class:      TopologyWorker
//
/**\class TopologyWorker TopologyWorker.cc
 TopQuarkAnalysis/TopTools/interface/TopologyWorker.h

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
     This class contains the topological methods as used in D0 (all hadronic)
 analyses.
*/
#ifndef __FREYATOOLSTOPOLOGYWORKER__
#define __FREYATOOLSTOPOLOGYWORKER__

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "TClass.h"
#include "TF1.h"
#include "TLorentzVector.h"
#include "TMath.h"
#include "TMatrixD.h"
#include "TRandom.h"
#include "TString.h"

#include <vector>

namespace cu_ejetmet
{
    class TopologyWorker
    {
        public:
        TopologyWorker()
        {
        }
        TopologyWorker(bool boost);
        virtual ~TopologyWorker()
        {
        }

        void clear(void)
        {
            m_np = 0;
            m_np2 = 0;
            return;
        }

        void setPartList(std::vector<TLorentzVector>& e1,
                         std::vector<TLorentzVector>& e2);
        void setVerbose(bool loud)
        {
            m_verbose = loud;
            return;
        }

        void setThMomPower(double tp);
        double getThMomPower();
        void setFast(int nf);
        int getFast();

        TVector3 thrustAxis();
        TVector3 majorAxis();
        TVector3 minorAxis();

        TVector3 thrust();
        // thrust :: Corresponding thrust, major, and minor value.

        double oblateness();
        double get_sphericity();
        double get_aplanarity();
        double get_h10();
        double get_h20();
        double get_h30();
        double get_h40();
        double get_h50();
        double get_h60();

        void planes_sphe(double& pnorm, double& p2, double& p3);
        void planes_sphe_wei(double& pnorm, double& p2, double& p3);
        void planes_thrust(double& pnorm, double& p2, double& p3);
        void sumangles(float& sdeta, float& sdr);

        double get_ht()
        {
            return m_ht;
        }
        double get_ht3()
        {
            return m_ht3;
        }
        double get_et0()
        {
            return m_et0;
        }
        double get_sqrts()
        {
            return m_sqrts;
        }
        double get_njetW()
        {
            return m_njetsweighed;
        }
        double get_et56()
        {
            return m_et56;
        }
        double get_centrality()
        {
            return m_centrality;
        }

        private:
        bool m_verbose{false};
        void getetaphi(
            double px, double py, double pz, double& eta, double& phi);
        double ulAngle(double x, double y);
        double sign(double a, double b);
        void ludbrb(TMatrix* mom,
                    double the,
                    double phi,
                    double bx,
                    double by,
                    double bz);

        int iPow(int man, int exp);

        double m_dSphMomPower{2.0};
        // PARU(41): Power of momentum dependence in sphericity finder.

        double m_dDeltaThPower{0};
        // PARU(42): Power of momentum dependence in thrust finder.

        int m_iFast{4};
        // MSTU(44): # of initial fastest particles choosen to start search.

        double m_dConv{0.0001};
        // PARU(48): Convergence criteria for axis maximization.

        int m_iGood{2};
        // MSTU(45): # different starting configurations that must
        // converge before axis is accepted as correct.

        TMatrix m_dAxes;
        // data: results
        // m_dAxes[1] is the Thrust axis.
        // m_dAxes[2] is the Major axis.
        // m_dAxes[3] is the Minor axis.

        TVector3 m_ThrustAxis;
        TVector3 m_MajorAxis;
        TVector3 m_MinorAxis;
        TVector3 m_Thrust;

        TRandom m_random;

        TMatrix m_mom;
        TMatrix m_mom2;

        double m_dThrust[4]{};
        double m_dOblateness{};
        int m_np{-1};
        int m_np2{-1};
        bool m_sanda_called{false};
        bool m_fowo_called{false};
        bool m_boost{};
        bool m_sumangles_called{false};
        double m_sph{-1};
        double m_apl{-1};
        double m_h10{-1};
        double m_h20{-1};
        double m_h30{-1};
        double m_h40{-1};
        double m_h50{};
        double m_h60{};
        double m_ht{0};
        double m_ht3{0};
        double m_et0{0};
        double m_sqrts{0};
        double m_njetsweighed{};
        double m_et56{0};
        double m_centrality{};

        void sanda();
        void fowo();
        static int m_maxpart;

        void CalcWmul();
        void CalcSqrts();
        void CalcHTstuff();
        double CalcPt(int i)
        {
            return sqrt(pow(m_mom(i, 1), 2) + pow(m_mom(i, 2), 2));
        }
        double CalcPt2(int i)
        {
            return sqrt(pow(m_mom2(i, 1), 2) + pow(m_mom2(i, 2), 2));
        }
        double CalcEta(int i)
        {
            double eta, phi;
            getetaphi(m_mom(i, 1), m_mom(i, 2), m_mom(i, 3), eta, phi);
            return eta;
        }
        double CalcEta2(int i)
        {
            double eta, phi;
            getetaphi(m_mom2(i, 1), m_mom2(i, 2), m_mom2(i, 3), eta, phi);
            return eta;
        }
    };

    class LessThan
    {
        public:
        // retrieve tru info MC stuff
        bool operator()(const TLorentzVector& tl1,
                        const TLorentzVector& tl2) const
        {
            return tl2.Pt() < tl1.Pt();
        }
    };
} // namespace cu_ejetmet

#endif
