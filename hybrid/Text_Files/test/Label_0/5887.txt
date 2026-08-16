#include <bits/stdc++.h>
using namespace std;
struct SegmentMaxTree {
  SegmentMaxTree(int default_value, int n) : default_value(default_value) {
    sz = 1;
    while (sz < n) {
      sz = sz << 1;
    }
    items.resize(2 * sz - 1, default_value);
  }
  void Set(int first, int last, int value) {
    return Set(first, last, value, 0, 0, sz - 1);
  }
  void Set(int first, int last, int value, size_t node, int segment_begin,
           int segment_last) {
    first = max(first, segment_begin);
    last = min(last, segment_last);
    if (first > last) {
      return;
    }
    if (first == segment_begin && last == segment_last) {
      items[node] = max(value, items[node]);
    } else {
      auto segment_mid = (segment_begin + segment_last + 1) / 2;
      Set(first, last, value, node * 2 + 1, segment_begin, segment_mid - 1);
      Set(first, last, value, node * 2 + 2, segment_mid, segment_last);
    }
  }
  int Get(int idx) { return Get(idx, 0, 0, sz - 1); }
  int Get(int idx, size_t node, int segment_begin, int segment_last) {
    int best_value = items[node];
    if (segment_begin == segment_last) {
      return best_value;
    }
    auto segment_mid = (segment_begin + segment_last + 1) / 2;
    if (segment_mid <= idx) {
      best_value =
          max(best_value, Get(idx, 2 * node + 2, segment_mid, segment_last));
    } else {
      best_value = max(best_value,
                       Get(idx, 2 * node + 1, segment_begin, segment_mid - 1));
    }
    return best_value;
  }
  int default_value, sz;
  vector<int> items;
};
struct CompressedSegmentMaxTree {
  CompressedSegmentMaxTree(int default_value, const set<long long>& items)
      : tree(default_value, items.size()) {
    int i = 0;
    for (auto el : items) {
      element2index[el] = i++;
    }
  }
  void Set(int first, int last, int value) {
    tree.Set(element2index.at(first), element2index.at(last), value);
  }
  int Get(int pos) { return tree.Get(element2index.at(pos)); }
  SegmentMaxTree tree;
  map<long long, int> element2index;
};
struct Record {
  int row, col;
  char c;
};
void solve() {
  int n, q;
  cin >> n >> q;
  vector<Record> records(q);
  set<long long> coordinates;
  for (int(i) = 0; (i) < (q); (i)++) {
    Record& rec = records[i];
    cin >> rec.col >> rec.row >> rec.c;
    rec.row--;
    rec.col--;
    coordinates.insert(rec.col);
    coordinates.insert(rec.row);
  }
  coordinates.insert(-1);
  CompressedSegmentMaxTree max_eaten_by_cols(-1, coordinates);
  CompressedSegmentMaxTree max_eaten_by_rows(-1, coordinates);
  set<int> seen_left, seen_up;
  for (auto& rec : records) {
    int row = rec.row;
    int col = rec.col;
    char c = rec.c;
    auto& active_set = (c == 'L') ? max_eaten_by_rows : max_eaten_by_cols;
    auto& anti_active_set = (c != 'L') ? max_eaten_by_rows : max_eaten_by_cols;
    int point = (c == 'L') ? row : col;
    int anti_point = (c != 'L') ? row : col;
    int can_eat_upto = active_set.Get(point);
    if (seen_left.find(row) != seen_left.end() ||
        seen_up.find(col) != seen_up.end()) {
      can_eat_upto = anti_point;
    } else {
      anti_active_set.Set(can_eat_upto, anti_point, point);
    }
    printf("%d\n", (anti_point - can_eat_upto));
    if (c == 'L') {
      seen_left.insert(row);
    } else {
      seen_up.insert(col);
    }
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  solve();
  return 0;
}
