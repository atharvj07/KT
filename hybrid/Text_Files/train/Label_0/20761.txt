#include <bits/stdc++.h>
using namespace std;
int main() {
  int x, y, a, b;
  cin >> x >> y >> a >> b;
  vector<pair<int, int> > v;
  vector<pair<int, int> > w;
  for (int i = a; i <= x; i++) {
    for (int j = b; j <= y; j++) {
      if (i > j) w.push_back(make_pair(i, j));
    }
  }
  cout << w.size() << endl;
  for (int i = 0; i < w.size(); i++)
    cout << w[i].first << " " << w[i].second << endl;
}
