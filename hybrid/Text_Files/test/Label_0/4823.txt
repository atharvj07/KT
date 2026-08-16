#include <bits/stdc++.h>
using namespace std;
int n, m, a[21][21];
bool check1(int l, int r, int num) {
  for (int i = l; i < r + 1; i++) {
    if (a[num][i] != (i + 1)) return 0;
  }
  return 1;
}
bool check(int ind, int x, int y) {
  if (a[ind][x] == (x + 1) && a[ind][y] == (y + 1) && check1(0, m - 1, ind)) {
    return 1;
  }
  if (a[ind][x] != (y + 1) && a[ind][y] != (x + 1)) {
    return 0;
  } else if (a[ind][x] != (y + 1)) {
    for (int i = 0; i < m; i++) {
      if (a[ind][i] == (y + 1) && a[ind][x] == (i + 1)) {
        swap(a[ind][i], a[ind][x]);
        swap(a[ind][x], a[ind][y]);
        if (check1(0, m - 1, ind)) {
          swap(a[ind][y], a[ind][x]);
          swap(a[ind][i], a[ind][x]);
          return 1;
        } else {
          swap(a[ind][y], a[ind][x]);
          swap(a[ind][i], a[ind][x]);
          return 0;
        }
      }
    }
    return 0;
  } else if (a[ind][y] != (x + 1)) {
    for (int i = 0; i < m; i++) {
      if (a[ind][i] == (x + 1) && a[ind][y] == (i + 1)) {
        swap(a[ind][i], a[ind][y]);
        swap(a[ind][x], a[ind][y]);
        if (check1(0, m - 1, ind)) {
          swap(a[ind][x], a[ind][y]);
          swap(a[ind][i], a[ind][y]);
          return 1;
        } else {
          swap(a[ind][x], a[ind][y]);
          swap(a[ind][i], a[ind][y]);
          return 0;
        }
      }
    }
    return 0;
  } else {
    swap(a[ind][x], a[ind][y]);
    int c = 0;
    for (int i = 0; i < m; i++) {
      if (a[ind][i] != (i + 1)) c++;
    }
    if (c <= 2) {
      swap(a[ind][x], a[ind][y]);
      return 1;
    } else {
      swap(a[ind][x], a[ind][y]);
      return 0;
    }
  }
}
int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) cin >> a[i][j];
  bool bb = 1;
  for (int i = 0; i < n; i++) {
    int c = 0;
    for (int j = 0; j < m; j++) {
      if (a[i][j] != (j + 1)) c++;
    }
    if (c > 2) bb = 0;
  }
  if (bb) {
    cout << "YES";
    return 0;
  }
  for (int u1 = 0; u1 < m; u1++) {
    for (int u2 = 0; u2 < m; u2++) {
      bool b = 1;
      for (int i = 0; i < n; i++) {
        b &= check(i, u1, u2);
      }
      if (b) {
        cout << "YES";
        return 0;
      }
    }
  }
  cout << "NO";
}
