#include <bits/stdc++.h>
using namespace std;
const long long int mod = 1e9 + 7;
int main() {
  long long int n, x, y;
  cin >> n >> x >> y;
  vector<pair<long long int, long long int> > V;
  for (long long int i = 0; i < n; ++i) {
    long long int a, b;
    cin >> a >> b;
    V.push_back(make_pair(a, 0));
    V.push_back(make_pair(b, 1));
  }
  sort(V.begin(), V.end());
  vector<long long int> st;
  long long int ans = 0;
  for (long long int i = 0; i < V.size(); ++i) {
    if (V[i].second == 1) {
      st.push_back(V[i].first);
      ans += y * V[i].first;
      ans %= mod;
    } else {
      ans -= y * V[i].first;
      ans += mod * y;
      ans %= mod;
      if (st.size() == 0) {
        ans += x;
      } else {
        long long int z = st[st.size() - 1];
        if (y * (V[i].first - z) <= x) {
          ans += y * (V[i].first - z);
          ans %= mod;
          st.pop_back();
        } else {
          ans += x;
          ans %= mod;
          st.clear();
        }
      }
    }
  }
  cout << ans % mod << "\n";
  return 0;
}
