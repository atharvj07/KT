#include <bits/stdc++.h>
using namespace std;
signed main() {
  long long n;
  cin >> n;
  long long a[n];
  map<long long, long long> m;
  for (long long i = 0; i < n; i++) {
    cin >> a[i];
    m[a[i]]++;
  }
  for (auto it = m.begin(); it != m.end(); it++) {
    if (it->second > 2) {
      cout << "NO" << endl;
      return 0;
    }
  }
  sort(a, a + n);
  vector<long long> v1, v2;
  for (long long i = 0; i < n; i++) {
    if (i % 2 == 0)
      v1.push_back(a[i]);
    else
      v2.push_back(a[i]);
  }
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end(), greater<long long>());
  cout << "YES" << endl;
  cout << v1.size() << endl;
  for (auto x : v1) cout << x << " ";
  cout << endl;
  cout << v2.size() << endl;
  for (auto x : v2) cout << x << " ";
}
