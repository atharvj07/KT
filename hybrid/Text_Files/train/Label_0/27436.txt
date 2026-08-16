#include <bits/stdc++.h>
using namespace std;
int n, m;
struct lut {
  string name;
  int cl;
  int val;
  int size;
};
struct an {
  string name;
  string whr;
  int cl;
  int val;
  int num;
};
vector<lut> l;
vector<an> anim;
vector<an> d[3];
vector<bool> used;
int all_size;
void Inputdata() {
  cin >> n;
  l.resize(n);
  for (int i = 0; i < n; i++) {
    string name;
    string cls;
    int a, b, c, s;
    cin >> name >> cls >> a >> b >> c >> s;
    l[i].name = name;
    l[i].size = s;
    all_size += s;
    if (cls == "weapon") {
      l[i].cl = 0;
      l[i].val = a;
    }
    if (cls == "armor") {
      l[i].cl = 1;
      l[i].val = b;
    }
    if (cls == "orb") {
      l[i].cl = 2;
      l[i].val = c;
    }
  }
  cin >> m;
  anim.resize(m);
  used.resize(m);
  for (int i = 0; i < m; i++) {
    string name, type, whr;
    int val;
    cin >> name >> type >> val >> whr;
    anim[i].name = name;
    anim[i].whr = whr;
    anim[i].val = val;
    anim[i].num = i;
    if (type == "gladiator") anim[i].cl = 0;
    if (type == "sentry") anim[i].cl = 1;
    if (type == "physician") anim[i].cl = 2;
    d[anim[i].cl].push_back(anim[i]);
  }
}
bool Comp(const an &a, const an &b) { return a.val > b.val; }
void Solve() {
  sort(d[0].begin(), d[0].end(), Comp);
  sort(d[1].begin(), d[1].end(), Comp);
  sort(d[2].begin(), d[2].end(), Comp);
  int ans[3];
  int max_val[3];
  for (int i = 0; i < 3; i++) max_val[i] = -10;
  if (all_size > m) {
    for (int i = 0; i < n; i++) {
      int type = l[i].cl;
      int now_val = l[i].val;
      for (int j = 0; j < min(l[i].size, int(d[type].size())); j++)
        now_val += d[type][j].val;
      if (max_val[type] < now_val) {
        max_val[type] = now_val;
        ans[type] = i;
      }
    }
    vector<string> ans_out[3];
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < min(l[ans[i]].size, int(d[i].size())); j++) {
        ans_out[i].push_back(d[i][j].name);
        used[d[i][j].num] = true;
      }
    }
    for (int i = 0; i < 3; i++) {
      int cnt = int(ans_out[i].size());
      for (int j = 0; j < m; j++) {
        if (cnt >= l[ans[i]].size) break;
        if (!used[j]) {
          ans_out[i].push_back(anim[j].name);
          used[j] = true;
          cnt++;
        }
      }
    }
    for (int i = 0; i < 3; i++) {
      cout << l[ans[i]].name << ' ';
      cout << ans_out[i].size() << ' ';
      for (int j = 0; j < ans_out[i].size(); j++) cout << ans_out[i][j] << ' ';
      cout << endl;
    }
  } else {
    int max_val[3];
    int ans[3];
    for (int i = 0; i < n; i++) {
      int type = l[i].cl;
      int now_val = l[i].val;
      for (int j = 0; j < m; j++)
        if (anim[j].whr == l[i].name && l[i].cl == anim[j].cl)
          now_val += anim[j].val;
      if (max_val[type] < now_val) {
        max_val[type] = now_val;
        ans[type] = i;
      }
    }
    vector<string> ans_out[3];
    for (int i = 0; i < 3; i++) {
      int type = l[ans[i]].cl;
      for (int j = 0; j < m; j++)
        if (anim[j].whr == l[ans[i]].name) ans_out[i].push_back(anim[j].name);
    }
    for (int i = 0; i < 3; i++) {
      cout << l[ans[i]].name << ' ';
      cout << ans_out[i].size() << ' ';
      for (int j = 0; j < ans_out[i].size(); j++) cout << ans_out[i][j] << ' ';
      cout << endl;
    }
  }
}
int main() {
  Inputdata();
  Solve();
  return 0;
}
