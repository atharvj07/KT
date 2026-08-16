#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e6 + 10;
int a[maxn];
bool used[maxn];
void dfs(int v) {
  used[v] = 1;
  if (!used[a[v]]) dfs(a[v]);
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(nullptr);
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) cin >> a[i];
  int x = n;
  for (int i = 1; i <= n; ++i)
    if (!used[i]) dfs(i), x--;
  if (n & 1) {
    if (x & 1)
      cout << "Petr";
    else
      cout << "Um_nik";
  } else {
    if (x & 1)
      cout << "Um_nik";
    else
      cout << "Petr";
  }
  return 0;
}
