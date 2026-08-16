#include <bits/stdc++.h>
using namespace std;
const int N = 100100;
int n, pos[N], f[N], m, sz[N];
set<int> mp1[N];
bool cmp(int fi, int se) { return sz[fi] > sz[se]; }
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> m;
  int sum = 0;
  for (int i = 1; i <= n; i++) {
    cin >> sz[i];
    sum += sz[i];
    for (int j = 1; j <= sz[i]; j++) {
      int x;
      cin >> x;
      mp1[i].insert(x);
    }
  }
  for (int i = 1; i <= n; i++) {
    pos[i] = i;
    f[i] = sum / n;
    if (i <= sum % n) ++f[i];
  }
  sort(pos + 1, pos + n + 1, cmp);
  int l = 1, r = n;
  vector<pair<pair<int, int>, int> > ansvec;
  while (l < r) {
    while (1) {
      if (sz[pos[l]] == f[l]) {
        ++l;
        break;
      }
      if (sz[pos[r]] == f[r]) {
        --r;
        break;
      }
      for (auto it = mp1[pos[l]].begin(); it != mp1[pos[l]].end(); it++) {
        int x = *it;
        if (mp1[pos[r]].find(x) != mp1[pos[r]].end()) continue;
        ++it;
        --sz[pos[l]];
        ++sz[pos[r]];
        mp1[pos[l]].erase(x);
        mp1[pos[r]].insert(x);
        ansvec.push_back({{pos[l], pos[r]}, x});
        if (sz[pos[l]] == f[l] || sz[pos[r]] == f[r]) break;
      }
    }
  }
  cout << ansvec.size() << "\n";
  for (auto it : ansvec)
    cout << it.first.first << ' ' << it.first.second << ' ' << it.second
         << "\n";
}
