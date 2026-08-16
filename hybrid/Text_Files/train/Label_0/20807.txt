#include <bits/stdc++.h>
using namespace std;
long long n, d, a, b;
pair<long long, long long> arr[100009];
vector<long long> vec;
int main() {
  cin >> n >> d;
  cin >> a >> b;
  for (long long i = 0; i < n; i++) {
    long long x, y;
    scanf("%lld%lld", &x, &y);
    arr[i].first = (a * x) + (b * y);
    arr[i].second = i + 1;
  }
  sort(arr, arr + n);
  for (long long i = 0; i < n; i++) {
    if (d - arr[i].first >= 0)
      vec.push_back(arr[i].second);
    else
      break;
    d -= arr[i].first;
  }
  int ans = vec.size();
  cout << ans << endl;
  for (int i = 0; i < ans; i++) printf("%lld ", vec[i]);
  cout << endl;
  return 0;
}
