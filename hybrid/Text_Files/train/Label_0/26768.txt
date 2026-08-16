#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main(){
	double a,b;
	for(;;){
		cin >>a>>b;
		if(!a && !b){break;}
		printf("%.6lf\n",a*a+2*a*sqrt((a/2)*(a/2)+b*b));
	}
}