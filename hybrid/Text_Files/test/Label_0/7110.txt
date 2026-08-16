#include <bits/stdc++.h>
using namespace std;
const int MOD = 1000000009;
int N, M, K, dp[100005][35];
char s[100005], t[100005];
long long hsh1[100005], hsh2[100005], power[100005];
inline long long substrHash(int l, int r, long long hsh[]) {
  return (hsh[r] - (hsh[l - 1] * power[r - l + 1] % MOD) + MOD) % MOD;
}
inline int lcp(int f, int s) {
  int low = 0, high = min(N - f, M - s), ans = 0;
  while (low <= high) {
    int mid = (low + high) / 2;
    if (substrHash(f + 1, f + mid, hsh1) == substrHash(s + 1, s + mid, hsh2)) {
      ans = mid;
      low = mid + 1;
    } else
      high = mid - 1;
  }
  return ans;
}
int main() {
  scanf("%d %s", &N, s + 1);
  scanf(" %d %s", &M, t + 1);
  scanf(" %d", &K);
  power[0] = 1;
  for (int i = 1; i <= N; i++) {
    hsh1[i] = (hsh1[i - 1] * 131 + s[i]) % MOD;
    power[i] = power[i - 1] * 131 % MOD;
  }
  for (int i = 1; i <= M; i++) {
    hsh2[i] = (hsh2[i - 1] * 131 + t[i]) % MOD;
    power[i] = power[i - 1] * 131 % MOD;
  }
  for (int i = 0; i < N; i++) {
    for (int g = 0; g <= K; g++) {
      dp[i + 1][g] = max(dp[i + 1][g], dp[i][g]);
      if (g != K) {
        int nxt = lcp(i, dp[i][g]);
        dp[i + nxt][g + 1] = max(dp[i + nxt][g + 1], dp[i][g] + nxt);
      }
    }
  }
  bool f = false;
  for (int i = 1; i <= K; i++) f |= (dp[N][i] == M);
  if (f)
    printf("YES\n");
  else
    printf("NO\n");
}
