#include <bits/stdc++.h>
using namespace std;
int main() {
  int N;
  cin >> N;
  int A[3][N];
  for (int i = 0; i < N; i++) cin >> A[0][i];
  for (int i = 0; i < N; i++) cin >> A[1][i];
  for (int i = 0; i < N; i++) cin >> A[2][i];
  long long DP[N][4];
  DP[0][0] = A[0][0];
  DP[0][1] = A[0][0];
  DP[0][2] = A[1][0];
  DP[0][3] = A[1][0];
  long long max_val;
  int i;
  for (i = 1; i < N - 1; i++) {
    DP[i][0] = A[0][i] + max(DP[i - 1][2], DP[i - 1][3]);
    DP[i][1] = A[1][i] + max(DP[i - 1][0], DP[i - 1][1]);
    DP[i][2] = A[1][i] + max(DP[i - 1][2], DP[i - 1][3]);
    DP[i][3] = A[2][i] + max(DP[i - 1][0], DP[i - 1][1]);
  }
  if (i >= 1) {
    DP[i][0] = A[0][i] + max(DP[i - 1][2], DP[i - 1][3]);
    DP[i][1] = A[1][i] + max(DP[i - 1][0], DP[i - 1][1]);
    DP[i][2] = A[0][i] + max(DP[i - 1][2], DP[i - 1][3]);
    DP[i][3] = A[1][i] + max(DP[i - 1][0], DP[i - 1][1]);
  }
  max_val = 0;
  max_val =
      max(max(DP[N - 1][0], DP[N - 1][1]), max(DP[N - 1][2], DP[N - 1][3]));
  if (N == 1) {
    cout << A[0][0] << endl;
  } else
    cout << max_val << endl;
  return 0;
}
