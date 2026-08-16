#include <bits/stdc++.h>
using namespace std;
const long double eps = 1e-9;
const long double pi = acos(-1.0);
int gcd(int a, int b) { return (b == 0) ? a : gcd(b, a % b); }
int xabs(int a) { return a > 0 ? a : -a; }
int getCost(int l, int w, int h, int rl, int rw, int cost) {
  int cnt = 1;
  int p = 2 * (l + w);
  int crl = rl;
  int pok = 0;
  while (true) {
    if (crl >= h)
      crl -= h;
    else {
      ++cnt;
      crl = rl;
      crl -= h;
    }
    pok += rw;
    if (pok >= p) break;
  }
  return cnt * cost;
}
int main() {
  int n;
  cin >> n;
  vector<int> l(n), w(n), h(n);
  for (int i = 0; i < n; ++i) cin >> l[i] >> w[i] >> h[i];
  int m;
  cin >> m;
  vector<int> rl(m), rw(m), cost(m);
  for (int i = 0; i < m; ++i) cin >> rl[i] >> rw[i] >> cost[i];
  int sum = 0;
  for (int i = 0; i < n; ++i) {
    int msum = -1;
    for (int j = 0; j < m; ++j) {
      if (rl[j] >= h[i]) {
        int s = getCost(l[i], w[i], h[i], rl[j], rw[j], cost[j]);
        if (msum == -1 || s < msum) msum = s;
      }
    }
    sum += msum;
  }
  cout << sum << endl;
  return 0;
}
