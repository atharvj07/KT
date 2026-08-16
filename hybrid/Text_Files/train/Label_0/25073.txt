#include <bits/stdc++.h>
using namespace std;
long long maxLL(long long a, long long b) { return (a > b ? a : b); }
long long minLL(long long a, long long b) { return (a < b ? a : b); }
void solve() {
  int n;
  cin >> n;
  int a[n], arrs = 0, ans = INT_MAX;
  for (long long i = 0; i < n; i++) {
    cin >> a[i];
  }
  for (long long i = 0; i < n; i++) {
    arrs += a[i];
    int sum = arrs * i;
    for (int j = i + 1; j < n; j++) sum += a[j] * j;
    ans = min(sum, ans);
  }
  cout << ans * 4;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  solve();
  return 0;
}
