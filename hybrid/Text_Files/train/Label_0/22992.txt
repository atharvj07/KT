#include <bits/stdc++.h>
using namespace std;
using lint = long long;
template<class T = int> using V = vector<T>;
template<class T = int> using VV = V< V<T> >;

int main() {
  cin.tie(nullptr); ios::sync_with_stdio(false);
  int h, w; cin >> h >> w;
  V<string> s(h); for (auto&& e : s) cin >> e;
  int res = 0;
  for (int i = 0; i < h; ++i) for (int j = 0; j < w; ++j) if (s[i][j] == 'B') {
    for (int x = 0; x < h; ++x) for (int y = 0; y < w; ++y) if (s[x][y] == 'B') {
      res = max(res, abs(i - x) + abs(j - y));
    }
  }
  cout << res << '\n';
}
