#include<bits/stdc++.h>
using namespace std;

int main(){
  int N, M;
  cin >> N >> M;
  vector<int> H(N);
  int A, B;
  vector<bool> X(N,true);
  for(int i=0; i<N; i++) cin >> H[i];
  for(int i=0; i<M; i++){
    cin >> A >> B;
    if(H[A-1]>=H[B-1]) X[B-1]=false;
    if(H[B-1]>=H[A-1]) X[A-1]=false;
  }
  int cnt=0;
  for(int i=0; i<N; i++){
    if(X[i]==true) cnt++;
  }
  cout <<cnt <<endl;
}