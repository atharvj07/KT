#include <bits/stdc++.h>
using namespace std;
const int MAXN = 55;
int N, M, a[MAXN][MAXN], b[MAXN][MAXN];
int main() {
  scanf("%d %d", &N, &M);
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < M; ++j) {
      scanf("%d", &a[i][j]);
    }
  }
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < M; ++j) {
      scanf("%d", &b[i][j]);
    }
  }
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < M; ++j) {
      if (a[i][j] > b[i][j]) {
        int temp = a[i][j];
        a[i][j] = b[i][j];
        b[i][j] = temp;
      }
    }
  }
  bool fail = false;
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < M; ++j) {
      if (i > 0 && a[i][j] <= a[i - 1][j]) {
        fail = true;
      }
      if (j > 0 && a[i][j] <= a[i][j - 1]) {
        fail = true;
      }
    }
  }
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < M; ++j) {
      if (i > 0 && b[i][j] <= b[i - 1][j]) {
        fail = true;
      }
      if (j > 0 && b[i][j] <= b[i][j - 1]) {
        fail = true;
      }
    }
  }
  if (fail) {
    printf("Impossible\n");
  } else {
    printf("Possible\n");
  }
  return 0;
}
