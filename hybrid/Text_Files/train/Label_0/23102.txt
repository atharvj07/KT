#include <bits/stdc++.h>
using namespace std;
using INT = unsigned long long;
const int N = 100000;
int f[11111], g[11111];
struct Ring {
  INT a[5];
  Ring() {}
  void clear() { memset(a, 0, sizeof a); }
  Ring operator+(Ring r) {
    Ring R = r;
    for (int i = 0; i < 5; i++) R.a[i] += a[i];
    return R;
  }
  void operator+=(Ring r) { (*this) = (*this) + r; }
  Ring operator*(Ring r) {
    Ring R;
    R.clear();
    for (int i = 0; i < 5; i++)
      for (int j = 0; j < 5; j++) {
        R.a[f[i + j]] += a[i] * r.a[j] * g[i + j];
      }
    return R;
  }
  void operator*=(Ring r) { (*this) = (*this) * r; }
  Ring operator<<(int k) {
    Ring R;
    for (int i = 0; i < 5; i++) R.a[f[i + k]] = a[i] * g[i + k];
    return R;
  }
  INT real() { return a[0] + a[1]; }
} x[N], tmp[10];
INT power(INT a, INT n, INT ans = 1) {
  for (; n; n >>= 1, a *= a)
    if (n & 1) ans *= a;
  return ans;
}
Ring power(Ring a, INT n) {
  Ring ans;
  ans.clear();
  ans.a[0] = 1;
  for (; n; n >>= 1, a *= a)
    if (n & 1) ans *= a;
  return ans;
}
void DFT(Ring *P, int op) {
  for (int i = 1; i < N; i *= 10) {
    for (int p = i * 10, j = 0; j < N; j += p) {
      for (int k = 0; k < i; k++) {
        for (int x = 0; x < 10; x++) tmp[x] = P[j + k + x * i];
        for (int x = 0, t = 0; x < 10; x++, t += op) {
          Ring &r = P[j + k + x * i];
          r.clear();
          for (int y = 0, d = 0; y < 10; y++, d += t) r += tmp[y] << d;
        }
      }
    }
  }
}
int n;
int main() {
  memset(x, 0, sizeof x);
  scanf("%d", &n);
  for (int i = 0, k; i < n; i++) {
    scanf("%d", &k);
    x[k].a[0]++;
  }
  for (int i = 0; i < 1111; i++) f[i] = i % 5, g[i] = i % 10 < 5 ? 1 : -1;
  DFT(x, 1);
  for (int i = 0; i < N; i++) x[i] = power(x[i], n);
  DFT(x, 9);
  INT inv = power(5, (1ull << 63) - 5);
  for (int i = 0; i < n; i++)
    printf("%I64d\n", (x[i].real() >> 5) * inv & ((1ull << 58) - 1));
}
