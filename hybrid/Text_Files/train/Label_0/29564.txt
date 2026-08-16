#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  long long int a;
  cin >> n;
  cin >> a;
  std::vector<int> v;
  while (a > 0) {
    int x = a % 10;
    a = a / 10;
    if (x == 1 || x == 0) {
      continue;
    } else if (x == 2 || x == 3 || x == 5 || x == 7) {
      v.push_back(x);
    } else if (x == 4) {
      v.push_back(2);
      v.push_back(2);
      v.push_back(3);
    } else if (x == 6) {
      v.push_back(3);
      v.push_back(5);
    } else if (x == 8) {
      v.push_back(2);
      v.push_back(2);
      v.push_back(2);
      v.push_back(7);
    } else {
      v.push_back(3);
      v.push_back(3);
      v.push_back(2);
      v.push_back(7);
    }
  }
  sort(v.begin(), v.end());
  for (int j = (int)v.size() - 1; j >= 0; j--) {
    cout << v[j];
  }
  return 0;
}
