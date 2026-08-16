#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define HUGE_NUM 99999999999999999
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;


#define NUM 100005

struct Edge{
	Edge(int arg_from,int arg_to,ll arg_cost,int arg_edge_index){
		from = arg_from;
		to = arg_to;
		cost = arg_cost;
		edge_index = arg_edge_index;
	}
	bool operator<(const struct Edge &arg) const{
		return cost < arg.cost;
	}
	int from,to,edge_index;
	ll cost;
};

struct Edge2{
	Edge2(int arg_to,int arg_edge_index,ll arg_cost){
		to = arg_to;
		edge_index = arg_edge_index;
		cost = arg_cost;
	}

	int to,edge_index;
	ll cost;
};

struct Info{
	Info(){
		edge_index = 0;
		cost = 0;
	}
	Info(int arg_edge_index,ll arg_cost){
		edge_index = arg_edge_index;
		cost = arg_cost;
	}
	bool operator<(const struct Info &arg) const{
		if(cost != arg.cost){
			return cost < arg.cost;
		}else{
			return edge_index < arg.edge_index;
		}
	}

	int edge_index;
	ll cost;
};

int V,E;
int boss[NUM],height[NUM];
ll MST_COST,ANS[2*NUM];
bool is_mst_edge[2*NUM];
vector<Edge2> MST[NUM],OTHER[NUM];
set<Info> SET[NUM];

int get_boss(int id){
	if(boss[id] == id)return id;
	else{
		return boss[id] = get_boss(boss[id]);
	}
}

int is_same_group(int x,int y){
	return get_boss(x) == get_boss(y);
}

void unite(int x,int y){
	int boss_x = get_boss(x);
	int boss_y = get_boss(y);

	if(boss_x == boss_y)return;

	if(height[x] > height[y]){

		boss[boss_y] = boss_x;

	}else if(height[x] < height[y]){

		boss[boss_x] = boss_y;

	}else{ //height[x] == height[y]

		boss[boss_y] = boss_x;
		height[x]++;
	}
}

void init(){

	for(int i = 0; i < V; i++){
		boss[i] = i;
		height[i] = 0;
	}
}

int count_group_num(){

	int ret = 0;

	for(int i = 0; i < V; i++){
		if(get_boss(i) == i){
			ret++;
		}
	}

	return ret;
}

void print_ans(){

	for(int i = 0; i < E; i++){
		printf("%lld\n",ANS[i]);
	}
}

void recursive(int index,int parent){

	for(int i = 0; i < OTHER[index].size(); i++){
		SET[index].emplace(Info(OTHER[index][i].edge_index,OTHER[index][i].cost));
	}

	for(int i = 0; i < MST[index].size(); i++){

		if(MST[index][i].to == parent)continue;
		recursive(MST[index][i].to,index);

		auto &self = SET[index];
		auto &desc = SET[MST[index][i].to];

		if(!desc.empty()){
			ANS[MST[index][i].edge_index] = MST_COST-MST[index][i].cost+desc.begin()->cost;
		}

		if(self.size() < desc.size()){
			swap(self,desc);
		}

		for(auto &at : desc){

			if(self.count(at)){

				self.erase(at);

			}else{

				self.emplace(at);
			}
		}
		desc.clear();
	}
}

int main(){

	scanf("%d %d",&V,&E);

	for(int i = 0; i < E; i++){
		ANS[i] = -1;
	}

	int from,to;
	ll cost;

	vector<Edge> G;

	for(int loop = 0; loop < E; loop++){

		scanf("%d %d %lld",&from,&to,&cost);
		from--;
		to--;
		G.push_back(Edge(from,to,cost,loop));
	}

	sort(G.begin(),G.end());

	init();

	MST_COST = 0;
	for(int i = 0; i < E; i++){
		is_mst_edge[i] = false;
	}

	for(int i = 0; i < E; i++){
		if(!is_same_group(G[i].from,G[i].to)){

			unite(G[i].from,G[i].to);
			MST_COST += G[i].cost;
			is_mst_edge[G[i].edge_index] = true;
		}
	}

	if(count_group_num() > 1){

		print_ans();
		return 0;
	}

	for(int i = 0; i < E; i++){
		if(is_mst_edge[G[i].edge_index]){

			MST[G[i].from].push_back(Edge2(G[i].to,G[i].edge_index,G[i].cost));
			MST[G[i].to].push_back(Edge2(G[i].from,G[i].edge_index,G[i].cost));

		}else{

			OTHER[G[i].from].push_back(Edge2(G[i].to,G[i].edge_index,G[i].cost));
			OTHER[G[i].to].push_back(Edge2(G[i].from,G[i].edge_index,G[i].cost));
			ANS[G[i].edge_index] = MST_COST;
		}
	}

	recursive(0,-1);

	print_ans();

	return 0;
}

