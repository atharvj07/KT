#include <bits/stdc++.h>
using namespace std;
long long arr[4002][3];
vector<int> v;
int main() {
  int n, d, p;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
  }
  for (int i = 0; i < n; i++) {
    while (arr[i][0] == -1 && i < n) i++;
    if (i >= n) break;
    v.push_back(i + 1);
    long long x = arr[i][0];
    long long y = 0;
    for (int j = i + 1; j < n; j++) {
      if (arr[j][0] == -1) continue;
      arr[j][2] -= (x + y);
      if (arr[j][2] < 0) {
        arr[j][0] = -1;
        y = y + arr[j][1];
      }
      if (x != 0) x--;
      if (x == 0 && y == 0) break;
    }
  }
  cout << v.size() << "\n";
  for (int i = 0; i < v.size(); i++) cout << v[i] << " ";
  cout << "\n";
  return 0;
}
