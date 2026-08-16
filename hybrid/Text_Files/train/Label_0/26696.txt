#include <bits/stdc++.h>
using namespace std;
int n, maxV, dist[300][300], a[300], b[300];
vector<int> start, destination, water_count;
inline void save_transfer(int x, int y, int count) {
  start.push_back(x + 1);
  destination.push_back(y + 1);
  water_count.push_back(count);
}
void transfer(int x, int y, int count) {
  if (dist[x][y] == 1) {
    save_transfer(x, y, count);
    return;
  }
  for (int i = 0; i < n; i++)
    if (dist[x][i] == 1 && dist[i][y] < dist[x][y]) {
      int tmp = count;
      if (a[i] < count) {
        save_transfer(x, i, count - a[i]);
        tmp = tmp - count + a[i];
      }
      transfer(i, y, count);
      if (tmp != 0) save_transfer(x, i, tmp);
      break;
    }
}
int abs(int x) { return x >= 0 ? x : -x; }
int min(int x, int y) { return x >= y ? y : x; }
int main() {
  int m;
  cin >> n >> maxV >> m;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) dist[i][j] = 1000000000;
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < n; i++) cin >> b[i];
  for (int i = 0; i < m; i++) {
    int x, y;
    cin >> x >> y;
    dist[x - 1][y - 1] = dist[y - 1][x - 1] = 1;
  }
  for (int k = 0; k < n; k++)
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
  for (int i = 0; i < n; i++)
    if (a[i] != b[i]) {
      int signI = (a[i] - b[i]) / abs(a[i] - b[i]);
      for (int j = 0; j < n; j++) {
        if (a[i] == b[i]) break;
        if (dist[i][j] != 1000000000 && a[j] != b[j]) {
          int signJ = (a[j] - b[j]) / abs(a[j] - b[j]);
          if (signI != signJ) {
            int needing_water = min(abs(a[i] - b[i]), abs(a[j] - b[j]));
            if (signI > 0) {
              transfer(i, j, needing_water);
              a[i] -= needing_water;
              a[j] += needing_water;
            } else {
              transfer(j, i, needing_water);
              a[i] += needing_water;
              a[j] -= needing_water;
            }
          }
        }
      }
      if (a[i] != b[i]) {
        cout << "NO";
        return 0;
      }
    }
  cout << start.size() << endl;
  for (int i = 0; i < start.size(); i++) {
    cout << start[i] << " " << destination[i] << " " << water_count[i] << endl;
  }
  return 0;
}
