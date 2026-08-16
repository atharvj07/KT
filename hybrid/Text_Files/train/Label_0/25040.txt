#include <bits/stdc++.h>
using namespace std;
const long long INF = 1e9;
int main() {
  long long n, k;
  cin >> n >> k;
  set<long long> s;
  long long a[1000001] = {};
  for (long long i = 0; i < n; i++) {
    long long temp;
    cin >> temp;
    s.insert(temp);
    a[temp]++;
  }
  set<long long>::iterator itr;
  vector<long long> v;
  for (itr = s.begin(); itr != s.end(); itr++) v.push_back(*itr);
  sort(v.begin(), v.end());
  long long ans = n;
  for (long long i = 0; i < v.size(); i++) {
    if (v[i] < v[i + 1] && v[i] + k >= v[i + 1]) ans -= a[v[i]];
  }
  cout << ans;
  return 0;
}
