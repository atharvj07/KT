#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int dy[] = {-1, 0, 0, 1};
int dx[] = {0, -1, 1, 0};

void solve() {
  int a[10][10];
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      cin >> a[i][j];
    }
  }
  int tmp[10][10];
  for (int i = 0; i < 1 << 10; i++) {
    memset(tmp, 0, sizeof(tmp));
    for (int j = 0; j < 10; j++) {
      if (i >> j & 1) tmp[0][j] = 1;
    }
    for (int j = 0; j + 1 < 10; j++) {
      for (int k = 0; k < 10; k++) {
        int sum = tmp[j][k];
        for (int l = 0; l < 4; l++) {
          int ny = j + dy[l], nx = k + dx[l];
          if (ny >= 0 && ny < 10 && nx >= 0 && nx < 10) sum += tmp[ny][nx];
        }
        if ((sum + a[j][k]) % 2 == 0) continue;
        tmp[j + 1][k] = 1;
      }
    }
    int tmp2[10][10];
    for (int j = 0; j < 10; j++) {
      for (int k = 0; k < 10; k++) {
        tmp2[j][k] = tmp[j][k];
        for (int l = 0; l < 4; l++) {
          int ny = j + dy[l], nx = k + dx[l];
          if (ny >= 0 && ny < 10 && nx >= 0 && nx < 10) (tmp2[j][k] += tmp[ny][nx]) %= 2;
        }
      }
    }
    bool ng = false;
    for (int j = 0; j < 10; j++) {
      for (int k = 0; k < 10; k++) {
        ng |= tmp2[j][k] != a[j][k];
      }
    }
    if (ng) continue;
    for (int j = 0; j < 10; j++) {
      for (int k = 0; k < 10; k++) {
        cout << tmp[j][k] << " \n"[k + 1 == 10];
      }
    }
    return;
  }
}

int main() {
  cin.tie(0);
  ios_base::sync_with_stdio(false);
  cout << fixed << setprecision(10);
  
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    solve();
  }

  return 0;
}
