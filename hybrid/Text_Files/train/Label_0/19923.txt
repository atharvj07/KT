#include<bits/stdc++.h>

using namespace std;


typedef long long int64;

int main()
{
  int X, Y, Z, A, B, C, N;
  int64 a[1000] = {}, b[1000] = {}, c[1000] = {};

  cin >> X >> Y >> Z >> A >> B >> C >> N;
  for(int i = 0; i < X; i++) ++a[abs(i - A) % N];
  for(int i = 0; i < Y; i++) ++b[abs(i - B) % N];
  for(int i = 0; i < Z; i++) ++c[abs(i - C) % N];

  int64 d[1000] = {}, ret[1000] = {};
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) d[(i + j) % N] += a[i] * b[j];
  }

  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) {
      ret[(i + j) % N] += d[i] * c[j];
    }
  }

  for(int i = 0; i < N; i++) {
    if(i > 0) cout << " ";
    cout << ret[i];
  }
  cout << endl;

}