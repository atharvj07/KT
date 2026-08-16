#include <bits/stdc++.h>
using namespace std;
void setIO(string name = "") {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  if ((int)name.size()) {
    freopen((name + ".in").c_str(), "r", stdin);
    freopen((name + ".out").c_str(), "w", stdout);
  }
}
int main() {
  auto ask = [&](vector<int> v) {
    cout << "next ";
    for (auto i : v) cout << i << " ";
    cout << endl;
    ;
    int k;
    cin >> k;
    vector<string> s(k);
    for (int i = 0; i < k; i++) {
      cin >> s[i];
    }
    return s;
  };
  vector<int> pos(10, 0);
  vector<string> q = ask({0, 1});
  q = ask({0});
  auto update = [&]() {
    for (int i = 0; i < (int)q.size(); i++) {
      if (q[i] == "stop") exit(0);
      for (auto c : q[i]) {
        pos[(c - '0')] = i;
      }
    }
  };
  update();
  while (pos[0] != pos[1]) {
    ask({0, 1});
    q = ask({0});
    update();
  }
  while (pos[2] != pos[0]) {
    q = ask({0, 2, 3, 4, 5, 6, 7, 8, 9});
    update();
  }
  while (pos[1] != pos[0]) {
    q = ask({1});
    update();
  }
  cout << "done" << endl;
  return 0;
}
