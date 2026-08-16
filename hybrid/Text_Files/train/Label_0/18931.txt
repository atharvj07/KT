#include<iostream>
#include<string>
#include<math.h>
using namespace std;
int main(){
    char a[8];
	long long h,l,n;
	cin>>n;
	for(int k=0;k<n;k++){
		for(int j=0;j<8;j++)
			cin>>a[j];
		for(int i=0;i<7;i++){
            for(int j=7;j>i;j--){
	            if(a[j]<a[j-1]){
	            int tmp=a[j];
	            a[j]=a[j-1];
	            a[j-1]=tmp;
	            }
            }
        }
		h=0,l=0;
		for(int j=0;j<8;j++){
			double t=j;
			l+=a[j]*pow(10,7-t);
			h+=a[7-j]*pow(10,7-t);
		}
		cout<<h-l<<endl;
	}
	return 0;
}