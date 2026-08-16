#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  vector<int> vec;
  vector<int> arr(10, 100);
  vector<int> arr2(10, 100);
  for (int i = 1; i <= n; i++) {
    int a;
    cin >> a;
    arr[a] = a;
  }
  for (int i = 1; i <= m; i++) {
    int a;
    cin >> a;
    arr2[a] = a;
    if (arr[a] == a) vec.push_back(a);
  }
  if (vec.size()) {
    sort(vec.begin(), vec.end());
    cout << vec.front();
    return 0;
  }
  sort(&arr[0], &arr[10]);
  sort(&arr2[0], &arr2[10]);
  int a = arr[0], b = arr2[0];
  cout << min(a, b) << max(a, b);
  return 0;
}
