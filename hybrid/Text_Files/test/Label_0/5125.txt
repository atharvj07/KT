#include <bits/stdc++.h>
using namespace std;
int f(vector<pair<int, int> > &v) {
  sort(v.begin(), v.end());
  return unique(v.begin(), v.end()) - v.begin();
}
int main() {
  vector<char> mapa(256);
  mapa['R'] = 0;
  mapa['G'] = 1;
  mapa['B'] = 2;
  mapa['Y'] = 3;
  mapa['W'] = 4;
  int n;
  while (cin >> n) {
    vector<pair<int, int> > v;
    for (int i = 0; i < n; ++i) {
      string s;
      cin >> s;
      int x, y;
      x = mapa[s[0]];
      y = s[1] - '1';
      v.push_back(make_pair(x, y));
    }
    v.resize(f(v));
    int mini = 1e9;
    for (int maskX = 0; maskX < 1 << 5; ++maskX) {
      for (int maskY = 0; maskY < 1 << 5; ++maskY) {
        vector<pair<int, int> > w(((int)v.size()));
        for (int i = 0; i < ((int)v.size()); ++i) {
          if (maskX & (1 << v[i].first)) w[i].first = v[i].first + 1;
          if (maskY & (1 << v[i].second)) w[i].second = v[i].second + 1;
        }
        if (f(w) == ((int)v.size()))
          mini =
              min(mini, __builtin_popcount(maskX) + __builtin_popcount(maskY));
      }
    }
    printf("%d\n", mini);
  }
}
