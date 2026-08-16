#include <iostream>
#include <cstdio>

using namespace std;
int i,j,make[100],kati[100];
char name[100];

void change(){
  int tmp1,tmp2;
  char tmp3;
  tmp1 = kati[j+1];
  kati[j+1] = kati[j];
  kati[j] = tmp1;
  
  tmp2 = make[j+1];
  make[j+1] = make[j];
  make[j] = tmp2;
  
  tmp3 = name[j+1];
  name[j+1] = name[j];
  name[j] = tmp3;
}

int main(){
  int n,s;
  while(1){
    cin >> n;
    if( n == 0 )break;
    for( i = 0;i < 100 ; i++){
      kati[i] = 0;
      make[i] = 0;
    }
    
    for( i = 0 ; i < n ; i++ ){
	cin >> name[i];
      for( j = 0; j < n-1 ; j++ ){
	cin >> s;
	if(s == 0)kati[i]++;
	if(s == 1)make[i]++;
      }
    }

    
    
    for( i = n-1;i >0 ; i--){
      for( j = 0; j < i ; j++){
	if(make[j] > make[j+1] ){
	  change();
	}
      }
    }
    
    for( i = n-1;i >0 ; i--){
      for( j = 0; j < i ; j++){
	if(kati[j] < kati[j+1] ){
	  change();
	}
      }
    }

    for(i = 0;i < n ;i++)cout << name[i] << endl;
    
  }
  return 0;
}