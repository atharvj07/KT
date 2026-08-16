#include <bits/stdc++.h>
using namespace std;

const int N = 100005;

int i, n, x, y, rs;
bool viz[N];
vector<int> lda[N], v, drum;

void dfs(int x) {
  viz[x] = 1;
  v.push_back(x);
  if(x == n) drum = v;
  for(auto to : lda[x]) {
    if(viz[to]) continue;
    dfs(to);
  }

  v.pop_back();
}

void solveDfs(int x) {
  viz[x] = 1; ++rs;

  for(auto to : lda[x]) if(!viz[to] && to != drum[(drum.size() + 1) / 2]) solveDfs(to);
}

int main() {
  ios_base::sync_with_stdio(0);

  cin >> n;
  for(i = 1; i < n; ++i) {
    cin >> x >> y;
    lda[x].push_back(y);
    lda[y].push_back(x);
  }

  dfs(1);

  memset(viz, 0, sizeof(viz));

  solveDfs(1);

  if(rs > n - rs) cout << "Fennec\n";
  else cout << "Snuke\n";

  return 0;
}