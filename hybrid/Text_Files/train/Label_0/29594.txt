#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int n;
  cin >> n;
  long long maxx = -1e9, minx = -1e9;
  long long maxy = -1e9, miny = -1e9;
  long long maxx_maxy = -1e9, maxx_miny = -1e9, minx_maxy = -1e9,
            minx_miny = -1e9;
  for (int i = 1; i <= n; i++) {
    long long x, y;
    cin >> x >> y;
    maxx = max(maxx, x);
    minx = max(minx, -x);
    maxy = max(maxy, y);
    miny = max(miny, -y);
    maxx_maxy = max(maxx_maxy, x + y);
    maxx_miny = max(maxx_miny, x - y);
    minx_maxy = max(minx_maxy, -x + y);
    minx_miny = max(minx_miny, -x - y);
  }
  long long cont = maxx + minx + maxy + miny;
  cont *= 2LL;
  long long ans = max(max(maxx + maxy + minx_miny, maxx + miny + minx_maxy),
                      max(minx + maxy + maxx_miny, minx + miny + maxx_maxy));
  ans *= 2LL;
  cout << ans << " ";
  for (int i = 4; i <= n; i++) {
    cout << cont << " ";
  }
  return 0;
}
