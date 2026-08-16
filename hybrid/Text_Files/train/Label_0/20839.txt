#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long t;
  cin >> t;
  while (t--) {
    long long i, j, k, l = 0, m, n, divisor = 0;
    cin >> n;
    vector<long long> v(n), x;
    for (i = 0; i < n; i++) cin >> v[i];
    sort(v.begin(), v.end());
    k = v[n - 1] * v[0];
    for (i = 2; i * i <= k; i++) {
      if (i * i == k)
        x.push_back(i);
      else if (k % i == 0)
        x.push_back(i), x.push_back(k / i);
    }
    sort(x.begin(), x.end());
    if (v == x)
      cout << k << endl;
    else
      cout << -1 << endl;
  }
  return 0;
}
