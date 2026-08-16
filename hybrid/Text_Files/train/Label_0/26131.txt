#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("Ofast,no-stack-protector")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("unroll-loops")
int on_bit(int N, int pos) { return N = N | (1 << pos); }
int off_bit(int N, int pos) { return N = N & ~(1 << pos); }
bool check_bit(long long int N, int pos) { return (bool)(N & (1 << pos)); }
template <class T>
inline bool read(T &x) {
  int c = getchar();
  int sgn = 1;
  while (~c && c < '0' || c > '9') {
    if (c == '-') sgn = -1;
    c = getchar();
  }
  for (x = 0; ~c && '0' <= c && c <= '9'; c = getchar()) x = x * 10 + c - '0';
  x *= sgn;
  return ~c;
}
int cap[200005];
int water[200005];
int parent[200005];
int find_parent(int x) {
  if (parent[x] == x) return x;
  return parent[x] = find_parent(parent[x]);
}
int main() {
  int n;
  cin >> n;
  for (int i = 0; i <= n + 2; i++) {
    parent[i] = i;
    water[i] = 0;
  }
  for (int i = 1; i <= n; i++) cin >> cap[i];
  int q;
  cin >> q;
  while (q--) {
    int x, y;
    cin >> x;
    if (x == 1) {
      cin >> x >> y;
      if (cap[find_parent(x)] - water[find_parent(x)] >= y)
        water[find_parent(x)] += y;
      else {
        y -= (cap[find_parent(x)] - water[find_parent(x)]);
        water[find_parent(x)] = cap[find_parent(x)];
        while (find_parent(x) <= n) {
          parent[find_parent(x)] = find_parent(x) + 1;
          if (cap[find_parent(x)] - water[find_parent(x)] >= y) {
            water[find_parent(x)] += y;
            break;
          } else {
            y -= (cap[find_parent(x)] - water[find_parent(x)]);
            water[find_parent(x)] = cap[find_parent(x)];
          }
        }
      }
    } else {
      cin >> x;
      cout << water[x] << "\n";
    }
  }
  return 0;
}
