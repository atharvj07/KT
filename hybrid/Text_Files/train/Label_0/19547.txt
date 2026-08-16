#include <bits/stdc++.h>
using namespace std;
signed main() {
  int n;
  cin >> n;
  vector<string> v(n);
  map<string, int> matc;
  for (int i = 0; i < n; i++) {
    cin >> v[i];
    set<string> subss;
    for (int j = 0; j < 9; j++) {
      for (int k = 0; k + j < 9; k++) {
        subss.insert(v[i].substr(k, j + 1));
      }
    }
    for (const auto& it : subss) {
      matc[it]++;
    }
  }
  for (int i = 0; i < n; i++) {
    string ans = "";
    for (int j = 0; j < 9; j++) {
      for (int k = 0; k + j < 9; k++) {
        string subs = v[i].substr(k, j + 1);
        if (matc[subs] == 1) {
          ans = subs;
          break;
        }
      }
      if (ans != "") break;
    }
    cout << ans << "\n";
  }
  return 0;
}
