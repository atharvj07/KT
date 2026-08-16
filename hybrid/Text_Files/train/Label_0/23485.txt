#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  string ar[n], s, throw_line, thr;
  int i = 0, count = 0, flag = 0, count2 = 0;
  vector<string> v;
  getline(cin, s);
  for (int i = 0; i < n; i++) {
    getline(cin, s);
    if (s.find("try") != -1 && flag != 1) {
      count++;
    } else if (s.find("try") != -1 && flag == 1) {
      int k;
      k = s.find('"');
      int j;
      j = s.find("try");
      if ((j = k + 1 && k > 0) || (k > j && k > 0)) {
      } else
        count2++;
    }
    if (s.find("throw") != -1) {
      throw_line = s;
      flag = 1;
    }
    if (s.find("catch") != -1) {
      if (flag == 0) {
        count--;
      } else {
        if (count2 != 0)
          count2--;
        else {
          if (count != 0) {
            count--;
            v.push_back(s);
          }
        }
      }
    }
  }
  for (int i = 0; i < throw_line.size(); i++) {
    if (throw_line[i] == '(') {
      i++;
      while (throw_line[i] != ')') {
        if (throw_line[i] != ' ') {
          thr.push_back(throw_line[i]);
        }
        i++;
      }
    }
  }
  count2 = 0;
  for (int i = 0; i < v.size(); i++) {
    s = v[i];
    if (s.find(thr) != -1 && count2 == 0) {
      count2++;
      for (int i = 0; i < s.size(); i++) {
        if (s[i] == '"') {
          i++;
          while (s[i] != '"') {
            cout << s[i];
            i++;
          }
        }
      }
    }
  }
  if (count2)
    cout << endl;
  else
    cout << "Unhandled Exception" << endl;
}
