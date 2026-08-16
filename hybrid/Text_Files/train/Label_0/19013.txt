#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;


enum Type{
	SMALL,
	BIG,
	EQUAL,
};

#define NUM 150
#define DIGIT 53

//辺を表す構造体{行先、容量、コスト、逆辺のインデックス}
struct Edge{
	Edge(int arg_to,int arg_capacity,int arg_num,int arg_rev_index,bool is_rev){
		to = arg_to;
		capacity = arg_capacity;
		num = arg_num;
		for(int i = 0; i < DIGIT; i++)cost[i] = 0;
		if(num != -1){
			if(is_rev == false){
				cost[num] = -1;
			}else{
				cost[num] = 1;
			}
		}
		rev_index = arg_rev_index;
	}

	int to,capacity,num,cost[DIGIT],rev_index;
};

int V; //頂点数
int H,W;
vector<Edge> G[NUM]; //グラフの隣接リスト表現
int dist[NUM][DIGIT]; //最短距離
int pre_node[NUM],pre_edge[NUM]; //直前の頂点と辺
char base_map[50][51];


//桁1～52を、'A'～'z'に対応させる。桁0はBIG_NUMの重み。桁が小さいほど重みが大きい
int getNUM(char ch){

	if(ch >= 'A' && ch <= 'Z'){
		return ch - 'A'+1;
	}else{
		return ch - 'a'+26+1;
	}
}

int getCHAR(int num){

	num--;

	if(num <= 25){
		return 'A'+num;
	}else{
		return 'a'+num-26;
	}
}


//fromからtoへ向かう容量capacity,コストcostの辺をグラフに追加する
void add_edge(int from,int to,int capacity,int arg_num){
	G[from].push_back(Edge(to,capacity,arg_num,G[to].size(),false));
	G[to].push_back(Edge(from,0,arg_num,G[from].size()-1,true));
}

//SMALL:Aの方が小さい BIG:Aの方が大きい EQUAL:同じ
Type compare_cost(int cost_A[DIGIT],int cost_B[DIGIT]){

	for(int i = 0; i < DIGIT; i++){
		if(cost_A[i] != cost_B[i]){
			if(cost_A[i] < cost_B[i]){
				return SMALL;
			}else{
				return BIG;
			}
		}
	}
	return EQUAL;
}

bool is_big_num(int array[DIGIT]){

	return array[0] == 1;
}

//sourceからsinkへの、流量flowの最小費用流を求める
//流せない場合は-1を返す
int min_cost_flow(int source,int sink,int flow){
	int ret = 0;

	int work[DIGIT];

	//int debug = 0;

	while(flow > 0){
		//ベルマンフォード方により、source-sink間最短経路を求める
		for(int i = 0; i < V; i++){
			dist[i][0] = 1; //BIG_NUM扱い
			for(int k = 1; k < DIGIT; k++)dist[i][k] = 0;
		}

		dist[source][0] = 0; //全桁0→コスト0扱い
		bool update = true;
		while(update){
			update = false;
			for(int node_id = 0; node_id < V; node_id++){
				if(is_big_num(dist[node_id]))continue; //辿り着けない
				for(int i = 0; i < G[node_id].size(); i++){
					Edge &e = G[node_id][i];

					for(int i = 0; i < DIGIT; i++)work[i] = dist[node_id][i]+e.cost[i]; //★配列形式のコスト★

					if(e.capacity > 0 && compare_cost(work,dist[e.to]) == SMALL){

						for(int i = 0; i < DIGIT; i++)dist[e.to][i] = work[i]; //node_idを経由した方が早い場合
						pre_node[e.to] = node_id;
						pre_edge[e.to] = i;
						update = true;
						//printf("%d-%dを経由したら早くなる\n",node_id,e.to);
						//printf("UPDATE!!\n");

					}
				}
			}
		}

		if(is_big_num(dist[sink])){
			//これ以上流せない
			return -1;
		}

		//printf("flow:%d\n",flow);
		//source-sink間最短路に沿って目いっぱい流す
		int tmp_flow = flow;
		for(int node_id = sink; node_id != source; node_id = pre_node[node_id]){
			//printf("node_id:%d\n",node_id);
			tmp_flow = min(tmp_flow,G[pre_node[node_id]][pre_edge[node_id]].capacity);
		}
		flow -= tmp_flow;
		//printf("flow:%d\n",flow);
		ret += 0; //戻り値不要
		for(int node_id = sink; node_id != source; node_id = pre_node[node_id]){
			Edge &e = G[pre_node[node_id]][pre_edge[node_id]];
			e.capacity -= tmp_flow;
			G[node_id][e.rev_index].capacity += tmp_flow;
		}
	}
	return ret;
}

int main(){

	int size;

	scanf("%d",&size);
	H = size;
	W = H;

	for(int row = 0; row < H; row++){
		scanf("%s",base_map[row]);
	}

	int source = 0,sink = 1,index = 2;
	int index_row[H],index_col[W];

	for(int row = 0; row < H; row++)index_row[row] = index++;
	for(int col = 0; col < W; col++)index_col[col] = index++;

	for(int i = 0; i < size; i++){
		add_edge(source,index_row[i],1,-1); //sourceから行ノードにcap1,cost0の辺を張る
	}

	for(int i = 0; i < size; i++){
		add_edge(index_col[i],sink,1,-1); //列ノードから行ノードにcap1,cost0の辺を張る
	}

	for(int row = 0; row < H; row++){
		for(int col = 0; col < W; col++){
			add_edge(index_row[row],index_col[col],1,getNUM(base_map[row][col])); //行と列を、文字のコストで結ぶ
		}
	}


	V = index;
	min_cost_flow(source,sink,size);

	vector<int> ANS;
	for(int row = 0; row < H; row++){
		for(int i = 0; i < G[index_row[row]].size(); i++){
			if(G[index_row[row]][i].capacity == 0){ //フローが流れた辺の値を取得する
				ANS.push_back(G[index_row[row]][i].num);
				break;
			}
		}
	}

	sort(ANS.begin(),ANS.end());

	for(int i = 0; i < size; i++)printf("%c",getCHAR(ANS[i]));
	printf("\n");

	return 0;
}

