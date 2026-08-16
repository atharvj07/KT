#include<iostream>
using namespace std;

int main(){
  int l,m,n;

  while(true){
    cin >> l;
    if(!l)break;

    int f = 1;
    for(int i=0;i<12;i++){
      cin >> m >> n;
      l -= m-n;
      if(l<=0 && f){
	cout << i+1 << endl;
	f = 0;
      }
    }
    if(l>0)cout << "NA" << endl;
  }
  return 0;
}