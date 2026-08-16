#include <bits/stdc++.h>
using std::abs;
using std::array;
using std::cerr;
using std::cin;
using std::cout;
using std::generate;
using std::get;
using std::make_pair;
using std::make_tuple;
using std::map;
using std::max;
using std::max_element;
using std::min;
using std::min_element;
using std::pair;
using std::queue;
using std::reverse;
using std::set;
using std::sort;
using std::string;
using std::swap;
using std::tuple;
using std::unique;
using std::vector;
template <typename T>
T input() {
  T res;
  cin >> res;
  {};
  return res;
}
template <typename IT>
void input_seq(IT b, IT e) {
  std::generate(b, e,
                input<typename std::remove_reference<decltype(*b)>::type>);
}
int main() {
  std::iostream::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<vector<int>> go(n);
  for (int i = 0; i < m; ++i) {
    int a, b;
    cin >> a >> b;
    --a, --b;
    go[a].push_back(b);
    go[b].push_back(a);
  }
  vector<int> col(n);
  vector<pair<int, int>> data(n);
  for (int i = 0; i < n; ++i) data[i] = make_pair(col[i] = input<int>() - 1, i);
  sort(data.begin(), data.end());
  for (auto x : data) {
    int v = x.second;
    vector<char> used(col[v] + 1);
    for (int u : go[v])
      if (col[u] <= col[v]) used[col[u]] = true;
    if (std::find(used.begin(), used.end(), false) != used.end() - 1) {
      cout << "-1\n";
      return 0;
    }
  }
  for (auto x : data) cout << 1 + x.second << " ";
  cout << "\n";
  return 0;
}
