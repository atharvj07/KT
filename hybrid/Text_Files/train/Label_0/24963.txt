#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 4;
const int mod = 1e9 + 7;
int dp[N];
char a[N];
int main() {
  scanf("%s", a + 1);
  int n = strlen(a + 1);
  int sum = 0;
  int ans = 0;
  int flag = 0;
  for (int i = 1; i <= n;) {
    if (a[i] == 'a') {
      dp[i] = sum + 1;
      dp[i] %= mod;
      ans += dp[i];
      ans %= mod;
    } else if (a[i] == 'b') {
      sum += ans;
      sum %= mod;
      ans = 0;
      while (a[i] != 'a' && i <= n) i++;
      i--;
    }
    i++;
  }
  sum = 0;
  for (int i = 1; i <= n; i++) {
    sum = sum + dp[i];
    sum %= mod;
  }
  cout << sum << endl;
}
