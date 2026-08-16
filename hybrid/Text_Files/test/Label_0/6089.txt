#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
template <class T, class U>
inline void add_self(T &a, U b) {
  a += b;
  if (a >= mod) a -= mod;
  if (a < 0) a += mod;
}
template <class T, class U>
inline void min_self(T &x, U y) {
  if (y < x) x = y;
}
template <class T, class U>
inline void max_self(T &x, U y) {
  if (y > x) x = y;
}
void _print() { cerr << "]\n"; }
template <typename T, typename... V>
void _print(T t, V... v) {
  cout << t;
  ;
  if (sizeof...(v)) cerr << ", ";
  _print(v...);
}
template <class T, class U>
void print_m(const map<T, U> &m, int w = 3) {
  if (m.empty()) {
    cout << "Empty" << endl;
    return;
  }
  for (auto x : m) cout << "(" << x.first << ": " << x.second << ")," << endl;
  cout << endl;
}
template <class T, class U>
void debp(const pair<T, U> &pr, bool end_line = 1) {
  cout << "{" << pr.first << " " << pr.second << "}";
  cout << (end_line ? "\n" : ", ");
}
template <class T>
void print_vp(const T &vp, int sep_line = 0) {
  if (vp.empty()) {
    cout << "Empty" << endl;
    return;
  }
  if (!sep_line) cout << "{ ";
  for (auto x : vp) debp(x, sep_line);
  if (!sep_line) cout << "}\n";
  cout << endl;
}
template <typename T>
void print(const T &v, bool show_index = false) {
  int w = 2;
  if (show_index) {
    for (int i = 0; i < int((v).size()); i++) cout << setw(w) << i << " ";
    cout << endl;
  }
  for (auto &el : v) cout << setw(w) << el << " ";
  cout << endl;
}
template <typename T>
void print_vv(const T &vv) {
  if (int((vv).size()) == 0) {
    cout << "Empty" << endl;
    return;
  }
  int w = 3;
  cout << setw(w) << " ";
  for (int j = 0; j < int((*vv.begin()).size()); j++)
    cout << setw(w) << j << " ";
  cout << endl;
  int i = 0;
  for (auto &v : vv) {
    cout << i++ << " {";
    for (auto &el : v) cout << setw(w) << el << " ";
    cout << "},\n";
  }
  cout << endl;
}
long long C(long long n, int r) {
  long long ans = 1;
  for (int i = 0; i < int(r); i++) ans *= (n - i);
  for (int i = 0; i < int(r); i++) ans /= (i + 1);
  return ans;
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n;
  while (cin >> n) {
    vector<int> a(n);
    map<int, int> cnt;
    for (int i = 0; i < int(n); i++) {
      cin >> a[i];
      cnt[a[i]]++;
    }
    sort(a.begin(), a.end());
    map<int, int> req;
    for (int i = 0; i < int(3); i++) req[a[i]]++;
    long long ans = 1;
    for (auto p : req) {
      ans *= C(cnt[p.first], p.second);
    }
    cout << ans << "\n";
  }
  return 0;
}
