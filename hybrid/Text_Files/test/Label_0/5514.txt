#include <bits/stdc++.h>
using namespace std;
void Get(int &T) {
  char C;
  bool F = 0;
  for (; C = getchar(), C < '0' || C > '9';)
    if (C == '-') F = 1;
  for (T = C - '0'; C = getchar(), C >= '0' && C <= '9'; T = T * 10 + C - '0')
    ;
  F && (T = -T);
}
int N, M;
int Cnt[125];
void Init() {
  Get(N);
  Get(M);
  Get(N);
  for (int i = 1, T; i <= N; i++) {
    Get(T);
    Cnt[std::min(T % M, M - T % M)]++;
  }
}
long long Ans;
void DFS(int X, bitset<125> Hash, int Last, long long Ans0) {
  (Ans += Ans0) %= (1000000007);
  if ((1 << X) > M) return;
  for (int i = Last + 1; i <= M; i++) {
    if (Cnt[i] == 0) continue;
    if ((Hash[M - i]) == 0 && (Hash[i]) == 0)
      DFS(X + 1,
          Hash | (Hash << i) | (Hash >> (M - i)) | (Hash >> i) |
              (Hash << (M - i)),
          i, (Ans0 * Cnt[i]) % (1000000007));
  }
}
void Work() { DFS(1, 1, 0, 1); }
void Output() { printf("%I64d\n", Ans); }
int main() {
  Init();
  Work();
  Output();
  return 0;
}
