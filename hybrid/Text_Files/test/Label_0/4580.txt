#include<bits/stdc++.h>
using namespace std;
int main(){
  int A,B;
  cin>>A>>B;
  int cnt=0;
  if((A<0&&abs(A)<abs(B))||(A>0&&abs(A)>abs(B))){
    A*=-1;
    cnt++;
  }
  cnt+=abs(abs(A)-abs(B));
  A+=abs(abs(A)-abs(B));
  if(A!=B)cnt++;
  cout<<cnt<<endl;
}