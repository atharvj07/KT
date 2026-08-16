#include <bits/stdc++.h>
using namespace std;
const int N = 1009;
char A[N];
int F[N];
int main() {
  int n, account, i, maxx, len;
  while (scanf("%d", &n) != EOF) {
    memset(F, 0, sizeof(F));
    account = 0;
    scanf("%s", A);
    len = n;
    for (i = 0; i < len; i++)
      if (A[i] == 'T') account++;
    maxx = 0;
    if (A[0] == 'T') F[0] = 1;
    for (i = 1; i < len; i++) {
      if (A[i] == 'T')
        F[i] = F[i - 1] + 1;
      else
        F[i] = F[i - 1];
    }
    maxx = max(maxx, F[account - 1]);
    for (i = 1; i <= len - account; i++) {
      maxx = max(maxx, F[account + i - 1] - F[i - 1]);
    }
    for (i = len - account + 1; i < len; i++) {
      maxx = max(maxx, F[len - 1] - F[i - 1] + F[account - len + i - 1]);
    }
    printf("%d\n", account - maxx);
  }
  return 0;
}
