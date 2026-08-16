#include <bits/stdc++.h>
using namespace std;
const long long INF = 1e18;
long long gettime(long long h, long long r, long long d) { return (d - h) / r; }
int main() {
  ios_base::sync_with_stdio(false);
  long long n, m, inc, dam, boun, k = 0;
  set<pair<pair<long long, long long>, pair<long long, long long> > > st;
  cin >> n >> m >> boun >> inc >> dam;
  vector<bool> ls(n, false);
  vector<long long> mxh(n), reg(n), entm(n, -1);
  long long strt;
  for (int j = 0; j < n; j++) {
    cin >> mxh[j] >> strt >> reg[j];
    st.insert({{0, 0}, {j, strt}});
  }
  long long id, tm;
  for (int j = 0; j < m; j++) {
    cin >> tm >> id >> strt;
    --id;
    st.insert({{tm, 0}, {id, strt}});
  }
  long long mx = 0;
  while (!st.empty()) {
    auto p = *st.begin();
    st.erase(st.begin());
    if (p.first.second) {
      if (p.first.first == INF && inc) {
        cout << -1;
        return 0;
      }
      mx = max(mx, k * (boun + p.first.first * inc));
      k--;
      ls[p.second.first] = false;
      entm[p.second.first] = -1;
    } else if (p.second.second <= dam) {
      mx = max(mx, k * (boun + (p.first.first - 1) * inc));
      if (!ls[p.second.first]) {
        k++;
        ls[p.second.first] = true;
      } else {
        st.erase(st.find({{entm[p.second.first], 1}, {p.second.first, INF}}));
        entm[p.second.first] = -1;
      }
      if (mxh[p.second.first] <= dam ||
          !reg[p.second.first] && p.second.second <= dam) {
        st.insert({{INF, 1}, {p.second.first, INF}});
        entm[p.second.first] = INF;
      } else if (reg[p.second.first]) {
        tm = gettime(p.second.second, reg[p.second.first], dam);
        st.insert({{p.first.first + tm, 1}, {p.second.first, INF}});
        entm[p.second.first] = p.first.first + tm;
      }
    } else if (ls[p.second.first]) {
      mx = max(mx, k * (boun + (p.first.first - 1) * inc));
      k--;
      ls[p.second.first] = false;
      if (entm[p.second.first] != -1) {
        st.erase(st.find({{entm[p.second.first], 1}, {p.second.first, INF}}));
        entm[p.second.first] = -1;
      }
    }
  }
  cout << mx;
}
