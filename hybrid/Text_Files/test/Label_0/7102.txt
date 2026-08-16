#include <bits/stdc++.h>
using namespace std;
vector<vector<long long> > zero(int r, int c) {
  return vector<vector<long long> >(r, vector<long long>(c, 0));
}
vector<vector<long long> > I(int n) {
  vector<vector<long long> > ret = zero(n, n);
  for (int i = 0; i < n; ++i) ret[i][i] = 1;
  return ret;
}
vector<vector<long long> > mult(const vector<vector<long long> >& a,
                                const vector<vector<long long> >& b) {
  vector<vector<long long> > ret = zero(a.size(), b[0].size());
  for (int i = 0; i < a.size(); ++i) {
    for (int k = 0; k < a[0].size(); ++k) {
      if (!a[i][k]) continue;
      for (int j = 0; j < b[0].size(); ++j) {
        ret[i][j] += (a[i][k] * b[k][j]) % 1000000007;
        ret[i][j] %= 1000000007;
      }
    }
  }
  return ret;
}
vector<vector<long long> > pow(const vector<vector<long long> >& a,
                               long long p) {
  if (!p) return I(a.size());
  if (p == 1ll) return a;
  vector<vector<long long> > x = mult(a, a);
  vector<vector<long long> > xx = pow(x, p / 2ll);
  if (p & 1ll) return mult(a, xx);
  return xx;
}
int main() {
  long long n;
  scanf("%lld", &n);
  vector<vector<long long> > init = zero(2, 1);
  init[0][0] = 1;
  vector<vector<long long> > trans = zero(2, 2);
  trans[0][0] = 3;
  trans[0][1] = 1;
  trans[1][0] = 1;
  trans[1][1] = 3;
  trans = pow(trans, n);
  init = mult(trans, init);
  printf("%lld\n", init[0][0]);
}
