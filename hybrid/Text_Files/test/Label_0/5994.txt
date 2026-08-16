#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 100;
long long tree[N];
bool a[N];
int sz[N];
int mapping[N];
int par[N];
long long n;
void print() {
  for (int i = 1; i <= n; i++) {
    if (a[i] == false) printf("%d ", i);
  }
}
long long query(int idx) {
  long long sum = 0;
  while (idx > 0) {
    sum += tree[idx];
    idx -= idx & (-idx);
  }
  return sum;
}
void print(int n) {
  cout << "--------------------\n";
  for (int i = 1; i <= n; i++) {
    cout << i << " " << query(mapping[i]) << " " << sz[i] << " mapp "
         << mapping[i] << endl;
    ;
  }
  cout << "-----------------\n";
}
void update(long long idx, long long x, long long n) {
  while (idx <= n) {
    tree[idx] += x;
    idx += idx & (-idx);
  }
}
void rangeUpdate(long long x, long long y, long long val, long long n) {
  update(x, val, n);
  update(y + 1, -val, n);
}
int cc = 1;
int len;
vector<int> v[N];
void dfs(int x, int pr, int dis) {
  len++;
  par[x] = pr;
  mapping[x] = cc;
  rangeUpdate(cc, cc, dis, n);
  cc++;
  int st = len;
  for (int i = 0; i < v[x].size(); i++) {
    int y = v[x][i];
    if (y != pr) dfs(y, x, dis + 1);
  }
  sz[x] = len - st;
}
int main() {
  long long q, i, j = 0, temp, t, k, ans = 0, sum = 0, x, y, z, cnt = 0, m,
                  fg = 0, mx = 0, mx1 = 0, mn = 8000000000000000000,
                  mn1 = 8000000000000000000;
  scanf("%lld %lld", &n, &k);
  for (int i = 0; i < n - 1; i++) {
    scanf("%lld %lld", &x, &y);
    v[x].push_back(y);
    v[y].push_back(x);
  }
  dfs(n, n, 0);
  if (k == 0) {
    print();
    return 0;
  }
  a[n] = true;
  k = n - k;
  k--;
  for (int i = n - 1; i >= 1; i--) {
    if (!k) break;
    if (a[i]) continue;
    int val = query(mapping[i]);
    if (val > k) continue;
    k -= val;
    j = i;
    while (!a[j]) {
      a[j] = true;
      rangeUpdate(mapping[j], mapping[j] + sz[j], -1, n);
      j = par[j];
    }
  }
  print();
}
