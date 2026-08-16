#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define HUGE_NUM 1000000000000000000
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;


#define SIZE 100005

struct Info{
	Info(int arg_node,int arg_dist){
		node = arg_node;
		dist = arg_dist;
	}
	bool operator<(const struct Info &arg) const{

		return dist > arg.dist;
	}
	int node,dist;
};

int N;
int max_dist[SIZE];
int number;
vector<int> G[SIZE];
vector<Info> children[SIZE];

void dfs(int node_id,int pre){

	int tmp_max = 0;

	for(int i = 0; i < G[node_id].size(); i++){

		int child = G[node_id][i];
		if(child == pre)continue;

		dfs(child,node_id);

		children[node_id].push_back(Info(child,max_dist[child]+1));
		tmp_max = max(tmp_max,max_dist[child]+1);
	}
	max_dist[node_id] = tmp_max;
}

void dfs2(int node_id,int pre){

	for(int i = 0; i < G[node_id].size(); i++){

		int child = G[node_id][i];
		if(child == pre){

			if(node_id == children[pre][0].node){ //自分が親の最大方向

				if(children[pre].size() == 1){ //親の子が自分しかいない

					children[node_id].push_back(Info(pre,1));
				}else{

					children[node_id].push_back(Info(pre,children[pre][1].dist+1));
				}

			}else{

				children[node_id].push_back(Info(pre,children[pre][0].dist+1));
			}
			break;
		}
	}

	int value;

	if(children[node_id].size() > 2){

		sort(children[node_id].begin(),children[node_id].end());

		if(children[node_id][0].dist == children[node_id][2].dist){

			value = children[node_id][0].dist + children[node_id][2].dist;
		}else{

			value = children[node_id][0].dist+children[node_id][2].dist+1;
		}

		//printf("node_id:%d\n",node_id);
		/*for(int i = 0; i < 3; i++){

			printf("child[%d]:%d dist:%d\n",i,children[node_id][i].node,children[node_id][i].dist);
		}*/

		number = max(number,value);
	}

	//親を先に処理
	for(int i = 0; i < G[node_id].size(); i++){

		int child = G[node_id][i];
		if(child == pre)continue;

		dfs2(child,node_id);
	}
}

int main(){

	scanf("%d",&N);

	int from,to;
	for(int i = 0; i < N-1; i++){

		scanf("%d %d",&from,&to);
		from--;
		to--;
		G[from].push_back(to);
		G[to].push_back(from);
	}

	if(N <= 2){

		for(int i = 0; i < N; i++){

			printf("1");
		}
		printf("\n");
		return 0;
	}

	for(int i = 0; i < N; i++){

		max_dist[i] = 0;
	}

	dfs(0,-1);

	number = -1;
	dfs2(0,-1);

	if(number <= 2){

		for(int i = 0; i < N; i++){

			printf("1");
		}
		printf("\n");
		return 0;
	}

	printf("11");
	for(int i = 3; i <= number-1; i++){

		printf("0");
	}
	for(int i = number; i <= N; i++){

		printf("1");
	}
	printf("\n");

	return 0;
}

