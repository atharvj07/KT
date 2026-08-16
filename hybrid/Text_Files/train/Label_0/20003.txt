#include<bits/stdc++.h>
using namespace std;
int cnt[109];

int main(){
  int h,w;
  cin>>h>>w;
  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      char c;
      cin>>c;
      cnt[c-'a']++;
    }
  }

  int t=0;
  for(int i=0;i<26;i++){
    t+=cnt[i]/4;
  }

  if(t<(h/2)*(w/2)){
    cout<<"No"<<endl;
    return(0);
  }

  int p=0;
  for(int i=0;i<26;i++){
    if(cnt[i]%2==1){
      p++;
    }
  }

  if(p==0||h%2==1&&w%2==1&&p==1){
    cout<<"Yes"<<endl;
  }
  else{
    cout<<"No"<<endl;
  }
  return(0);
}
