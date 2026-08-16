#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  vector<int> arr;
  int a = 0, b = 0, c = 0, d = 0, e = 0;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    if (x == 0)
      a = 1;
    else if (x == 100)
      b = 1;
    else if (x % 10 == 0)
      c = x;
    else if (x < 10)
      d = x;
    else
      e = x;
  }
  if (a) arr.push_back(0);
  if (b) arr.push_back(100);
  if (c) arr.push_back(c);
  if (d) arr.push_back(d);
  if (!c && !d && e) arr.push_back(e);
  cout << arr.size() << endl;
  for (auto i : arr) cout << i << " ";
  return 0;
}
