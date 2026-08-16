#include <bits/stdc++.h>
using namespace std;
const long long int INF = 1LL << 60;
long long int n, m;
long long int C, H;
long long int a00, a01, a10, a11;
int main() {
  cin >> n >> m;
  cin >> C;
  bool first = true;
  while (C--) {
    long long int x, y;
    cin >> x >> y;
    if (first) {
      first = false;
      a00 = x + y;
      a10 = -x + y;
      a01 = x - y;
      a11 = -x - y;
    } else {
      a00 = max(a00, x + y);
      a10 = max(a10, -x + y);
      a01 = max(a01, x - y);
      a11 = max(a11, -x - y);
    }
  }
  long long int d = INF, pos, cnt = 1;
  cin >> H;
  while (H--) {
    long long int x, y;
    cin >> x >> y;
    long long int mx =
        max(max(x + y + a11, -x - y + a00), max(-x + y + a01, x - y + a10));
    if (mx < d) {
      d = mx;
      pos = cnt;
    }
    cnt++;
  }
  cout << d << endl << pos << endl;
  return 0;
}
