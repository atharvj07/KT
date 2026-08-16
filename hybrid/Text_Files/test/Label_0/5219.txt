#include <bits/stdc++.h>
using namespace std;
struct punkt {
  int x;
  int y;
};
punkt stos[4000001];
int n, m, i, x, y, s;
char znak, w[2004][2004];
bool tab[2004][2004], blad;
int ile(int x, int y) {
  int r = 0;
  if (x < 1 || x > n || y < 1 || y > m || tab[x][y] == 0) return 111;
  if (!tab[x + 1][y]) r++;
  if (!tab[x - 1][y]) r++;
  if (!tab[x][y + 1]) r++;
  if (!tab[x][y - 1]) r++;
  return r;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin >> n >> m;
  for (int a = 1; a <= n; a++) {
    for (int b = 1; b <= m; b++) {
      cin >> znak;
      if (znak == '.') {
        tab[a][b] = 1;
      }
    }
  }
  for (int a = 1; a <= n; a++) {
    for (int b = 1; b <= m; b++) {
      i = 0;
      i = ile(a, b);
      if (i == 4) blad = 1;
      if (i == 3) {
        stos[++s].x = a;
        stos[s].y = b;
      }
    }
  }
  while (!blad && s > 0) {
    x = stos[s].x;
    y = stos[s].y;
    s--;
    if (ile(x, y) == 3) {
      if (tab[x + 1][y]) {
        w[x][y] = '^';
        w[x + 1][y] = 'v';
        tab[x][y] = 0;
        tab[x + 1][y] = 0;
        if (ile(x + 1, y + 1) == 3) {
          stos[++s].x = x + 1;
          stos[s].y = y + 1;
        }
        if (ile(x + 2, y) == 3) {
          stos[++s].x = x + 2;
          stos[s].y = y;
        }
        if (ile(x + 1, y - 1) == 3) {
          stos[++s].x = x + 1;
          stos[s].y = y - 1;
        }
      } else if (tab[x - 1][y]) {
        w[x - 1][y] = '^';
        w[x][y] = 'v';
        tab[x][y] = 0;
        tab[x - 1][y] = 0;
        if (ile(x - 1, y + 1) == 3) {
          stos[++s].x = x - 1;
          stos[s].y = y + 1;
        }
        if (ile(x - 2, y) == 3) {
          stos[++s].x = x - 2;
          stos[s].y = y;
        }
        if (ile(x - 1, y - 1) == 3) {
          stos[++s].x = x - 1;
          stos[s].y = y - 1;
        }
      } else if (tab[x][y + 1]) {
        w[x][y] = '<';
        w[x][y + 1] = '>';
        tab[x][y] = 0;
        tab[x][y + 1] = 0;
        if (ile(x - 1, y + 1) == 3) {
          stos[++s].x = x - 1;
          stos[s].y = y + 1;
        }
        if (ile(x + 1, y + 1) == 3) {
          stos[++s].x = x + 1;
          stos[s].y = y + 1;
        }
        if (ile(x, y + 2) == 3) {
          stos[++s].x = x;
          stos[s].y = y + 2;
        }
      } else if (tab[x][y - 1]) {
        w[x][y - 1] = '<';
        w[x][y] = '>';
        tab[x][y] = 0;
        tab[x][y - 1] = 0;
        if (ile(x + 1, y - 1) == 3) {
          stos[++s].x = x + 1;
          stos[s].y = y - 1;
        }
        if (ile(x - 1, y - 1) == 3) {
          stos[++s].x = x - 1;
          stos[s].y = y - 1;
        }
        if (ile(x, y - 2) == 3) {
          stos[++s].x = x;
          stos[s].y = y - 2;
        }
      } else {
        blad = 1;
      }
    }
  }
  for (int a = 1; a <= n; a++) {
    for (int b = 1; b <= m; b++) {
      if (tab[a][b]) {
        blad = 1;
      }
    }
  }
  if (blad)
    cout << "Not unique";
  else {
    for (int a = 1; a <= n; a++) {
      for (int b = 1; b <= m; b++) {
        if (w[a][b] == 0)
          cout << '*';
        else
          cout << w[a][b];
      }
      cout << endl;
    }
  }
  return 0;
}
