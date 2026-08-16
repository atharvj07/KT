#include <bits/stdc++.h>
using namespace std;
const int N = 200002;
vector<vector<pair<int, int> > > ans;
vector<vector<int> > cs, twoCs, threeCs;
int n, p[N];
int main() {
  ios::sync_with_stdio(0);
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> p[i];
  bool mark[N] = {};
  for (int i = 1; i <= n; i++)
    if (!mark[i] && p[i] != i) {
      vector<int> newC;
      int v = i;
      while (!mark[v]) {
        mark[v] = 1;
        newC.push_back(v);
        v = p[v];
      }
      cs.push_back(newC);
    }
  for (int i = 0; i < cs.size(); i++)
    while (cs[i].size() >= 4) {
      vector<pair<int, int> > move;
      for (int j = max(0, (int)cs[i].size() - 5); j + 1 < cs[i].size(); j++)
        move.push_back(make_pair(cs[i][j], cs[i][j + 1]));
      move.push_back(
          make_pair(cs[i].back(), cs[i][max((int)cs[i].size() - 5, 0)]));
      ans.push_back(move);
      for (int j = 0; j < 4; j++) cs[i].pop_back();
    }
  for (int i = 0; i < cs.size(); i++)
    if (cs[i].size() == 2)
      twoCs.push_back(cs[i]);
    else if (cs[i].size() == 3)
      threeCs.push_back(cs[i]);
  while (threeCs.size()) {
    vector<pair<int, int> > move;
    vector<int> &tt = threeCs.back();
    move.push_back(make_pair(tt[0], tt[1]));
    move.push_back(make_pair(tt[1], tt[2]));
    move.push_back(make_pair(tt[2], tt[0]));
    threeCs.pop_back();
    if (twoCs.size()) {
      tt = twoCs.back();
      move.push_back(make_pair(tt[0], tt[1]));
      move.push_back(make_pair(tt[1], tt[0]));
      twoCs.pop_back();
    } else if (threeCs.size()) {
      tt = threeCs.back();
      move.push_back(make_pair(tt[0], tt[1]));
      move.push_back(make_pair(tt[1], tt[0]));
      vector<int> newC;
      newC.push_back(tt[0]);
      newC.push_back(tt[2]);
      twoCs.push_back(newC);
      threeCs.pop_back();
    }
    ans.push_back(move);
  }
  while (twoCs.size()) {
    vector<pair<int, int> > move;
    vector<int> &tt = twoCs.back();
    move.push_back(make_pair(tt[0], tt[1]));
    move.push_back(make_pair(tt[1], tt[0]));
    twoCs.pop_back();
    if (twoCs.size()) {
      tt = twoCs.back();
      move.push_back(make_pair(tt[0], tt[1]));
      move.push_back(make_pair(tt[1], tt[0]));
      twoCs.pop_back();
    }
    ans.push_back(move);
  }
  cout << ans.size() << endl;
  for (int i = 0; i < ans.size(); i++) {
    cout << ans[i].size() << endl;
    for (int j = 0; j < ans[i].size(); j++) cout << ans[i][j].first << " ";
    cout << endl;
    for (int j = 0; j < ans[i].size(); j++) cout << ans[i][j].second << " ";
    cout << endl;
  }
}
