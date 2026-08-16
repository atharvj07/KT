#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 10;
struct Node {
  int x, y, id;
  Node operator+(Node A) { return (Node){x + A.x, y + A.y, id}; }
  Node operator-(Node A) { return (Node){x - A.x, y - A.y, id}; }
  long long operator*(Node A) const { return 1ll * x * A.y - 1ll * y * A.x; }
  long long dis() const { return 1ll * x * x + 1ll * y * y; }
} A[N], P[N], bs;
int n, tot, vis[N], sta[N], top;
int cmp1(const Node& A, const Node& B) {
  return A.y != B.y ? A.y < B.y : A.x < B.x;
}
int cmp2(const Node& A, const Node& B) {
  return A * B == 0 ? A.dis() < B.dis() : A * B > 0;
}
void Convex() {
  sort(A + 1, A + tot + 1, cmp1);
  bs = A[1];
  top = 0;
  for (int i = tot; i >= 1; i--) A[i] = A[i] - A[1];
  sort(A + 1, A + tot + 1, cmp2);
  for (int i = 1; i <= tot; sta[++top] = i, i++)
    while (top >= 2 &&
           (A[i] - A[sta[top - 1]]) * (A[sta[top]] - A[sta[top - 1]]) >= 0)
      top--;
  for (int i = 1; i <= top; i++) {
    A[i] = A[sta[i]];
    Node P = bs + A[i];
    if ((P.x & 1) || (P.y & 1)) puts("Ani"), exit(0);
  }
}
int main() {
  cin >> n;
  for (int i = 1; i <= n; i++) scanf("%d%d", &P[i].x, &P[i].y), P[i].id = i;
  P[++n] = (Node){0, 0, 0};
  for (int i = 1; i <= n; i++) A[i] = P[i];
  tot = n;
  Convex();
  tot = 0;
  for (int i = 1; i <= top; i++) vis[A[i].id] = (i & 1) ? 1 : 2;
  for (int i = 1; i <= n; i++)
    if (vis[i] != 1) A[++tot] = P[i];
  Convex();
  tot = 0;
  for (int i = 1; i <= n; i++)
    if (vis[i] != 2) A[++tot] = P[i];
  Convex();
  puts("Borna");
}
