#include "TFile.h"
#include "TCanvas.h"
#include "TH3F.h"
#include "TH2F.h"
#include "TH1F.h"
#include "TAxis.h"

void show_dose(){
  TFile *f = new TFile("../output/output-Dose.root");
  TH3F *h3 = (TH3F*) f->Get("histo");
  TH1F *hz = (TH1F*) h3->ProjectionZ();
  TH2F *hxy = (TH2F*) h3->Project3D("xy");

  TCanvas *c = new TCanvas("c","dose histograms", 1000, 800);
  c->Divide(3,2);
  // plot total dose profile in z and xy radiography (integrated)
  c->cd(1);
  hz->DrawClone();
  c->cd(2);
  hxy->DrawClone("colz");

  // find the bin number corresponding to the entrance, midpoint, end of the waterbox
  // the dose corresponding to the z position is given by the integral of the histogram (any, hz or hxy)
  // at the bin (ie. the bin content). The integrated dose goes from the entrance bin to the z you need
  Int_t entranceBin = 1;
  Int_t exitBin = hz->GetXaxis()->GetLast();
  Int_t binAtZero = hz->GetXaxis()->FindBin(0.);
  
  cout << "evaluated dose at the entrance of the waterbox " << hz->Integral(entranceBin, entranceBin) << endl;
  cout << "evaluated dose up to the midplane of the waterbox " << hz->Integral(entranceBin, binAtZero) << endl;
  cout << "evaluated dose up to the end of the waterbox " << hz->Integral(entranceBin, exitBin) << endl;

  // plots of the doses released at each section
  // entrance
  h3->GetZaxis()->SetRange(entranceBin, entranceBin+1);
  TH2F *hxyEntrance = (TH2F*) h3->Project3D("xy");
  c->cd(4);
  hxyEntrance->DrawClone("colz");
  // midplane
  h3->GetZaxis()->SetRange(binAtZero, binAtZero);
  TH2F *hxyMidPlane = (TH2F*) h3->Project3D("xy");
  c->cd(5);
  hxyMidPlane->DrawClone("colz");
  // mid plane, integrated dose from entrance to midplane
  h3->GetZaxis()->SetRange(entranceBin, binAtZero);
  TH2F *hxyIntegrated = (TH2F*) h3->Project3D("xy");
  c->cd(6);
  hxyIntegrated->DrawClone("colz");
  
  c->SaveAs("dosesPlots.png");
}
