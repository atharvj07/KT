#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define HUGE_NUM 99999999999999999
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;



#define SIZE 100005


int N;
ll max_data[SIZE*8],add_data[SIZE*8];

void init(ll first_N){
	while(N < first_N)N *= 2;
}

void add(int left,int right,ll value,int node_id,int node_left,int node_right){

	if(right < node_left || left > node_right){
		return;
	}
	else if(left <= node_left && right >= node_right){

		add_data[node_id] += value;

		while(node_id != 0){

			node_id = (node_id-1)/2;
			max_data[node_id] = max(max_data[2*node_id+1]+add_data[2*node_id+1],max_data[2*node_id+2]+add_data[2*node_id+2]);
		}
	}else{

		add(left,right,value,2*node_id+1,node_left,(node_left+node_right)/2);
		add(left,right,value,2*node_id+2,(node_left+node_right)/2+1,node_right);
	}
}


ll getMax(int left,int right,int node_id,int node_left,int node_right){
	if(right < node_left || left > node_right)return -HUGE_NUM;
	else if(left <= node_left && right >= node_right){
		return max_data[node_id]+add_data[node_id];

	}else{

		ll  left_max  = getMax(left,right,2*node_id+1,node_left,(node_left+node_right)/2);
		ll  right_max = getMax(left,right,2*node_id+2,(node_left+node_right)/2+1,node_right);
		return max(left_max,right_max)+add_data[node_id];
	}
}

int main(){

	int first_N,Q;
	scanf("%d %d",&first_N,&Q);

	N = 1;
	init(first_N);

	for(ll i = 0; i <= 2*N-2; i++){
		max_data[i] = 0;
		add_data[i] = 0;
	}

	int from,to;
	ll num;

	int tmp = 0;

	for(int loop = 0; loop < Q; loop++){

		scanf("%d %d %lld",&from,&to,&num);
		from--;
		to--;

		while(tmp < to){
			tmp++;
			add(tmp,N-1,1,0,0,N-1);
		}

		add(from,to,num,0,0,N-1);
		printf("%lld\n",getMax(0,N-1,0,0,N-1));
	}

	return 0;
}

