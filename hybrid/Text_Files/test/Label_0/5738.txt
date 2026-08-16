#include <bits/stdc++.h>
using namespace std;
long long int a[200005];
int main() {
  long long int n, k;
  scanf("%lld", &n), scanf("%lld", &k);
  for (long long int i = 1; i <= n; ++i) {
    scanf("%lld", &a[i]);
  }
  long long int total = n;
  long long int acc = 0LL;
  long long int j = 1LL;
  for (long long int i = 1; i <= n; ++i) {
    long long sub = (long long)((j - 1) * (total - j) * a[i]);
    if ((acc - sub) < k) {
      printf("%lld\n", i);
      --total;
    } else {
      long long val = (long long)(a[i] * (j - 1));
      acc += val;
      ++j;
    }
  }
  return 0;
}
