#include <bits/stdc++.h>
using namespace std;
using lint = long long;
template<class T = int> using V = vector<T>;
template<class T = int> using VV = V< V<T> >;


int main() {
  cin.tie(nullptr); ios::sync_with_stdio(false);
  int n; cin >> n;
  V<char> p(n); for (auto&& e : p) cin >> e;
  auto M = [](char x, char y) -> char {
    return x == 'F' or y == 'T' ? 'T' : 'F';
  };
  char res = M(p[0], p[1]);
  for (int i = 2; i < n; ++i) {
    res = M(res, p[i]);
  }
  cout << res << '\n';
}
