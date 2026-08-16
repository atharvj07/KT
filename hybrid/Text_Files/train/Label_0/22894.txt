#include <bits/stdc++.h>
char _;
using namespace std;
void PRINT(int x, int y) {
  for (int i = y - 1; i >= 0; i--) {
    cout << ((0u == (x & (1 << i))) ? 0u : 1u);
  }
  cout << endl;
}
vector<string> vec_splitter(string s) {
  s += ',';
  vector<string> res;
  while (!s.empty()) {
    res.push_back(s.substr(0, s.find(',')));
    s = s.substr(s.find(',') + 1);
  }
  return res;
}
void debug_out(vector<string> __attribute__((unused)) args,
               __attribute__((unused)) int idx,
               __attribute__((unused)) int LINE_NUM) {
  cerr << endl;
}
template <typename Head, typename... Tail>
void debug_out(vector<string> args, int idx, int LINE_NUM, Head H, Tail... T) {
  if (idx > 0)
    cerr << ", ";
  else
    cerr << "Line(" << LINE_NUM << ") ";
  stringstream ss;
  ss << H;
  cerr << args[idx] << " = " << ss.str();
  debug_out(args, idx + 1, LINE_NUM, T...);
}
int bit[600005] = {0};
void add(int pos, int val) {
  while (pos < 600005) {
    bit[pos] += val;
    pos += pos & -pos;
  }
}
int sum(int pos) {
  int summ = 0;
  while (pos > 0) {
    summ += bit[pos];
    pos -= pos & -pos;
  }
  return summ;
}
map<int, int> rnk;
int mn[300005] = {0}, mx[300005] = {0};
int main() {
  cin.sync_with_stdio(0);
  cin.tie(0);
  int offset = 300001;
  int n, m;
  cin >> n >> m;
  for (int x = 1; x <= n; x++) {
    rnk.insert({x, x + offset});
    add(x + offset, 1);
    mn[x] = mx[x] = x;
  }
  while (m--) {
    int cur;
    cin >> cur;
    auto it = rnk.find(cur);
    mx[cur] = max(mx[cur], sum(it->second));
    add(it->second, -1);
    mn[cur] = 1;
    it->second = --offset;
    add(offset, 1);
  }
  for (auto it = rnk.begin(); it != rnk.end(); it++) {
    mx[it->first] = max(mx[it->first], sum(it->second));
  }
  for (int x = 1; x <= n; x++) {
    cout << mn[x] << " " << mx[x] << "\n";
  }
  return 0;
}
