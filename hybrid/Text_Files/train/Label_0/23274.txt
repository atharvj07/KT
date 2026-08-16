#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  int DIV = 1e+9 + 7;
  int N, M; cin >> N >> M;
  int S[N]; for (int i = 0; i < N; i++) cin >> S[i];
  int T[M]; for (int j = 0; j < M; j++) cin >> T[j];
  int D[N+1][M+1];
  for (int i = 0; i <= N; i++) D[i][0] = 1;
  for (int j = 0; j <= M; j++) D[0][j] = 1;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      D[i+1][j+1] = (D[i+1][j] + D[i][j+1]) % DIV;
      if (S[i] != T[j])
        D[i+1][j+1] = (D[i+1][j+1] - D[i][j] + DIV) % DIV;
    }
  }
  cout << D[N][M] << endl;
}