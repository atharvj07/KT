#include <bits/stdc++.h>
using namespace std;
const int inf = 2000000000;
const long long infLL = 9000000000000000000;
template <typename first, typename second>
ostream& operator<<(ostream& os, const pair<first, second>& p) {
  return os << "(" << p.first << ", " << p.second << ")";
}
template <typename T>
ostream& operator<<(ostream& os, const vector<T>& v) {
  os << "{";
  for (auto it = v.begin(); it != v.end(); ++it) {
    if (it != v.begin()) os << ", ";
    os << *it;
  }
  return os << "}";
}
template <typename T>
ostream& operator<<(ostream& os, const set<T>& v) {
  os << "[";
  for (auto it = v.begin(); it != v.end(); ++it) {
    if (it != v.begin()) os << ",";
    os << *it;
  }
  return os << "]";
}
template <typename T>
ostream& operator<<(ostream& os, const multiset<T>& v) {
  os << "[";
  for (auto it = v.begin(); it != v.end(); ++it) {
    if (it != v.begin()) os << ", ";
    os << *it;
  }
  return os << "]";
}
template <typename first, typename second>
ostream& operator<<(ostream& os, const map<first, second>& v) {
  os << "[";
  for (auto it = v.begin(); it != v.end(); ++it) {
    if (it != v.begin()) os << ", ";
    os << it->first << " = " << it->second;
  }
  return os << "]";
}
void faltu() { cerr << '\n'; }
template <typename T>
void faltu(T a[], int n) {
  for (int i = 0; i < n; ++i) cerr << a[i] << ' ';
  cerr << '\n';
}
template <typename T, typename... hello>
void faltu(T arg, const hello&... rest) {
  cerr << arg << ' ';
  faltu(rest...);
}
const int mx = 2e5 + 5;
int m, n, k, t;
vector<pair<pair<int, int>, int>> vec;
vector<pair<int, int>> store;
int a[mx];
bool check(int idx) {
  store.clear();
  for (auto x : vec) {
    if (x.second > a[idx]) store.push_back(x.first);
  }
  int cnt = n + 1;
  int le = -1, ri = -2;
  for (auto x : store) {
    if (ri == -2) {
      le = x.first, ri = x.second;
      continue;
    }
    if (x.first > ri) {
      cnt += 2 * (ri - le + 1);
      le = x.first;
      ri = x.second;
    } else {
      ri = max(ri, x.second);
    }
  }
  cnt += 2 * (ri - le + 1);
  if (idx == 1) do {
      cerr << "cnt"
           << " : ";
      faltu(cnt);
    } while (0);
  if (cnt > t) return 0;
  return 1;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  cin >> m >> n >> k >> t;
  for (int i = 0; i < m; ++i) {
    cin >> a[i];
  }
  sort(a, a + m, greater<int>());
  for (int i = 0; i < k; ++i) {
    int l, r, d;
    cin >> l >> r >> d;
    vec.push_back(make_pair(make_pair(l, r), d));
  }
  sort(vec.begin(), vec.end());
  int lo = 0, hi = m - 1, mid;
  while (lo <= hi) {
    mid = (lo + hi) / 2;
    if (check(mid))
      lo = mid + 1;
    else
      hi = mid - 1;
  }
  cout << hi + 1 << '\n';
}
