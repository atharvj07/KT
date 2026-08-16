#include <bits/stdc++.h>
using namespace std;
long long int n, x, sum = 0, cnt = 0, a[100005], an;
vector<long long int> vt[100005];
map<long long int, long long int> use, mp;
map<long long int, long long int>::iterator it;
long long int dfs(long long int node, long long int par) {
  long long int tmp, siz = vt[node].size(), tpp = 0, lol = 0;
  for (int i = 0; i < siz; i++) {
    tmp = vt[node][i];
    if (tmp == par) continue;
    tpp++;
    lol |= dfs(tmp, node);
  }
  if (tpp == 0) lol = 1LL;
  if (lol) sum ^= a[node], use[a[node]]++, cnt++;
  return (lol ^ 1LL);
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  scanf("%lld", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%lld", &a[i]);
    mp[a[i]]++;
  }
  for (int i = 1; i < n; i++) {
    scanf("%lld", &x);
    vt[x].push_back(i + 1), vt[i + 1].push_back(x);
  }
  dfs(1, 0);
  if (sum == 0) {
    an = (cnt * (cnt - 1)) >> 1;
    cnt = n - cnt;
    an += ((cnt * (cnt - 1)) >> 1);
    for (it = use.begin(); it != use.end(); it++) {
      long long int i = it->first;
      an += (use[i] * (mp[i] - use[i]));
    }
  } else {
    for (it = use.begin(); it != use.end(); it++) {
      long long int i = it->first;
      an += (use[i] * (mp[sum ^ i] - use[sum ^ i]));
    }
  }
  printf("%lld\n", an);
  return 0;
}
