#include <bits/stdc++.h>
using namespace std;
struct Item {
  string name;
  int size;
  int pt;
};
vector<Item> items[3];
struct Res {
  string name;
  string home;
  int bonus;
};
struct G {
  bool operator()(const Res& a, const Res& b) { return a.bonus > b.bonus; }
};
vector<Res> res[3];
set<string> names;
int main() {
  int n;
  cin >> n;
  int sum = 0;
  for (int i = 0; i < n; i++) {
    string name, cl;
    int size;
    int p[3];
    cin >> name >> cl >> p[0] >> p[1] >> p[2] >> size;
    int index = 0;
    if (cl == "weapon") {
      index = 0;
    } else if (cl == "armor") {
      index = 1;
    } else if (cl == "orb") {
      index = 2;
    } else {
      assert(false);
    }
    items[index].push_back(Item{name, size, p[index]});
    sum += size;
  }
  int k;
  cin >> k;
  for (int i = 0; i < k; i++) {
    string name, tp, home;
    int bounus;
    cin >> name >> tp >> bounus >> home;
    int index = 0;
    if (tp == "gladiator") {
      index = 0;
    } else if (tp == "sentry") {
      index = 1;
    } else if (tp == "physician") {
      index = 2;
    }
    res[index].push_back(Res{name, home, bounus});
    names.insert(name);
  }
  if (sum == k) {
    for (int i = 0; i < 3; i++) {
      map<string, int> total;
      int m = -1;
      string mname;
      for (auto it : items[i]) {
        total[it.name] = it.pt;
        if (it.pt > m) {
          m = it.pt;
          mname = it.name;
        }
      }
      for (auto r : res[i]) {
        if (total.count(r.home)) {
          total[r.home] += r.bonus;
          if (total[r.home] > m) {
            m = total[r.home];
            mname = r.home;
          }
        }
      }
      cout << mname;
      vector<string> mem;
      for (int j = 0; j < 3; j++) {
        for (auto r : res[j]) {
          if (r.home == mname) {
            mem.push_back(r.name);
          }
        }
      }
      cout << " " << mem.size();
      for (auto r : mem) {
        cout << " " << r;
      }
      cout << endl;
    }
    return 0;
  }
  Item ret0[3];
  vector<string> ret[3];
  for (int i = 0; i < 3; i++) {
    sort(res[i].begin(), res[i].end(), G());
    int m = -1;
    Item mit;
    for (auto it : items[i]) {
      for (int j = 0; j < min(it.size, (int)res[i].size()); j++) {
        it.pt += res[i][j].bonus;
      }
      if (it.pt > m) {
        m = it.pt;
        mit = it;
      }
    }
    ret0[i] = mit;
    for (int j = 0; j < min(mit.size, (int)res[i].size()); j++) {
      names.erase(res[i][j].name);
      ret[i].push_back(res[i][j].name);
    }
  }
  for (int i = 0; i < 3; i++) {
    while (ret0[i].size > ret[i].size() && names.size()) {
      ret[i].push_back(*names.begin());
      names.erase(names.begin());
    }
    cout << ret0[i].name << " " << ret[i].size();
    for (auto r : ret[i]) {
      cout << " " << r;
    }
    cout << endl;
  }
  return 0;
}
