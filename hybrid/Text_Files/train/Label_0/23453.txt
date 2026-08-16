#include <bits/stdc++.h>
using namespace std;
int dx4[] = {0, 0, 1, -1};
int dy4[] = {1, -1, 0, 0};
int dx8[] = {0, 0, 1, -1, 1, 1, -1, -1};
int dy8[] = {1, -1, 0, 0, 1, -1, 1, -1};
int dxH[] = {2, 2, -2, -2, 1, 1, -1, -1};
int dyH[] = {1, -1, 1, -1, 2, -2, 2, -2};
const double GRS = (1 + sqrt(5)) / 2;
template <typename T>
T power(T X, T P) {
  T ans = (T)1;
  for (T i = 1; i <= P; i++) {
    ans = ans * X;
  }
  return ans;
}
template <typename T>
T ABS(T A, T B) {
  T ret = A - B;
  if (ret < 0) return -ret;
  return ret;
}
const long long MOD = 1000000007;
const long long BIGMAX = power(2, 63) - 1;
template <typename T>
T ADD(T X, T Y, T M) {
  if (X + Y < 0)
    return (X - M) + Y;
  else if (X + Y >= M)
    return X + Y - M;
  else
    return X + Y;
}
template <typename T>
T prod(T a, T b, T c) {
  T x = 0, y = a % c;
  while (b > 0) {
    if (b % 2 == 1) {
      x = ADD(x, y, c);
    }
    y = (y * 2) % c;
    b /= 2;
  }
  return x % c;
}
template <typename T>
T bigmod(T a, T b, T c) {
  T x = 1, y = a % c;
  while (b > 0) {
    if (b % 2 == 1) {
      x = prod(x, y, c);
    }
    y = prod(y, y, c);
    b /= (long long)2;
  }
  return x;
}
template <typename T>
T MODINVERSE(T a) {
  return bigmod(a, MOD - 2);
}
long long ncrdp[900][1000];
long long NCR(int n, int r) {
  if (r == 1)
    return n;
  else if (n == r)
    return 1;
  else {
    if (ncrdp[n][r] != -1)
      return ncrdp[n][r];
    else {
      ncrdp[n][r] = NCR(n - 1, r) + NCR(n - 1, r - 1);
      return ncrdp[n][r];
    }
  }
}
const int MAXN = 1000000;
int status[(MAXN / 32) + 10];
int primelist[1234567];
int primesz = 0;
bool check(int n, int pos) { return (bool)(n & (1 << pos)); }
int SET(int n, int pos) { return n = n | (1 << pos); }
void sieve() {
  int sqrtN = int(sqrt(MAXN));
  status[1 >> 5] = SET(status[1 >> 5], 1 & 31);
  for (int j = 4; j <= MAXN; j = j + 2)
    status[j >> 5] = SET(status[j >> 5], j & 31);
  for (int i = 3; i <= sqrtN; i = i + 2) {
    if (check(status[i >> 5], i & 31) == 0) {
      for (int j = i * i; j <= MAXN; j = j + (i << 1)) {
        status[j >> 5] = SET(status[j >> 5], j & 31);
      }
    }
  }
  primelist[primesz++] = 2;
  for (int i = 3; i <= MAXN; i = i + 2) {
    if (check(status[i >> 5], i & 31) == 0) {
      primelist[primesz++] = i;
    }
  }
}
template <typename T>
T GCD(T x, T y) {
  while (y != 0) {
    T z = x % y;
    x = y;
    y = z;
  }
  return x;
}
vector<int> G[123456];
int color[123456];
bool visited[123456];
int shuru[123456], sesh[123456];
bool DFS(int u, int precolor, int rong) {
  if (precolor != rong) return false;
  visited[u] = true;
  int sz = G[u].size();
  bool ret = true;
  for (int i = 0; i < sz; i++) {
    int v = G[u][i];
    if (!visited[v]) {
      ret = ret & DFS(v, rong, color[v]);
    }
  }
  return ret;
}
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 1; i <= n - 1; i++) {
    int u, v;
    scanf("%d %d", &u, &v);
    G[u].push_back(v);
    G[v].push_back(u);
    shuru[i] = u, sesh[i] = v;
  }
  for (int i = 1; i <= n; i++) {
    scanf("%d", color + i);
  }
  bool Thik = true;
  int u, v;
  for (int i = 1; i <= n; i++) {
    for (auto it : G[i]) {
      if (color[it] != color[i]) {
        Thik = false;
        u = i;
        v = it;
      }
    }
  }
  if (Thik) {
    printf("YES\n");
    printf("1");
  } else {
    memset(visited, false, sizeof visited);
    bool res = true;
    visited[u] = true;
    for (int j = 0; j < G[u].size(); j++) {
      int node = G[u][j];
      res = res & DFS(node, color[node], color[node]);
    }
    if (res) {
      printf("YES\n");
      printf("%d\n", u);
      return 0;
    }
    memset(visited, false, sizeof visited);
    visited[v] = true;
    res = true;
    for (int j = 0; j < G[v].size(); j++) {
      int node = G[v][j];
      res = res & DFS(node, color[node], color[node]);
    }
    if (res) {
      printf("YES\n");
      printf("%d\n", v);
      return 0;
    }
    printf("NO");
  }
  return 0;
}
