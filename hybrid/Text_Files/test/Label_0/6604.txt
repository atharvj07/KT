#include <bits/stdc++.h>
using namespace std;
int si();
long long sl();
string ss(int);
char sc();
float sf();
double sd();
long double sld();
template <typename T>
void print(T, char = '\n');
template <typename T, typename... Args>
void print(T, Args...);
void pi(const int&, char = '\n');
void pl(const long long&, char = '\n');
void pf(const float&, char = '\n');
void pc(const char&, char = '\n');
void pd(const double&, char = '\n');
void pld(const long double&, char = '\n');
void ps(const string&, char = '\n');
template <typename T>
void pv(const vector<T>& v, char = ' ', char = '\n');
template <typename It>
void out(It begin, It end, char = ' ', char = '\n');
long long russian(long long, long long, long long);
long long fastpow(long long, long long, long long);
long long slowpow(long long, long long, long long);
long long _gcd(long long, long long);
long long _lcm(long long, long long);
long long extgcd(long long, long long, long long&, long long&);
long long _inv(long long, long long);
const int INF = 1e9;
const long long LINF = 1e18;
const int N = (1 << 17) + 7;
bool A[N];
int DP[N][2][2];
int main() {
  int n = (1 << si()), k = si();
  while (k--) A[si() - 1] = true;
  for (int i = 1; i < n; ++i)
    for (int t1 = 0; t1 < 2; ++t1)
      for (int t2 = 0; t2 < 2; ++t2) DP[i][t1][t2] = -INF;
  for (int i = 0; i < n; i += 2) {
    int t1 = A[i], t2 = A[i + 1];
    int idx = (i + n) >> 1;
    int val = t1 || t2 ? 1 : 0;
    DP[idx][t1][t2] = DP[idx][t2][t1] = val;
  }
  for (int i = (n >> 1) - 1; i > 0; --i) {
    int left = i << 1;
    int right = left + 1;
    for (int t1 = 0; t1 < 2; ++t1)
      for (int t2 = 0; t2 < 2; ++t2) {
        for (int l1 = 0; l1 < 2; ++l1)
          for (int l2 = 0; l2 < 2; ++l2)
            for (int r1 = 0; r1 < 2; ++r1)
              for (int r2 = 0; r2 < 2; ++r2) {
                if (t1 != l1 && t1 != r1) continue;
                int valup = l1 || r1 ? 1 : 0;
                int down = t1 == l1 ? r1 : l1;
                if (t2 != down && t2 != l2 && t2 != r2) continue;
                int valdown = r2 || l2 ? 1 : 0;
                int valadd =
                    t2 == down ? (t2 || valdown ? 1 : 0) : (t2 || down ? 1 : 0);
                DP[i][t1][t2] =
                    max(DP[i][t1][t2], DP[left][l1][l2] + DP[right][r1][r2] +
                                           valup + valdown + valadd);
              }
      }
  }
  int res = 0;
  for (int t1 = 0; t1 < 2; ++t1)
    for (int t2 = 0; t2 < 2; ++t2)
      res = max(res, DP[1][t1][t2] + (t1 || t2 ? 1 : 0));
  pi(res);
  return 0;
}
template <typename T>
T scanf_t(string&& token) {
  T a;
  scanf(token.c_str(), &a);
  return a;
}
int si() { return scanf_t<int>("%d"); }
long long sl() { return scanf_t<long long>("%lld"); }
string ss(int n) {
  char T[n + 7];
  scanf("%s", T);
  return string(T);
}
char sc() { return scanf_t<char>(" %c"); }
float sf() { return scanf_t<float>("%f"); }
double sd() { return scanf_t<double>("%lf"); }
long double sld() { return scanf_t<long double>("%Lf"); }
template <typename T>
void print(T a, char sep) {
  string token;
  if (is_same<T, int>::value)
    token = "%d";
  else if (is_same<T, long long>::value)
    token = "%lld";
  else if (is_same<T, string>::value)
    token = "%s";
  else if (is_same<T, char>::value)
    token = "%c";
  else if (is_same<T, float>::value)
    token = "%.6f";
  else if (is_same<T, double>::value)
    token = "%.8lf";
  else if (is_same<T, long double>::value)
    token = "%.10Lf";
  token.push_back(sep);
  printf(token.c_str(), a);
}
template <typename T, typename... Args>
void print(T first, Args... rest) {
  print(first, ' ');
  print(rest...);
}
void pi(const int& a, char sep) { printf("%d%c", a, sep); }
void pl(const long long& a, char sep) { printf("%lld%c", a, sep); }
void pf(const float& a, char sep) { printf("%.6f%c", a, sep); }
void pc(const char& a, char sep) { printf("%c%c", a, sep); }
void pd(const double& a, char sep) { printf("%.8lf%c", a, sep); }
void pld(const long double& a, char sep) { printf("%.12Lf%c", a, sep); }
void ps(const string& a, char sep) { printf("%s%c", a.c_str(), sep); }
template <typename It>
void out(It begin, It end, char sep, char endl) {
  if (begin == end) {
    printf("%c", endl);
    return;
  }
  while (begin + 1 != end) print(*begin, sep), ++begin;
  if (begin != end) print(*begin, ' '), printf("%c", endl);
}
template <typename T>
void pv(const vector<T>& v, char sep, char endl) {
  out(v.begin(), v.end(), sep, endl);
}
long long russian(long long a, long long k, long long m) {
  long long res = 0;
  while (k) {
    if (k & 1LL) res = (res + a) % m;
    a = (a + a) % m;
    k >>= 1LL;
  }
  return res;
}
long long fastpow(long long a, long long k, long long m) {
  long long res = 1;
  while (k) {
    if (k & 1LL) res = (res * a) % m;
    a = (a * a) % m;
    k >>= 1LL;
  }
  return res;
}
long long slowpow(long long a, long long k, long long m) {
  long long res = 1;
  while (k) {
    if (k & 1LL) res = russian(res, a, m);
    a = russian(a, a, m);
    k >>= 1LL;
  }
  return res;
}
long long _gcd(long long a, long long b) {
  while (b) swap(a %= b, b);
  return a;
}
long long _lcm(long long a, long long b) { return a / _gcd(a, b) * b; }
long long extgcd(long long a, long long b, long long& k, long long& l) {
  if (b == 0) {
    k = 1;
    l = 0;
    return a;
  }
  long long res = extgcd(a, a % b, l, k);
  l -= a / b * k;
  return res;
}
long long _inv(long long a, long long p) { return fastpow(a, p - 2, p); }
