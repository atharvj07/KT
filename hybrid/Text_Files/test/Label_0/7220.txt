#include <bits/stdc++.h>
using namespace std;
bool prime(int x) {
  if (x <= 1) return false;
  if (x <= 3) return true;
  if (x % 3 == 0 || x % 2 == 0) return false;
  for (int i = 5; i <= x / i; i += 6) {
    if ((x % i == 0) || (x % (i + 2) == 0)) return false;
  }
  return true;
}
bool _prime(int x) {
  for (int i = 2; i <= x / i; i++) {
    if (x % i == 0) return false;
  }
  return true;
}
int cal(int n, int k) {
  if (!prime(k)) return 0;
  if (k >= n) return (k == n);
  int res = n / k;
  for (int i = 2; i < k && i <= n / k; i++) {
    res -= cal(n / k, i);
  }
  return res;
}
int main() {
  int a, b, k;
  scanf("%d%d%d", &a, &b, &k);
  printf("%d\n", cal(b, k) - cal(a - 1, k));
  return 0;
}
