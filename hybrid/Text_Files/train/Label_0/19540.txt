#include <bits/stdc++.h>
using namespace std;
template <class T, class first>
inline bool checkbit(T a, first pos) {
  T t = 1;
  return ((a & (t << pos)) > 0);
}
template <class T, class first>
inline T setbit(T a, first pos) {
  T t = 1;
  return (a | (t << pos));
}
template <class T, class first>
inline T resetbit(T a, first pos) {
  T t = 1;
  return (a & (~(t << pos)));
}
template <class T, class first>
inline T togglebit(T a, first pos) {
  T t = 1;
  return (a ^ (t << pos));
}
template <typename T>
T POW(T B, T P) {
  if (P == 0) return 1;
  if (P & 1)
    return B * POW(B, P - 1);
  else
    return (POW(B, P / 2) * POW(B, P / 2));
}
template <typename T>
T Bigmod(T base, T power, T mod) {
  T ret = 1;
  while (power) {
    if (power & 1) ret = (ret * base) % mod;
    base = (base * base) % mod;
    power >>= 1;
  }
  return ret;
}
template <typename T>
T ModInverse(T number, T mod) {
  return Bigmod(number, mod - 2, mod);
}
template <typename T>
T GCD(T a, T b) {
  if (a < 0) return gcd(-a, b);
  if (b < 0) return gcd(a, -b);
  return (b == 0) ? a : gcd(b, a % b);
}
template <typename T>
T LCM(T a, T b) {
  if (a < 0) return lcm(-a, b);
  if (b < 0) return lcm(a, -b);
  return a * (b / gcd(a, b));
}
template <typename T>
T EUCLIDE(T a, T b, T &x, T &y) {
  if (a < 0) {
    T d = euclide(-a, b, x, y);
    x = -x;
    return d;
  }
  if (b < 0) {
    T d = euclide(a, -b, x, y);
    y = -y;
    return d;
  }
  if (b == 0) {
    x = 1;
    y = 0;
    return a;
  } else {
    T d = euclide(b, a % b, x, y);
    T t = x;
    x = y;
    y = t - (a / b) * y;
    return d;
  }
}
template <typename T>
T ABS(T a) {
  if (a < 0)
    return -a;
  else
    return a;
}
double DEG(double x) { return (180.0 * x) / ((2.0 * acos(0.0))); }
double RAD(double x) { return (x * (double)(2.0 * acos(0.0))) / (180.0); }
template <typename T>
T DIS(T x1, T y1, T x2, T y2) {
  return sqrt((double)((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
}
template <typename T>
T ANGLE(T x1, T y1, T x2, T y2) {
  return atan(double(y1 - y2) / double(x1 - x2));
}
template <typename T>
long long isLeft(T a, T b, T c) {
  return (c.x - a.x) * (b.y - a.y) - (b.x - a.x) * (c.y - a.y);
}
template <class T>
inline bool setmin(T &a, T b) {
  return a > b ? a = b, true : false;
}
template <class T>
inline bool setmax(T &a, T b) {
  return a < b ? a = b, true : false;
}
void P_ARR(int *ar, int a, int b) {
  if (a > b) swap(a, b);
  if (a <= b) cout << ar[a];
  for (int i = a + 1; i <= b; i++) cout << " " << ar[i];
  cout << endl;
}
template <typename T>
T in() {
  char ch;
  T n = 0;
  bool ng = false;
  while (1) {
    ch = getchar();
    if (ch == '-') {
      ng = true;
      ch = getchar();
      break;
    }
    if (ch >= '0' && ch <= '9') break;
  }
  while (1) {
    n = n * 10 + (ch - '0');
    ch = getchar();
    if (ch < '0' || ch > '9') break;
  }
  return (ng ? -n : n);
}
char a[5007];
char b[5007];
int ase[27];
int cnt[27];
int main() {
  scanf("%s", a + 1);
  scanf("%s", b + 1);
  int la = strlen(a + 1);
  int lb = strlen(b + 1);
  for (int i = 1; i <= la; i++) ase[a[i] - 'a']++;
  int pos = -1;
  int let = -1;
  for (int i = 1; i <= lb; i++) {
    bool flag = 1;
    for (int j = 0; j <= 25; j++)
      if (ase[j] < cnt[j]) {
        flag = 0;
        break;
      }
    if (flag)
      for (int j = 0; j <= 25; j++)
        if (ase[j] - cnt[j] > 0 && (j + 'a') > b[i]) {
          pos = i;
          let = j;
          break;
        }
    cnt[b[i] - 'a']++;
  }
  bool flag = 1;
  for (int i = 0; i <= 25; i++)
    if (ase[i] < cnt[i]) {
      flag = 0;
      break;
    }
  if (flag && la > lb) {
    for (int i = 1; i <= lb; i++) cout << b[i], ase[b[i] - 'a']--;
    for (int i = 0; i <= 25; i++)
      for (int j = 1; j <= ase[i]; j++) cout << char(i + 'a');
    puts("");
    ;
    return 0;
  }
  if (pos == -1)
    cout << -1 << endl;
  else {
    for (int i = 1; i <= pos - 1; i++) {
      cout << b[i];
      ase[b[i] - 'a']--;
    }
    cout << char(let + 'a');
    if (let >= 0) ase[let]--;
    for (int i = 0; i <= 25; i++)
      for (int j = 1; j <= ase[i]; j++) cout << char(i + 'a');
    puts("");
    ;
  }
  return 0;
}
