#include <bits/stdc++.h>
using namespace std;
int a, b, c, res;
int main() {
  cin >> a >> b >> c;
  vector<int> v = {a, b, c};
  sort(v.begin(), v.end());
  while (v[0] + v[1] <= v[2]) v[0]++, res++;
  cout << res << endl;
  return 0;
}
