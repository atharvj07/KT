#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
double x[10010],y[10010];
double ans;
int pd;
int n;
int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>x[i]>>y[i];
		x[i+n]=x[i],y[i+n]=y[i];
	}
	for(int j=1;j<=n-1;j++){
		double xx=x[j],yy=y[j];
		for(int i=1;i<=2*n;i++){
			x[i]-=xx,y[i]-=yy;
		}
		for(int i=3+j-1;i<=n+j-1;i++){
			if(x[i-1]*y[i]-x[i]*y[i-1]<0) pd=1;
		}
		for(int i=1;i<=2*n;i++){
			x[i]-=xx,y[i]-=yy;
		}
	}
	cout<<(pd^1)<<endl; 
	return 0;
}
