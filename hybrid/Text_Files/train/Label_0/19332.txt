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
struct Point {
  double X, Y, Z;
};
Point Cp(Point U, Point V) {
  return (Point){U.Y * V.Z - U.Z * V.Y, U.Z * V.X - U.X * V.Z,
                 U.X * V.Y - U.Y * V.X};
}
double Cross(Point A, Point V, Point P) {
  P.X -= A.X;
  P.Y -= A.Y;
  P.Z -= A.Z;
  return (P.X * V.X + P.Y * V.Y + P.Z * V.Z) /
         (V.X * V.X + V.Y * V.Y + V.Z * V.Z);
}
Point S, V;
double R;
void Init() {
  scanf("%lf%lf%lf%lf%lf%lf%lf", &S.X, &S.Y, &S.Z, &V.X, &V.Y, &V.Z, &R);
}
double Ans;
void Check(Point A, Point V, Point P, double R) {
  double T = Cross(A, V, P);
  double DX = A.X + V.X * T - P.X;
  double DY = A.Y + V.Y * T - P.Y;
  double DZ = A.Z + V.Z * T - P.Z;
  DX *= DX;
  DY *= DY;
  DZ *= DZ;
  double Dis2 = DX + DY + DZ;
  R *= R;
  R -= Dis2;
  R /= (V.X * V.X + V.Y * V.Y + V.Z * V.Z);
  if (R < 0) return;
  double DT = sqrt(R);
  T -= DT;
  if (T > 0 && Ans > T) Ans = T;
}
int N, M;
void Work() {
  Ans = 1 / 0.;
  Get(N);
  for (int i = 1; i <= N; i++) {
    Point P;
    double R0;
    Point Q;
    scanf("%lf%lf%lf%lf", &P.X, &P.Y, &P.Z, &R0);
    Check(S, V, P, R + R0);
    Get(M);
    for (int i = 1; i <= M; i++) {
      scanf("%lf%lf%lf", &Q.X, &Q.Y, &Q.Z);
      Q.X += P.X;
      Q.Y += P.Y;
      Q.Z += P.Z;
      Check(S, V, Q, R);
    }
  }
}
void Output() {
  if (Ans >= 1 / 0.)
    puts("-1");
  else
    printf("%lf\n", Ans);
}
int main() {
  Init();
  Work();
  Output();
  return 0;
}
