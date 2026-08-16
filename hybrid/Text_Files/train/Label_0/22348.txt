#include <bits/stdc++.h>
using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
long long mul(long long a, long long b) { return (a * b) % (1000000007); }
long long add(long long a, long long b) { return (a + b) % (1000000007); }
long long sub(long long a, long long b) {
  return ((a - b) % (1000000007) + (1000000007)) % (1000000007);
}
void upd(long long &a, long long b) {
  a = (a % (1000000007) + b % (1000000007)) % (1000000007);
}
inline int read() {
  int x = 0, f = 1;
  char ch = getchar();
  while (!isdigit(ch)) {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (isdigit(ch)) {
    x = x * 10 + ch - '0';
    ch = getchar();
  }
  return x * f;
}
long long a2[1234567], a[1234567];
long long c[2500000] = {};
long long abs2(long long a) { return max(a, -a); }
int main() {
  int n = read();
  for (int i = 1; i <= n; i++) a[i] = read() - i, a2[i] = a[i] + i;
  long long ans = 0;
  for (int i = 1; i <= n; i++) ans += abs2(a[i]);
  long long p = 0, lcnt = 0;
  for (int i = 1; i <= n; i++)
    if (a[i] < 0)
      lcnt++;
    else
      c[a[i]]++;
  long long m1 = 0, m2 = ans;
  for (int i = 1; i <= n - 1; i++) {
    int v = a[n - i + 1];
    ans -= abs2(v + n - i + 1 - n);
    if (v < i - 1)
      lcnt--;
    else
      c[v]--;
    v += n;
    lcnt += c[i - 1];
    c[i - 1] = 0;
    ans += lcnt - (n - lcnt - 1);
    if (v <= i - 1)
      lcnt++;
    else
      c[v]++;
    ans += abs2(v - i);
    if (ans < m2) {
      m2 = ans;
      m1 = i;
    }
  }
  cout << m2 << ' ' << m1 << endl;
  return 0;
}
