#include <bits/stdc++.h>
using namespace std;
const long long MAXN = 1e5 + 20;
long long n;
long long vec[MAXN];
long long p[MAXN];
long long ans[MAXN];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n;
  for (long long i = 0; i < n; i++) cin >> vec[i];
  sort(vec, vec + n, greater<long long>());
  for (long long i = n - 1; i >= 0; i--) p[i] = (p[i + 1] + vec[i]);
  for (long long i = 1; i < n; i++) {
    ans[i] = p[1];
    long long s = i;
    for (long long j = i + 1; j < n; s *= i, j += s) ans[i] += p[j];
  }
  long long q;
  cin >> q;
  while (q--) {
    long long k;
    cin >> k;
    k = min(k, n - 1);
    cout << ans[k] << " ";
  }
  cout << endl;
  return 0;
}
