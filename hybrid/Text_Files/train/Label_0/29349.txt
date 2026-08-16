#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){

  int n,a,d,m,k;
  cin >> n;
  cin >> a >> d;
  cin >> m;
  vector<int> x(m),y(m),z(m);
  for(int i=0; i<m; i++){
    cin >> x[i] >> y[i] >> z[i];
    y[i]--;
    z[i]--;
  }
  cin >> k;
  k--;
  vector<int> com;
  for(int i=m-1; i>=0; i--){
    if(x[i]==0 && (y[i]<=k && k<=z[i])){
      k = y[i]+z[i]-k;
      //cout << "1 " << i << endl;;
    }else{
      if(y[i]<=k && k<=z[i]){
        com.push_back(x[i]);
      }
    }
  }
  //cout << k << endl;
  int num = a+d*k;
  //cout << com.size() << endl;
  for(int i=com.size()-1;i>=0;i--){
      if(com[i]==1){
          num++;
      }else if(com[i]==2){
          num/=2;
      }
  }
  
  cout << num << endl;

  return 0;
}