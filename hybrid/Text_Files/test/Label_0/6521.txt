#include <bits/stdc++.h>
using namespace std;
bool isodd(long long int x) { return x % 2; }
int main() {
  long long int n;
  cin >> n;
  vector<long long int> arr(n), ans;
  for (int i = n - 1; i != -1; i--) cin >> arr[i];
  if (n == 1) {
    cout << arr[0];
    return 0;
  }
  ans.push_back(arr[0]);
  int size = n / 2 - 1;
  pair<long long int, long long int> p[size];
  int b = 1, e = n - 2;
  for (int i = 0; i < size; i++) {
    p[i] = make_pair(arr[e], arr[b]);
    b++, e--;
  }
  for (int i = 0; i < size; i++) {
    if (i % 2)
      ans.push_back(p[i].second);
    else
      ans.push_back(p[i].first);
  }
  if (n % 2 == 1) ans.push_back(arr[n / 2]);
  for (int i = size - 1; i != -1; i--) {
    if (i % 2)
      ans.push_back(p[i].first);
    else
      ans.push_back(p[i].second);
  }
  for (int i = 0; i < n - 1; i++) cout << ans[i] << " ";
  cout << arr[n - 1];
}
