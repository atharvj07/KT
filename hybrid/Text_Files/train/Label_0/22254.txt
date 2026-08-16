#include <bits/stdc++.h>
using namespace std;
const int N = 110;
int n, a[N];
long long ans, k;
bool check(long long d, long long k) {
  long long sum = 0;
  for (int i = 1; i <= n; i++) sum += (a[i] + d - 1) / d;
  return sum <= k;
}
int main() {
  cin >> n >> k;
  for (int i = 1; i <= n; i++) cin >> a[i], k += a[i];
  for (long long l = 1, r; l <= k; l = r + 1) {
    r = k / (k / l);
    if (check(r, k / r)) ans = max(ans, r);
  }
  cout << ans << endl;
  return 0;
}
