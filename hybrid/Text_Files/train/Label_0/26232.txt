#include <bits/stdc++.h>
using namespace std;
const long long maxn = 6e5 + 100;
const long long mx = 1e9 + 10;
long long n, a[maxn];
long double sum, ans, cc[maxn], tree[maxn];
vector<long double> v;
long long getid(long long x) {
  return lower_bound(v.begin(), v.end(), x) - v.begin() + 1;
};
long long lowbit(long long x) { return x & (-x); }
void add(long long id, long double x) {
  for (long long i = id; i <= maxn; i += lowbit(i)) tree[i] += x;
}
long double getsum(long long x) {
  long double ret = 0;
  for (long long i = x; i; i -= lowbit(i)) ret += tree[i];
  return ret;
}
void adds(long long id) {
  for (long long i = id; i <= maxn; i += lowbit(i)) cc[i]++;
}
long double getsums(long long x) {
  long double ret = 0;
  for (long long i = x; i; i -= lowbit(i)) ret += cc[i];
  return ret;
}
int main() {
  cin >> n;
  for (long long i = 1; i <= n; ++i) {
    cin >> a[i];
    v.push_back(a[i]);
    v.push_back(a[i] + 1);
    v.push_back(a[i] - 2);
  }
  sort(v.begin(), v.end());
  v.erase(unique(v.begin(), v.end()), v.end());
  for (long long i = 1; i <= n; ++i) {
    long long id = getid(a[i]), id1 = getid(a[i] + 1), id2 = getid(a[i] - 2);
    ans += a[i] * (i - 1 - (getsums(id1) - getsums(id2))) -
           (sum - (getsum(id1) - getsum(id2)));
    sum += a[i];
    add(id, a[i]);
    adds(id);
  }
  cout << setprecision(0) << fixed;
  cout << ans << endl;
  return 0;
}
