#include <bits/stdc++.h>
using namespace std;
long long dx[] = {0, 0, 1, -1};
long long dy[] = {1, -1, 0, 0};
const long long sz = 100005;
void showArr(long long *arr, long long n) {
  for (long long i = 0; i < n; i++) cout << arr[i] << " ";
}
int32_t main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  string s1, s2;
  cin >> s1 >> s2;
  vector<long long> v[26];
  for (long long i = 0; i < s1.length(); i++) {
    v[s1[i] - 'a'].push_back(i);
  }
  long long ans = 1, pos = -1;
  for (long long i = 0; i < s2.length(); i++) {
    long long idx = s2[i] - 'a';
    if (v[idx].size() == 0) {
      cout << -1 << "\n";
      exit(0);
    }
    long long it =
        upper_bound(v[idx].begin(), v[idx].end(), pos) - v[idx].begin();
    if (it != v[idx].size()) {
      pos = v[idx][it];
    } else {
      ans++;
      pos = v[idx][0];
    }
  }
  cout << ans << "\n";
  return 0;
}
