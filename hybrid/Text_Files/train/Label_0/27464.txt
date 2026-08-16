#include <bits/stdc++.h>
#include <math.h>

using namespace std;

long long inf=1000000007;

int main(){
	long long und;
	cin>>und;

	for(long long i=1;i<=3500;i++){
		for(long long j=1;j<=3500;j++){
			if((4*i*j-und*j-und*i)>0 && (und*i*j)%(4*i*j-und*j-und*i)==0){
				cout<<i<<" "<<j<<" "<<(und*i*j)/(4*i*j-und*j-und*i)<<endl;
				return 0;
			}
		}
	}

	return 0;
}
