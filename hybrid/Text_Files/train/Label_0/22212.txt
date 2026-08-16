#include <bits/stdc++.h>
using namespace std;
int n;
int T[200005];
int t[200005];
void up(int idx, int val) {
  while (idx <= n) {
    t[idx] += val;
    idx += (idx & -idx);
  }
}
int que(int idx) {
  int sum = 0;
  while (idx > 0) {
    sum += t[idx];
    idx -= (idx & -idx);
  }
  return sum;
}
void update(int idx, int val) {
  while (idx <= n) {
    T[idx] += val;
    idx += (idx & -idx);
  }
}
int query(int idx) {
  int sum = 0;
  while (idx > 0) {
    sum += T[idx];
    idx -= (idx & -idx);
  }
  return sum;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin >> n;
  pair<int, int> A[n];
  long long int sm = 0;
  int arr[n];
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
    if (arr[i] == 1) update(i + 1, 1);
  }
  for (int i = 0; i < n; i++)
    if (arr[i] == 0) {
      A[i].first = i;
      A[i].second = i;
    } else {
      A[i].first = n - i - 1;
      A[i].second = i;
    }
  sort(A, A + n);
  for (int i = n - 1; i >= 0; i--) {
    int x = query(A[i].second);
    int yy1 = query(n);
    int yy2 = query(A[i].second + 1);
    int y = (n - yy1) - (A[i].second + 1 - yy2);
    sm += x + y;
    int s = que(n) - que(A[i].second);
    sm -= s;
    if (arr[A[i].second] == 1) update(A[i].second + 1, -1);
    up(A[i].second + 1, 1);
  }
  cout << sm << "\n";
  return 0;
}
