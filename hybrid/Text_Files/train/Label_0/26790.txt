#include <bits/stdc++.h>
using namespace std;
int n, m, k;
string str;
int main() {
  while (cin >> n >> m >> k) {
    vector<vector<int> > a(n, vector<int>(m)), b(n, vector<int>(m)),
        c(n, vector<int>(m));
    for (int i = 0; i < (n); ++i) {
      cin >> str;
      for (int j = 0; j < (m); ++j) {
        scanf("%d%d%d", &a[i][j], &b[i][j], &c[i][j]);
      }
    }
    int ans = 0;
    for (int f = 0; f < (n); ++f)
      for (int t = 0; t < (n); ++t)
        if (f != t) {
          vector<pair<int, int> > idx(m);
          for (int j = 0; j < (m); ++j) {
            idx[j].first = b[t][j] - a[f][j];
            idx[j].second = j;
          }
          sort((idx).rbegin(), (idx).rend());
          int now = 0;
          int nK = k;
          for (int j = 0; j < (m); ++j) {
            int val = idx[j].first;
            int i = idx[j].second;
            if (val < 0) {
              break;
            }
            int count = min(c[f][i], nK);
            nK -= count;
            now += val * count;
          }
          ans = max(ans, now);
        }
    cout << ans << endl;
  }
  return 0;
}
