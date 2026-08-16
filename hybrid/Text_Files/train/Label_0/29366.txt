#include <bits/stdc++.h>
using namespace std;
long long gcd(long long a, long long b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long n;
  cin >> n;
  map<pair<long long, long long>, set<long double> > m;
  vector<pair<long long, long long> > a(n);
  for (long long i = 0; i < n; i++) {
    cin >> a[i].first >> a[i].second;
  }
  for (long long i = 0; i < n; i++) {
    for (long long j = i + 1; j < n; j++) {
      long long x1 = a[i].first;
      long long y1 = a[i].second;
      long long x2 = a[j].first;
      long long y2 = a[j].second;
      long long num = y2 - y1;
      long long den = x2 - x1;
      long long g = gcd(num, den);
      num /= g;
      den /= g;
      long long c = den * y1 - num * x1;
      m[make_pair(num, den)].insert(c);
    }
  }
  long long ans = 0;
  long long total = 0;
  vector<long long> si;
  for (auto &i : m) {
    total += i.second.size();
    si.push_back(i.second.size());
  }
  for (auto &i : si) {
    ans += (i) * (total - i);
  }
  ans /= 2;
  cout << ans << endl;
}
