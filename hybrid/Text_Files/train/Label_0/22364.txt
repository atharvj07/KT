#include <cstdio>
#include <algorithm>

int main(){
	int N,i;
	scanf("%d",&N);
	long long A[100000]={0},large=0;
	for(i=0;i<N;i++){
		scanf("%lld",&A[i]);
	}
	std::sort(A,A+N);

	int color_num=N;


	large=A[0];

	for(i=1;i<N;i++){
		if(large*2<A[i]){
			color_num=N-i;
		}
		large+=A[i];
	}
	printf("%d",color_num);
}