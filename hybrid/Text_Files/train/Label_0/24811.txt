#include <bits/stdc++.h>
using namespace std;
const int MAX_N = int(1e5) + 10;
int p[MAX_N];
bool used[MAX_N];
vector<vector<int> > bs, cs;
void putInOrder(vector<int> cyc, bool isNew = true) {
  vector<int> b = cyc;
  vector<int> c = b;
  rotate(c.begin(), c.begin() + 1, c.end());
  if (isNew)
    bs.push_back(b), cs.push_back(c);
  else {
    bs.back().insert(bs.back().end(), b.begin(), b.end());
    cs.back().insert(cs.back().end(), c.begin(), c.end());
  }
}
void putLastInOrder(vector<int>& cyc, int len, bool isNew = true) {
  vector<int> b(cyc.end() - len, cyc.end());
  vector<int> c = b;
  rotate(c.begin(), c.begin() + 1, c.end());
  if (isNew) {
    bs.push_back(b), cs.push_back(c);
  } else {
    bs.back().insert(bs.back().end(), b.begin(), b.end());
    cs.back().insert(cs.back().end(), c.begin(), c.end());
  }
  cyc.erase(cyc.end() - len + 1, cyc.end());
}
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> p[i];
    --p[i];
  }
  vector<vector<int> > cyc2, cyc3;
  for (int i = 0; i < n; ++i)
    if (!used[i]) {
      int x = i;
      vector<int> cyc;
      while (!used[x]) {
        used[x] = true;
        cyc.push_back(x);
        x = p[x];
      }
      while (cyc.size() > 5) {
        putLastInOrder(cyc, 5);
      }
      if (cyc.size() >= 4) {
        putInOrder(cyc);
        continue;
      }
      if (cyc.size() == 2) {
        cyc2.push_back(cyc);
      } else if (cyc.size() == 3) {
        cyc3.push_back(cyc);
      }
    }
  for (;;) {
    if (!cyc2.empty() && !cyc3.empty()) {
      putInOrder(cyc2.back()), cyc2.pop_back();
      putInOrder(cyc3.back(), false), cyc3.pop_back();
      continue;
    }
    if (cyc3.size() >= 2) {
      putInOrder(cyc3.back()), cyc3.pop_back();
      vector<int> cyc = cyc3.back();
      cyc3.pop_back();
      putLastInOrder(cyc, 2, false);
      cyc2.push_back(cyc);
      continue;
    }
    if (cyc2.size() >= 2) {
      putInOrder(cyc2.back()), cyc2.pop_back();
      putInOrder(cyc2.back(), false), cyc2.pop_back();
      continue;
    }
    if (cyc2.size() >= 1) {
      putInOrder(cyc2.back()), cyc2.pop_back();
      continue;
    }
    if (cyc3.size() >= 1) {
      putInOrder(cyc3.back()), cyc3.pop_back();
      continue;
    }
    break;
  }
  cout << bs.size() << endl;
  for (int i = 0; i < bs.size(); ++i) {
    vector<int> b = bs[i], c = cs[i];
    cout << b.size() << endl;
    for (int j = 0; j < b.size(); ++j) {
      cout << b[j] + 1 << " ";
    }
    cout << endl;
    for (int j = 0; j < c.size(); ++j) {
      cout << c[j] + 1 << " ";
    }
    cout << endl;
  }
  return 0;
}
