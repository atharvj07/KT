#include<iostream>
using namespace std;
int main()
{
  int n,i,t,mh=0,res=0;
  cin >> n;
  for(i=0;i<n;i++){
    cin >> t;
    if(t>=mh){
      res++;
      mh=t;
    }
  }
  cout << res << endl;
  return 0;
}