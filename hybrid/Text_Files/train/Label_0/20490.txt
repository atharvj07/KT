#include <bits/stdc++.h>
#pragma comment(linker, "/stack:256000000")
using namespace std;
mt19937_64 gen(time(NULL));
int const maxn = 3e5 + 5;
long long idx[maxn];
unordered_map<long long, bool> go[maxn];
signed main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long n;
  cin >> n;
  long long m;
  cin >> m;
  for (long long i = 1; i <= n; i++) {
    long long t;
    cin >> t;
    idx[t] = i;
  }
  for (long long i = 0; i < m; i++) {
    long long u, v;
    cin >> u >> v;
    if (idx[u] > idx[v])
      continue;
    else {
      u = idx[u];
      v = idx[v];
      go[u][v] = 1;
    }
  }
  vector<long long> kek = {0};
  long long ans = 0;
  for (long long i = 1; i <= n; i++) kek.push_back(i);
  for (long long i = n - 1; i >= 1; i--) {
    long long j = i;
    while (j < n && go[kek[j]][kek[j + 1]]) {
      if (kek[j + 1] == n) {
        ans++;
      }
      swap(kek[j], kek[j + 1]);
      j++;
    }
  }
  cout << ans << endl;
  return 0;
}
