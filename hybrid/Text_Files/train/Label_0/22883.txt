#include <bits/stdc++.h>
using namespace std;

int MOD=1000000007;

int main(){
  int N; long long K; cin >> N >> K;
  int A[2000];
  for(int i=0; i<N; i++) cin >> A[i];
  
  long long inner=0,outer=0;
  for(int i=0; i<N; i++){
    for(int j=0; j<N; j++){
      if(A[i]>A[j]){
        outer++;
        if(i<j) inner++;
      }
    }
  }
  cout << (inner*K+outer*(K*(K-1)/2%MOD))%MOD << endl;
}