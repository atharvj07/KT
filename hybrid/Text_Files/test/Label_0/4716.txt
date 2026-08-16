#include <bits/stdc++.h>
using namespace std;
bool collinear(int x1, int y1, int x2, int y2, int x3, int y3) {
  return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2);
}
int main() {
  int n, x, y;
  cin >> n;
  vector<pair<int, int> > points;
  for (int i = 0; i < n; i++) {
    cin >> x >> y;
    points.push_back(make_pair(x, y));
  }
  long long ans = 0;
  for (int i = 0; i < n - 2; i++)
    for (int j = i + 1; j < n - 1; j++)
      for (int k = j + 1; k < n; k++) {
        if (!collinear(points[i].first, points[i].second, points[j].first,
                       points[j].second, points[k].first, points[k].second))
          ans++;
      }
  cout << ans << endl;
  return 0;
}
