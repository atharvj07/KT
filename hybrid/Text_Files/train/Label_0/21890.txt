#include <bits/stdc++.h>
using namespace std;
const int Prime[25] = {2,  3,  5,  7,  11, 13, 17, 19, 23, 29, 31, 37, 41,
                       43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
const int Mod[4] = {300690390, 2044926619, 1808691197, 2073080791};
vector<int> opt[17][4];
int N, V[17], len;
int d;
long long c, M[31111];
bool vis[25];
string S;
int Calc(int P) {
  int Ds = 0;
  for (int i = 0; i < len; i++) Ds = Ds * (d + 1) + V[i];
  if (opt[d][P][Ds] != -1) return opt[d][P][Ds];
  opt[d][P][Ds] = 1;
  for (int i = 0; i < len; i++)
    if (V[i] == d) {
      for (int j = 0; j < d; j++) {
        V[i] = j;
        opt[d][P][Ds] = (long long)opt[d][P][Ds] * Calc(P) % Mod[P];
      }
      V[i] = d;
      return opt[d][P][Ds];
    }
  int D1 = 0;
  for (int i = 0; i < len; i++) D1 = D1 * d + V[i];
  if (D1 < N) opt[d][P][Ds] = M[D1] % Mod[P];
  return opt[d][P][Ds];
}
void Pri() {
  for (int i = 0; i < 25; i++)
    if (vis[i]) {
      printf("%d\n", Prime[i]);
      return;
    }
  printf("-1\n");
}
int main() {
  ios::sync_with_stdio(false);
  cin >> N;
  for (int i = 0; i < N; i++) cin >> M[i];
  for (int i = 2; i <= 16; i++) {
    int k1 = 1, k2 = 1;
    len = 0;
    for (; k1 < N; k1 *= i, k2 *= i + 1) {
    }
    for (int j = 0; j < 4; j++) opt[i][j].resize(k2, -1);
  }
  int T;
  cin >> T;
  while (T--) {
    cin >> d >> S >> c;
    int k1 = 1, k2 = 1;
    len = 0;
    for (; k1 < N; k1 *= d, k2 *= d + 1, len++) {
    }
    for (int i = 0; i < len; i++) {
      int k = S.length() - len + i;
      if (S[k] == '?')
        V[i] = d;
      else {
        if (S[k] <= '9' && S[k] >= '0')
          V[i] = S[k] - '0';
        else
          V[i] = S[k] - 'A' + 10;
      }
      if (k < 0) V[i] = 0;
    }
    memset(vis, false, sizeof(vis));
    for (int i = 0; i < 4; i++) {
      int tmp = Calc(i);
      tmp = (tmp + c) % Mod[i];
      for (int j = 0; j < 25; j++)
        if (Mod[i] % Prime[j] == 0 && tmp % Prime[j] == 0) vis[j] = true;
    }
    Pri();
  }
  return 0;
}
