#include <bits/stdc++.h>
using namespace std;
void sf(int &x) { scanf("%d", &x); }
void sf(long long &x) { scanf("%lld", &x); }
void sf(long long &x, long long &y) { scanf("%lld%lld", &x, &y); }
void sf(float &x) { scanf("%f", &x); }
void sf(double &x) { scanf("%lf", &x); }
void sf(int &x, int &y) { scanf("%d%d", &x, &y); }
void sf(float &x, float &y) { scanf("%f%f", &x, &y); }
void sf(double &x, double &y) { scanf("%lf%lf", &x, &y); }
void sf(double &x, double &y, double &z) { scanf("%lf%lf%lf", &x, &y, &z); }
void sf(int &x, int &y, int &z) { scanf("%d%d%d", &x, &y, &z); }
void sf(long long &x, long long &y, long long &z) {
  scanf("%lld%lld%lld", &x, &y, &z);
}
void sf(float &x, float &y, float &z) { scanf("%u%u%u", &x, &y, &z); }
void sf(char &x) { x = getchar(); }
void sf(char *s) { scanf("%s", s); }
void sf(string &s) { cin >> s; }
void pf(int x) { printf("%d\n", x); }
void pf(int x, int y) { printf("%d %d\n", x, y); }
void pf(long long x, long long y) { printf("%lld %lld\n", x, y); }
void pf(int x, int y, int z) { printf("%d %d %d\n", x, y, z); }
void pf(long long x) { printf("%lld\n", x); }
void pf(float x) { printf("%u\n", x); }
void pf(double x) { printf("%.6lf\n", x); }
void pf(double x, double y) { printf("%.5lf %.5lf\n", x, y); }
void pf(char x) { printf("%c\n", x); }
void pf(char *x) { printf("%s\n", x); }
void pf(string x) {
  cout << x;
  puts("");
}
template <class T>
T bigmod(T b, T p, T m) {
  if (p == 0) return 1 % m;
  T x = b;
  T ans = 1;
  while (p) {
    if (p & 1) ans = (ans * x) % m;
    p >>= 1;
    x = (x * x) % m;
  }
  return ans;
}
template <class T>
T gcd(T x, T y) {
  if (y == 0) return x;
  return gcd(y, x % y);
}
template <typename T>
T POW(T b, T p) {
  if (p == 1) return b;
  if (p % 2 == 0) {
    T s = POW(b, p / 2);
    return s * s;
  }
  return b * POW(b, p - 1);
}
template <typename T>
T modinv(T num, T m) {
  return bigmod(num, m - 2, m);
}
int n;
string s, ss;
int main() {
  cin >> n >> s;
  int l = s.size();
  n--;
  int an = l;
  while (n--) {
    sf(ss);
    int k = 0;
    for (int i = 0; i < l; i++) {
      if (s[i] != ss[i]) break;
      k++;
    }
    if (an > k) an = k;
  }
  pf(an);
  return 0;
}
