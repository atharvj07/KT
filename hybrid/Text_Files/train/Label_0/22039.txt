#include <bits/stdc++.h>
using namespace std;
const int N = 2020;
namespace Gause {
static const int N = ::N;
int equ, var;
bitset<N> a[N];
int x[N];
int free_x[N];
int free_num;
int l[N];
void ini(int n) {
  for (int i = (0); i < (n); ++i) x[i] = 0;
  for (int i = (0); i < (n); ++i) a[i].reset();
}
int Gauss() {
  int max_r, col, k;
  free_num = 0;
  for (k = 0, col = 0; k < equ && col < var; k++, col++) {
    max_r = k;
    for (int i = k + 1; i < equ; i++) {
      if (abs(a[i][col]) > abs(a[max_r][col])) max_r = i;
    }
    if (a[max_r][col] == 0) {
      k--;
      free_x[free_num++] = col;
      continue;
    }
    l[k] = col;
    if (max_r != k) {
      swap(a[k], a[max_r]);
    }
    for (int i = k + 1; i < equ; i++) {
      if (a[i][col] != 0) a[i] ^= a[k];
    }
  }
  for (int i = k; i < equ; i++) {
    if (a[i][col] != 0) return -1;
  }
  for (int i = k - 1; i >= 0; i--) {
    int t = l[i];
    x[t] = a[i][var];
    for (int j = t + 1; j < var; j++) x[t] ^= (a[i][j] & x[j]);
  }
  return 0;
}
}  // namespace Gause
int T, n, m, u, v;
bool du[N], vis[N][N];
int main() {
  std::ios::sync_with_stdio(0);
  std::cin.tie(0);
  cin >> T;
  for (int cas = (0); cas < (T); ++cas) {
    cin >> n >> m;
    Gause ::ini(n);
    for (int i = (1); i < (n + 1); ++i)
      for (int j = (1); j < (n + 1); ++j) vis[i][j] = 0;
    for (int i = (1); i < (n + 1); ++i) du[i] = 0;
    for (int i = (1); i < (m + 1); ++i) {
      cin >> u >> v;
      du[u] ^= 1;
      du[v] ^= 1;
      vis[u][v] = vis[v][u] = 1;
    }
    Gause ::equ = Gause ::var = n;
    for (int i = (1); i < (n + 1); ++i) {
      vis[i][i] = du[i];
      for (int j = (1); j < (n + 1); ++j) Gause ::a[i - 1][j - 1] = vis[i][j];
      Gause ::a[i - 1][n] = du[i];
    }
    Gause::Gauss();
    bool Vis[2] = {0};
    for (int i = (1); i < (n + 1); ++i) Vis[Gause::x[i - 1]] = 1;
    if (Vis[0] && Vis[1]) {
      cout << 2 << "\n";
    } else {
      cout << 1 << "\n";
      if (Vis[1])
        for (int i = (1); i < (n + 1); ++i) Gause::x[i - 1] = 0;
    }
    for (int i = (1); i < (n + 1); ++i) cout << Gause::x[i - 1] + 1 << " ";
    cout << "\n";
  }
  return 0;
}
