#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;
int main(){
  int N,M;
  cin>>N>>M;
  pair<int,int> p[100000];
  for(int i=0;i<M;i++){
    int a,b;
    cin>>a>>b;
    p[i]=make_pair(b,a);
  }
  sort(p,p+M);
  int broken=0;
  int answer=0;
  for(int i=0;i<M;i++){
    if(broken<p[i].second){
      answer++;
      broken=p[i].first-1;
    }
  }
  cout<<answer<<endl;
  
  return 0;
}