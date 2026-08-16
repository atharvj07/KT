#include <bits/stdc++.h>
using namespace std;
string totaal;
string s;
int tok[5000], tok_cnt;
int cell_cnt[5000];
int main() {
  while (cin >> s) totaal += s;
  memset(cell_cnt, 0, sizeof(cell_cnt));
  int len = (int)(totaal.size()), tok_cnt = 0;
  string x;
  for (int pos = (0); pos < (len); pos++) {
    x += totaal[pos];
    if (totaal[pos] == '>') {
      if (x == "<table>") {
        tok[tok_cnt] = 0;
        tok_cnt++;
      } else if (x == "</table>") {
        tok[tok_cnt] = 1;
        tok_cnt++;
      } else if (x == "<td>") {
        tok[tok_cnt] = 4;
        tok_cnt++;
      } else if (x == "</td>") {
        tok[tok_cnt] = 5;
        tok_cnt++;
      }
      x = "";
    }
  }
  int cur_cell_cnt = 0;
  for (int pos = (0); pos < (len); pos++) {
    if (tok[pos] == 5) cur_cell_cnt++;
    cell_cnt[pos] = cur_cell_cnt;
  }
  vector<pair<int, int> > stapel;
  vector<int> sizes;
  int geteld = 0;
  for (int pos = (0); pos < (len); pos++) {
    if (tok[pos] == 0) stapel.push_back(make_pair(geteld, pos));
    if (tok[pos] == 1) {
      pair<int, int> van = stapel.back();
      stapel.pop_back();
      int van_p = van.second, num = van.first;
      int d = cell_cnt[pos] - cell_cnt[van_p] - (geteld - num);
      sizes.push_back(d);
      geteld += d;
    }
  }
  sort(sizes.begin(), sizes.end());
  for (int i = (0); i < ((int)(sizes.size())); i++) cout << sizes[i] << " ";
  cout << endl;
}
