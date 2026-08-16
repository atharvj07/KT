#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define HUGE_NUM 99999999999999999
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;


#define SIZE 45

enum Type{
	UNDEFINED,
	TRUE,
	FALSE,
};

struct Info{
	Info(int arg_main_value,int arg_sub_value){
		main_value = arg_main_value;
		sub_value = arg_sub_value;
	}
	bool operator<(const struct Info &arg) const{

		if(main_value != arg.main_value){

			return main_value < arg.main_value;
		}else{

			return sub_value < arg.sub_value;
		}
	}

	int main_value,sub_value;
};

int N,M;
int table[1005][SIZE];
vector<int> G[SIZE];
vector<Info> info;
int ans;
Type type[SIZE];

void recursive(int node_id,int count){

	if(count+(M-node_id+1) <= ans)return;

	if(node_id == M){

		ans = max(ans,count);

		return;
	}

	if(type[node_id] != UNDEFINED){ //決定済

		recursive(node_id+1,count);
		return;
	}

	Type pre[SIZE];
	for(int i = 0; i < M; i++){
		pre[i] = type[i];
	}

	type[node_id] = FALSE;
	recursive(node_id+1,count);

	for(int i = 0; i < M; i++){

		type[i] = pre[i];
	}

	type[node_id] = TRUE;
	for(int i = 0; i < G[node_id].size(); i++){

		type[G[node_id][i]] = FALSE;
	}
	recursive(node_id+1,count+1);
}

void func(){

	info.clear();

	for(int i = 0; i < SIZE; i++){
		G[i].clear();
	}

	for(int i = 0; i < N; i++){
		for(int k = 0; k < M; k++){
			scanf("%d",&table[i][k]);
		}
	}

	//同時に昇順にできないペアを探す
	for(int i = 0; i < M-1; i++){
		for(int k = i+1; k < M; k++){

			info.clear();

			for(int a = 0; a < N; a++){

				info.push_back(Info(table[a][i],table[a][k]));
			}

			sort(info.begin(),info.end());

			bool FLG = true;

			for(int a = 0; a < N-1; a++){
				for(int b = a+1; b < N; b++){
					if(info[a].main_value < info[b].main_value && info[a].sub_value > info[b].sub_value){
						FLG = false;
						break;
					}
				}
				if(!FLG)break;
			}

			if(!FLG){

				G[i].push_back(k);
				G[k].push_back(i);
			}
		}
	}

	ans = 1;
	int first_count = 0;

	for(int i = 0; i < M; i++){

		if(G[i].size() > 0){
			type[i] = UNDEFINED;
		}else{
			type[i] = TRUE; //無条件採用
			first_count++;
		}
	}

	recursive(0,first_count);

	printf("%d\n",ans);
}

int main(){

	while(true){
		scanf("%d %d",&N,&M);
		if(N == 0 && M == 0)break;

		func();
	}

	return 0;
}

