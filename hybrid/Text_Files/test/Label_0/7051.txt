#include <bits/stdc++.h>
using namespace std;
bool sortin(const pair<long long int, long long int> &e,
            const pair<long long int, long long int> &f) {
  return (e.first < f.first);
}
long long int i, j, k, l, m, n, c, p, q;
long long int a[250002], b[100002], x[100002];
int main() {
  {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
  };
  cin >> q;
  while (q--) {
    map<long long int, long long int> mp, np;
    cin >> n;
    cin >> m;
    cin >> l;
    for (int i = 0; i <= n - 1; i++) cin >> a[i];
    for (int i = 0; i <= l - 1; i++) mp[a[i]]++;
    c = mp.size();
    for (int i = l; i <= n - 1; i++) {
      mp[a[i - l]]--;
      if (mp[a[i - l]] == 0) mp.erase(a[i - l]);
      mp[a[i]]++;
      k = mp.size();
      c = min(c, k);
    }
    cout << c;
    cout << endl;
  }
}
