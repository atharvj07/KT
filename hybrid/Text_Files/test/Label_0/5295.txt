#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;
int main() {
  int n;
  while (cin >> n) {
    int minX, maxX, minY, maxY;
    long long totalS = 0;
    for (int i = 0; i < n; i++) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      long long s = (x2 - x1);
      s *= (y2 - y1);
      totalS += s;
      if (i == 0) {
        minX = x1;
        minY = y1;
        maxX = x2;
        maxY = y2;
      } else {
        minX = min(x1, minX);
        minY = min(y1, minY);
        maxX = max(x2, maxX);
        maxY = max(y2, maxY);
      }
    }
    int w = maxX - minX;
    int h = maxY - minY;
    bool hasS = true;
    if (w != h) {
      hasS = false;
    }
    long long ss = w;
    ss *= h;
    if (ss != totalS) {
      hasS = false;
    }
    if (hasS) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
  return 0;
}
