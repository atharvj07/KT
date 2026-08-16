#include <bits/stdc++.h>
using namespace std;
const int MAX = 5010;
int N, K, A[MAX], B[MAX], D[MAX][MAX];
int main() {
  ios_base::sync_with_stdio(0), cin.tie(0);
  cin >> N >> K;
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  int j = 0;
  sort(A, A + N);
  for (int i = 0; i < N; i++) {
    while (j + 1 < N && A[j + 1] <= A[i] + 5) j++;
    B[i] = j;
  }
  for (int j = 1; j <= K; j++)
    for (int i = N - 1; i >= 0; i--) {
      D[i][j] = max(D[i + 1][j], D[B[i] + 1][j - 1] + B[i] - i + 1);
    }
  cout << D[0][K];
}
