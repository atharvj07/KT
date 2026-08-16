#include <bits/stdc++.h>
using namespace std;
const long long maxn = 5e5 + 7;
const long long mod = 1e9 + 7;
const long long INF = 1e9 + 7;
const long long mlog = 20;
const long long SQ = 400;
long long a[maxn];
int32_t main() {
  ios_base::sync_with_stdio(false), cin.tie(), cout.tie();
  ;
  long long t = 1;
  cin >> t;
  while (t--) {
    long long n, k;
    cin >> n >> k;
    bool ok = (n == 1);
    bool present = false;
    for (long long i = 0; i < n; i++) {
      cin >> a[i];
      ok = ok || (a[i] >= k &&
                  ((i >= 1 && a[i - 1] >= k) || (i >= 2 && a[i - 2] >= k)));
      present = present || (a[i] == k);
    }
    if (ok && present)
      cout << "yes\n";
    else
      cout << "no\n";
  }
  return 0;
}
