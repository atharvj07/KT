#include <bits/stdc++.h>
using namespace std;
const int MOD = 998244353;
const int N = 200005;
const double PI = 4 * atan(1);
const double eps = 1e-7;
const long long oo = 1e10;
const int K = 205;
long long t;
vector<long long> v[3];
vector<long long> vv;
long long si[3];
long long x;
long long ind1, ind2, ind3;
long long val1, val2, val3;
long long getval(long long val1, long long val2, long long val3) {
  return (val1 - val2) * (val1 - val2) + (val1 - val3) * (val1 - val3) +
         (val2 - val3) * (val2 - val3);
}
long long sear(long long ind, long long val, long long ty) {
  if (ty == 0) {
    if (v[ind][0] > val) return -1;
    int pos = lower_bound(v[ind].begin(), v[ind].end(), val) - v[ind].begin();
    if (pos == si[ind]) {
      return v[ind][pos - 1];
    }
    if (v[ind][pos] == val) return val;
    return v[ind][pos - 1];
  }
  if (v[ind][si[ind] - 1] < val) return -1;
  int pos = upper_bound(v[ind].begin(), v[ind].end(), val) - v[ind].begin();
  pos--;
  if (pos < 0) pos++;
  if (v[ind][pos] >= val) return v[ind][pos];
  pos++;
  if (pos == si[ind]) return v[ind][pos - 1];
  return v[ind][pos];
}
int main() {
  scanf("%lld", &t);
  while (t--) {
    scanf("%lld %lld %lld", si + 0, si + 1, si + 2);
    vv.clear();
    vv.push_back(0);
    vv.push_back(1);
    vv.push_back(2);
    long long ans = 4e18;
    for (int i = 0; i < 3; i++) {
      v[i].clear();
      for (int j = 0; j < si[i]; j++) {
        scanf("%lld", &x);
        v[i].push_back(x);
      }
      sort((v[i]).begin(), (v[i]).end());
    }
    do {
      ind1 = vv[0];
      ind2 = vv[1];
      ind3 = vv[2];
      for (int i = 0; i < si[ind1]; i++) {
        val1 = v[ind1][i];
        val2 = sear(ind2, val1, 0);
        if (val2 == -1) continue;
        val3 = sear(ind3, val1, 1);
        if (val3 == -1) continue;
        ans = (ans < getval(val1, val2, val3) ? ans : getval(val1, val2, val3));
      }
    } while (next_permutation((vv).begin(), (vv).end()));
    printf("%lld\n", ans);
  }
  return 0;
}
