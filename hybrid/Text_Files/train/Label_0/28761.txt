#include <bits/stdc++.h>
using namespace std;
void err(istream_iterator<string> it) { cerr << endl; }
template <typename T, typename... Args>
void err(istream_iterator<string> it, T a, Args... args) {
  cerr << "[ " << *it << " = " << a << " ] ";
  err(++it, args...);
}
int main() {
  long long int n, i, j, p;
  scanf("%lld", &(n));
  vector<long long int> a(n), b(n), dif(n);
  for (i = 0; i < n; i++) scanf("%lld", &(a[i]));
  for (i = 0; i < n; i++) scanf("%lld", &(b[i])), dif[i] = a[i] - b[i];
  sort(dif.begin(), dif.end());
  long long int ans = 0, maxi;
  auto r = dif.end();
  for (i = 0; i < n - 1; i++) {
    maxi = 1 - dif[i];
    auto l = lower_bound(dif.begin() + i + 1, dif.end(), maxi);
    ans += (r - l);
  }
  printf("%lld\n", ans);
  return 0;
}
