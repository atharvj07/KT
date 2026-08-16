#include <iostream>

int main(){
 long long N;
 std::cin>>N;
 long long ans=0;
 if(N%2==1){
  std::cout<<ans<<std::endl;
  return 0;
 }
 N=N/2;
 while(N>0){
  ans+=N/5;
  N=N/5;
 }
 std::cout<<ans<<std::endl;
}