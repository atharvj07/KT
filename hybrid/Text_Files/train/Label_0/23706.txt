#include <bits/stdc++.h>
using namespace std;
long long block_size;
bool cmp(const pair<pair<long long, long long>, long long> &a,
         const pair<pair<long long, long long>, long long> &b) {
  long long bl_a = a.first.first / block_size;
  long long bl_b = b.first.first / block_size;
  if (bl_a == bl_b) {
    if (a.first.second == b.first.second) {
      if (a.first.first == b.first.first) {
        return a.second < b.second;
      }
      return a.first.first < b.first.first;
    }
    return a.first.second < b.first.second;
  }
  return bl_a < bl_b;
}
int main() {
  ios_base ::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long n, i, t;
  cin >> n >> t;
  vector<long long> a(n);
  vector<long long> answer(t);
  vector<pair<pair<long long, long long>, long long>> queries(t);
  for (i = 0; i < n; i++) {
    cin >> a[i];
  }
  for (i = 0; i < t; i++) {
    cin >> queries[i].first.first >> queries[i].first.second;
    queries[i].first.first--;
    queries[i].first.second--;
    queries[i].second = i;
  }
  block_size = sqrt(n);
  sort(queries.begin(), queries.end(), cmp);
  long long l = 0, r = -1, *cnt = new long long[(long long)1e6 + 1];
  long long ans = 0;
  for (i = 0; i < t; i++) {
    while (l > queries[i].first.first) {
      l--;
      ans -= cnt[a[l]] * cnt[a[l]] * a[l];
      cnt[a[l]]++;
      ans += cnt[a[l]] * cnt[a[l]] * a[l];
    }
    while (r < queries[i].first.second) {
      r++;
      ans -= cnt[a[r]] * cnt[a[r]] * a[r];
      cnt[a[r]]++;
      ans += cnt[a[r]] * cnt[a[r]] * a[r];
    }
    while (l < queries[i].first.first) {
      ans -= cnt[a[l]] * cnt[a[l]] * a[l];
      cnt[a[l]]--;
      ans += cnt[a[l]] * cnt[a[l]] * a[l];
      l++;
    }
    while (r > queries[i].first.second) {
      ans -= cnt[a[r]] * cnt[a[r]] * a[r];
      cnt[a[r]]--;
      ans += cnt[a[r]] * cnt[a[r]] * a[r];
      r--;
    }
    answer[queries[i].second] = ans;
  }
  for (auto it : answer) {
    cout << it << '\n';
  }
  return 0;
}
