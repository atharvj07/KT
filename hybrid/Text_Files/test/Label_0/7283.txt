#include <bits/stdc++.h>
using namespace std;
const int inf = 1000000007;
const long long linf = 1000000000000000000LL;
const double eps = 0.000001;
const double pi = 3.14159265358979323846;
template <class T>
T abs(T k) {
  return k >= 0 ? k : -k;
}
template <class T>
T sqr(T n) {
  return n * n;
}
template <class T>
T gcd(T a, T b) {
  return b ? gcd(b, a % b) : a;
}
template <class T>
T mod(T a, T b) {
  return (a % b + b) % b;
}
template <class T>
void mode(T &a, T b) {
  a = mod(a, b);
}
template <class T>
void maxe(T &a, T b) {
  a = max(a, b);
}
template <class T>
void mine(T &a, T b) {
  a = min(a, b);
}
void fileio_in_out() {
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
}
void fileio_txt() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
}
int test;
int n, m, k, ans;
int a[2][2];
char s1[2222222], s2[2222222];
const char aa[][7] = {"Draw", "First", "Second"};
int getans() {
  for (int i = 0; i < 2 * n; i++) a[s1[i] - '0'][s2[i] - '0']++;
  if (a[1][1] & 1) {
    if (a[0][1] == 0) return 1;
    a[0][1]--;
  }
  return (a[1][0] == a[0][1] || a[1][0] + 1 == a[0][1])
             ? 0
             : ((a[1][0] > a[0][1]) ? 1 : 2);
}
int main() {
  scanf("%d", &n);
  scanf("%s%s", s1, s2);
  printf("%s\n", aa[getans()]);
  return 0;
}
