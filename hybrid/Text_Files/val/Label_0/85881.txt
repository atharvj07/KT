#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int n, L, a;
  cin >> n >> L >> a;
  int ans = 0;
  int prevEnd = 0;
  for (int i = 0; i < n; i++) {
    int t, l;
    cin >> t >> l;
    ans += (t - prevEnd) / a;
    prevEnd = t + l;
  }
  ans += (L - prevEnd) / a;
  cout << ans << endl;
  return 0;
}
