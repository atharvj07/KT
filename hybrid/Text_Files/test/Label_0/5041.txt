#include <bits/stdc++.h>
using namespace std;
long long n, m, r;
set<long long> np, vs;
int main() {
  ios_base::sync_with_stdio(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    long long t;
    cin >> t;
    np.insert(t);
  }
  for (int i = 0; i < m; i++) {
    long long t;
    cin >> t;
    vs.insert(t);
  }
  for (set<long long>::iterator it = np.begin(); it != np.end(); it++) {
    if (vs.find(*it) != vs.end()) continue;
    long long t = *it;
    set<long long>::iterator it1;
    if (*vs.rbegin() > t && *vs.begin() < t)
      it1 = vs.upper_bound(t);
    else if (t > *vs.rbegin()) {
      it1 = vs.end();
      it1--;
    } else {
      r = max(r, abs(t - *vs.begin()));
      continue;
    }
    long long v1 = *it1;
    it1--;
    long long v2 = *it1;
    r = max(r, min(abs(t - v1), abs(t - v2)));
  }
  cout << r;
  return 0;
}
