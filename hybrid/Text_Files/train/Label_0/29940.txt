#include <bits/stdc++.h>
using namespace std;
long long prime[1000009];
long long isprime(long long x) {
  long long i = 2, flag = 1;
  if (x == 1) return 0;
  if (prime[x] != -1) return prime[x];
  while ((i * i) <= x) {
    if (x % i == 0) {
      flag = 0;
      break;
    }
    i = i + 1;
  }
  prime[x] = flag;
  return flag;
}
int main() {
  memset(prime, -1, sizeof(prime));
  long long n, i;
  cin >> n;
  long long a[n], flag[n];
  long double x, diff;
  flag[0] = 0;
  for (i = 0; i < n; i++) {
    cin >> a[i];
    x = sqrt(a[i]);
    diff = x - (long long)x;
    if (diff != 0.0) {
      flag[i] = 0;
      continue;
    } else {
      flag[i] = isprime((long long)x);
    }
  }
  for (i = 0; i < n; i++) {
    if (flag[i])
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}
