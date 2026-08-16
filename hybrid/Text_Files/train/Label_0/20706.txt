#include <bits/stdc++.h>
using namespace std;
long long int i, j, x, y, k;
const int MOD = 1e9 + 7;
long long int m1 = LLONG_MAX;
bool sortbysec(const pair<int, int> &a, const pair<int, int> &b) {
  return (a.second < b.second);
}
long long int m2 = LLONG_MIN;
int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long int t;
  cin >> t;
  while (t--) {
    long long int n, m, q;
    cin >> n;
    vector<long long int> a(n + 1, 1);
    map<long long int, long long int> mp;
    for (i = 1; i <= n; i++) {
      long long int b;
      cin >> b;
      mp[i] = b;
    }
    for (i = 1; i <= n; i++) {
      vector<long long int> b;
      j = mp[i];
      while (j != i) {
        b.push_back(j);
        j = mp[j];
        a[i]++;
      }
      for (k = 0; k < b.size(); k++) {
        mp[b[k]] = b[k];
        a[b[k]] = a[i];
      }
      b.clear();
    }
    for (i = 1; i <= n; i++) cout << a[i] << " ";
    cout << endl;
  }
}
