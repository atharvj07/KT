#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  for (int tc = 0; tc < t; tc++) {
    int h, m;
    cin >> h >> m;
    long long int x = ((24 - h - 1) * 60) + (60 - m);
    cout << x << endl;
  }
}
