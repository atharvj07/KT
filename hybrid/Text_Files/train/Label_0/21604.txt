#include <bits/stdc++.h>
using namespace std;
long long astd[100010], aend[100010], bstd[100010], bend[100010];
int main() {
  int n, m;
  while (cin >> n) {
    memset(astd, 0, sizeof(astd));
    memset(bstd, 0, sizeof(bstd));
    memset(aend, 0, sizeof(aend));
    memset(bend, 0, sizeof(bend));
    int x, y;
    for (int i = 1; i <= n; i++) {
      cin >> x;
      if (astd[x] == 0)
        astd[x] = i;
      else
        aend[x] = i;
    }
    cin >> m;
    long long v = 0, p = 0;
    for (int i = 1; i <= m; i++) {
      cin >> y;
      if (astd[y] != 0) {
        if (aend[y] != 0) {
          v += astd[y];
          p += n - aend[y] + 1;
        } else {
          v += astd[y];
          p += n - astd[y] + 1;
        }
      }
    }
    cout << v << " " << p << endl;
  }
  return 0;
}
