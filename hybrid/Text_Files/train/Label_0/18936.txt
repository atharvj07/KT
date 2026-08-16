#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main(){
  int i,j,n,a[3],flag,r;
  int na[3];
  while(1){
    cin >> a[0] >> a[1] >> a[2];
    if(a[0] == 0 && a[1] == 0 && a[2] == 0) break;
    cin >> n;

    for(i=0;i<2;i++) na[i] = a[i] * a[i] + a[i+1] * a[i+1];
    na[2] = a[2]*a[2] + a[0] * a[0];

    for(i=0;i<n;i++){
      cin >> r;
      flag = 0;
      for(j=0;j<3;j++){
	if(r*r*4 > na[j]){
	  flag = 1;
	  break;
	}
      }

      if(flag == 1) cout << "OK" << endl;
      else cout << "NA" << endl;
    }


  }
  return 0;
}