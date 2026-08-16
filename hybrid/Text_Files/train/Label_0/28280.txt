#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for(int i=0; i<(int)(n); i++)
int main(){
int N, M=0; cin >> N; long x[N], y[N]; map<pair<long, long>, int> m;
REP(i, N){ cin >> x[i] >> y[i]; }
REP(i, N-1){ for(int j=i+1; j<N; j++){
  long X=x[j]-x[i], Y=y[j]-y[i];
  if(Y==0){ X=abs(X); }else if(Y<0){ X=-X; Y=-Y; }
  pair<long, long> p=make_pair(X, Y);
  M=max(M, ++m[p]);  
} }
cout << N-M << "\n";
}