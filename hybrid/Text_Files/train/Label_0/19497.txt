#include <bits/stdc++.h>
using namespace std;
pair<int, int> point;
pair<pair<int, int>, pair<int, int> > segments[10];
set<pair<int, int> > second;
const int INF = 1e9 + 7;
int main() {
  for (int i = 0; i < 4; i++) {
    int x, y, a, b;
    scanf("%d %d %d %d", &x, &y, &a, &b);
    second.insert({x, y});
    second.insert({a, b});
    segments[i] = {{x, y}, {a, b}};
  }
  if (second.size() == 4) {
    int ymin = INF, xmin = INF, ymax = -INF, xmax = -INF;
    for (auto a : second) {
      xmin = min(xmin, a.first);
      xmax = max(xmax, a.first);
      ymin = min(ymin, a.second);
      ymax = max(ymax, a.second);
    }
    if (xmin == xmax || ymin == ymax)
      printf("NO\n");
    else {
      pair<int, int> v1 = {xmax, ymin}, v2 = {xmax, ymax}, v3 = {xmin, ymin},
                     v4 = {xmin, ymax};
      bool top = 0, left = 0, right = 0, bottom = 0;
      for (int i = 0; i < 4; i++) {
        if ((segments[i].first == v1 && segments[i].second == v2) ||
            (segments[i].second == v1 && segments[i].first == v2))
          top = true;
        if ((segments[i].first == v2 && segments[i].second == v4) ||
            (segments[i].second == v2 && segments[i].first == v4))
          right = true;
        if ((segments[i].first == v4 && segments[i].second == v3) ||
            (segments[i].second == v4 && segments[i].first == v3))
          bottom = true;
        if ((segments[i].first == v1 && segments[i].second == v3) ||
            (segments[i].second == v1 && segments[i].first == v3))
          left = true;
      }
      if (top + right + bottom + left == 4)
        printf("YES\n");
      else
        printf("NO\n");
    }
  } else {
    printf("NO\n");
  }
  return 0;
}
