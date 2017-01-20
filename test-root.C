{
  cout << "This is a test of ROOT" << endl;
  TH1D * h = new TH1D("h", "", 10, 0, 10);
  h->FillRandom("gaus", 100);
  cout << h->GetMean() << endl;
  return 0; // cos ROOT returns 1 by default
}