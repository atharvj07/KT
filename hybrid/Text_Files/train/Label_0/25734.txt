#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = double;
const ll MODBASE = 1000000007LL;
const int MAXN = 110;
const int MAXM = 1000;
const int MAXK = 16;
const int MAXQ = 200010;
int t, a[4][2], b[4][2], dir[4], range[4][2], resZ[4], resDir[4], c[4][2];
pair<int, int> common(int l, int r, int u, int v) {
  pair<int, int> res = pair<int, int>(max(l, u), min(r, v));
  if (res.first <= res.second) return res;
  return pair<int, int>(-1e9, -1e9);
}
bool process(int len) {
  for (int i = (0); i <= (3); i++) {
    int nex = (i + 1) % 4;
    int w = i % 2;
    if (dir[i] != dir[nex]) {
      if (dir[i] == 1 - w) {
        int diff = abs(b[i][1 - dir[i]] - b[nex][dir[nex]]);
        if (len < diff) return false;
        range[i][0] = range[i][1] = b[i][1 - dir[i]];
      } else {
        int diff = abs(b[i][dir[i]] - b[nex][1 - dir[nex]]);
        if (len < diff) return false;
        range[i][0] = range[i][1] = b[nex][1 - dir[nex]];
      }
    } else {
      if (dir[i] == 1 - w) {
        if (b[i][1 - dir[i]] != b[nex][1 - dir[nex]]) return false;
        range[i][0] = range[i][1] = b[i][1 - dir[i]];
      } else {
        int diff = abs(b[i][dir[i]] - b[nex][dir[nex]]);
        if (len * 2 < diff) return false;
        range[i][0] = max(b[i][dir[i]], b[nex][dir[nex]]) - len;
        range[i][1] = min(b[i][dir[i]], b[nex][dir[nex]]) + len;
      }
    }
  }
  return true;
}
bool solve(int len) {
  if (!process(len)) return false;
  int Min = 1e9, Max = 0;
  pair<int, int> q1 =
      common(range[0][0], range[0][1], range[2][0], range[2][1]);
  for (int i = (0); i <= (1); i++)
    for (int j = (0); j <= (1); j++)
      Max = max(Max, abs(range[0][i] - range[2][j]));
  if (q1.first == -1e9) {
    for (int i = (0); i <= (1); i++)
      for (int j = (0); j <= (1); j++)
        Min = min(Min, abs(range[0][i] - range[2][j]));
  } else {
    Min = 0;
  }
  int Min2 = 1e9, Max2 = 0;
  pair<int, int> q2 =
      common(range[1][0], range[1][1], range[3][0], range[3][1]);
  for (int i = (0); i <= (1); i++)
    for (int j = (0); j <= (1); j++)
      Max2 = max(Max2, abs(range[1][i] - range[3][j]));
  if (q2.first == -1e9) {
    for (int i = (0); i <= (1); i++)
      for (int j = (0); j <= (1); j++)
        Min2 = min(Min2, abs(range[1][i] - range[3][j]));
  } else {
    Min2 = 0;
  }
  pair<int, int> q = common(Min, Max, Min2, Max2);
  if (q.first == -1e9) return false;
  if (q.second == 0) return false;
  return true;
}
void solve2(int len) {
  process(len);
  int Min = 1e9, Max = 0;
  pair<int, int> q1 =
      common(range[0][0], range[0][1], range[2][0], range[2][1]);
  for (int i = (0); i <= (1); i++)
    for (int j = (0); j <= (1); j++)
      Max = max(Max, abs(range[0][i] - range[2][j]));
  if (q1.first == -1e9) {
    for (int i = (0); i <= (1); i++)
      for (int j = (0); j <= (1); j++)
        Min = min(Min, abs(range[0][i] - range[2][j]));
  } else {
    Min = 0;
  }
  int Min2 = 1e9, Max2 = 0;
  pair<int, int> q2 =
      common(range[1][0], range[1][1], range[3][0], range[3][1]);
  for (int i = (0); i <= (1); i++)
    for (int j = (0); j <= (1); j++)
      Max2 = max(Max2, abs(range[1][i] - range[3][j]));
  if (q2.first == -1e9) {
    for (int i = (0); i <= (1); i++)
      for (int j = (0); j <= (1); j++)
        Min2 = min(Min2, abs(range[1][i] - range[3][j]));
  } else {
    Min2 = 0;
  }
  pair<int, int> q = common(Min, Max, Min2, Max2);
  int p = q.first;
  if (p == 0) p++;
  pair<int, int> x, y;
  int u = range[0][0] + p, v = range[0][1] + p;
  q = common(u, v, range[2][0], range[2][1]);
  if (q.first != -1e9) {
    x.second = q.first;
    x.first = q.first - p;
  } else {
    u = range[0][0] - p;
    v = range[0][1] - p;
    q = common(u, v, range[2][0], range[2][1]);
    x.second = q.first;
    x.first = q.first + p;
  }
  u = range[1][0] + p;
  v = range[1][1] + p;
  q = common(u, v, range[3][0], range[3][1]);
  if (q.first != -1e9) {
    y.second = q.first;
    y.first = q.first - p;
  } else {
    u = range[1][0] - p;
    v = range[1][1] - p;
    q = common(u, v, range[3][0], range[3][1]);
    y.second = q.first;
    y.first = q.first + p;
  }
  c[0][0] = x.first;
  c[0][1] = y.second;
  c[1][0] = x.first;
  c[1][1] = y.first;
  c[2][0] = x.second;
  c[2][1] = y.first;
  c[3][0] = x.second;
  c[3][1] = y.second;
}
bool check(int len) {
  int z[4];
  for (int i = (0); i <= (3); i++) z[i] = i;
  do {
    for (int i = (0); i <= (3); i++) {
      b[i][0] = a[z[i]][0];
      b[i][1] = a[z[i]][1];
    }
    for (int i = (0); i <= (1); i++)
      for (int j = (0); j <= (1); j++)
        for (int k = (0); k <= (1); k++)
          for (int l = (0); l <= (1); l++) {
            dir[0] = i;
            dir[1] = j;
            dir[2] = k;
            dir[3] = l;
            if (solve(len)) {
              for (int I = (0); I <= (3); I++) resZ[I] = z[I];
              for (int I = (0); I <= (3); I++) resDir[I] = dir[I];
              return true;
            }
          }
  } while (next_permutation(z, z + 4));
  return false;
}
void printResult(int res) {
  if (res > 2e8) {
    cout << -1 << "\n";
    return;
  }
  cout << res << "\n";
  check(res);
  for (int i = (0); i <= (3); i++) {
    b[i][0] = a[resZ[i]][0];
    b[i][1] = a[resZ[i]][1];
    dir[i] = resDir[i];
  }
  solve2(res);
  for (int i = (0); i <= (3); i++)
    for (int j = (0); j <= (3); j++)
      if (resZ[j] == i) cout << c[j][0] << ' ' << c[j][1] << "\n";
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(nullptr);
  cin >> t;
  while (t--) {
    for (int i = (0); i <= (3); i++) cin >> a[i][0] >> a[i][1];
    int dau = 0, cuoi = 2e8;
    while (dau <= cuoi) {
      int mid = (dau + cuoi) >> 1;
      if (check(mid))
        cuoi = mid - 1;
      else
        dau = mid + 1;
    }
    printResult(dau);
  }
  return 0;
}
