#include <bits/stdc++.h>
using namespace std;

int main(){
  int N,j=0;
  cin>>N;
  for(int i=0;i<N;i++){
    int a;
    cin>>a;
    j+=a-1;
  }
  cout<<j<<endl;
}