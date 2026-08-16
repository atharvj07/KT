#include <bits/stdc++.h>

using namespace std;

bool solve(string s)
{
  if(s == "ABC") return true;
  if(s.find("ABC") == string::npos) return false;
  set<char> st;
  for(int i = 0; i < s.size(); i++) {
    if(i+3 <= s.size() && s.substr(i, 3) == "ABC") i += 2;
    else st.insert(s[i]);
  }
  bool ret = false;
  for(char c = 'A'; c < 'D'; c++) {
    if(st.find(c) != st.end()) continue;
    string t = "";
    for(int i = 0; i < s.size(); i++) {
      if(i+3 <= s.size() && s.substr(i, 3) == "ABC") t += c, i += 2;
      else t += s[i];
    }
    ret |= solve(t);
  }
  return ret;
}

int main()
{
  string s; cin >> s;
  cout << (solve(s) ? "Yes" : "No") << endl;
}