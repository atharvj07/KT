#include <bits/stdc++.h>
using namespace std;
int n, U[100010], D[100010], L[100010], R[100010], s[3010][3010], K,
    cl[3010][3010], Le[3010][3010], Up[3010][3010];
int ans[100010];
void read(int &x) {
  char ch = getchar();
  int mark = 1;
  for (; ch != '-' && (ch < '0' || ch > '9'); ch = getchar())
    ;
  if (ch == '-') mark = -1, ch = getchar();
  for (x = 0; ch >= '0' && ch <= '9'; ch = getchar()) x = x * 10 + ch - 48;
  x *= mark;
}
int Getsum(int x1, int y1, int x2, int y2) {
  return s[x2][y2] - s[x2][y1 - 1] - s[x1 - 1][y2] + s[x1 - 1][y1 - 1];
}
void Print(int x1, int y1, int x2, int y2) {
  printf("YES ");
  int cnt = 0;
  for (int i = 1; i <= n; i++)
    if (U[i] >= x1 && D[i] <= x2 && L[i] >= y1 && R[i] <= y2) ans[++cnt] = i;
  printf("%d\n", cnt);
  for (int i = 1; i <= cnt; i++) printf("%d ", ans[i]);
  printf("\n");
}
int main() {
  read(n);
  for (int i = 1; i <= n; i++) {
    read(U[i]);
    read(L[i]);
    read(D[i]);
    read(R[i]);
    U[i]++;
    L[i]++;
    K = max(K, D[i]);
    K = max(K, R[i]);
    for (int j = U[i]; j <= D[i]; j++)
      for (int k = L[i]; k <= R[i]; k++) s[j][k]++, cl[j][k] = i;
    for (int j = U[i]; j <= D[i]; j++) Le[j][L[i]] = 1;
    for (int j = L[i]; j <= R[i]; j++) Up[U[i]][j] = 1;
  }
  for (int i = 1; i <= K; i++)
    for (int j = 1; j <= K; j++)
      s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + s[i][j];
  for (int i = 1; i <= K; i++)
    for (int j = 1; j <= K; j++)
      if (Up[i][j]) Up[i][j] += Up[i][j - 1];
  for (int i = 1; i <= K; i++)
    for (int j = 1; j <= K; j++)
      if (Le[i][j]) Le[i][j] += Le[i - 1][j];
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= K; j++) {
      if (D[i] - j + 1 <= 0 || R[i] - j + 1 <= 0) break;
      if (Getsum(D[i] - j + 1, R[i] - j + 1, D[i], R[i]) != j * j) break;
      if (cl[D[i]][R[i] - j + 1] == cl[D[i] + 1][R[i] - j + 1]) break;
      if (cl[D[i] - j + 1][R[i]] == cl[D[i] - j + 1][R[i] + 1]) break;
      if (Le[D[i]][R[i] - j + 1] >= j && Up[D[i] - j + 1][R[i]] >= j) {
        Print(D[i] - j + 1, R[i] - j + 1, D[i], R[i]);
        return 0;
      }
    }
  }
  printf("NO\n");
  return 0;
}
