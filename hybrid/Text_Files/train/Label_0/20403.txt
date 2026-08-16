#include <bits/stdc++.h>
using namespace std;
long long N, T, ans = 0;
int M;
long long C[41][41];
long long solve(long long pos, long long len, int level, int L) {
  if (L < 0 || level < L) return 0;
  if (len == 1) return 1;
  if (pos > len / 2) {
    return (level - 1 >= 0 && L >= 0 ? C[level - 1][L] : 0) +
           solve(pos - len / 2, len / 2, level - 1, L - 1);
  }
  return solve(pos, len / 2, level - 1, L);
}
int main() {
  cin >> N >> T;
  C[0][0] = 1;
  for (int i = 1; i <= 40; ++i) {
    for (int j = 0; j <= i; ++j) {
      if (j == 0 || j == i) {
        C[i][j] = 1;
      } else {
        C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
      }
    }
  }
  int L = log2(T);
  if (1ll << L != T) {
    cout << 0 << endl;
  } else {
    long long ans = 0;
    int level = 1;
    long long total = 0;
    for (;;) {
      total += 1ll << level;
      if (total >= N) break;
      ++level;
    }
    for (int i = 1; i <= level - 1; ++i) {
      ans += C[i][L];
    }
    ans += solve(N - total + (1ll << level), 1ll << level, level, L);
    cout << ans << endl;
  }
}
