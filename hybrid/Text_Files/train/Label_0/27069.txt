#include <bits/stdc++.h>
using namespace std;
const int N = 101110;
struct MAT {
  int a[2][2];
  MAT() { memset(a, 0, sizeof(MAT)); }
  MAT(int x, int y, int u, int v) {
    a[0][0] = x;
    a[0][1] = y;
    a[1][0] = u;
    a[1][1] = v;
  }
  int* operator[](int i) { return a[i]; }
  bool operator==(MAT x) {
    for (int i = 0; i < 2; i++)
      for (int j = 0; j < 2; j++)
        if (a[i][j] != x[i][j]) return false;
    return true;
  }
  MAT operator*(MAT x) {
    MAT ans(0, 0, 0, 0);
    for (int i = 0; i < 2; i++)
      for (int j = 0; j < 2; j++)
        for (int k = 0; k < 2; k++)
          ans[i][j] = (int)((ans[i][j] + (long long)a[i][k] * x[k][j]) %
                            (int)(1e9 + 7));
    return ans;
  }
  MAT operator+(MAT x) {
    MAT ans;
    for (int i = 0; i < 2; i++)
      for (int j = 0; j < 2; j++) {
        ans[i][j] = a[i][j] + x[i][j];
        ans[i][j] %= (int)(1e9 + 7);
      }
    return ans;
  }
  MAT operator^(int k) {
    MAT x = *this;
    MAT ans(1, 0, 0, 1);
    while (k) {
      if (k & 1) ans = ans * x;
      x = x * x;
      k >>= 1;
    }
    return ans;
  }
};
int A[N], l[4 * N], h[4 * N];
MAT T[4 * N], Sum[4 * N];
int n, m;
void build(int x, int i, int j) {
  l[x] = i;
  h[x] = j;
  T[x] = MAT(1, 0, 0, 1);
  if (i == j)
    Sum[x] = MAT(1, 1, 1, 0) ^ (A[i] - 1);
  else {
    int mid = (i + j) / 2;
    build(2 * x, i, mid);
    build(2 * x + 1, mid + 1, j);
    Sum[x] = Sum[2 * x] + Sum[2 * x + 1];
  }
}
void UP(int x) {
  if (!(T[x] == MAT(1, 0, 0, 1))) {
    Sum[x] = Sum[x] * T[x];
    if (l[x] != h[x]) {
      T[2 * x] = T[2 * x] * T[x];
      T[2 * x + 1] = T[2 * x + 1] * T[x];
    }
    T[x] = MAT(1, 0, 0, 1);
  }
}
void update(int x, int i, int j, MAT val) {
  UP(x);
  if (l[x] > j || h[x] < i) return;
  if (l[x] >= i && h[x] <= j) {
    T[x] = T[x] * val;
    UP(x);
    return;
  }
  update(2 * x, i, j, val);
  update(2 * x + 1, i, j, val);
  Sum[x] = Sum[2 * x] + Sum[2 * x + 1];
}
MAT cal(int x, int i, int j) {
  UP(x);
  if (l[x] > j || h[x] < i) return MAT();
  if (l[x] >= i && h[x] <= j) return Sum[x];
  return cal(2 * x, i, j) + cal(2 * x + 1, i, j);
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) scanf("%d", &A[i]);
  build(1, 1, n);
  while (m--) {
    int type, x, l, r, val;
    scanf("%d", &type);
    type++;
    if (type == 1) {
      scanf("%d%d", &x, &val);
      if (val != 0) update(1, x, x, MAT(1, 1, 1, 0) ^ val);
    }
    if (type == 2) {
      scanf("%d%d%d", &l, &r, &val);
      if (val != 0) update(1, l, r, MAT(1, 1, 1, 0) ^ val);
    }
    if (type == 3) {
      scanf("%d%d", &l, &r);
      printf("%d\n", cal(1, l, r)[0][0]);
    }
  }
}
