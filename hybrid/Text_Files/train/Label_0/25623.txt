#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
int n,L;
#define Maxn 3005
#define pi acos(-1)
double T[Maxn];
double x,y;
inline void add(double rad,int cnt){
	x+=cos(rad)*cnt;
    y+=sin(rad)*cnt;
}
int main(){
	scanf("%d%d",&n,&L);
	for(register int i=0;i<n;++i){
		scanf("%lf",&T[i]);
		T[i]=T[i]/L*2*pi;
	}
    for(register int i=0;i<n;++i)
        for(register int j=i+1;j<n;++j){
        	double m1=(T[i]+T[j])/2;
		    double m2=m1+pi;
		    add(m1,i+n-j-1);
			add(m2,j-i-1);
		}
	double all=1.0*n*(n-1)*(n-2)/6;
	x/=all;y/=all;
	printf("%.11lf\n %.11lf\n",x,y);
	return 0;
}