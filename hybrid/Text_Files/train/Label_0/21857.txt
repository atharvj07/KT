#include <bits/stdc++.h>
namespace FastIO {
template <typename T>
inline void readInteger(T& ret) {
  char ch = getchar();
  bool flag = false;
  while ((ch < '0' || ch > '9') && ch != '-') ch = getchar();
  if (ch == '-') {
    flag = true;
    ch = getchar();
  }
  ret = 0;
  while (ch >= '0' && ch <= '9') {
    ret = ret * 10 + (ch - '0');
    ch = getchar();
  }
  if (flag) ret = -ret;
}
inline int nextInt() {
  int x;
  readInteger(x);
  return x;
}
inline long long nextLong() {
  long long x;
  readInteger(x);
  return x;
}
template <typename T>
inline void outInteger(T x) {
  if (x < 0) {
    putchar('-');
    x = -x;
  }
  if (x >= 10) {
    outInteger(x / 10);
  }
  putchar(x % 10 + '0');
}
inline void newline() { putchar('\n'); }
}  // namespace FastIO
using namespace std;
using namespace FastIO;
int deg[11000];
int main() {
  int N, u, v;
  scanf("%d", &N);
  for (int i = 1; i < N; i++) {
    scanf("%d%d", &u, &v);
    u--, v--;
    deg[u]++;
    deg[v]++;
  }
  long long ans = 0;
  for (int i = 0; i < N; i++) {
    ans += (long long)deg[i] * (deg[i] - 1) / 2;
  }
  printf("%I64d\n", ans);
  return 0;
}
