#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k, q;
  cin >> n >> k >> q;
  vector<int> T(n);
  for (int i = 0; i < n; ++i) cin >> T[i];
  set<pair<int, int> > S;
  int type, id;
  for (int i = 0; i < q; ++i) {
    cin >> type >> id;
    id--;
    if (type == 1) {
      S.insert(make_pair(-T[id], id));
      if (S.size() > k) S.erase(--S.end());
    } else {
      if (S.find(make_pair(-T[id], id)) != S.end())
        cout << "YES\n";
      else
        cout << "NO\n";
    }
  }
  return 0;
}
