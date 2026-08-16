#include <bits/stdc++.h>
using namespace std;
int inf = 1e9;
const int N = 1e5 + 10;
int a[N], n;
multiset<int> suff, pref;
long long sumsuff, sumpref;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
    suff.insert(a[i]);
    sumsuff += a[i];
  }
  for (int i = 1; i <= n; i++) {
    sumpref += a[i];
    sumsuff -= a[i];
    suff.erase(suff.find(a[i]));
    pref.insert(a[i]);
    long long diff = abs(sumsuff - sumpref);
    if (diff % 2 == 0) {
      if (!diff) return cout << "YES", 0;
      diff /= 2;
      if (sumsuff > sumpref) {
        auto x = suff.lower_bound(diff);
        if (x != suff.end() && *x == diff) return cout << "YES\n", 0;
      } else {
        auto x = pref.lower_bound(diff);
        if (x != pref.end() && *x == diff) return cout << "YES\n", 0;
      }
    }
  }
  cout << "NO";
}
