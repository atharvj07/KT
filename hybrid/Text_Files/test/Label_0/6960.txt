#include <bits/stdc++.h>
using namespace std;
int Lower[1000000 + 1], Higher[1000000 + 1];
char Used[1000000 + 1];
long long SumNat(long long n) {
  long long p = n, q = n + 1;
  if (p % 2)
    q /= 2;
  else
    p /= 2;
  return (p) * (q);
}
long long PrimePi(long long n) {
  long long v = sqrt(n + 1e-9), p, temp, q, j, end, i, d, t;
  for (int i = 0; i <= 1000000; i++) Used[i] = 0;
  Higher[1] = n - 1;
  for (p = 2; p <= v; p++) {
    Lower[p] = p - 1;
    Higher[p] = (n / p) - 1;
  }
  for (p = 2; p <= v; p++) {
    if (Lower[p] == Lower[p - 1]) continue;
    temp = Lower[p - 1];
    q = p * p;
    Higher[1] -= Higher[p] - temp;
    j = 1 + (p & 1);
    end = (v <= n / q) ? v : n / q;
    for (i = p + j; i <= 1 + end; i += j) {
      if (Used[i]) continue;
      d = i * p;
      if (d <= v)
        Higher[i] -= Higher[d] - temp;
      else {
        t = n / d;
        Higher[i] -= Lower[t] - temp;
      }
    }
    if (q <= v)
      for (i = q; i <= end; i += p * j) Used[i] = 1;
    for (i = v; i >= q; i--) {
      t = i / p;
      Lower[i] -= Lower[t] - temp;
    }
  }
  return Higher[1];
}
bool prime[10000000 + 1];
long long piii[10000000 + 1];
long long Prim(long long n) {
  if (n <= 10000000) return piii[n];
  return PrimePi(n);
}
int main() {
  long long n, i, j;
  long long answer;
  for (i = 2; i * i <= 10000000; i++)
    if (!prime[i])
      for (j = i * i; j <= 10000000; j += i) prime[j] = true;
  for (i = 2; i <= 10000000; i++) {
    piii[i] = piii[i - 1];
    if (!prime[i]) piii[i]++;
  }
  cin >> n;
  for (i = 1;; i++) {
    if (i * i * i > n) break;
  }
  answer = Prim(i - 1);
  for (i = 2; i < (n / i); i++)
    if (!prime[i]) answer += (Prim(n / i) - Prim(i));
  cout << answer;
  return 0;
}
