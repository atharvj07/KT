#include <bits/stdc++.h>
using namespace std;
long long mod = 1e9 + 7;
const double pi = acos(-1);
int n;
pair<int, int> arr[150005];
unordered_map<int, int> mp, mp2;
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%d%d", &arr[i].first, &arr[i].second);
  for (int i = 2; i <= sqrt(arr[n - 1].first); i++) {
    if (arr[n - 1].first % i == 0) {
      mp[i] = 1;
      mp[arr[n - 1].first / i] = 1;
    }
  }
  if (mp.size() == 0) mp[arr[n - 1].first]++;
  long long temp = mp.size();
  for (int i = 2; i <= sqrt(arr[n - 1].second); i++) {
    if (arr[n - 1].second % i == 0) {
      mp[i] = 1;
      mp[arr[n - 1].second / i] = 1;
    }
  }
  if (mp.size() == temp && mp[arr[n - 1].second] == 0) mp[arr[n - 1].second]++;
  for (auto &j : mp) {
    for (int i = 0; i < n - 1; i++) {
      if (arr[i].first % j.first == 0) {
        j.second++;
      } else if (arr[i].second % j.first == 0) {
        j.second++;
      } else
        break;
    }
    if (j.second >= n && j.first != 1) {
      printf("%d", j.first);
      return 0;
    }
  }
  printf("-1");
  return 0;
}
