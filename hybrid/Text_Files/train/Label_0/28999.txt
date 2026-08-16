#include <bits/stdc++.h>
using namespace std;
const int M = 100000 + 10;
int hpos[M], hneg[M];
set<int> criminal;
int claim[M];
int main() {
  int n, m;
  cin >> n >> m;
  int pos = 0;
  int neg = 0;
  for (int i = 1; i <= n; i++) {
    string s;
    cin >> s;
    int num = 0;
    for (int i = 1; i < s.length(); i++) {
      num = num * 10 + s[i] - '0';
    }
    if (s[0] == '+') {
      hpos[num]++;
      pos++;
      claim[i] = num;
    } else {
      hneg[num]++;
      neg++;
      claim[i] = -num;
    }
  }
  for (int i = 1; i <= n; i++) {
    int num = hpos[i] + neg - hneg[i];
    if (num == m) {
      criminal.insert(i);
    }
  }
  for (int i = 1; i <= n; i++) {
    int id = claim[i];
    if (id > 0) {
      if (criminal.find(id) == criminal.end()) {
        cout << "Lie" << endl;
      } else {
        if (criminal.size() == 1) {
          cout << "Truth" << endl;
        } else {
          cout << "Not defined" << endl;
        }
      }
    } else {
      id = -id;
      if (criminal.find(id) == criminal.end()) {
        cout << "Truth" << endl;
      } else {
        if (criminal.size() == 1) {
          cout << "Lie" << endl;
        } else {
          cout << "Not defined" << endl;
        }
      }
    }
  }
  return 0;
}
