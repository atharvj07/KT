#include<cstdio>
using ll = long long;
using ull = unsigned long long;
const static int MOD = 1000000007;

int main(){
	int N;
	scanf("%d\n", &N);
	char top[N+1], bottom[N+1];
	scanf("%s", top);
	scanf("%s", bottom);
	ull answer;
	int begin = 1;
	if(top[0] == bottom[0]) answer = 3;
	else{
		answer = 6;
		begin++;
	}
	for (int i = begin; i < N; ++i){
		if(top[i] == bottom[i]){
			if(top[i-1] == bottom[i-1]){
				answer = answer*2 %MOD;
			}
		}else{
			answer *= top[i-1] == bottom[i-1] ? 2 : 3;
			answer %= MOD;
			i++;
		}
	}
	printf("%llu\n", answer);
	return 0;
}