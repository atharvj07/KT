#include <bits/stdc++.h>
using namespace std;
bool marked[100010 + 10], bad[100010 + 10];
int cnt[100010 + 10];
int part[100010 + 10];
vector<long long> v;
int p;
int add(long long a, long long b) {
  a %= p;
  b %= p;
  return (((a + b) % p) + p) % p;
}
int mul(long long a, long long b) {
  a %= p;
  b %= p;
  return (a * b) % p;
}
int main() {
  long long n, m;
  long long l, r;
  cin >> n >> m >> l >> r >> p;
  l *= l;
  r *= r;
  for (long long i = 2; i <= 100010; i++)
    if (!marked[i]) {
      for (long long j = i; j <= 100010; j += i) {
        bad[j] |= ((j % (i * i)) == 0);
        marked[j] = true;
        cnt[j]++;
      }
    }
  long long ans = 0;
  for (int i = 1; i <= 100010; i++) {
    if (bad[i]) continue;
    long long tmp = 0;
    v.clear();
    for (long long j = i; j <= m + 1; j += i) {
      v.push_back(j * j);
      part[v.size()] = add(part[v.size() - 1], m + 1 - j);
    }
    for (long long j = i; j <= n + 1; j += i) {
      int en = upper_bound(v.begin(), v.end(), r - j * j) - v.begin();
      int st = lower_bound(v.begin(), v.end(), l - j * j) - v.begin();
      tmp = add(tmp, mul(part[en] - part[st], n + 1 - j));
    }
    if (cnt[i] % 2)
      ans = add(ans, -2 * tmp);
    else
      ans = add(ans, 2 * tmp);
  }
  if (l == 1) {
    ans = add(ans, mul(n + 1, m));
    ans = add(ans, mul(m + 1, n));
  }
  cout << ans << endl;
}
