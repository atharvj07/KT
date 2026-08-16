#include <bits/stdc++.h>
using namespace std;
auto clk = clock();
void solve() {
  long long n, m;
  cin >> n >> m;
  vector<long long> a(n);
  for (long long i = 0; i < n; i++) cin >> a[i];
  vector<long long> b(m);
  for (long long i = 0; i < m; i++) cin >> b[i];
  stack<long long> s;
  for (long long i = n - 1; i >= 0; i--) s.push(a[i]);
  long long ans = 0;
  set<long long> f;
  for (long long i = 0; i < m; i++) {
    if (f.count(b[i]) != 0) {
      ans++;
      f.erase(b[i]);
    } else {
      while (s.top() != b[i]) {
        f.insert(s.top());
        s.pop();
      }
      s.pop();
      ans += 2 * (f.size()) + 1;
    }
  }
  cout << ans << "\n";
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cout << fixed << setprecision(8);
  long long t = 1;
  cin >> t;
  while (t--) solve();
  return 0;
}
