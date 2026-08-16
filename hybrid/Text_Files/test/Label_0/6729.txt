#include <bits/stdc++.h>
using namespace std;
inline int read(register int ans = 0, register int sgn = ' ',
                register int ch = getchar()) {
  for (; ch < '0' || ch > '9'; sgn = ch, ch = getchar())
    ;
  for (; ch >= '0' && ch <= '9'; (ans *= 10) += ch - '0', ch = getchar())
    ;
  return sgn - '-' ? ans : -ans;
}
struct Hash {
  int h1, h2;
  Hash() {}
  Hash(int _h1, int _h2) { h1 = _h1, h2 = _h2; }
  inline Hash operator+(Hash b) {
    return Hash((h1 + b.h1) % 1004535809, (h2 + b.h2) % 1000000009);
  }
  inline Hash operator-(Hash b) {
    return Hash((h1 + 1004535809 - b.h1) % 1004535809,
                (h2 + 1000000009 - b.h2) % 1000000009);
  }
  inline Hash operator*(Hash b) {
    return Hash((long long)h1 * b.h1 % 1004535809,
                (long long)h2 * b.h2 % 1000000009);
  }
  inline bool operator==(Hash b) { return h1 == b.h2 && h2 == b.h2; }
  inline bool operator!=(Hash b) { return h1 ^ b.h1 || h2 ^ b.h2; }
} B[100000 + 5];
inline bool operator<(Hash a, Hash b) {
  return a.h1 ^ b.h1 ? a.h1 < b.h1 : a.h2 < b.h2;
}
map<Hash, int> G;
char _c[2];
long long Ans;
struct Tree {
  vector<int> e[100000 + 5];
  Hash h[100000 + 5];
  int fa[100000 + 5], n;
  Tree() { n = 1; }
  inline int New(int f, char _c) {
    return h[++n] = Hash(_c, _c), e[fa[n] = f].push_back(n), n;
  }
} T[2];
int main() {
  static int q;
  static Hash h;
  q = read();
  B[0] = Hash(1, 1), B[1] = Hash(313, 313);
  for (register int i = 2; i <= q + 1; B[i] = B[i - 1] * B[1], i++)
    ;
  Ans = G[Hash(0, 0)] = 1;
  for (register int j, o, f; q--; printf("%I64d\n", Ans))
    if (o = read() - 1, f = read(), scanf("%s", _c), j = T[o].New(f, _c[0]),
        o) {
      for (h = Hash(0, 0); j; ++G[h], h = h * B[1] + T[1].h[j], j = T[1].fa[j])
        ;
      for (Ans = 0, j = 1; j <= T[0].n;
           Ans += G.count(T[0].h[j]) ? G[T[0].h[j]] : 0, j++)
        ;
    } else
      T[0].h[j] = T[0].h[T[0].fa[j]] * B[1] + T[0].h[j],
      Ans += G.count(T[0].h[j]) ? G[T[0].h[j]] : 0;
  return 0;
}
