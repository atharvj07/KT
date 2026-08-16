#include <bits/stdc++.h>
using namespace std;
const long long N = 1e9 + 7;
void solve() {
  long long n;
  cin >> n;
  long long arr[n];
  for (long long i = 0; i < n; i++) cin >> arr[i];
  map<long long, long long> ff;
  map<long long, long long> f;
  long long ans = 0;
  for (long long i = 0; i < n; i++) {
    if (ff[f[arr[i]]] > 0) ff[f[arr[i]]]--;
    if (ff[f[arr[i]]] == 0) ff.erase(f[arr[i]]);
    f[arr[i]]++;
    ff[f[arr[i]]]++;
    if (ff.size() == 2) {
      auto itr = ff.begin();
      long long a1 = itr->first;
      long long a2 = itr->second;
      itr++;
      long long b1 = itr->first;
      long long b2 = itr->second;
      if (a2 == 1) {
        if (a1 - b1 == 1 || a1 == 1) {
          ans = max(ans, i + 1);
        }
      }
      if (b2 == 1) {
        if (b1 - a1 == 1 || b1 == 1) {
          ans = max(ans, i + 1);
        }
      }
    }
    if (ff.size() == 1) {
      auto itr = ff.begin();
      long long x = itr->first;
      if (x == 1)
        ans = max(ans, i + 1);
      else if (itr->second == 1)
        ans = max(ans, i + 1);
    }
  }
  cout << ans;
}
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  long long T = 1;
  while (T--) solve();
}
