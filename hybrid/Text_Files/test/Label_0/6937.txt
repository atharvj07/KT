#include <bits/stdc++.h>
using namespace std;
int n, q, p;
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
inline unsigned int C(int n, int r) {
  vector<int> tmp;
  for (int i = 1; i <= r; i++) tmp.push_back(n - i + 1);
  for (int i = 1; i <= r; i++) {
    int zjk = i;
    for (auto &t : tmp)
      if (t != 1) {
        int g = gcd(zjk, t);
        zjk /= g, t /= g;
      }
  }
  unsigned int res = 1;
  for (auto t : tmp) res *= t;
  return res;
}
inline unsigned int Pow(unsigned int x, int y) {
  unsigned int res = 1;
  for (; y; y >>= 1, x *= x)
    if (y & 1) res *= x;
  return res;
}
unsigned int t[150];
int main() {
  scanf("%d%d%d", &n, &p, &q), p = min(p, n - 1);
  for (int i = 0; i <= p; i++) t[i] = C(n, i);
  unsigned int res = 0;
  for (int i = 1; i <= q; i++) {
    unsigned int tmp = 0;
    for (int j = 0; j <= p; j++) tmp += t[j] * Pow(i, j);
    res ^= tmp * i;
  }
  printf("%u\n", res);
  return 0;
}
