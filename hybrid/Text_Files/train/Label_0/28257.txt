#include <bits/stdc++.h>
using namespace std;
void Q_Q() {
  ios::sync_with_stdio(0);
  ios_base::sync_with_stdio(0);
  cin.tie(0), cout.tie(0);
}
int main() {
  Q_Q();
  int n;
  cin >> n;
  int arr[n];
  deque<int> dq;
  int ans = 0;
  int a = 1;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  for (int i = n - 1; i > 0; i--) {
    if (i == n - 1) {
      if (arr[i] <= arr[0]) {
        dq.push_front(arr[i]);
        ans++;
      } else {
        break;
      }
    } else {
      if (arr[i] <= arr[i + 1]) {
        dq.push_front(arr[i]);
        ans++;
      } else {
        break;
      }
    }
  }
  for (int i = 0; i < n; i++) {
    dq.push_back(arr[i]);
  }
  for (int i = 0; i < n; i++) {
    if (i != n - 1) {
      if (dq[i] > dq[i + 1]) {
        cout << -1;
        return 0;
      } else if (dq[i] == dq[i + 1]) {
        a++;
      }
    }
  }
  if (a == n) {
    cout << 0;
  } else {
    cout << ans;
  }
  return 0;
}
