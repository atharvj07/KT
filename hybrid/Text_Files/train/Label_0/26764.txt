#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main(void){
	while(1){
		int x,h;
		double th;

		cin >> x >> h;
		if( x==0 && h==0 ) break;

		th=sqrt(double(x*x/4.0+h*h));
		printf("%.8f\n",x*x+2*x*th);
	}
	return 0;
}