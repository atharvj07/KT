#include <bits/stdc++.h>
using namespace std;
int cur;
int a[55][55][55];
void yz_xy_xz(int n) {
  assert(a[n - 1][0][0] == cur);
  int x = n;
  int y, z;
  for (z = 0; z <= n; z++) {
    if (z & 1) {
      for (y = n - 1; y >= 0; y--) {
        a[x][y][z] = ++cur;
      }
    } else {
      for (y = 0; y < n; y++) {
        a[x][y][z] = ++cur;
      }
    }
  }
  z = n;
  for (x = n - 1; x >= 0; x--) {
    if (y == -1) {
      for (y = 0; y < n; y++) {
        a[x][y][z] = ++cur;
      }
    } else {
      for (y = n - 1; y >= 0; y--) {
        a[x][y][z] = ++cur;
      }
    }
  }
  assert(a[0][n - 1][n] == cur);
  y = n;
  if (n & 1) {
    for (int z = n; z >= 0; z--) {
      if (z & 1) {
        for (int x = 0; x < int(n + 1); x++) {
          a[x][y][z] = ++cur;
        }
      } else {
        for (int x = n; x >= 0; x--) {
          a[x][y][z] = ++cur;
        }
      }
    }
  } else {
    for (int x = 0; x < int(n + 1); x++) {
      if (x & 1) {
        for (int z = 1; z <= int(n); z++) {
          a[x][y][z] = ++cur;
        }
      } else {
        for (int z = n; z >= 1; z--) {
          a[x][y][z] = ++cur;
        }
      }
    }
    for (int x = n; x >= 0; x--) {
      a[x][y][0] = ++cur;
    }
  }
}
void reverse_cube(int n) {
  int N = n * n * n;
  for (int i = 0; i < int(n); i++) {
    for (int j = 0; j < int(n); j++) {
      for (int k = 0; k < int(n); k++) {
        a[i][j][k] = N + 1 - a[i][j][k];
      }
    }
  }
}
int b[55][55];
void rotate_cube(int n) {
  for (int z = 0; z < int(n); z++) {
    for (int x = 0; x < int(n); x++) {
      for (int y = 0; y < int(n); y++) {
        b[n - y - 1][x] = a[x][y][z];
      }
    }
    for (int x = 0; x < int(n); x++) {
      for (int y = 0; y < int(n); y++) {
        a[x][y][z] = b[x][y];
      }
    }
  }
}
void out(int n) {
  for (int i = 0; i < int(n); i++) {
    if (i) printf("\n");
    for (int j = 0; j < int(n); j++) {
      for (int k = 0; k < int(n); k++) {
        if (k) printf(" ");
        printf("%d", a[i][j][k]);
      }
      printf("\n");
    }
  }
}
int main() {
  int n;
  cin >> n;
  cur = 1;
  a[0][0][0] = 1;
  for (int i = 1; i <= int(n - 1); i++) {
    yz_xy_xz(i);
    reverse_cube(i + 1);
    rotate_cube(i + 1);
  }
  out(n);
  return 0;
}
