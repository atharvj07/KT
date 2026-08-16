#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2000111;
const int MOD = 1000000007;
int sr;
int sum(int a, int b) {
  sr = a + b;
  if (sr >= MOD) sr -= MOD;
  return sr;
}
int mul(int a, int b) { return (int)((1LL * a * b) % (1LL * MOD)); }
int pow(int a, int k) {
  int ret = 1, t = a;
  while (k) {
    if (k & 1) {
      ret = mul(ret, t);
    }
    t = mul(t, t);
    k >>= 1;
  }
  return ret;
}
int P[MAXN], Pc;
int Id[MAXN], Sp[MAXN];
int Mc[MAXN], Max[MAXN];
bool Vis(int a) { return Mc[Id[a]]; }
void Push(int a, int t) {
  a = Id[a];
  if (Max[a] < t) {
    Max[a] = t;
    Mc[a] = 1;
  } else if (Max[a] == t)
    ++Mc[a];
}
int Ans;
bool Ask(int a, int t) {
  a = Id[a];
  if (Max[a] > t || Mc[a] > 1) {
    return true;
  }
  return false;
}
int N = 2000000;
int A[MAXN];
bool _[MAXN];
int main() {
  for (int i = 2; i <= N; ++i) Id[i] = 1;
  for (int i = 2; i <= N; ++i) {
    if (Id[i]) {
      P[++Pc] = i;
      Id[i] = Pc;
      Sp[i] = i;
    }
    for (int j = 1; j <= Pc && P[j] <= N / i; ++j) {
      Id[i * P[j]] = 0;
      Sp[i * P[j]] = P[j];
      if (i % P[j] == 0) break;
    }
  }
  cin >> N;
  for (int i = 1; i <= N; ++i) cin >> A[i];
  sort(A + 1, A + N + 1);
  for (int i = N, v; i >= 1; --i) {
    v = A[i];
    if (Vis(v)) {
      _[i] = true;
      for (int k = v - 1, c = 0, p = Sp[k]; k > 1;) {
        if (Sp[k] != p) {
          Push(p, c);
          c = 0;
          p = Sp[k];
        }
        ++c;
        k /= Sp[k];
        if (k == 1) Push(p, c);
      }
    } else
      Push(v, 1);
  }
  Ans = 1;
  for (int i = 1; i <= Pc; ++i)
    if (Mc[i]) Ans = mul(Ans, pow(P[i], Max[i]));
  for (int i = N, v; i >= 1; --i) {
    v = A[i];
    bool w = true;
    if (_[i]) {
      for (int k = v - 1, c = 0, p = Sp[k]; k > 1;) {
        if (Sp[k] != p) {
          w &= Ask(p, c);
          c = 0;
          p = Sp[k];
        }
        ++c;
        k /= Sp[k];
        if (k == 1) w &= Ask(p, c);
      }
    } else
      w &= Ask(v, 1);
    if (w) {
      cout << Ans + 1 << endl;
      return 0;
    }
  }
  cout << Ans << endl;
  return 0;
}
