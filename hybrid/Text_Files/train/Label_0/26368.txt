#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
#define int long long
signed main(){
	vector<int> primes(50050,1);
	for(int i=2;i<230;i++){
		if(primes[i]==0) continue;
		for(int j=i+1;j<50050;j++){
			if(j%i==0) primes[j] = 0;
		}
	}
	int a;
	int prev = -1;
	while( scanf("%lld", &a) != EOF ){
		for(int i=0;i<50050;i++){
			if(i<a && primes[i]==1) prev = i;
			if(a<i && primes[i]==1 ){ cout << prev << " " << i << endl; break;}
		}
	}
	return 0;
}