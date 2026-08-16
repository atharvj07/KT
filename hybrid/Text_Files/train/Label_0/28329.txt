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
struct comp_t {
  vector<int> cycle;
  int size;
};
int main() {
  std::iostream::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  int n = input<int>();
  vector<int> go(n);
  vector<vector<int>> graph(n);
  vector<vector<int>> graph2(n);
  for (int i = 0; i != n; ++i) {
    go[i] = input<int>() - 1;
    graph[go[i]].push_back(i);
    graph2[go[i]].push_back(i);
    graph2[i].push_back(go[i]);
  }
  vector<int> compid(n, -1);
  vector<comp_t> comps;
  int szcomp = 0;
  std::function<void(int, int)> dfs = [&](int v, int c) {
    ++szcomp;
    compid[v] = c;
    for (int u : graph2[v])
      if (compid[u] == -1) dfs(u, c);
  };
  vector<char> is_cycle(n, false);
  vector<int> pos(n, -1);
  for (int i = 0; i != n; ++i)
    if (compid[i] == -1) {
      szcomp = 0;
      dfs(i, int((comps).size()));
      comps.resize(int((comps).size()) + 1);
      comps.back().size = szcomp;
      vector<int> arr;
      int p = i;
      for (; pos[p] == -1; p = go[p]) {
        pos[p] = int((arr).size());
        arr.push_back(p);
      }
      arr.erase(arr.begin(), arr.begin() + pos[p]);
      comps.back().cycle = arr;
      for (int elem : arr) is_cycle[elem] = 1;
      for (int i = 0; i != int((arr).size()); ++i) pos[arr[i]] = i;
    }
  vector<vector<tuple<int, int, int>>> buckets(int((comps).size()));
  vector<vector<pair<int, int>>> notcycle(n);
  int q = input<int>();
  vector<int> answers(q, -1);
  for (int i = 0; i != q; ++i) {
    int64_t m;
    int y;
    cin >> m >> y;
    --y;
    if (is_cycle[y]) {
      int clen = int((comps[compid[y]].cycle).size());
      int total = comps[compid[y]].size;
      if (m >= clen + total) m = total + (m - total) % clen;
      buckets[compid[y]].emplace_back(m, pos[y], i);
    } else
      notcycle[y].emplace_back(m, i);
  }
  auto merge = [&](vector<int>& a, vector<int>& b) {
    if (not(int((a).size()) >= int((b).size()))) swap(a, b);
    for (int p = 0; p != int((b).size()); ++p)
      a[int((a).size()) - int((b).size()) + p] += b[p];
  };
  std::function<vector<int>(int, vector<pair<int, int>>&, int, int)> solve =
      [&](int v, vector<pair<int, int>>& go, int to, int len) {
        go.emplace_back(len, to);
        vector<int> res = {1};
        for (int u : graph[v]) {
          auto rs = solve(u, go, to, len + 1);
          rs.push_back(0);
          merge(res, rs);
        }
        for (auto elem : notcycle[v])
          if (elem.first < int((res).size()))
            answers[elem.second] = res[int((res).size()) - 1 - elem.first];
          else
            answers[elem.second] = 0;
        return res;
      };
  for (int c = 0; c != int((comps).size()); ++c) {
    sort(buckets[c].begin(), buckets[c].end());
    vector<pair<int, int>> go;
    for (int i = 0; i != int((comps[c].cycle).size()); ++i)
      for (int u : graph[comps[c].cycle[i]])
        if (not is_cycle[u]) solve(u, go, i, 1);
    sort(go.begin(), go.end());
    int ptr = 0;
    vector<int> state(int((comps[c].cycle).size()), 1);
    int curt = 0;
    int off = 0;
    for (auto quer : buckets[c]) {
      while (curt != get<0>(quer)) {
        ++curt;
        off -= 1;
        if (off < 0) off += int((state).size());
        while (ptr < int((go).size()) and go[ptr].first == curt) {
          state[(go[ptr].second + off) % int((state).size())] += 1;
          ++ptr;
        }
      }
      answers[get<2>(quer)] = state[(get<1>(quer) + off) % int((state).size())];
    }
  }
  for (int i = 0; i != q; ++i) cout << answers[i] << "\n";
  return 0;
}
