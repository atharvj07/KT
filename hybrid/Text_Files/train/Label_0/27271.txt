#include <bits/stdc++.h>
using namespace std;
struct Interval {
  int left, right, start, end;
};
struct SegmentNode {
  int left, right;
  vector<pair<int, int>> edges;
};
struct DsuState {
  vector<int> parent, size, parity;
  stack<int> ops;
  DsuState(int n) : parent(n), size(n, 1), parity(n, 0) {
    for (int i = 0; i < n; i++) parent[i] = i;
  }
  pair<int, int> get_parent_and_parity(int x) {
    if (parent[x] != x) {
      auto r = get_parent_and_parity(parent[x]);
      return {r.first, (r.second + parity[x]) & 1};
    }
    return {x, 0};
  }
  void merge(int x, int y) {
    auto ppx = get_parent_and_parity(x), ppy = get_parent_and_parity(y);
    if (ppx.first != ppy.first) {
      if (size[ppx.first] < size[ppy.first]) {
        parent[ppx.first] = ppy.first;
        size[ppy.first] += size[ppx.first];
        parity[ppx.first] = (ppx.second + ppy.second + 1) & 1;
        ops.push(ppx.first);
      } else {
        parent[ppy.first] = ppx.first;
        size[ppx.first] += ppy.first;
        parity[ppy.first] = (ppx.second + ppy.second + 1) & 1;
        ops.push(ppy.first);
      }
    }
  }
  void rollback() {
    int x = ops.top(), px = get_parent_and_parity(x).first;
    ops.pop();
    size[px] -= size[x];
    parity[px] = 0;
    parent[x] = x;
  }
};
void build_segments(vector<SegmentNode> &segments, int id, int l, int r) {
  segments[id].left = l;
  segments[id].right = r;
  if (l < r) {
    int m = (l + r) >> 1;
    build_segments(segments, (id << 1) + 1, l, m);
    build_segments(segments, (id + 1) << 1, m + 1, r);
  }
}
void add_interval(vector<SegmentNode> &segments, int id, Interval interval) {
  if (interval.left > segments[id].right || interval.right < segments[id].left)
    return;
  if (interval.left <= segments[id].left &&
      interval.right >= segments[id].right) {
    segments[id].edges.push_back({interval.start, interval.end});
    return;
  }
  add_interval(segments, (id << 1) + 1, interval);
  add_interval(segments, (id + 1) << 1, interval);
}
void dfs(vector<SegmentNode> &segments, int id, DsuState &state,
         vector<bool> &ans) {
  int merge_count = 0;
  bool flag = true;
  for (int i = 0; i < segments[id].edges.size(); i++) {
    auto edge = segments[id].edges[i];
    auto r1 = state.get_parent_and_parity(edge.first);
    auto r2 = state.get_parent_and_parity(edge.second);
    if (r1.first == r2.first) {
      if ((r1.second + r2.second) % 2 == 0) {
        flag = false;
        break;
      }
    } else {
      state.merge(edge.first, edge.second);
      merge_count++;
    }
  }
  if (flag) {
    if (segments[id].left == segments[id].right) {
      ans[segments[id].left] = true;
    } else {
      dfs(segments, (id << 1) + 1, state, ans);
      dfs(segments, (id + 1) << 1, state, ans);
    }
  }
  for (int i = 0; i < merge_count; i++) state.rollback();
}
int main() {
  int n, q;
  scanf("%d %d", &n, &q);
  vector<Interval> intervals;
  map<pair<int, int>, int> edges;
  for (int i = 0; i < q; i++) {
    int x, y;
    scanf("%d %d", &x, &y);
    x--, y--;
    if (edges.count({x, y})) {
      intervals.push_back({edges[{x, y}], i - 1, x, y});
      edges.erase({x, y});
    } else {
      edges.insert({{x, y}, i});
    }
  }
  for (auto &p : edges)
    intervals.push_back({p.second, q - 1, p.first.first, p.first.second});
  vector<SegmentNode> segments(q * 4);
  build_segments(segments, 0, 0, q - 1);
  for (auto interval : intervals) {
    add_interval(segments, 0, interval);
  }
  DsuState state(n);
  vector<bool> ans(q, false);
  dfs(segments, 0, state, ans);
  for (int i = 0; i < q; i++)
    if (ans[i])
      printf("YES\n");
    else
      printf("NO\n");
  return 0;
}
