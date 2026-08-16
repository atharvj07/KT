#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:1024000000,1024000000")
using namespace std;
const int INF = 0x3f3f3f3f;
const double inf = 0x3f3f3f3f3f3f;
const long long LNF = 0x3f3f3f3f3f3f;
const double PI = acos(-1.0);
const double eps = 1e-8;
const int maxn = 1e2 + 100;
const int mod = 1e9 + 7;
const int dr[] = {-1, 0, 1, 0};
const int dc[] = {0, 1, 0, -1};
const char *Hex[] = {"0000", "0001", "0010", "0011", "0100", "0101",
                     "0110", "0111", "1000", "1001", "1010", "1011",
                     "1100", "1101", "1110", "1111"};
int n, m;
const int mon[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
const int monn[] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
inline int Min(int a, int b) { return a < b ? a : b; }
inline int Max(int a, int b) { return a > b ? a : b; }
inline long long Min(long long a, long long b) { return a < b ? a : b; }
inline long long Max(long long a, long long b) { return a > b ? a : b; }
inline int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
inline int lcm(int a, int b) { return a * b / gcd(a, b); }
inline bool is_in(int r, int c) { return r >= 0 && r < n && c >= 0 && c < m; }
struct Node {
  int l, r;
  Node() {}
  Node(int ll, int rr) : l(ll), r(rr) {}
  bool operator<(const Node &p) const { return l < p.l; }
};
Node a[205];
int main() {
  while (scanf("%d", &n) == 1) {
    int s, d;
    int cnt = 1;
    a[0] = Node(0, 0);
    cin >> s >> d;
    printf("%d %d\n", s, s + d - 1);
    a[cnt++] = Node(s, s + d - 1);
    for (int i = 1; i < n; ++i) {
      cin >> s >> d;
      --d;
      sort(a, a + cnt);
      if (a[cnt - 1].r < s) {
        printf("%d %d\n", s, s + d);
        a[cnt++] = Node(s, s + d);
        continue;
      }
      bool ok = false;
      for (int j = 0; j < cnt - 1; ++j) {
        if (s > a[j].r && s + d < a[j + 1].l) {
          ok = true;
          printf("%d %d\n", s, s + d);
          a[cnt++] = Node(s, s + d);
          break;
        }
      }
      if (!ok) {
        bool ok1 = false;
        for (int j = 1; j < cnt; ++j) {
          if (a[j].l - a[j - 1].r > d + 1) {
            printf("%d %d\n", a[j - 1].r + 1, a[j - 1].r + d + 1);
            a[cnt++] = Node(a[j - 1].r + 1, a[j - 1].r + d + 1);
            ok1 = true;
            break;
          }
        }
        if (!ok1) {
          printf("%d %d\n", a[cnt - 1].r + 1, a[cnt - 1].r + 1 + d);
          a[cnt] = Node(a[cnt - 1].r + 1, a[cnt - 1].r + d + 1);
          ++cnt;
        }
      }
    }
  }
  return 0;
}
