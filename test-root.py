from __future__ import print_function
import ROOT

print("This is a test of PyROOT")
h = ROOT.TH1D("h", "", 10, 0, 10)
h.FillRandom("gaus", 100)
print(h.GetMean())