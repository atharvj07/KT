#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  vector < pair<int,int> > br;
  int n;
  while(1){
    cin>>n;
    if(n==0) break;
    br.clear();
    for(int i=0;i<n;i++){
      int m,a,b;
      cin>>m>>a>>b;
      br.push_back(make_pair(a,m));
      br.push_back(make_pair(b,(-1)*m));
    }
    sort(br.begin(),br.end());
    bool f=0;
    int brsum=0;
    for(int i=0;i<br.size();i++){
    brsum+=br[i].second;
    if(brsum>150){
      f=1;
      break;
    }
    }
    if(f==0) cout<<"OK"<<endl;
    else cout <<"NG"<<endl;
  }
  return 0;
}