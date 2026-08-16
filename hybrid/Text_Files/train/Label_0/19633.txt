#include <iostream>
#include <algorithm>
#include <map>
#include <cstring>
#define FMAX 10000
#define initarr(a) memset(a, 0, sizeof(a))
using namespace std;
typedef map<short, map<short, short> > V;

short calc_x_arr[FMAX];

void add_vertex(V &vertexes, short x, short y, short t) {
  auto &xv = vertexes[y];
  auto &sum = xv[x];
  sum += t;
}

int main() {
  short n, r;
  while (cin >> n >> r, n || r) {
    // load
    short x1, y1, x2, y2;
    short min_x = FMAX, min_y = FMAX, max_x = 0, max_y = 0;
    V vertexes;
    for (short i = 0; i < n; i++) {
      cin >> x1 >> y1 >> x2 >> y2;
      add_vertex(vertexes, x1, y1, 1);
      add_vertex(vertexes, x1, y2, -1);
      add_vertex(vertexes, x2, y1, -1);
      add_vertex(vertexes, x2, y2, 1);
      min_x = min(min_x, x1);
      min_y = min(min_y, y1);
      max_x = max(max_x, x2);
      max_y = max(max_y, y2);
    }

    // calc
    int area = 0, perimeter = 0;
    short prev_y = -1;
    short prev_partial_vertical_perimeter = 0;
    short prev_partial_area = 0;
    initarr(calc_x_arr);
    for (auto yvit = vertexes.begin(); yvit != vertexes.end(); yvit++) {
      area += prev_partial_area * (yvit->first - prev_y - 1);
      prev_partial_area = 0;
      if (r == 2) {
        perimeter += prev_partial_vertical_perimeter * (yvit->first - prev_y - 1);
        prev_partial_vertical_perimeter = 0;
      }
      short left = 0;
      short xsum = 0;
      auto xvit = yvit->second.begin();
      for (short x = min_x; x <= max_x; x++) {
        if (x == xvit->first) {
          xsum += xvit->second;
          if (++xvit == yvit->second.end()) {
            xvit = yvit->second.begin();
          }
        }
        short current = xsum + calc_x_arr[x];
        if (current != 0) prev_partial_area++;
        if (r == 2) {
          bool vdelta = left == 0 ^ current == 0;
          prev_partial_vertical_perimeter += vdelta;
          perimeter += vdelta + (calc_x_arr[x] == 0 ^ current == 0);
        }
        left = calc_x_arr[x] = current;
      }
      area += prev_partial_area;
      prev_y = yvit->first;
    }

    cout << area << endl;
    if (r == 2) cout << perimeter << endl;
  }
  return 0;
}