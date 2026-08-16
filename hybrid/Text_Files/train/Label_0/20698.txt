#include <bits/stdc++.h>
using namespace std;
const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-9;
const int INF = (1 << 31) - 1;
const long long LLINF = (1LL << 63) - 1;
typedef const vector<vector<int> >& GraphRef;
typedef const vector<vector<pair<int, int> > >& WeightedGraphRef;
char buf[1 << 20];
int main() {
  int n;
  cin >> n;
  scanf("%s", buf);
  string a(buf);
  scanf("%s", buf);
  string b(buf);
  vector<vector<int> > posA(26);
  vector<vector<int> > posB(26);
  for (int i = 0; i < n; ++i) {
    posA[a[i] - 'A'].push_back(i);
    posB[b[i] - 'A'].push_back(i);
  }
  double res = 0;
  double sum = 0;
  for (int i = 1; i <= n; ++i) sum += 1LL * i * i;
  for (int c = 0; c < 26; ++c) {
    vector<int> x = posA[c];
    vector<int> y = posB[c];
    if (x.empty() || y.empty()) continue;
    ;
    vector<long long> sx(x.size());
    for (int i = 0; i < sx.size(); ++i) {
      if (i) sx[i] += sx[i - 1];
      sx[i] += x[i] + 1;
    }
    vector<long long> se(x.size());
    se.push_back(0);
    for (int i = x.size() - 1; i >= 0; --i) {
      if (i + 1 < se.size()) se[i] += se[i + 1];
      se[i] += n - x[i];
    }
    for (int i = 0; i < y.size(); ++i) {
      int f = distance(x.begin(), upper_bound((x).begin(), (x).end(), y[i]));
      if (f - 1 >= 0) res += 1LL * (n - y[i]) * sx[f - 1];
      res += 1LL * (1 + y[i]) * se[f];
    }
  }
  printf("%lf\n", 1.0 * res / sum);
  return 0;
}
