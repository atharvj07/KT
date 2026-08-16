#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<bitset>
#include<algorithm>

using namespace std;

template<class T> inline void chmin(T &a,T b){
	a=min(a,b);
}
template<class T> inline void chmax(T &a,T &b){
	a=max(a,b);
}

string getBin(int n){
	string res="";
/*	for(int i=26;i>=0;i--){
		if((n>>i)&1) res+='1';
		else res+='0';
		if(i>0&&i%9==0) res+=' ';
	}*/
	for(int i=0;i<27;i++){
		if((n>>i)&1) res+='1';
		else res+='0';
		if(i==8||i==17) res+=' ';
	}
	return res;
}

int id=0;
bool cur_block[24][3][3][3];
bool cur[3][3][3];
bool tmp[3][3][3];

int encode_(){
	int c=0;
	int res=0;
	for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++){
		if(cur[i][j][k]) res|=(1<<c);
		c++;
	}
	return res;
}

void put(){
	int enc=0;
	int c=0;
	for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++){
		cur_block[id][i][j][k]=cur[i][j][k];
		if(cur[i][j][k]) enc|=(1<<c);
		c++;
	}
	id++;
//	cerr<<"id="<<id<<"\n";
//	cerr<<getBin(enc)<<"\n";
}

void cp(){
	for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++){
		cur[i][j][k]=tmp[i][j][k];
	}
}

void rot3(){
	for(int x=0;x<2;x++){
		for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++){
			tmp[2-j][2-i][2-k]=cur[i][j][k];
		}
		cp();
		put();
	}
}

void rot2(){
	for(int x=0;x<3;x++){
		for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++){
			tmp[j][k][i]=cur[i][j][k];
		}
		cp();
		rot3();
	}
}

void rot1(){
	for(int x=0;x<4;x++){
		for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++){
			tmp[2-j][i][k]=cur[i][j][k];
		}
		cp();
		rot2();
	}
}

int csum;
vector<int> cur_block_encode;
int goal;

void encode(int id){
	int c=0;
	int res=0;
	int mini=3,minj=3,mink=3;
	int maxi=-1,maxj=-1,maxk=-1;
	for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++){
		if(cur_block[id][i][j][k]){
			chmin(mini,i);
			chmin(minj,j);
			chmin(mink,k);
			chmax(maxi,i);
			chmax(maxj,j);
			chmax(maxk,k);
		}
	}
	memset(cur,false,sizeof(cur));
	for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++){
		cur[i][j][k]=(i+mini<3&&j+minj<3&&k+mink<3)?cur_block[id][i+mini][j+minj][k+mink]:false;
	}
	for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++){
		if(cur[i][j][k]) res|=(1<<c);
		c++;
	}
//	cur_block_encode.push_back(res);
	csum=maxi+maxj+maxk-mini-minj-mink+3;
	int I=3-(maxi-mini+1),J=3-(maxj-minj+1),K=3-(maxk-mink+1);
	for(int mi=0;mi<=I;mi++) for(int mj=0;mj<=J;mj++) for(int mk=0;mk<=K;mk++){
	//	int x=9*mk+3*mi+mj;
		int x=mk+3*mj+9*mi;
		if(((res<<x)&goal)!=(res<<x)) continue;
		cur_block_encode.push_back(res<<x);
	}
//	return res;
}

void encode(){
	cur_block_encode.clear();
	for(int i=0;i<24;i++){
//		int cur_encode=encode(i);
//		if((goal&cur_encode)==cur_encode) cur_block_encode.push_back(cur_encode);
		encode(i);
	}
	sort(cur_block_encode.begin(),cur_block_encode.end());
	cur_block_encode.erase(unique(cur_block_encode.begin(),cur_block_encode.end()),cur_block_encode.end());
}

struct Block{
	int weight;
	int sum;//W+H+D
	vector<int> nums;
};

bool operator<(const Block &b1,const Block &b2){
	if(b1.weight!=b2.weight) return b1.weight<b2.weight;
	return b1.sum<b2.sum;
}

int W,H,D;

int N;

void inputGoal(){
	scanf("%d%d%d",&W,&D,&H);
	if(W==0&&D==0&&H==0) exit(0);
	goal=0;
	int c=0;
	for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++){
		if(i<H&&j<W&&k<D) goal|=(1<<c);
		c++;
	}
//	cerr<<getBin(goal)<<"\n";
}

vector<Block> blocks;

void inputBlock(){
	memset(cur_block,false,sizeof(cur_block));
	memset(cur,false,sizeof(cur));
	memset(tmp,false,sizeof(tmp));
	int w,d,h;
	int weight=0;
	scanf("%d%d%d",&w,&d,&h);
	char ch[10];
	for(int i=0;i<h;i++) for(int j=0;j<d;j++){
		scanf("%s",ch);
		for(int k=0;k<w;k++){
			cur[h-1-i][k][j]=ch[k]=='*';
			if(ch[k]=='*') weight++;
		}
	}
	int a=encode_();
//	cerr<<"init="<<getBin(a)<<"\n";
	if(weight==1) return;
	id=0;
	rot1();
	encode();
	Block b;
	b.nums=cur_block_encode;
	b.sum=csum;
	b.weight=weight;
	blocks.push_back(b);
//	cerr<<"enc = "<<getBin(b.nums[0])<<"\n";
//	cerr<<weight<<"\n";
}

void inputBlocks(){
	blocks.clear();
	scanf("%d",&N);
	for(int i=0;i<N;i++) inputBlock();
}

bitset<(1<<27)> calculated,memo;

bool dfs(int id,int curVal){
	if(calculated[curVal]) return memo[curVal];
//	cerr<<"id="<<id<<"val="<<getBin(curVal)<<"\n";
	if(id==blocks.size()){
		calculated[curVal]=true;
		memo[curVal]=true;
		return true;
	}
	vector<int> &nums=blocks[id].nums;
	for(int i=0;i<nums.size();i++){
		if(curVal&nums[i]) continue;
		bool flg=dfs(id+1,curVal|nums[i]);
		if(flg){
			calculated[curVal]=true;
			memo[curVal]=true;
			return true;
		}
	}
	calculated[curVal]=true;
	memo[curVal]=false;
	return false;
}

bool solve(){
	sort(blocks.begin(),blocks.end());
	reverse(blocks.begin(),blocks.end());
	calculated.reset();
	memo.reset();
	/*for(int i=0;i<blocks.size();i++){
		cerr<<"i="<<i<<"\n";
		for(int j=0;j<blocks[i].nums.size();j++){
			int n=blocks[i].nums[j];
			cerr<<getBin(n)<<"\n";
		}
		cerr<<"\n";
	}*/
	bool res=dfs(0,0);
	return res;
}

int main(){
	while(true){
		inputGoal();
		inputBlocks();
		bool ans=solve();
		if(ans) printf("Yes\n");
		else printf("No\n");
	}
	return 0;
}