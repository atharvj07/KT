#include <bits/stdc++.h>
using namespace std;
int main() {
  int h1, a1, c1, h2, a2;
  cin >> h1 >> a1 >> c1 >> h2 >> a2;
  vector<bool> z;
  while (h2 > 0) {
    if (h1 > a2) {
      z.push_back(0);
      h2 -= a1;
    } else if (h1 <= a2) {
      if (h2 <= a1) {
        z.push_back(0);
        h2 -= a1;
      } else {
        z.push_back(1);
        h1 += c1;
      }
    }
    h1 = h1 - a2;
  }
  cout << z.size() << '\n';
  for (int i = 0; i < z.size(); i++) {
    if (z[i] == 0) {
      cout << "STRIKE\n";
    } else
      cout << "HEAL\n";
  }
  return 0;
}
