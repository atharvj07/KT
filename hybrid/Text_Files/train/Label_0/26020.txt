#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int n;
    cin >> n;
    map<int, int> game;
    for (int j = 0; j < n; j++) {
      int a;
      cin >> a;
      game[a]++;
    }
    for (auto at : game) {
      if (at.second >= 2 && at.first < 2048) {
        game[at.first * 2] += at.second / 2;
        at.second = 0;
      }
    }
    cout << (game[2048] > 0 ? "YES" : "NO") << endl;
  }
}
