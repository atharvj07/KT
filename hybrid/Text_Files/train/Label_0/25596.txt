#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int a, b;
  cin >> a >> b;
  int cnt = 0;
  int x = a, y = b;
  pair<int, pair<int, int>> ad, bd;
  while (a % 2 == 0) {
    a /= 2;
    ++ad.first;
  }
  while (a % 3 == 0) {
    a /= 3;
    ++ad.second.first;
  }
  while (a % 5 == 0) {
    a /= 5;
    ++ad.second.second;
  }
  while (b % 2 == 0) {
    b /= 2;
    ++bd.first;
  }
  while (b % 3 == 0) {
    b /= 3;
    ++bd.second.first;
  }
  while (b % 5 == 0) {
    b /= 5;
    ++bd.second.second;
  }
  if (a != b)
    return cout << -1, 0;
  else {
    return cout << (abs(ad.first - bd.first) +
                    abs(ad.second.first - bd.second.first) +
                    abs(ad.second.second - bd.second.second)),
           0;
  }
}
