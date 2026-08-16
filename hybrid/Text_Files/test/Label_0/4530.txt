#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, temp;
  vector<int> P;
  vector<int> N;
  vector<int> Z;
  cin >> n;
  while (n--) {
    cin >> temp;
    if (temp > 0)
      P.push_back(temp);
    else if (temp < 0)
      N.push_back(temp);
    else
      Z.push_back(temp);
  }
  if (P.size() == 0) {
    P.push_back(N[0]);
    P.push_back(N[1]);
    N.erase(N.begin() + 0);
    N.erase(N.begin() + 0);
  }
  if (N.size() % 2 == 0) {
    Z.push_back(N[0]);
    N.erase(N.begin() + 0);
  }
  cout << N.size();
  for (int i = 0; i < N.size(); i++) {
    cout << " " << N[i];
  }
  cout << '\n' << P.size();
  for (int i = 0; i < P.size(); i++) {
    cout << " " << P[i];
  }
  cout << '\n' << Z.size();
  for (int i = 0; i < Z.size(); i++) {
    cout << " " << Z[i];
  }
}
