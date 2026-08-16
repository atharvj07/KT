#include <bits/stdc++.h>
using namespace std;
set<pair<int, int> > valid;
int d[8][2] = {{0, 1},  {-1, 1}, {-1, 0}, {-1, -1},
               {0, -1}, {1, -1}, {1, 0},  {1, 1}};
int main() {
  int x1, y1, x2, y2;
  cin >> x1 >> y1 >> x2 >> y2;
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int r, a, b;
    cin >> r >> a >> b;
    for (int j = a; j <= b; j++) {
      valid.insert({r, j});
    }
  }
  map<pair<int, int>, int> dist;
  queue<pair<int, int> > q;
  q.push({x1, y1});
  dist[{x1, y1}]++;
  while (!q.empty()) {
    pair<int, int> p = q.front();
    q.pop();
    for (int i = 0; i < 8; i++) {
      int tr = p.first + d[i][0], tc = p.second + d[i][1];
      if (tr < 1000000001 && tc < 1000000001 && valid.count({tr, tc}) &&
          dist[{tr, tc}] == 0) {
        if (tr == x2 && tc == y2) {
          cout << dist[p];
          return 0;
        }
        q.push({tr, tc});
        dist[{tr, tc}] = dist[p] + 1;
      }
    }
  }
  cout << -1;
}
