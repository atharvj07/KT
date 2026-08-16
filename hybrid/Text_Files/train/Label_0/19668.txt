#include <bits/stdc++.h>
using namespace std;
template <typename T1, typename T2>
ostream& operator<<(ostream& out, pair<T1, T2>& p) {
  out << "{" << p.first << ", " << p.second << "} ";
  return out;
}
template <typename T1, typename T2>
istream& operator>>(istream& in, pair<T1, T2>& p) {
  in >> p.first >> p.second;
  return in;
}
template <typename T>
istream& operator>>(istream& in, vector<T>& arr) {
  for (auto& i : arr) in >> i;
  return in;
}
template <typename T>
ostream& operator<<(ostream& out, vector<T>& arr) {
  for (auto i : arr) out << i << ' ';
  out << endl;
  return out;
}
signed main() {
  int64_t n, m;
  cin >> n >> m;
  vector<int64_t> ki(m), fi(m);
  for (int64_t i = 0; i < m; ++i) {
    cin >> ki[i] >> fi[i];
  }
  set<int64_t> possible;
  bool ok = true;
  for (int64_t fl = 1; fl < 102; ++fl) {
    ok = true;
    for (int64_t i = 0; i < m && ok; ++i) {
      int64_t currfloor = (ki[i] - 1) / fl + 1;
      if (currfloor != fi[i]) {
        ok = false;
      }
    }
    if (ok) {
      possible.insert((n - 1) / fl + 1);
    }
  }
  if (possible.size() != 1) {
    cout << -1;
    return 0;
  }
  cout << *possible.begin();
  return 0;
}
