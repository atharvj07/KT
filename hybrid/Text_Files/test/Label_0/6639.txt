#include <bits/stdc++.h>
#pragma GCC optimize("Ofast,inline")
#pragma GCC target( \
    "sse,sse2,sse3,ssse3,sse4,sse4.1,sse4.2,popcnt,abm,mmx,avx,avx2,tune=native")
#pragma GCC optimize(1)
#pragma G++ optimize(1)
#pragma GCC optimize(2)
#pragma G++ optimize(2)
#pragma GCC optimize(3)
#pragma G++ optimize(3)
#pragma GCC optimize("-funsafe-loop-optimizations")
#pragma GCC optimize("-funroll-loops")
#pragma GCC optimize("-fwhole-program")
#pragma GCC optimize("-fthread-jumps")
#pragma GCC optimize("-falign-functions")
#pragma GCC optimize("-falign-jumps")
#pragma GCC optimize("-falign-loops")
#pragma GCC optimize("-falign-labels")
#pragma GCC optimize("-fcaller-saves")
#pragma GCC optimize("-fcrossjumping")
#pragma GCC optimize("-fcse-follow-jumps")
#pragma GCC optimize("-fcse-skip-blocks")
#pragma GCC optimize("-fdelete-null-pointer-checks")
#pragma GCC optimize("-fexpensive-optimizations")
#pragma GCC optimize("-fgcse")
#pragma GCC optimize("-fgcse-lm")
#pragma GCC optimize("-finline-small-functions")
#pragma GCC optimize("-findirect-inlining")
#pragma GCC optimize("-foptimize-sibling-calls")
#pragma GCC optimize("-fpeephole2")
#pragma GCC optimize("-freorder-blocks")
#pragma GCC optimize("-freorder-functions")
#pragma GCC optimize("-frerun-cse-after-loop")
#pragma GCC optimize("-fsched-interblock")
#pragma GCC optimize("-fsched-spec")
#pragma GCC optimize("-fschedule-insns")
#pragma GCC optimize("-fschedule-insns2")
#pragma GCC optimize("-fstrict-aliasing")
#pragma GCC optimize("-fstrict-overflow")
#pragma GCC optimize("-ftree-switch-conversion")
#pragma GCC optimize("-ftree-pre")
#pragma GCC optimize("-ftree-vrp")
using namespace std;
inline void rdl(long long &val) {
  long long x = 0;
  int f = 1;
  char ch = getchar();
  while ((ch < '0' or ch > '9') and ch != '-') ch = getchar();
  if (ch == '-') {
    f = -1;
    ch = getchar();
  }
  while (ch >= '0' and ch <= '9') {
    x = (x << 3) + (x << 1) + ch - '0';
    ch = getchar();
  }
  val = x * f;
}
inline void rdi(int &val) {
  int x = 0;
  int f = 1;
  char ch = getchar();
  while ((ch < '0' or ch > '9') and ch != '-') ch = getchar();
  if (ch == '-') {
    f = -1;
    ch = getchar();
  }
  while (ch >= '0' and ch <= '9') {
    x = (x << 3) + (x << 1) + ch - '0';
    ch = getchar();
  }
  val = x * f;
}
inline long long rdl() {
  long long x = 0;
  int f = 1;
  char ch = getchar();
  while ((ch < '0' or ch > '9') and ch != '-') ch = getchar();
  if (ch == '-') {
    f = -1;
    ch = getchar();
  }
  while (ch >= '0' and ch <= '9') {
    x = (x << 3) + (x << 1) + ch - '0';
    ch = getchar();
  }
  return x * f;
}
inline int rdi() {
  int x = 0;
  int f = 1;
  char ch = getchar();
  while ((ch < '0' or ch > '9') and ch != '-') ch = getchar();
  if (ch == '-') {
    f = -1;
    ch = getchar();
  }
  while (ch >= '0' and ch <= '9') {
    x = (x << 3) + (x << 1) + ch - '0';
    ch = getchar();
  }
  return x * f;
}
inline void write(int x) {
  if (x < 0) putchar('-'), x = -x;
  if (x > 9) write(x / 10);
  putchar(x % 10 + '0');
}
inline void _write(int x) {
  write(x);
  putchar(' ');
}
inline void print(int x) {
  write(x);
  putchar('\n');
}
inline void write(long long x) {
  if (x < 0) putchar('-'), x = -x;
  if (x > 9) write(x / 10);
  putchar(x % 10 + '0');
}
inline void _write(long long x) {
  write(x);
  putchar(' ');
}
inline void print(long long x) {
  write(x);
  putchar('\n');
}
string s;
inline int get(int x, int y, char c) {
  if (c == '&') return x & y;
  if (c == '|') return x | y;
  if (c == '^') return x ^ y;
}
inline int go() {
  char op, c = getchar();
  int l, r, rt = 0;
  if (c == '(') {
    l = go();
    op = getchar();
    r = go();
    getchar();
    for (int i = (0); i <= (3); ++i)
      if (l & (1 << i))
        for (int j = (0); j <= (3); ++j)
          if (r & (1 << j)) rt |= 1 << get(i, j, op);
    return rt;
  }
  if (c == '0') return 1;
  if (c == '1') return 8;
  return 6;
}
int main() {
  scanf("%*d ");
  int ans = go();
  if (ans & 6)
    cout << "YES\n";
  else
    cout << "NO\n";
  return 0;
}
