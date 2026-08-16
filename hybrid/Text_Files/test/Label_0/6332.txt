#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <iostream>
#include <complex>
#include <string>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

#include <functional>
#include <cassert>

typedef long long ll;
using namespace std;

#ifndef LOCAL
#define debug(x) ;
#else
#define debug(x) cerr << __LINE__ << " : " << #x << " = " << (x) << endl;

template <typename T1, typename T2>
ostream &operator<<(ostream &out, const pair<T1, T2> &p) {
  out << "{" << p.first << ", " << p.second << "}";
  return out;
}

template <typename T>
ostream &operator<<(ostream &out, const vector<T> &v) {
  out << '{';
  for (const T &item : v) out << item << ", ";
  out << "\b\b}";
  return out;
}
#endif

#define mod 1000000007 //1e9+7(prime number)
#define INF 1000000000 //1e9
#define LLINF 2000000000000000000LL //2e18
#define SIZE 200010

/* Aho Corasick */

struct ACNode{
  int val;
  ACNode *next[26], *failure;
  int id;

  ACNode():val(0) { memset(next, 0, sizeof(next)); }

  void insert(char *s, int _id){
    id = _id;
    if(!*s){ val++; return; }
    int al = *s - 'a';
    if(next[al] == NULL) next[al] = new ACNode;
    next[al]->insert(s+1, _id+1);
  }

  ACNode *nextNode(char c){
    int al = c - 'a';
    if (next[al]) return next[al];
    return failure == this ? this : failure->nextNode(c);
  }
};

struct AhoCorasick{
  ACNode *node;

  AhoCorasick(){node = new ACNode;}

  void insert(char *s) {
    node->insert(s, 0);
  }

  void build() {
    queue<ACNode*> que;
    que.push(node);
    node->failure = node;

    while(que.size()){
      ACNode *p = que.front();
      que.pop();

      for(int i=0;i<26;i++){
        if(p->next[i]){
          ACNode *failure = p->failure;
          while(!failure->next[i] && failure != node)
            failure = failure->failure;

          if (failure->next[i] && failure != p){
            p->next[i]->failure = failure->next[i];
            p->next[i]->val += failure->next[i]->val;
          }else{
            p->next[i]->failure = node;
          }
          que.push(p->next[i]);
        }
      }
    }
  }
};

vector<int> apply(vector<int> &a, vector<int> &b) {
  vector<int> res;

  assert(a.size() == b.size());

  for(int i=0; i<a.size(); i++) {
    res.push_back(b[a[i]]);
  }

  return res;
}

vector<int> apply2(vector<int> &a, vector<int> &b) {
  vector<int> res(a.size(), 0);
  assert(a.size() == b.size());

  for(int i=0; i<a.size(); i++) {
    res[b[i]] += a[i];
  }

  return res;
}

/* SegmentTree(Sum) */
//0-index

struct SegTree{
  int segn2;
  vector<vector<int> > data;
  vector<vector<int> > rep;
  vector<int> base;

  vector<int> merge(vector<int> &a, vector<int> &b) {
    vector<int> res = a;

    for(int i=0; i<a.size(); i++)
      res[i] += b[i];

    return res;
  }

  SegTree(int n, int m){
    for(segn2=1; segn2<n; segn2*=2);

    vector<int> v(m);

    data.assign(segn2*2, v);

    v[0] = 1;

    for(int i=segn2-1; i<segn2-1+n; i++) {
      data[i] = v;
    }

    for(int i=segn2-2; i>=0; i--) {
      data[i] = merge(data[i*2+1], data[i*2+2]);
    }

    base.assign(m, 0);
    iota(base.begin(), base.end(), 0);
    rep.assign(segn2*2, base);
  }

  //get sum of [a, b)
  vector<int> query(int a, int b, int l = 0, int r = -1, int k = 0){
    if(r == -1) r = segn2;

    if(r <= a || b <= l) return vector<int>(data[k].size(), 0);
    if(a <= l && r <= b) return data[k];

    auto res1 = query(a, b, l, (l+r)/2, k*2+1);
    auto res2 =  query(a, b, (l+r)/2, r, k*2+2);
    auto res12 = merge( res1, res2 );

    return apply2(res12, rep[k]);
  }

  //add x to [a, b)
  void add(int a, int b, vector<int> &x, vector<int> &u, int l = 0, int r = -1, int k = 0){
    if(r == -1) r = segn2;

    rep[k] = apply(rep[k], u);

    vector<int> res1, res2;

    if(a <= l && r <= b) {
      rep[k] = apply(rep[k], x);
      data[k] = apply2(data[k], u);
      data[k] = apply2(data[k], x);
    } else if(a < r && l < b) {
      add(a, b, x, rep[k], l, (l+r)/2, k*2+1);
      add(a, b, x, rep[k], (l+r)/2, r, k*2+2);
      rep[k] = base;
      auto v = merge(data[k*2+1], data[k*2+2]);
      data[k] = v;
    } else {
      data[k] = apply2(data[k], u);
    }
  }
};

int main(){
  char S[21];
  int N, Q, M;

  ACNode *start[21];

  scanf("%s%d%d", S, &N, &Q);
  M = strlen(S);

  AhoCorasick aho;

  aho.insert(S);
  aho.build();

  start[0] = aho.node;

  SegTree seg(N, M+1);

  for(int i=0; i<M; i++) {
    start[i+1] = start[i]->nextNode(S[i]);
  }


  for(int i=0; i<Q; i++) {
    int q, l, r;
    char c[11];

    scanf("%d%d%d", &q, &l, &r);
    l--;

    if(q == 1) {
      scanf("%s", c);

      vector<int> vec;
      for(int j=0; j<=M; j++) {
        ACNode *p = start[j];

        for(int k=0; c[k]; k++) {
          p = p->nextNode(c[k]);
        }
        vec.push_back(p->id);
      }

      seg.add(l, r, vec, seg.base);
    } else {
      vector<int> res = seg.query(l, r);
      printf("%d\n", res[M]);
    }
  }


  return 0;
}

