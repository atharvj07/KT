#include <bits/stdc++.h>
using namespace std;
const int NN = 56;
map<string, int> zade, emtiaz, abraj;
void fun(int x, int y, string a, string b) {
  zade[a] += x;
  zade[b] += y;
  abraj[a] += x;
  abraj[b] += y;
  abraj[a] -= y;
  abraj[b] -= x;
  if (x > y) {
    emtiaz[a] += 3;
  } else if (x < y)
    emtiaz[b] += 3;
  else
    emtiaz[a]++, emtiaz[b]++;
}
void rev_fun(int x, int y, string a, string b) {
  zade[a] -= x;
  zade[b] -= y;
  abraj[a] -= x;
  abraj[b] -= y;
  abraj[a] += y;
  abraj[b] += x;
  if (x > y) {
    emtiaz[a] -= 3;
  } else if (x < y)
    emtiaz[b] -= 3;
  else
    emtiaz[a]--, emtiaz[b]--;
}
vector<pair<int, pair<int, pair<int, string> > > > sort_team() {
  vector<pair<int, pair<int, pair<int, string> > > > teams;
  for (map<string, int>::iterator Iter = zade.begin(); Iter != zade.end();
       ++Iter) {
    string a = Iter->first;
    teams.push_back(
        make_pair(-emtiaz[a], make_pair(-abraj[a], make_pair(-zade[a], a))));
  }
  sort(teams.begin(), teams.end());
  return teams;
}
int main() {
  ios::sync_with_stdio(false);
  map<string, int> played;
  for (int i = 0; i < 5; i++) {
    string a, b, c;
    cin >> a >> b >> c;
    int x = c[0] - '0', y = c[2] - '0';
    fun(x, y, a, b);
    if (a != "BERLAND") played[a]++;
    if (b != "BERLAND") played[b]++;
  }
  string other = "";
  for (map<string, int>::iterator Iter = played.begin(); Iter != played.end();
       ++Iter) {
    if (Iter->second == 2) {
      other = Iter->first;
    }
  }
  vector<pair<int, pair<int, pair<int, string> > > > teams;
  int ansX = 1000000, ansY = 0;
  for (int X = 0; X < 44; X++) {
    for (int Y = X - 1; Y >= 0; Y--) {
      if (X - Y > ansX - ansY) break;
      fun(X, Y, "BERLAND", other);
      teams = sort_team();
      int pos = -1;
      for (int i = 0; i < ((int)teams.size()); i++)
        if (teams[i].second.second.second == "BERLAND") pos = i;
      if (pos <= 1) {
        if (ansX - ansY > X - Y || (ansX - ansY == X - Y && ansY > Y)) {
          ansX = X;
          ansY = Y;
        }
      }
      rev_fun(X, Y, "BERLAND", other);
    }
  }
  if (ansX == 1000000)
    printf("IMPOSSIBLE\n");
  else
    printf("%d:%d\n", ansX, ansY);
}
