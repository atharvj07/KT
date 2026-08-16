#include <bits/stdc++.h>
using namespace std;
int N, Ans, F[105][105][2];
struct Nod {
  int x, l;
} A[105];
bool Cmp(Nod a, Nod b) { return a.x < b.x; }
int main() {
  scanf("%d", &N);
  for (int i = 1; i <= N; i++) scanf("%d%d", &A[i].x, &A[i].l);
  sort(A + 1, A + N + 1, Cmp);
  A[0].x = -(1 << 30);
  for (int i = 0; i <= N; i++)
    for (int j = 0; j <= i; j++)
      for (int k = 0; k <= 1; k++) {
        int Pr = A[j].x + k * A[j].l, Max = -1, a, b;
        Ans = max(Ans, F[i][j][k]);
        for (int t = i + 1; t <= N; t++)
          for (int p = 0; p <= 1; p++) {
            int Nr = A[t].x + p * A[t].l;
            if (Nr > Max) Max = Nr, a = t, b = p;
            F[t][a][b] =
                max(F[t][a][b], F[i][j][k] + min(A[t].l, Nr - Pr) + Max - Nr);
          }
      }
  printf("%d\n", Ans);
}
