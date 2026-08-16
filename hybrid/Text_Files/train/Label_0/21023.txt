#include <bits/stdc++.h>
using namespace std;
int n,s1,s2,s3,a[303];
double f[303][303][303];
#define AC ios::sync_with_stdio(0),cin.tie(0);
int main(){
	AC
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
		if(a[i]==1)s1++;
		if(a[i]==2)s2++;
		if(a[i]==3)s3++;
	}
	f[0][0][0]=0;
	for(int i=0;i<=n;i++){
		for(int j=0;j<=n;j++){
			for(int k=0;k<=n;k++){
				if(i)f[i][j][k]+=(f[i-1][j+1][k])*i/(i+j+k);
				if(j)f[i][j][k]+=(f[i][j-1][k+1])*j/(i+j+k);
				if(k)f[i][j][k]+=(f[i][j][k-1])*k/(i+j+k);
				if(i||j||k)f[i][j][k]+=(double)n/(i+j+k);
			}
		}
	}
	cout<<fixed<<setprecision(14)<<f[s3][s2][s1]<<endl;
	return 0;
}
