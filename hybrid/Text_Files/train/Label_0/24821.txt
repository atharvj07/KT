#include <bits/stdc++.h>
using namespace std;
const long long N = 1e6 + 5;
long long a[N];
vector<int> vec;
long long yinzi[N];
long long summ[N];
int main() {
  long long n, m, i, j, k, ans, num = 0, sum, maxa = 0;
  scanf("%lld", &n);
  for (i = 1; i <= n; i++) {
    scanf("%lld", &a[i]);
    maxa = max(maxa, a[i]);
    if (a[i] >= 1) vec.push_back(i), num += a[i];
  }
  for (i = 0; i < vec.size(); i++) summ[i] = summ[i - 1] + vec[i];
  sum = num;
  long long tot = 0;
  for (i = 2; i * i <= sum; i++) {
    if (sum % i == 0) {
      yinzi[tot++] = i;
      while (sum % i == 0) sum /= i;
    }
    if (sum == 1) break;
  }
  if (sum != 1) yinzi[tot++] = sum;
  long long maxx, pos, maxxx, maxnum;
  ans = 1e18;
  for (i = 0; i < tot; i++) {
    maxx = maxxx = 0;
    for (j = 1; j <= n; j++) {
      maxxx += a[j];
      maxxx %= yinzi[i];
      maxx += min(maxxx, yinzi[i] - maxxx);
    }
    ans = min(ans, maxx);
  }
  if (ans == 1e18)
    printf("-1\n");
  else
    printf("%lld\n", ans);
  return 0;
}
