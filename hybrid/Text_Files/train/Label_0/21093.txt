#include <bits/stdc++.h>
using namespace std;
template <typename tp>
inline void read(tp& x) {
  x = 0;
  char tmp;
  bool key = 0;
  for (tmp = getchar(); !isdigit(tmp); tmp = getchar()) key = (tmp == '-');
  for (; isdigit(tmp); tmp = getchar()) x = (x << 3) + (x << 1) + (tmp ^ '0');
  if (key) x = -x;
}
template <typename tp>
inline void ckmn(tp& x, tp y) {
  x = x < y ? x : y;
}
template <typename tp>
inline void ckmx(tp& x, tp y) {
  x = x < y ? y : x;
}
struct point {
  int x, y;
  point(int x = 0, int y = 0) : x(x), y(y) {}
  point operator+(const point& a) const { return point(x + a.x, y + a.y); }
  point operator-(const point& a) const { return point(x - a.x, y - a.y); }
};
long long cross(point a, point b) { return 1ll * a.x * b.y - 1ll * a.y * b.x; }
long long dot(point a, point b) { return 1ll * a.x * b.x + 1ll * a.y * b.y; }
const int N = 1010, K = 10;
int n, k, ans, per[K], tmp, vis[N], rec;
point p1[N], p2[N];
vector<int> pat[K][N];
bool dfs(int cur) {
  if (tmp >= k) return false;
  int x = per[++tmp];
  for (int i = (0); i <= ((int)pat[x][cur].size() - 1); ++i) {
    if (vis[pat[x][cur][i]] != rec) {
      if (!dfs(pat[x][cur][i])) return false;
    }
  }
  vis[cur] = rec;
  return true;
}
int main() {
  read(k), read(n);
  for (int i = (1); i <= (k); ++i) read(p1[i].x), read(p1[i].y);
  for (int i = (1); i <= (n); ++i) read(p2[i].x), read(p2[i].y);
  for (int i = (1); i <= (k); ++i)
    for (int a = (1); a <= (n); ++a)
      for (int b = (1); b <= (n); ++b)
        if (cross(p2[b] - p1[i], p2[a] - p1[i]) == 0) {
          if (dot(p1[i] - p2[b], p2[a] - p2[b]) < 0) pat[i][a].push_back(b);
        }
  for (int i = (1); i <= (n); ++i) {
    int key = 0;
    for (int j = (1); j <= (k); ++j) per[j] = j;
    do {
      tmp = 0;
      ++rec;
      if (dfs(i)) {
        key = 1;
        break;
      }
    } while (next_permutation(per + 1, per + k + 1));
    ans += key;
  }
  cout << ans << endl;
  return 0;
}
