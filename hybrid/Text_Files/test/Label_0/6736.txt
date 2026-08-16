#include <bits/stdc++.h>
using namespace std;
int a[15][15];
int main() {
  ios::sync_with_stdio(0);
  memset(a, 0, sizeof(a));
  int r, c, n, k;
  cin >> r >> c >> n >> k;
  int ann = 0;
  for (int j = 0; j < n; j++) {
    int x, y;
    cin >> x >> y;
    x--;
    y--;
    a[x][y] = 1;
  }
  for (int i = 0; i < r; i++)
    for (int j = 0; j < c; j++)
      for (int i1 = i; i1 < r; i1++)
        for (int j1 = j; j1 < c; j1++) {
          int ans = 0;
          for (int ii = i; ii <= i1; ii++)
            for (int jj = j; jj <= j1; jj++)
              if (a[ii][jj]) ans++;
          if (ans >= k) ann++;
        }
  cout << ann << endl;
  return 0;
}
