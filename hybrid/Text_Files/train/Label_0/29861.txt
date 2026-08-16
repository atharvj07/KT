#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int sum = 0;
  set<int> st;
  st.insert(0);
  for (int i = 0; i < 4; i++) {
    set<int> ins;
    int add;
    cin >> add;
    sum += add;
    for (auto j : st) {
      ins.insert(j + add);
    }
    for (auto j : ins) {
      st.insert(j);
    }
  }
  if (sum & 1 || !st.count(sum / 2)) {
    cout << "NO" << endl;
  } else {
    cout << "YES" << endl;
  }
}
