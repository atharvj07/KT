#include <stdio.h>
#include <utility>
#include <queue>
#include <vector>
#include <bitset>
using namespace std;
typedef pair<int,int> pi;
#define F first
#define S second
#define MP make_pair
#define PB push_back
const int INF=1e9+10;
const int N=1e5+10;
const int M=2e5+10;
struct seg_tree{
    struct seg{
        seg* l;
        seg* r;
        int top;
        int flag;
        void pull(){
            top=0;
            if(l)top=max(top,l->top);
            if(r)top=max(top,r->top);
            return ;
        }
        void in(int val){
            if(top>val){
                top=val;
                flag=val;
            }
            return ;
        }
        seg(){
            top=flag=INF;
            l=r=nullptr;
        }
    };
    seg* root;
    int size;
    seg_tree(int n){
        root=new seg();
        size=n;
        init(root,0,size);
    }
    void add(seg* n,int k,int l,int r,int L,int R){
        if(L<=l&&r<=R)n->in(k);
        else if(!(r<L||R<l)){
            if(n->flag!=INF){
                n->l->in(n->flag);
                n->r->in(n->flag);
                n->flag=INF;
            }
            int mid=(l+r)>>1;
            add(n->l,k,l,mid,L,R);
            add(n->r,k,mid+1,r,L,R);
            n->pull();
        }
        return ;
    }
    int ask(seg* n,int l,int r,int pos){
        if(l==r)return n->top;
        if(n->flag!=INF){
            n->l->in(n->flag);
            n->r->in(n->flag);
            n->flag=INF;
        }
        int mid=(l+r)>>1;
        if(pos>mid)return ask(n->r,mid+1,r,pos);
        else return ask(n->l,l,mid,pos);
    }
private:
    void init(seg* n,int l,int r){
        if(l==r)return ;
        int mid=(l+r)>>1;
        n->l=new seg();
        init(n->l,l,mid);
        n->r=new seg();
        init(n->r,mid+1,r);
        return ;
    }
};
struct side{
    int a;
    int b;
    int w;
    inline void in(){
        scanf("%d%d%d",&a,&b,&w);
        return ;
    }
};
struct cmp{bool operator()(const pair<side,int> &a,const pair<side,int> &b){return a.F.w>b.F.w;}};
seg_tree* st[N];
int d[N],to[N],top[N],dep[N],p[N];
vector<pi> son[N];
void lca(int a,int b,int k){
    while(top[a]!=top[b]){
        if(dep[top[a]]>dep[top[b]]){
            st[a]->add(st[a]->root,k,0,st[a]->size,0,dep[a]-dep[top[a]]);
            a=p[top[a]];
        }
        else{
            st[b]->add(st[b]->root,k,0,st[b]->size,0,dep[b]-dep[top[b]]);
            b=p[top[b]];
        }
    }
    if(a!=b){
        if(dep[a]>dep[b])st[a]->add(st[a]->root,k,0,st[a]->size,dep[b]-dep[top[b]]+1,dep[a]-dep[top[a]]);
        else st[a]->add(st[a]->root,k,0,st[a]->size,dep[a]-dep[top[a]]+1,dep[b]-dep[top[b]]);
    }
    return ;
}
int build(int n){
    int val=1,temp,top=0;
    to[n]=n;
    for(int i=0;i<son[n].size();i++)if(p[n]!=son[n][i].F){
        p[son[n][i].F]=n;
        dep[son[n][i].F]=dep[n]+1;
        temp=build(son[n][i].F);
        if(top<temp){
            to[n]=i;
            top=temp;
        }
        val+=temp;
    }
    return val;
}
void init(int n,int from){
    bool f=true;
    top[n]=from;
    for(int i=0;i<son[n].size();i++)if(p[n]!=son[n][i].F){
        if(i==to[n]){
            init(son[n][i].F,from);
            st[n]=st[son[n][i].F];
        }
        else init(son[n][i].F,son[n][i].F);
        f=false;
    }
    if(f)st[n]=new seg_tree(dep[n]-dep[from]);
}
int find(int n){
    if(d[n]==n)return n;
    return d[n]=find(d[n]);
}
int main(){
    int n,m,l,r;
    long long int ans=0,out;
    bitset<M> used;
    side s[M];
    pair<side,int>temp;
    priority_queue<pair<side,int>,vector<pair<side,int>>,cmp>pq;
    scanf("%d%d",&n,&m);
    used.reset();
    for(int i=1;i<=n;i++)d[i]=i;
    for(int i=0;i<m;i++){
        s[i].in();
        pq.push(MP(s[i],i));
    }
    while(!pq.empty()){
        temp=pq.top();
        pq.pop();
        l=find(temp.F.a);
        r=find(temp.F.b);
        if(l!=r){
            used[temp.S]=true;
            ans+=temp.F.w;
            son[temp.F.a].PB(MP(temp.F.b,temp.F.w));
            son[temp.F.b].PB(MP(temp.F.a,temp.F.w));
            if(l>r)d[l]=r;
            else d[r]=l;
            n--;
            if(n<=1)break;
        }
    }
    if(n>1){
        for(int i=0;i<m;i++)printf("-1\n");
        return 0;
    }
    p[1]=dep[1]=0;
    build(1);
    init(1,1);
    for(int i=0;i<m;i++)
        if(!used[i])lca(s[i].a,s[i].b,s[i].w);
    for(int i=0;i<m;i++)if(!used[i])printf("%lld\n",ans);
    else {
        l=dep[s[i].a]>dep[s[i].b]?s[i].a:s[i].b;
        out=st[l]->ask(st[l]->root,0,st[l]->size,dep[l]-dep[top[l]]);
        if(out==INF)printf("-1\n");
        else printf("%lld\n",ans+out-s[i].w);
    }
}
