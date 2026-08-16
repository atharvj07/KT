#include <bits/stdc++.h>
using namespace std;
int N, M;
int E[2010], F[2010];
int main() {
  scanf("%d%d", &N, &M);
  for (int i = 1; i <= N; i++) scanf("%d", &E[i]);
  long long l = 0, r = 2e9;
  while (l <= r) {
    long long mid = (l + r) >> 1;
    int mi = 10000;
    for (int i = 1; i <= N; i++) {
      F[i] = i - 1;
      for (int j = 1; j < i; j++)
        if (abs(E[i] - E[j]) <= mid * (i - j))
          F[i] = min(F[i], F[j] + (i - j - 1));
      mi = min(mi, F[i] + N - i);
    }
    if (mi > M)
      l = mid + 1;
    else
      r = mid - 1;
  }
  cout << l << endl;
  return 0;
}
