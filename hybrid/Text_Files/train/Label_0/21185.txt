#include <bits/stdc++.h>
using namespace std;
class TrieNode {
 public:
  bool postive, leaf;
  TrieNode *zero, *one;
  TrieNode() {
    postive = leaf = 0;
    zero = one = NULL;
  }
};
void add(string &s, int idx, bool postive, TrieNode *cur) {
  cur->postive |= postive;
  if (idx == s.size()) {
    cur->leaf = 1;
    return;
  }
  if (s[idx] == '1') {
    if (cur->one == NULL) cur->one = new TrieNode();
    add(s, idx + 1, postive, cur->one);
  } else {
    if (cur->zero == NULL) cur->zero = new TrieNode();
    add(s, idx + 1, postive, cur->zero);
  }
  if (cur->one != NULL && cur->zero != NULL && cur->one->leaf &&
      cur->zero->leaf) {
    cur->leaf = 1;
  }
}
bool search(string &s, int idx, bool postive, TrieNode *cur) {
  if (cur->leaf) return 1;
  if (idx == s.size()) return postive;
  if (s[idx] == '1') {
    if (cur->one == NULL) return 0;
    return search(s, idx + 1, postive, cur->one);
  } else {
    if (cur->zero == NULL) return 0;
    return search(s, idx + 1, postive, cur->zero);
  }
}
vector<string> ips;
void solve(string &s, TrieNode *cur) {
  if (!cur->postive) {
    ips.push_back(s);
    return;
  }
  if (cur->zero != NULL) {
    s += '0';
    solve(s, cur->zero);
    s.pop_back();
  }
  if (cur->one != NULL) {
    s += '1';
    solve(s, cur->one);
    s.pop_back();
  }
}
string to_binary(int num) {
  string ret;
  while (num != 0) {
    ret += (num % 2) + '0';
    num /= 2;
  }
  while (ret.size() < 8) ret += '0';
  reverse(ret.begin(), ret.end());
  return ret;
}
string convert(string s) {
  int bs = -1;
  vector<int> sub;
  int cur = 0;
  for (int i = 1; i < s.size(); i++) {
    if (s[i] == 47) {
      bs = i;
      break;
    }
    if (s[i] == '.') {
      sub.push_back(cur);
      cur = 0;
    } else {
      cur *= 10;
      cur += (s[i] - '0');
    }
  }
  sub.push_back(cur);
  string ret;
  for (auto &x : sub) ret += to_binary(x);
  if (bs != -1) {
    cur = 0;
    for (int i = bs + 1; i < s.size(); i++) {
      cur *= 10;
      cur += s[i] - '0';
    }
    ret = ret.substr(0, cur);
  }
  return ret;
}
string to_number(string s) {
  int mul = 1;
  int ret = 0;
  for (int i = s.size() - 1; i >= 0; i--) {
    ret += mul * (s[i] - '0');
    mul *= 2;
  }
  string ret2;
  if (ret == 0) ret2 = "0";
  while (ret != 0) {
    ret2 += (ret % 10) + '0';
    ret /= 10;
  }
  reverse(ret2.begin(), ret2.end());
  return ret2;
}
string tostring(int number) {
  if (number == 0) return "0";
  string ret;
  while (number != 0) {
    ret += (number % 10) + '0';
    number /= 10;
  }
  reverse(ret.begin(), ret.end());
  return ret;
}
void to_ip() {
  for (auto &s : ips) {
    string cur = s;
    int r = s.size();
    while (cur.size() < 32) cur += '0';
    s = "";
    for (int i = 0; i < 32; i += 8) {
      string sub = cur.substr(i, 8);
      if (i) s += '.';
      s += to_number(sub);
    }
    s += 47;
    s += tostring(r);
  }
}
int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  TrieNode *root = new TrieNode();
  vector<string> black, white;
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    if (s[0] == '-')
      black.push_back(s);
    else
      white.push_back(s);
  }
  for (auto &x : black) {
    string cur = convert(x);
    if (!search(cur, 0, 0, root)) add(cur, 0, 0, root);
  }
  for (auto &x : white) {
    string cur = convert(x);
    if (search(cur, 0, 1, root)) {
      cout << -1;
      return 0;
    }
  }
  for (auto &x : white) {
    string cur = convert(x);
    if (!search(cur, 0, 1, root)) add(cur, 0, 1, root);
  }
  string s;
  solve(s, root);
  to_ip();
  cout << ips.size() << '\n';
  for (auto &x : ips) cout << x << '\n';
}
