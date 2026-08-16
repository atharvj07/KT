#include <bits/stdc++.h>
using namespace std;
const int maxn = 100005;
const long long mod = 1e9 + 7;
int n;
long long a[maxn], sol[maxn], aux[maxn];
long long delta(int i, long long x) { return a[i] - 3 * x * x + 3 * x - 1; }
long long bb(long long d, int id) {
  if (a[id] - 1 <= d) return 0;
  long long ini = 0, fin = a[id], ret = -1;
  while (ini <= fin) {
    long long mit = (ini + fin) / 2;
    if (delta(id, mit) >= d) {
      ret = mit, ini = mit + 1;
    } else
      fin = mit - 1;
  }
  return ret;
}
long long up(long long v) {
  long long ret = 0;
  for (int i = 1; i <= n; i++) {
    long long c = bb(v, i);
    sol[i] = min(a[i], c);
    ret += sol[i];
  }
  return ret;
}
void prnt(vector<long long> &v) {
  for (auto &i : v) cerr << i << " ";
  cerr << "\n";
}
long long bi[maxn];
long long evbi() {
  long long ret = 0;
  for (int i = 1; i <= n; i++) ret += bi[i] * (a[i] - bi[i] * bi[i]);
  return ret;
}
long long evsol(vector<long long> sol) {
  long long ret = 0;
  for (int i = 1; i <= n; i++) ret += sol[i] * (a[i] - sol[i] * sol[i]);
  return ret;
}
int main() {
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  long long k;
  cin >> n >> k;
  for (int i = 1; i <= n; i++) cin >> a[i];
  long long ini = -4e18, fin = 4e18;
  long long delt = 0;
  while (ini <= fin) {
    long long mit = (ini + fin) / 2;
    if (up(mit) >= k) {
      delt = mit;
      ini = mit + 1;
    } else
      fin = mit - 1;
  }
  up(delt);
  long long acc = 0;
  for (int i = 1; i <= n; i++) acc += sol[i];
  long long quitar = acc - k;
  assert(quitar >= 0);
  priority_queue<pair<long long, long long>,
                 vector<pair<long long, long long> >,
                 greater<pair<long long, long long> > >
      q;
  for (int i = 1; i <= n; i++) {
    if (sol[i]) q.push({delta(i, sol[i]), i});
  }
  for (int i = 1; i <= quitar; i++) {
    pair<long long, long long> v = q.top();
    q.pop();
    sol[v.second]--;
    if (sol[v.second]) q.push({delta(v.second, sol[v.second]), v.second});
  }
  for (int i = 1; i <= n; i++) cout << sol[i] << " \n"[i == n];
  return 0;
}
