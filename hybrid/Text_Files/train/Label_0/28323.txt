#include <bits/stdc++.h>
using namespace std;
template <class T>
void debug(T a, T b) {
  for (; a != b; a++) cerr << *a << ' ';
  cerr << endl;
}
template <class T>
bool isprime(T x) {
  long long till = (T)sqrt(x + .0);
  if (x <= 1) return 0;
  if (x == 2) return 1;
  if (x / 2 * 2 == x) return 0;
  for (long long i = 3; i <= till; i += 2)
    if (x / i * i == x) return 0;
  return 1;
}
int n, p;
long long x, y;
int a[1000000];
inline long long mod(long long foo) {
  foo += p;
  return foo - foo / p * p;
}
struct Matrix {
  int row, col;
  vector<vector<long long> > body;
  Matrix(int row, int col) {
    this->row = row;
    this->col = col;
    body = vector<vector<long long> >(row, vector<long long>(col, 0));
  }
  Matrix(vector<vector<long long> > matrix) {
    row = (long long)(matrix).size();
    col = (long long)(matrix[0]).size();
    body = matrix;
  }
  Matrix operator*(Matrix other) const {
    Matrix ret = Matrix(row, other.col);
    assert(col == other.row);
    for (int i = 0; i < row; i++)
      for (int j = 0; j < other.col; j++)
        for (int k = 0; k < col; k++) {
          ret.body[i][j] += mod(1LL * body[i][k] * other.body[k][j]);
          ret.body[i][j] = mod(ret.body[i][j]);
        }
    return ret;
  }
};
Matrix binpow(Matrix a, long long n) {
  assert(n >= 1);
  Matrix ret = a;
  n--;
  while (n > 0) {
    if (n & 1) {
      ret = ret * a;
      n--;
    }
    a = a * a;
    n >>= 1;
  }
  return ret;
}
int alacazam(int s, int f, int l, long long x) {
  if (x == 0) return s;
  return (Matrix(vector<vector<long long> >{{s, f, l}}) *
          binpow(Matrix(vector<vector<long long> >{
                     {3, 0, 0}, {-1, 1, 0}, {-1, 0, 1}}),
                 x))
      .body[0][0];
}
int fibazam(int f1, int f2, long long x) {
  if (x == 0) return f2;
  return (Matrix(vector<vector<long long> >{{f1, f2}}) *
          binpow(Matrix(vector<vector<long long> >{{0, 1}, {1, 1}}), x))
      .body[0][1];
}
int main() {
  scanf(
      "%d "
      "%l"
      "ld"
      " "
      "%l"
      "ld"
      " %d",
      &n, &x, &y, &p);
  int sum = 0;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    a[i] = mod(a[i]);
    sum = mod(sum + a[i]);
  }
  if (n == 1) {
    printf("%d", sum);
    return 0;
  }
  sum = alacazam(sum, a[0], a[n - 1], x);
  a[n - 1] = fibazam(a[n - 2], a[n - 1], x);
  sum = alacazam(sum, a[0], a[n - 1], y);
  printf("%d", sum);
  return EXIT_SUCCESS;
}
