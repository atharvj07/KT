#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int k;
  cin >> k;
  int c = 0;
  map<int, int> mapping;
  for (int i = 0; i < k; i++) {
    int m;
    cin >> m;
    for (int j = 0; j < m; j++) {
      int x;
      cin >> x;
      mapping[x] = i;
    }
  }
  int smallest = mapping.begin()->second;
  for (map<int, int>::iterator it = mapping.begin(); it != mapping.end();
       it++) {
    if (it->second == smallest)
      c++;
    else
      break;
  }
  int ans = n - 1 + n - k;
  ans -= 2 * (c - 1);
  cout << ans << endl;
  return 0;
}
