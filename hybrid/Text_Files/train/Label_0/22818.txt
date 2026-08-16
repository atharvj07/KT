#include <bits/stdc++.h>
using namespace std;
const double pi = 3.14159265358979;
int main() {
  string s;
  deque<pair<int, char> > t;
  vector<pair<int, int> > a;
  cin >> s;
  int l = 0, r = -1, ans = 0, tl = s.length(), tr = -1, temp;
  for (int i = 0; i < s.length(); ++i) {
    if (s[i] == ']') {
      if (!t.empty() && t.back().second == '[') {
        tl = min(tl, t.back().first);
        tr = max(tr, i);
        t.pop_back();
      } else {
        if (tl <= tr) a.push_back(make_pair(tl, tr));
        tl = s.length();
        tr = -1;
        while (t.size()) t.pop_back();
      }
    } else if (s[i] == ')') {
      if (!t.empty() && t.back().second == '(') {
        tl = min(tl, t.back().first);
        tr = max(tr, i);
        t.pop_back();
      } else {
        if (tl <= tr) a.push_back(make_pair(tl, tr));
        tl = s.length();
        tr = -1;
        while (t.size()) t.pop_back();
      }
    } else {
      t.push_back(make_pair(i, s[i]));
      if (tl <= tr) {
        a.push_back(make_pair(tl, tr));
        tl = s.length();
        tr = -1;
      }
    }
  }
  if (tl <= tr) {
    a.push_back(make_pair(tl, tr));
    tl = s.length();
    tr = -1;
  }
  tl = s.length();
  tr = -1;
  sort(a.begin(), a.end());
  for (int i = 0; i < a.size(); ++i) {
    if (a[i].first >= tl && a[i].second <= tr) continue;
    if (tr == -1) {
      tl = a[i].first;
      tr = a[i].second;
    } else {
      if (tr == a[i].first - 1) {
        tr = a[i].second;
      } else {
        temp = 0;
        for (int j = tl; j <= tr; ++j) {
          if (s[j] == '[') {
            ++temp;
          }
        }
        if (temp > ans) {
          ans = temp;
          l = tl;
          r = tr;
        }
        tl = a[i].first;
        tr = a[i].second;
      }
    }
  }
  temp = 0;
  for (int j = tl; j <= tr; ++j) {
    if (s[j] == '[') {
      ++temp;
    }
  }
  if (temp > ans) {
    ans = temp;
    l = tl;
    r = tr;
  }
  cout << ans << endl;
  for (int j = l; j <= r; ++j) {
    cout << s[j];
  }
  return 0;
}
