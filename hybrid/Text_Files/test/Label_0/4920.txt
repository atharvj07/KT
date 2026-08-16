#include <bits/stdc++.h>
using namespace std;
inline int read() {
  char c = getchar();
  int num = 0, f = 1;
  for (; !isdigit(c); c = getchar()) f = c == '-' ? -1 : f;
  for (; isdigit(c); c = getchar()) num = num * 10 + c - '0';
  return num * f;
}
const int N = 25005;
int n, m, l;
bitset<N> a, b, c, d;
char s[100005];
int main() {
  n = read(), m = read(), l = read();
  for (int i = 0; i < n; ++i) {
    scanf("%s", s);
    for (int j = 0; j < m; ++j) {
      if (s[j] == '#')
        b.set(i * m + j);
      else
        a.set(i * m + j);
      if (s[j] == 'E') d.set(i * m + j);
    }
  }
  scanf("%s", s + 1);
  c = a;
  if (c == d) {
    puts("0");
    return 0;
  }
  for (int i = 1; i <= l; ++i) {
    if (s[i] == 'U')
      c = (c >> m & a) | (c & (b << m));
    else if (s[i] == 'D')
      c = (c << m & a) | (c & (b >> m));
    else if (s[i] == 'L')
      c = (c >> 1 & a) | (c & (b << 1));
    else
      c = (c << 1 & a) | (c & (b >> 1));
    if (c == d) {
      printf("%d", i);
      return 0;
    }
  }
  puts("-1");
  return 0;
}
