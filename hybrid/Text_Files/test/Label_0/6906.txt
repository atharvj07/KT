#include <bits/stdc++.h>
template <class T>
inline void read(T &);
template <class T>
inline void write(const T &);
typedef const int &ci;
const int iinf = 2147483647;
const long long llinf = 9223372036854775807ll;
using std::abs;
using std::max;
using std::min;
using std::sort;
const int N = 300005;
const int M = 1000005;
void add(int, int);
int hed[N], nxt[M], to[M], id;
int mat[N], cnt;
bool vis[N];
int main() {
  int t;
  read(t);
  while (t--) {
    int n, m;
    read(n), read(m);
    for (int i = 1; i <= 3 * n; ++i) {
      hed[i] = vis[i] = 0;
    }
    id = 0;
    for (int i = 1; i <= m; ++i) {
      int u, v;
      read(u), read(v);
      add(u, v), add(v, u);
    }
    cnt = 0;
    for (int i = 1; i <= 3 * n; ++i) {
      if (vis[i]) {
        continue;
      }
      for (int j = hed[i]; j; j = nxt[j]) {
        int v = to[j];
        if (vis[v]) {
          continue;
        }
        vis[v] = true;
        vis[i] = true;
        mat[++cnt] = (j + 1) >> 1;
        break;
      }
    }
    if (cnt >= n) {
      puts("Matching");
      for (int i = 1; i <= n; ++i) {
        write(mat[i]), putchar(' ');
      }
      putchar('\n');
      continue;
    }
    int num = 3 * n - cnt * 2;
    if (num >= n) {
      puts("IndSet");
      cnt = 0;
      for (int i = 1; i <= 3 * n && cnt < n; ++i) {
        if (!vis[i]) {
          write(i), putchar(' ');
          ++cnt;
        }
      }
      putchar('\n');
      continue;
    }
    puts("Impossible");
  }
  return 0;
}
template <class T>
void read(T &Re) {
  T k = 0;
  char ch = getchar();
  int flag = 1;
  while (!(ch >= '0' && ch <= '9')) {
    if (ch == '-') {
      flag = -1;
    }
    ch = getchar();
  }
  while ((ch >= '0' && ch <= '9')) {
    k = (k << 1) + (k << 3) + ch - '0';
    ch = getchar();
  }
  Re = flag * k;
}
template <class T>
void write(const T &Wr) {
  if (Wr < 0) {
    putchar('-');
    write(-Wr);
  } else {
    if (Wr < 10) {
      putchar(Wr + '0');
    } else {
      write(Wr / 10);
      putchar((Wr % 10) + '0');
    }
  }
}
void add(int u, int v) {
  nxt[++id] = hed[u];
  hed[u] = id;
  to[id] = v;
}
