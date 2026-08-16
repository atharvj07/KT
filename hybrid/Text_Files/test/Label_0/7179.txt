#include <bits/stdc++.h>
using namespace std;
int main() {
  string s, d, f, g;
  cin >> s >> d >> f;
  g = s + d;
  sort(g.begin(), g.end());
  sort(f.begin(), f.end());
  for (int i = 0; i < max(g.size(), f.size()); i++) {
    if (g[i] != f[i]) {
      cout << "NO";
      return 0;
    }
  }
  cout << "YES";
  return 0;
}
