#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  vector<pair<char, int> > v(9);
  v[0].first = '6';
  v[1].first = '7';
  v[2].first = '8';
  v[3].first = '9';
  v[4].first = 'T';
  v[5].first = 'J';
  v[6].first = 'Q';
  v[7].first = 'K';
  v[8].first = 'A';
  v[0].second = 6;
  v[1].second = 7;
  v[2].second = 8;
  v[3].second = 9;
  v[4].second = 10;
  v[5].second = 11;
  v[6].second = 12;
  v[7].second = 13;
  v[8].second = 14;
  char trump;
  string s1, s2;
  long valu_s1, valu_s2;
  cin >> trump;
  cin >> s1 >> s2;
  if (s1[1] == trump && s2[1] != trump)
    cout << "YES" << endl;
  else if (s1[1] == s2[1]) {
    for (int i = 0; i < 9; i++) {
      if (s1[0] == v[i].first) valu_s1 = v[i].second;
      if (s2[0] == v[i].first) valu_s2 = v[i].second;
    }
    if (valu_s1 > valu_s2)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  } else
    cout << "NO" << endl;
  return 0;
}
