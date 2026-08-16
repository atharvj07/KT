#include <bits/stdc++.h>
using namespace std;
long long n, m, a, b, x, y, res;
map<long long, long long> mp1, mp2;
set<long long> st;
int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n;
  for (long long i = 0; i < n; i++) {
    cin >> a >> x;
    mp1[a] = x;
    st.insert(a);
  }
  cin >> m;
  for (long long i = 0; i < m; i++) {
    cin >> b >> y;
    mp2[b] = y;
    st.insert(b);
  }
  for (auto x : st) res += max(mp1[x], mp2[x]);
  cout << res;
  return 0;
}
