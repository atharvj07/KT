#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define HUGE_NUM 99999999999999999
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;


#define SIZE 100005


struct Info{
	Info(){

		mid_index = 0;
		value = 0;
	}
	Info(int arg_mid_index,ll arg_value){
		mid_index = arg_mid_index;
		value = arg_value;
	}
	bool operator<(const struct Info &arg) const{

		return value > arg.value; //値の昇順(PQ)
	}

	int mid_index;
	ll value;
};

ll N;
ll A[SIZE],BIT[SIZE];
ll L_TOP[SIZE],MID[SIZE];
ll L[SIZE],R[SIZE],SAME_L_TOP[SIZE],count_table[SIZE];
bool is_L_TOP[SIZE],is_R_BOTTOM[SIZE];
vector<ll> V,R_BOTTOM;
map<ll,ll> MAP;

ll max_data[8*SIZE],add_data[8*SIZE];
ll seg_N = 1;

void add(ll loc,ll value){

	BIT[loc] += value;

	loc += loc & -loc;

	while(loc <= N){
		BIT[loc] += value;
		loc += loc & -loc;
	}
}

ll getSum(ll loc){

	ll sum = BIT[loc];

	loc -= loc & -loc;

	while(loc > 0){
		sum += BIT[loc];
		loc -= loc & -loc;
	}
	return sum;
}

ll calc(ll left,ll right){
	return getSum(right)-getSum(left-1);
}


//RAQ and RMQ
void init(ll first_N){
	while(seg_N < first_N)seg_N *= 2;
}


