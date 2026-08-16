#include<bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0;i<(n);i++)
#define pb push_back
#define eb emplace_back
#define all(v) (v).begin(),(v).end()
#define fi first
#define se second
typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;

template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

template<class A,class B>
ostream& operator<<(ostream& ost,const pair<A,B>&p){
	ost<<"{"<<p.first<<","<<p.second<<"}";
	return ost;
}

template<class T>
ostream& operator<<(ostream& ost,const vector<T>&v){
	ost<<"{";
	for(int i=0;i<v.size();i++){
		if(i)ost<<",";
		ost<<v[i];
	}
	ost<<"}";
	return ost;
}


using W=int;
using E=pair<W,int>;
struct Node{
	E e; 
	W put;
	Node *l,*r;
	Node(const E e=E()):e(e),put(0),l(nullptr),r(nullptr){}
	Node* push(){
		e.first+=put;
		if(l)l->put+=put;
		if(r)r->put+=put;
		put=0;
		return this;
	}
};
Node* merge(Node *a,Node *b){
	if(!a)return b;
	if(!b)return a;
	a->push();b->push();
	if(a->e>b->e)swap(a,b);
	a->r=merge(a->r,b);
	swap(a->l,a->r);
	return a;
}
Node pool[2222222];
int tail;

struct EHeap{
	Node* root;
	EHeap():root(nullptr){}
	void pop(){
		root->push();
		root=merge(root->l,root->r);
	}
	void push(E e){
		pool[tail]=Node(e);
		Node *p=&pool[tail++];
		root=merge(root,p);
	}
	void add(W a){
		if(root)root->put+=a;
	}
	E top(){
		return root->push()->e;
	}
	void meld(EHeap &eh){
		root=merge(root,eh.root);
	}
};


struct MinimumWeightArborescence{
	int n;
	vector<vector<E>>G;
	MinimumWeightArborescence(int n):n(n),G(n){}

	void addEdge(int a,int b,W c){
		G[a].emplace_back(c,b);
	}

	W calc(int r){
		tail=0;
		vector<int>par(n);iota(par.begin(),par.end(),0);
		function<int(int)>find=[&](int x){return x==par[x]?x:par[x]=find(par[x]);};
		
		vector<int>st(n);
		vector<EHeap>eh(n);
		
		for(int v=0;v<n;v++)for(auto &e:G[v])eh[e.second].push(E(e.first,v));
		
		st[r]=2;
		W ans=0;
		for(int i=0;i<n;i++){
			if(st[i])continue;
			int v=i;
			vector<E>es;
			
			while(st[v]!=2){
				st[v]=1;
				int u;W c;
				tie(c,u)=eh[v].top();eh[v].pop();
				u=find(u);
				if(u==v)continue;
				ans+=c;
				if(st[u]!=1){
					es.push_back(E(c,v));
					v=u;
					continue;
				}

				eh[v].add(-c);
				while(v!=u){
					int w;
					tie(c,w)=es.back();es.pop_back();
					eh[w].add(-c);
					eh[w].meld(eh[v]);	
					par[v]=u;
					v=w;
				}
			}
			for(auto &e:es)st[e.second]=2;
		}
		return ans;
	}
};


signed main(){
	int N,M;
	scanf("%d%d",&N,&M);
	MinimumWeightArborescence mwa(N);
	vint in(N);
	rep(i,M){
		int a,b;
		scanf("%d%d",&a,&b);
		mwa.addEdge(a,b,0);
		mwa.addEdge(b,a,1);
		in[b]++;
	}
	
	vpint lis;
	rep(i,N){
		if(in[i])continue;
		int tmp=mwa.calc(i);
		lis.eb(tmp,i);
	}
	sort(all(lis));
	vint ans;
	rep(i,lis.size())if(lis[i].fi==lis[0].fi)ans.pb(lis[i].se);
	printf("%d %d\n",(int)ans.size(),lis[0].fi);
	rep(i,ans.size()){
		if(i)printf(" ");
		printf("%d",ans[i]);
	}puts("");
	return 0;
}
