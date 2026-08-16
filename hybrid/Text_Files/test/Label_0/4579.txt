#include <bits/stdc++.h>
using namespace std;
int main(){
 int N;
  cin>>N;
  long double sum=0;
  for(int i=0;i<N;i++){
  long double a;
    cin>>a;
    sum+=(1/a);
  }
  cout<<1/sum<<endl;
  
}