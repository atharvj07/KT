#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
template <typename T>
inline void print(T val) {
  cout << val << '\n';
}
template <typename Iterator>
inline void print(Iterator begin, Iterator end) {
  for (auto it = begin; it != end; it = next(it)) {
    cout << *it << ' ';
  }
  cout << '\n';
}
void solve() {
  string s;
  cin >> s;
  int n = s.size();
  bool last = false;
  string ans;
  for (auto i = 0; i < n; ++i) {
    if (i > 0 && s[i] == s[i - 1]) {
      continue;
    }
    int cnt = 0;
    for (auto j = i; j < n; ++j) {
      if (s[j] == s[i]) {
        ++cnt;
      }
    }
    if (cnt & 1) {
      ans += s[i];
    }
  }
  sort(ans.begin(), ans.end());
  set<char> x(ans.begin(), ans.end());
  string k(x.begin(), x.end());
  print(k);
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
