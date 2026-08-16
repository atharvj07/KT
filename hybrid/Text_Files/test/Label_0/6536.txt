#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n, h, g;
  vector<int> home, guest;
  cin >> n;
  while (n--) {
    cin >> h >> g;
    home.push_back(h);
    guest.push_back(g);
  }
  n = home.size();
  h = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (home[i] == guest[j]) h++;
    }
  }
  cout << h << "\n";
  return 0;
}
