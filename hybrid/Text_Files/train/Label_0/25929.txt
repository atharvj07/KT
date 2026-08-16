#include <bits/stdc++.h>
using namespace std;
const int N = 500005;
unordered_set<int> cntX[N], cntY[N];
vector<int> Gx[N], Gy[N];
int n;
int x[N], y[N];
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int(i) = (1); (i) <= (n); ++(i)) {
    cin >> x[i] >> y[i];
    Gx[x[i]].push_back(y[i]);
    Gy[y[i]].push_back(x[i]);
    cntX[x[i]].insert(y[i]);
    cntY[y[i]].insert(x[i]);
  }
  long long ans = 0;
  for (int(i) = (1); (i) <= (n); ++(i)) {
    if (Gx[x[i]].size() < sqrt(n)) {
      for (auto ny : Gx[x[i]]) {
        int d = y[i] - ny;
        if (d > 0 && x[i] >= d) {
          ans += (cntX[x[i] - d].count(y[i]) && cntX[x[i] - d].count(y[i] - d));
        }
      }
    } else {
      for (auto nx : Gy[y[i]]) {
        int d = x[i] - nx;
        if (d > 0 && y[i] >= d) {
          ans += (cntY[y[i] - d].count(x[i]) && cntY[y[i] - d].count(x[i] - d));
        }
      }
    }
  }
  cout << ans;
}
