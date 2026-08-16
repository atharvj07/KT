#include <bits/stdc++.h>
using namespace std;
long long n, ans = 0, sum = 0, a[19] = {}, dp[20][3000];
long long subtact(long long i, long long value) {
  if (i == n) return (value % 360 == 0);
  long long answer = 0;
  answer = subtact(i + 1, (value + a[i]));
  answer |= subtact(i + 1, (value - a[i]));
  return answer;
}
int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  memset(dp, -1, sizeof dp);
  (subtact(0, 0)) ? cout << "YES" : cout << "NO";
  return 0;
}
