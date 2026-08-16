#include <bits/stdc++.h>
using namespace std;
const long long int mod = 998244353ll;
const long long int P = 1000000007ll;
const long long int N = 1005ll;
char t[N][N];
int u[N][N];
int d[N][N];
int l[N][N];
int r[N][N];
int col[N][N];
int row[N][N];
int a[N][N];
long long int n, m;
void solve() {
  cin >> n >> m;
  vector<pair<pair<long long int, long long int>, long long int>> ans;
  for (long long int i = (1); i <= (n); ++i) cin >> (t[i] + 1);
  for (long long int i = (1); i <= (n); ++i)
    for (long long int j = (1); j <= (m); ++j)
      if (t[i][j] == '*') l[i][j] = l[i][j - 1] + 1;
  for (long long int j = (1); j <= (m); ++j)
    for (long long int i = (1); i <= (n); ++i)
      if (t[i][j] == '*') u[i][j] = u[i - 1][j] + 1;
  for (long long int i = (1); i <= (n); ++i)
    for (int j = m; j; --j)
      if (t[i][j] == '*') r[i][j] = r[i][j + 1] + (int)(t[i][j] == '*');
  for (long long int j = (1); j <= (m); ++j)
    for (int i = n; i; --i)
      if (t[i][j] == '*') d[i][j] = d[i + 1][j] + (int)(t[i][j] == '*');
  for (long long int i = (1); i <= (n); ++i)
    for (long long int j = (1); j <= (m); ++j)
      if (t[i][j] == '*') {
        long long int x = min(min(l[i][j], r[i][j]), min(u[i][j], d[i][j]));
        if (x > 1) {
          ans.push_back(make_pair(make_pair(i, j), x - 1));
          col[i - x + 1][j]++;
          col[i + x][j]--;
          row[i][j - x + 1]++;
          row[i][j + x]--;
        }
      }
  for (long long int i = (1); i <= (n); ++i) {
    int f = 0;
    for (long long int j = (1); j <= (m); ++j) {
      f += row[i][j];
      if (f > 0) a[i][j] = 1;
    }
  }
  for (long long int j = (1); j <= (m); ++j) {
    int f = 0;
    for (long long int i = (1); i <= (n); ++i) {
      f += col[i][j];
      if (f > 0) a[i][j] = 1;
    }
  }
  for (long long int i = (1); i <= (n); ++i)
    for (long long int j = (1); j <= (m); ++j)
      if (t[i][j] == '*' && a[i][j] == 0) {
        cout << -1;
        return;
      }
  cout << ans.size() << "\n";
  for (auto v : ans)
    cout << v.first.first << " " << v.first.second << " " << v.second << "\n";
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long int t = 1;
  while (t--) {
    solve();
  }
  return 0;
}
