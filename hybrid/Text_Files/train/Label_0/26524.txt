#include <bits/stdc++.h>
using namespace std;
map<pair<int, int>, int> dis;
set<pair<int, int> > edge;
int main() {
  int x0, y0, x1, y1;
  cin >> x0 >> y0 >> x1 >> y1;
  int n, r, L, R;
  cin >> n;
  while (n--) {
    cin >> r >> L >> R;
    for (int i = L; i <= R; i++) {
      edge.insert(make_pair(r, i));
    }
  }
  queue<pair<int, int> > q;
  q.push(make_pair(x0, y0));
  dis[make_pair(x0, y0)] = 0;
  while (!q.empty()) {
    pair<int, int> a = q.front();
    int x = a.first;
    int y = a.second;
    int d = dis[make_pair(x, y)];
    q.pop();
    for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        int X = x + i, Y = y + j;
        if (dis.count(make_pair(X, Y)) || !edge.count(make_pair(X, Y))) {
          continue;
        }
        q.push(make_pair(X, Y));
        dis[make_pair(X, Y)] = 1 + d;
      }
    }
  }
  if (!dis.count(make_pair(x1, y1))) dis[make_pair(x1, y1)] = -1;
  cout << dis[make_pair(x1, y1)];
}
