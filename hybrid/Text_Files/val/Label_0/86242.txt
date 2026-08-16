#include <bits/stdc++.h>
using namespace std;
const long long inf = 9223372036854775806;
const long long mod = 1e9 + 7;
const double pi = 3.1415926;
const long long N = 1e5 + 10;
const long long small = 251;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long n, m;
  cin >> n >> m;
  long long a[small][small];
  for (long long i = 1; i <= n; i++)
    for (long long j = 1; j <= m; j++) cin >> a[i][j];
  long long bl[small * small] = {0};
  set<pair<long long, long long> > st;
  long long ans[small][small] = {0};
  for (long long i = 1; i <= n; i++) {
    long long temp = 0;
    for (long long j = 1; j <= m; j++) temp = max(temp, a[i][j]);
    bl[temp] = 1;
    st.insert(make_pair(temp, 1));
  }
  for (long long j = 1; j <= m; j++) {
    long long temp = 0;
    for (long long i = 1; i <= n; i++) temp = max(temp, a[i][j]);
    bl[temp] = 1;
    st.insert(make_pair(temp, -1));
  }
  long long hang = 1, lie = 1, now = 1;
  while (!st.empty()) {
    pair<long long, long long> u = *st.begin();
    st.erase(u);
    pair<long long, long long> tmp = *st.begin();
    if (u.first == tmp.first) {
      u.second = 2;
      st.erase(tmp);
    }
    vector<long long> v;
    ans[hang][lie] = u.first;
    if (u.second == 1) {
      v.clear();
      for (long long i = lie + 1; i <= m; i++) {
        while (bl[now]) now++;
        v.push_back(now);
        now++;
      }
      for (long long i = m, j = 0; i >= lie + 1; i--) {
        ans[hang][i] = v[j];
        j++;
      }
      hang++;
    } else if (u.second == -1) {
      v.clear();
      for (long long i = hang + 1; i <= n; i++) {
        while (bl[now]) now++;
        v.push_back(now);
        now++;
      }
      for (long long i = n, j = 0; i >= hang + 1; i--) {
        ans[i][lie] = v[j];
        j++;
      }
      lie++;
    } else {
      v.clear();
      for (long long i = lie + 1; i <= m; i++) {
        while (bl[now]) now++;
        v.push_back(now);
        now++;
      }
      for (long long i = m, j = 0; i >= lie + 1; i--) {
        ans[hang][i] = v[j];
        j++;
      }
      v.clear();
      for (long long i = hang + 1; i <= n; i++) {
        while (bl[now]) now++;
        v.push_back(now);
        now++;
      }
      for (long long i = n, j = 0; i >= hang + 1; i--) {
        ans[i][lie] = v[j];
        j++;
      }
      hang++;
      lie++;
    }
  }
  for (long long i = 1; i <= n; i++) {
    for (long long j = 1; j <= m; j++) cout << ans[i][j] << " ";
    cout << "\n";
  }
  return 0;
}
