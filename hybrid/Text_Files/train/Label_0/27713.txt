//53
#include<iostream>

using namespace std;

int main(){
  for(int L;cin>>L,L;){
    int m=0;
    for(int i=1;i<=12;i++){
      int M,N;
      cin>>M>>N;
      L-=M-N;
      if(m==0&&L<=0){
	m=i;
      }
    }
    if(m){
      cout<<m<<endl;
    }else{
      cout<<"NA"<<endl;
    }
  }
  return 0;
}
  