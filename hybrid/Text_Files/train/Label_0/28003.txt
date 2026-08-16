#include <bits/stdc++.h>
using namespace std;
const double eps = 1e-3;
const int inf = (int)1e9;
const int MAX_N = 100 + 10;
const int REM = inf + 7;
set<string> N, M;
int main() {
  int n, m;
  double k;
  cin >> n >> m >> k;
  vector<pair<string, int> > ans;
  for (int i = 0; i < n; i++) {
    string cur;
    int num;
    cin >> cur >> num;
    double t = num * k + eps;
    num = (int)t;
    if (num >= 100) {
      N.insert(cur);
      ans.push_back(pair<string, int>(cur, num));
    }
  }
  for (int i = 0; i < m; i++) {
    string cur;
    cin >> cur;
    if (N.find(cur) == N.end()) ans.push_back(pair<string, int>(cur, 0));
  }
  sort(ans.begin(), ans.end());
  cout << ((int)ans.size()) << endl;
  for (int i = 0; i < ((int)ans.size()); i++) {
    cout << ans[i].first << " " << ans[i].second << endl;
  }
  return 0;
}
