#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:36777216")
using namespace std;
const double pi = acos(-1.0);
const double eps = 1e-11;
const int oo = 0x3f3f3f3f;
template <class T>
inline void checkmin(T &a, T b) {
  if (b < a) a = b;
}
template <class T>
inline void checkmax(T &a, T b) {
  if (b > a) a = b;
}
template <class T>
inline T sqr(T x) {
  return x * x;
}
template <class T>
inline T lowbit(T n) {
  return (n ^ (n - 1)) & n;
}
template <class T>
inline int countbit(T n) {
  return (n == 0) ? 0 : (1 + countbit(n & (n - 1)));
}
template <class T>
inline T gcd(T a, T b) {
  T c;
  while (a != 0) {
    c = a;
    a = b % a;
    b = c;
  }
  return b;
}
template <class T>
inline T mabs(T a) {
  if (a < 0)
    return -a;
  else
    return a;
}
typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<string> VS;
const int N = (int)14;
const int MOD = (int)1e9 + 7;
long long a[N], ta[N];
inline int solve(int testnum) {
  for (int i = (0); i < int(N); i++) scanf("%lld", &a[i]);
  long long res = -1;
  for (int i = (0); i < int(N); i++) {
    long long v = a[i];
    if (!v) continue;
    for (int j = (0); j < int(N); j++) ta[j] = i == j ? 0 : a[j];
    if (v > N) {
      long long add = v / N, rem = v % N;
      for (int i = (0); i < int(N); i++) ta[i] += add;
      for (int j = (i + 1) % N; rem > 0; j = (j + 1) % N) ta[j]++, rem--;
    } else {
      for (int j = (i + 1) % N; v > 0; j = (j + 1) % N) ta[j]++, v--;
    }
    long long cnt = 0LL;
    for (int j = (0); j < int(N); j++)
      if (ta[j] % 2 == 0) cnt += ta[j];
    checkmax(res, cnt);
  }
  printf("%lld\n", res);
  return 0;
}
int main(int argc, char *argv[]) {
  ios::sync_with_stdio(false);
  int t = 1;
  if (argc > 1) t = atoi(argv[1]);
  for (int _t = (1); _t < int(t + 1); _t++) {
    int ret = ::solve(_t);
    if (ret == -1) {
      cerr << "Failed test #" << _t << endl;
      break;
    }
    cerr << "Solved test #" << _t << endl;
  }
  return 0;
}