void add(int left,int right,ll value,int node_id,int node_left,int node_right){

	if(right < node_left || left > node_right){
		//範囲外ならreturn
		return;
	}
	else if(left <= node_left && right >= node_right){ //このノードのカバーしている区間が、更新区間の部分区間である場合

		add_data[node_id] += value; //一様に加える値を加算

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
	if(right < node_left || left > node_right)return -BIG_NUM;
	else if(left <= node_left && right >= node_right){
		return max_data[node_id]+add_data[node_id];

	}else{

		ll  left_max  = getMax(left,right,2*node_id+1,node_left,(node_left+node_right)/2);
		ll  right_max = getMax(left,right,2*node_id+2,(node_left+node_right)/2+1,node_right);
		return max(left_max,right_max)+add_data[node_id];
	}
}


int main(){

	scanf("%lld",&N);

	for(int i = 0; i < N; i++){

		scanf("%lld",&A[i]);
		V.push_back(A[i]);
	}

	sort(V.begin(),V.end());
	V.erase(unique(V.begin(),V.end()),V.end());

	for(int i = 0; i < V.size(); i++){

		MAP[V[i]] = i;
	}

	for(int i = 0; i <= V.size(); i++)BIT[i] = 0;

	ll swap_count = 0;

	for(ll i = 0; i < N; i++){
		swap_count += i-getSum(MAP[A[i]]+1);
		add(MAP[A[i]]+1,1);
	}

	if(swap_count == 0){

		for(int i = 1; i < N; i++){
			if(A[i-1] == A[i]){

				printf("0\n");
				return 0;
			}
		}

		printf("1\n");
		return 0;
	}

	ll maximum = -1;
	int index_L_TOP = 0;

	//左上候補点
	for(int i = 0; i < N; i++){

		if(MAP[A[i]] > maximum){

			maximum = MAP[A[i]];
			L_TOP[index_L_TOP++] = i;
			is_L_TOP[i] = true;

		}else{

			is_L_TOP[i] = false;
		}
	}

	ll minimum = BIG_NUM;

	stack<int> tmp_R;
	//右下候補点
	for(int i = N-1; i >= 0; i--){

		if(MAP[A[i]] < minimum){
			minimum = MAP[A[i]];
			tmp_R.push(i);
			is_R_BOTTOM[i] = true;

		}else{

			is_R_BOTTOM[i] = false;
		}
	}
	while(!tmp_R.empty()){

		R_BOTTOM.push_back(tmp_R.top());
		tmp_R.pop();
	}

	int index_MID = 0;
	int left,right,mid;

	for(int i = 0; i < N; i++){

		if(is_L_TOP[i] || is_R_BOTTOM[i])continue;

		MID[index_MID] = i;

		/*自分より左上にある点の範囲を求める*/

		//右端
		left = 0,right = index_L_TOP-1,mid = (left+right)/2;
		R[index_MID] = -1;

		while(left <= right){

			if(L_TOP[mid] < i){

				R[index_MID] = mid;
				left = mid+1;

			}else{

				right = mid-1;
			}
			mid = (left+right)/2;
		}

		//左端
		left = 0,right = index_L_TOP-1,mid = (left+right)/2;
		L[index_MID] = N;

		while(left <= right){

			if(A[L_TOP[mid]] > A[i]){

				L[index_MID] = mid;
				right = mid-1;

			}else{

				left = mid+1;
			}
			mid = (left+right)/2;
		}

		//自分と同じ数の、L_TOPがあるか調べる
		left = 0,right = index_L_TOP-1,mid = (left+right)/2;
		SAME_L_TOP[index_MID] = -1;

		while(left <= right){

			if(A[L_TOP[mid]] > A[i]){

				right = mid-1;

			}else if(A[L_TOP[mid]] == A[i]){

				SAME_L_TOP[index_MID] = mid;
				break;

			}else{

				left = mid+1;
			}
			mid = (left+right)/2;
		}

		index_MID++;
	}

	init(N);

	for(ll i = 0; i <= 2*seg_N-2; i++){
		max_data[i] = 0;
		add_data[i] = 0;
	}

	ll max_contain = 0;
	int tmp_index = 0;

	priority_queue<Info> Q;

	int seg_L = 0,seg_R = index_L_TOP-1;

	for(int i = 0; i <= V.size(); i++){

		count_table[i] = 0; //数字の個数
	}

	ll pre_bottom = -1;
	vector<Info> work;

	for(int i = 0; i < R_BOTTOM.size(); i++){

		int r_bottom = R_BOTTOM[i];

		//自分未満になったMIDを出す
		while(Q.empty() == false && Q.top().value < A[r_bottom]){

			if(L[Q.top().mid_index] <= R[Q.top().mid_index]){

				if(A[MID[Q.top().mid_index]] != pre_bottom){

					add(L[Q.top().mid_index],R[Q.top().mid_index],-2,0,0,seg_N-1);

				}else{ //前回の下線に位置していた点の場合

					add(L[Q.top().mid_index],R[Q.top().mid_index],-1,0,0,seg_N-1);
				}
			}
			Q.pop();
		}

		//自分と同じ数があったら、2を加算しているので1を引く(左上とは交換する必要あるが右下とは不要なため)
		while(Q.empty() == false && Q.top().value == A[r_bottom]){

			add(L[Q.top().mid_index],R[Q.top().mid_index],-1,0,0,seg_N-1);
			work.push_back(Q.top());
			Q.pop();
		}
		for(int k = 0; k < work.size(); k++){

			Q.push(work[k]);
		}
		work.clear();

		//自分以上になったMIDを入れる
		while(tmp_index < index_MID && MID[tmp_index] < r_bottom){

			count_table[MAP[A[MID[tmp_index]]]]++;

			if(A[MID[tmp_index]] > A[r_bottom]){


				if(L[tmp_index] <= R[tmp_index]){

					add(L[tmp_index],R[tmp_index],2,0,0,seg_N-1);
				}
				if(SAME_L_TOP[tmp_index] != -1){ //自分より左に自分と同じ数があれば足す

					add(SAME_L_TOP[tmp_index],SAME_L_TOP[tmp_index],1,0,0,seg_N-1);
				}
				Q.push(Info(tmp_index,A[MID[tmp_index]]));

			}else if(A[MID[tmp_index]] == A[r_bottom]){ //下線と同じ高さ

				if(L[tmp_index] <= R[tmp_index]){

					add(L[tmp_index],R[tmp_index],1,0,0,seg_N-1);
				}
				Q.push(Info(tmp_index,A[MID[tmp_index]]));
			}
			tmp_index++;
		}


		//自分以下になった左上の点を抜く
		while(seg_L < index_L_TOP && A[L_TOP[seg_L]] <= A[r_bottom])seg_L++;

		if(seg_L <= seg_R){

			ll tmp_contain = getMax(seg_L,seg_R,0,0,seg_N-1)+1;
			max_contain = max(max_contain,tmp_contain);
		}

		pre_bottom = A[r_bottom];
	}

	printf("%lld\n",swap_count-max_contain);

	return 0;
}

