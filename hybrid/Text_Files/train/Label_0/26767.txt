#include "bits/stdc++.h"
using namespace std;
using namespace std;

int main(){
double a,b;
while(1){
	cin>>a>>b;
	if(a==0&&b==0)break;
	printf("%.7f\n",a*a+sqrt((a/2.0)*(a/2.0)+b*b)*a/2.0*4.0);
}
}