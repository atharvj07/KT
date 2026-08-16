#include <bits/stdc++.h>
using std::cout;
using std::endl;
using std::max;
using std::min;
using std::sort;
int read() {
  int h = 0;
  char c = getchar();
  while (c < '0' || c > '9') c = getchar();
  while (c >= '0' && c <= '9') h = (h << 1) + (h << 3) + c - '0', c = getchar();
  return h;
}
int t;
int n, m, k;
int g[4040][4040];
int gcd(int a, int b) {
  if (a <= 4000 && b <= 4000 && g[a][b]) return g[a][b];
  int ansn = (b == 0 ? a : gcd(b, a % b));
  if (a <= 4000 && b <= 4000) g[a][b] = ansn;
  return ansn;
}
struct Node {
  int pos, col;
} sta[200100];
int cnt;
bool cmp(Node x, Node y) { return x.pos < y.pos; }
void work1() {
  cnt = 0;
  if (n == m) {
    puts("Yes");
    return;
  }
  if (n > m) n ^= m ^= n ^= m;
  int gcd_ = gcd(n, m);
  long long lcm = 1ll * (n / gcd_) * m;
  for (int i = n; i < lcm; i += n) {
    sta[++cnt].pos = i;
    sta[cnt].col = 1;
  }
  for (int i = m; i < lcm; i += m) {
    sta[++cnt].pos = i;
    sta[cnt].col = 2;
  }
  sort(sta + 1, sta + cnt + 1, cmp);
  long long cntn = 1, mx = 0;
  for (int i = 2; i <= cnt; i++) {
    if (sta[i].col != sta[i - 1].col)
      cntn = 0;
    else {
      cntn++;
      mx = max(mx, cntn);
    }
  }
  if (mx < k)
    puts("Yes");
  else
    puts("No");
}
void work2() {
  if (n == m) {
    puts("OBEY");
    return;
  }
  if (n > m) n ^= m ^= n ^= m;
  long long gcd_ = gcd(n, m);
  long long cntn = (m - 1 - gcd_) / n + 1;
  if (cntn < k)
    puts("OBEY");
  else
    puts("REBEL");
}
int main() {
  t = read();
  for (int i = 1; i <= t; i++) {
    n = read(), m = read(), k = read();
    work2();
  }
  return 0;
}
