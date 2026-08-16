#include <iostream>
using namespace std;

bool so[10000001] = {0};

int main() {

  for(int i=2;i*i<=10000000;i++) {
    if(so[i] == 0) {
      int k = i;
      for(int j=2;j<=10000000;j++) {
	if(k+i > 10000000)break;
	so[k+i] = 1;
	k += i;
	//	cout << i*j << endl;
      }
    }
  }


  while(1) {

    int n;
    cin >> n;

    if(n ==0) break;

    for(int i=n;i>=13;i--) {
      if(so[i]+so[i-2]+so[i-6]+so[i-8] == 0) {
	cout <<i<<endl;
	break;
      }
      }

  }



  return 0;

}