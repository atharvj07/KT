#include <bits/stdc++.h>
using namespace std;
const int MXN = 1e6 + 30;
const int MAXN = 1e3 + 2;
const long long INF = 1e9 + 7;
const long long BINF = 1e15;
const int MOD = 1e9 + 7;
const long double EPS = 1e-15;
long long n, m;
long long a[MXN];
long long used[MXN];
multiset<long long> st;
multiset<long long>::iterator it;
long long cnt, ans;
int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
  }
  for (int i = 1; i <= n; i++) {
    if (i != m && a[i] == 0) a[i] = 1000000;
  }
  if (a[m] != 0) {
    a[m] = 0, ans++;
  }
  for (int i = 1; i <= n; i++) {
    used[a[i]]++;
    st.insert(a[i]);
  }
  long long o = 0;
  while (cnt < n) {
    if (!used[o]) {
      used[o]++, cnt++, ans++;
      it = st.end(), it--;
      used[*it]--;
      st.erase(it);
    } else {
      cnt += used[o];
    }
    o++;
  }
  cout << ans;
  return 0;
}
