#include <bits/stdc++.h>
using namespace std;
int solve() {
  long long n;
  cin >> n;
  map<long long, long long> mp;
  long long mx = 1;
  set<long long> st;
  for (int i = 1; i <= n; i++) {
    long long x;
    cin >> x;
    mp[x]++;
    mx = max(mx, mp[x]);
    st.insert(x);
  }
  long long ct = 0;
  for (auto it : mp) {
    if (it.second == mx) ct++;
  }
  long long tt = n - mx * ct + mx - 1;
  long long dvd = tt / (mx - 1);
  cout << (dvd - 1 + ct - 1) << endl;
  return 0;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
