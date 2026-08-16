#include <bits/stdc++.h>
using namespace std;
struct Item {
  string nazwa, typ;
  int pkt, wlk;
};
struct Resident {
  string nazwa, typ;
  int pkt;
  string item;
};
string it[] = {"weapon", "armor", "orb"};
string re[] = {"gladiator", "sentry", "physician"};
bool por(Resident a, Resident b) {
  if (a.pkt > b.pkt) return true;
  if (a.pkt < b.pkt) return false;
  return (a.nazwa < b.nazwa);
}
void Usun(vector<Resident>& a, string x) {
  vector<Resident> b;
  for (int i = 0; i < a.size(); ++i)
    if (a[i].nazwa != x) b.push_back(a[i]);
  a = b;
}
int main() {
  ios_base::sync_with_stdio(0);
  int n;
  cin >> n;
  vector<Item> I(n);
  int sWlk = 0;
  for (int i = 0; i < n; ++i) {
    int x, y, z;
    cin >> I[i].nazwa >> I[i].typ >> x >> y >> z >> I[i].wlk;
    if (I[i].typ == it[0]) I[i].pkt = x;
    if (I[i].typ == it[1]) I[i].pkt = y;
    if (I[i].typ == it[2]) I[i].pkt = z;
    sWlk += I[i].wlk;
  }
  int m;
  cin >> m;
  vector<Resident> R(m);
  for (int i = 0; i < m; ++i)
    cin >> R[i].nazwa >> R[i].typ >> R[i].pkt >> R[i].item;
  vector<string> nazwyItOdp(3);
  vector<int> wynOdp(3, -1);
  vector<vector<string> > nazwyReOdp(3);
  if (m == sWlk) {
    for (int i = 0; i < n; ++i) {
      int wynT = 0;
      vector<string> nazwyT;
      for (int j = 0; j < 3; ++j) {
        if (I[i].typ != it[j]) continue;
        for (int k = 0; k < m; ++k) {
          if (R[k].item == I[i].nazwa) {
            if (R[k].typ == re[j]) wynT += R[k].pkt;
            nazwyT.push_back(R[k].nazwa);
          }
        }
        wynT += I[i].pkt;
        if (wynT > wynOdp[j]) {
          nazwyItOdp[j] = I[i].nazwa;
          wynOdp[j] = wynT;
          nazwyReOdp[j] = nazwyT;
        }
      }
    }
  } else {
    vector<int> wlkOdp(3);
    for (int i = 0; i < n; ++i) {
      vector<Resident> T;
      int wynT = 0;
      vector<string> nazwyT;
      for (int j = 0; j < 3; ++j) {
        if (I[i].typ != it[j]) continue;
        for (int k = 0; k < m; ++k)
          if (R[k].typ == re[j]) T.push_back(R[k]);
        sort(T.begin(), T.end(), por);
        for (int k = 0; k < min((int)I[i].wlk, (int)T.size()); ++k) {
          wynT += T[k].pkt;
          nazwyT.push_back(T[k].nazwa);
        }
        wynT += I[i].pkt;
        if (wynT > wynOdp[j]) {
          nazwyItOdp[j] = I[i].nazwa;
          wynOdp[j] = wynT;
          wlkOdp[j] = I[i].wlk;
          nazwyReOdp[j] = nazwyT;
        }
      }
    }
    for (int i = 0; i < 3; ++i)
      for (int j = 0; j < nazwyReOdp[i].size(); ++j) Usun(R, nazwyReOdp[i][j]);
    for (int i = 0; i < R.size(); ++i) {
      if (nazwyReOdp[0].size() < wlkOdp[0]) {
        nazwyReOdp[0].push_back(R[i].nazwa);
        continue;
      }
      if (nazwyReOdp[1].size() < wlkOdp[1]) {
        nazwyReOdp[1].push_back(R[i].nazwa);
        continue;
      }
      if (nazwyReOdp[2].size() < wlkOdp[2]) {
        nazwyReOdp[2].push_back(R[i].nazwa);
        continue;
      }
    }
  }
  for (int i = 0; i < 3; ++i) {
    cout << nazwyItOdp[i] << " " << nazwyReOdp[i].size() << " ";
    for (int j = 0; j < nazwyReOdp[i].size(); ++j)
      cout << nazwyReOdp[i][j] << " ";
    cout << endl;
  }
  return 0;
}
