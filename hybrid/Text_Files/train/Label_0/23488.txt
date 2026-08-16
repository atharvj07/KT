#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAX_N = 2e5 + 9;
void fixit(string &s) {
  string tmp = s;
  while (tmp.size() > 0 && tmp.back() == ' ') tmp.pop_back();
  reverse(tmp.begin(), tmp.end());
  while (tmp.size() > 0 && tmp.back() == ' ') tmp.pop_back();
  reverse(tmp.begin(), tmp.end());
  s = tmp;
}
pair<string, string> SolveCatch(string s) {
  int idx = 0;
  string ret, ret2;
  while (s[idx++] != '(')
    ;
  idx += (s[idx] == ' ');
  while (s[idx] != ',') ret.push_back(s[idx++]);
  idx++;
  int cnt = 0;
  while (cnt < 2) {
    cnt += (s[idx] == '"');
    if (s[idx] != '"' && cnt) ret2.push_back(s[idx]);
    idx++;
  }
  fixit(ret), fixit(ret2);
  return {ret, ret2};
}
string solvethrow(string s) {
  string ret;
  int idx = 0;
  while (s[idx++] != '(')
    ;
  idx += (s[idx] == ' ');
  while (s[idx] != ')') ret.push_back(s[idx++]);
  if (ret.back() == ' ') ret.pop_back();
  fixit(ret);
  return ret;
}
stack<int> tries;
int main() {
  ios_base::sync_with_stdio(0), cin.tie(0);
  int n;
  cin >> n;
  string s;
  cin.ignore();
  string excep = "$";
  int idx = -1;
  for (int i = 1; i <= n; i++) {
    getline(cin, s);
    fixit(s);
    if (s[0] == 'c') {
      auto it = SolveCatch(s);
      int thetop = tries.top();
      tries.pop();
      if (thetop < idx && it.first == excep) cout << it.second, exit(0);
    } else if (s.substr(0, 2) == "th")
      excep = solvethrow(s), idx = i;
    else if (s[0] == 't')
      tries.push(i);
  }
  cout << "Unhandled Exception";
}
