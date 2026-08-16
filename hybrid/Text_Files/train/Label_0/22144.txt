#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <cfloat>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <iostream>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;

struct Info{
	Info(ll arg_value){
		value = arg_value;
	}
	bool operator<(const struct Info &arg) const{
		return value < arg.value;
	};
	ll value;
};

int main(){

	int N;
	ll P,Q,tmp;

	scanf("%d %lld %lld",&N,&P,&Q);

	priority_queue<Info> PQ;

	for(int i = 1; i <= N; i++){
		scanf("%lld",&tmp);
		PQ.push(Info(tmp+P*(i-1)));
	}

	ll sum = 0;
	ll num_self = N;
	ll ans = P*(num_self*Q + num_self*(num_self-1));

	while(!PQ.empty()){
		num_self--;
		sum += PQ.top().value;
		ans = max(ans,sum+P*(num_self*Q+num_self*(num_self-1)));
		PQ.pop();
	}

	for(ll i = 1; i <= N-1; i++)ans -= P*i;

	printf("%lld\n",ans);

	return 0;
}