#include <bits/stdc++.h>
using namespace std;
long long power(long long x, long long y, long long p) {
  long long res = 1;
  x = x % p;
  while (y > 0) {
    if (y & 1) res = (res * x) % p;
    y = y >> 1;
    x = (x * x) % p;
  }
  return res;
}
const int N = 2e2 + 7;
const int xinc[] = {0, 0, 1, -1};
const int yinc[] = {1, -1, 0, 0};
const long double PI = 3.141592653589793;
int n, k, a[N], ans;
void solve() {
  cin >> n >> k;
  for (int i = 0; i < n; i++) cin >> a[i];
  ans = INT_MIN;
  for (int l = 0; l < n; l++)
    for (int r = l; r < n; r++) {
      vector<int> orig, temp;
      for (int i = l; i <= r; i++) orig.push_back(a[i]);
      for (int i = 0; i < l; i++) temp.push_back(a[i]);
      for (int i = r + 1; i < n; i++) temp.push_back(a[i]);
      sort((temp).begin(), (temp).end(), greater<int>());
      int ns = min((int)temp.size(), k);
      temp.resize(ns);
      for (auto i : temp) orig.push_back(i);
      sort((orig).begin(), (orig).end(), greater<int>());
      orig.resize(r - l + 1);
      int sum = 0;
      for (auto i : orig) sum += i;
      ans = max(sum, ans);
    }
  cout << ans << '\n';
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int t;
  t = 1;
  while (t--) solve();
  return 0;
}
