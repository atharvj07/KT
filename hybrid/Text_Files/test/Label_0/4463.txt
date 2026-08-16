#include <bits/stdc++.h>
using namespace std;
set<int> s;
vector<int> v;
vector<int> v1;
int main() {
  ios::sync_with_stdio(false);
  cout.tie(NULL);
  cin.tie(NULL);
  int n;
  cin >> n;
  int o_x = -100000000, o_y = -100000000;
  int c_x = 100000000, c_y = 100000000;
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    if (x > o_x) {
      o_x = x;
    }
    if (y > o_y) {
      o_y = y;
    }
  }
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    if (x < c_x) {
      c_x = x;
    }
    if (y < c_y) {
      c_y = y;
    }
  }
  cout << o_x + c_x << " " << o_y + c_y;
  return 0;
}
