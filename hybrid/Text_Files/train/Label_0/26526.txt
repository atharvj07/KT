#include <bits/stdc++.h>
using namespace std;
bool isvalid(int x, int y) {
  if ((x >= 1 && x <= 1000000000) && y >= 1 && y <= 1000000000)
    return 1;
  else
    return 0;
}
int main() {
  map<pair<int, int>, int> m;
  int x0, y0, x1, y1;
  cin >> x0 >> y0 >> x1 >> y1;
  int n;
  cin >> n;
  int r, a, b;
  for (int i = 0; i < n; i++) {
    cin >> r >> a >> b;
    for (int j = a; j <= b; j++) {
      if (m[make_pair(r, j)] == 0) {
        m[make_pair(r, j)]++;
      }
    }
  }
  queue<pair<pair<int, int>, int> > q;
  q.push(make_pair(make_pair(x0, y0), 0));
  pair<pair<int, int>, int> temp;
  while (!q.empty()) {
    temp = q.front();
    q.pop();
    int i = temp.first.first;
    int j = temp.first.second;
    int dist = temp.second;
    if (i == x1 && j == y1) {
      cout << dist << endl;
      return 0;
    }
    if (isvalid(i - 1, j - 1)) {
      if (m[make_pair(i - 1, j - 1)]) {
        m[make_pair(i - 1, j - 1)]--;
        q.push(make_pair(make_pair(i - 1, j - 1), dist + 1));
      }
    }
    if (isvalid(i - 1, j)) {
      if (m[make_pair(i - 1, j)]) {
        m[make_pair(i - 1, j)]--;
        q.push(make_pair(make_pair(i - 1, j), dist + 1));
      }
    }
    if (isvalid(i - 1, j + 1)) {
      if (m[make_pair(i - 1, j + 1)]) {
        m[make_pair(i - 1, j + 1)]--;
        q.push(make_pair(make_pair(i - 1, j + 1), dist + 1));
      }
    }
    if (isvalid(i, j - 1)) {
      if (m[make_pair(i, j - 1)]) {
        m[make_pair(i, j - 1)]--;
        q.push(make_pair(make_pair(i, j - 1), dist + 1));
      }
    }
    if (isvalid(i, j + 1)) {
      if (m[make_pair(i, j + 1)]) {
        m[make_pair(i, j + 1)]--;
        q.push(make_pair(make_pair(i, j + 1), dist + 1));
      }
    }
    if (isvalid(i + 1, j - 1)) {
      if (m[make_pair(i + 1, j - 1)]) {
        m[make_pair(i + 1, j - 1)]--;
        q.push(make_pair(make_pair(i + 1, j - 1), dist + 1));
      }
    }
    if (isvalid(i + 1, j)) {
      if (m[make_pair(i + 1, j)]) {
        m[make_pair(i + 1, j)]--;
        q.push(make_pair(make_pair(i + 1, j), dist + 1));
      }
    }
    if (isvalid(i + 1, j + 1)) {
      if (m[make_pair(i + 1, j + 1)]) {
        m[make_pair(i + 1, j + 1)]--;
        q.push(make_pair(make_pair(i + 1, j + 1), dist + 1));
      }
    }
  }
  cout << -1 << endl;
}
