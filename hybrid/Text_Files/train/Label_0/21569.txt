#include <bits/stdc++.h>
using namespace std;
int* a[5005];
int first[5555], second[5555];
int d[5005 * 5005 / 2];
int cm[5005 * 5005 / 2];
int c[33333];
int par[5555];
int sz[5555];
int tp[5555];
int n, k, com;
int u[5555];
vector<int> e[5005];
int P(int first) {
  return (first == par[first]) ? (first) : (par[first] = P(par[first]));
}
inline void U(int first, int second) {
  if (rand() % 2) {
    par[first] = second;
    sz[second] += sz[first];
  } else {
    par[second] = first;
    sz[first] += sz[second];
  }
}
void dfs_r(int v, int num) {
  u[v] = num;
  tp[v] ^= 1;
  for (int(i) = 0; (i) < ((int)e[v].size()); ++(i))
    if (u[e[v][i]] != num) dfs_r(e[v][i], num);
}
inline void ren(int first, int second, int now) {
  if (sz[first] >= sz[second])
    dfs_r(second, now + 1);
  else
    dfs_r(first, now + 1);
}
int main() {
  scanf("%d", &n);
  for (int(i) = 0; (i) < (n); ++(i)) a[i] = new int[i + 1];
  for (int(i) = 0; (i) < (n); ++(i)) {
    scanf("%d%d", &first[i], &second[i]);
    e[i].reserve(n);
  }
  for (int(i) = 0; (i) < (n); ++(i))
    for (int(j) = 0; (j) < (i + 1); ++(j))
      a[i][j] = abs(first[i] - first[j]) + abs(second[i] - second[j]);
  k = 0;
  for (int(i) = 0; (i) < (n); ++(i))
    for (int(j) = 0; (j) < (i + 1); ++(j)) {
      c[a[i][j] + 1]++;
      ++k;
    }
  for (int i = 1; i < 33333; ++i) c[i] += c[i - 1];
  for (int(i) = 0; (i) < (n); ++(i))
    for (int(j) = 0; (j) < (i + 1); ++(j)) {
      d[c[a[i][j]]] = i * n + j;
      c[a[i][j]]++;
    }
  reverse(d, d + k);
  for (int(i) = 0; (i) < (n); ++(i)) par[i] = i;
  com = n;
  for (int(i) = 0; (i) < (n); ++(i))
    for (int(j) = 0; (j) < (i + 1); ++(j)) a[i][j] *= -1;
  for (int(i) = 0; (i) < (k); ++(i)) {
    int v1 = d[i] / n;
    int v2 = d[i] % n;
    if (v1 < v2) swap(v1, v2);
    int p1 = P(v1);
    int p2 = P(v2);
    if (v1 == v2) break;
    if (p1 == p2) {
      if (tp[v1] == tp[v2]) {
        int ans = 1;
        cout << -a[v1][v2] << endl;
        int pos = i - 1;
        while (pos < k &&
               a[max(d[pos] / n, d[pos] % n)][min(d[pos] / n, d[pos] % n)] ==
                   a[v1][v2])
          --pos;
        com = cm[pos];
        for (int(i) = 0; (i) < (com); ++(i)) ans = (ans * 2) % 1000000007;
        cout << ans << endl;
        return 0;
      }
    } else {
      com--;
      if (tp[v2] == tp[v1]) ren(v1, v2, i);
      U(p1, p2);
    }
    e[v1].push_back(v2);
    e[v2].push_back(v1);
    cm[i] = com;
  }
  cout << "0\n2\n";
}
