#include <bits/stdc++.h>
using namespace std;
int i, b[105], g[105], m, n, j, cont;
int vabs(int x) {
  if (x < 0)
    return -x;
  else
    return x;
}
int main() {
  cin >> n;
  for (i = 0; i < n; i++) {
    cin >> b[i];
  }
  cin >> m;
  for (i = 0; i < m; i++) {
    cin >> g[i];
  }
  sort(b, b + n);
  sort(g, g + m);
  i = 0;
  j = 0;
  while (i < n && j < m) {
    if (vabs(b[i] - g[j]) <= 1) {
      cont++;
      i++;
      j++;
    } else {
      if (b[i] < g[j]) {
        i++;
      } else {
        j++;
      }
    }
  }
  cout << cont << endl;
  return 0;
}
