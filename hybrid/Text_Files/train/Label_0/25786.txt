#include <bits/stdc++.h>
using namespace std;
int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int m, a[5005], b[5005], p[10000], k = 0;
bool v[35000];
void make() {
  for (int i = 2; i < 35000; i++)
    if (!v[i]) {
      p[k++] = i;
      for (int j = i + i; j < 35000; j += i) v[j] = 1;
    }
}
bool Fi(int n) {
  int L = 0, R = m - 1;
  while (L <= R) {
    int mid = (L + R) >> 1;
    if (b[mid] == n) return 1;
    if (b[mid] > n)
      R = mid - 1;
    else
      L = mid + 1;
  }
  return 0;
}
int Mi(int n) {
  if (n == 1) return 1;
  for (int i = 0; i < k; i++)
    if (n % p[i] == 0) return p[i];
  return n;
}
int F(int n) {
  if (n == 1) return 0;
  int M = Mi(n);
  return F(n / M) + (Fi(M) == 1 ? -1 : 1);
}
int Cacu(int n) {
  int ans = 0;
  for (int i = 0; i < k; i++)
    if (n % p[i] == 0) {
      int w = 0;
      while (n % p[i] == 0) n /= p[i], w++;
      if (Fi(p[i]))
        ans -= w;
      else
        ans += w;
      if (n == 1) break;
    }
  if (n != 1) ans = ans + (Fi(n) == 1 ? -1 : 1);
  return ans;
}
int main() {
  make();
  int n;
  cin >> n >> m;
  for (int i = 0; i < n; i++) scanf("%d", &a[i]);
  for (int i = 0; i < m; i++) scanf("%d", &b[i]);
  if (n == 1) {
    int w = Cacu(a[0]);
    printf("%d\n", w < 0 ? 0 : w);
    return 0;
  }
  while (1) {
    int d = a[0], pos = -1, u;
    for (int i = 1; i < n; i++) {
      d = gcd(a[i], d);
      if (d == 1) break;
      if (Cacu(d) <= 0) u = d, pos = i;
    }
    for (int i = 0; i <= pos; i++) a[i] /= u;
    if (pos == -1 || gcd(a[0], a[1]) == 1) break;
  }
  int ans = 0, w = Cacu(a[0]);
  if (w > 0) ans += w;
  for (int i = 1; i < n; i++) ans += F(a[i]);
  cout << ans << endl;
  return 0;
}
