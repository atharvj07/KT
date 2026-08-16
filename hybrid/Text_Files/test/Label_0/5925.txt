#include<iostream>
#include<complex>
#include<cmath>
#include<vector>
#include<iomanip>
#include<set>
#include<functional>
#include<algorithm>
#include<cstdlib>
#include<cassert>

using namespace std;

typedef double elem;
typedef complex<elem> point, vec;
typedef pair<point,point> pp;
const elem eps = 1e-8;
const elem inf = 1e40;
const elem pi = 2*acos(0.0);

#define foreach(it,o) for(__typeof((o).begin()) it = (o).begin(); (it) != (o).end(); it++)

bool eq(elem a, elem b){
  return abs(b-a)<eps;
}
bool lt(elem a, elem b){
  return !eq(a,b) && a<b;
}
bool leq(elem a, elem b){
  return eq(a,b) || a<b;
}

elem varg(const vec &a, const vec &b){
  elem ret = arg(a)-arg(b);
  if(ret<0)ret += 2*pi;
  if(ret>2*pi)ret -= 2*pi;
  if(eq(ret,2*pi))ret= 0;
  return ret;
}

struct circle{
  point c;
  elem r;
  circle():c(0,0),r(0){}
  circle(const point &c, elem r):c(c),r(r){} 
};

enum cir_rel{cir_1c=0x01,cir_1ic=0x02,cir_0c=0x04,cir_cont=0x08,cir_2c=0x10,cir_same=0x20};

int circlesRel(const circle &c1, const circle &c2){
  elem d = abs(c1.c- c2.c);
  elem r1=c1.r, r2=c2.r;
  if(lt(r1,r2))swap(r1,r2);
  if(eq(d,r1+r2))return cir_1c;
  if(eq(d,r1-r2))return cir_1ic;
  if(lt(r1+r2,d))return cir_0c;
  if(lt(d,r1-r2))return cir_cont;
  if(lt(d,r1+r2))return cir_2c;
  if(eq(abs(c1.c-c2.c),0)&&eq(c1.r,c2.r))return cir_same;
}

bool inCircle(const circle &a, const circle &b){
  return circlesRel(a,b) & (cir_1ic|cir_cont|cir_same);
}

void removeIncircles(vector<circle> &vc){
  for(int i = 0; i < (int)vc.size(); ++i){
    for(int j = i+1; j < (int)vc.size(); ++j){
      if( !lt(vc[i].r, abs(vc[i].c-vc[j].c) + vc[j].r) ){
        vc.erase( vc.begin() + j );
        j = i;
      }
    }
  }
}

vec uvec(const vec &a){ return a / abs(a); }

int intersectionCC(const circle &c1, const circle &c2, pp &p){
  if( !(circlesRel(c1,c2) & (cir_1ic|cir_1c|cir_2c)))return 0;
  elem d = abs(c1.c-c2.c);
  vec ab = c2.c- c1.c;
  elem k = (c1.r*c1.r-c2.r*c2.r+d*d) / (2*d*d);
  point t = k*ab+c1.c;
  elem x = sqrt(c1.r*c1.r-(d*d*k*k));
  
  if( eq(x,0) ){
    p.first = t; return 1;
  }else{
    p.first = x * uvec(ab*point(0,1))+t;
    p.second = x * uvec(ab*point(0,-1))+t;
    return 2;
  }
}

bool checkAll(const circle &c, const vector<circle> &vc){
  for(int i = 0; i < (int)vc.size(); ++i){
    if( lt(c.r, abs(vc[i].c-c.c)+vc[i].r ) ) return false;
  }
  return true;
}

int getEncirclingCircle(elem r, const circle &c1, const circle &c2, const vector<circle> &vc,
                        pair<circle,circle> &ret){
  circle x(c1.c, r-c1.r);
  circle y(c2.c, r-c2.r);

  pp p;
  int cc_ret = intersectionCC(x,y,p);
  if( cc_ret == 1 ){
    ret.first = circle(p.first,r);
    if( !checkAll(ret.first, vc) ) cc_ret--;
  }else if( cc_ret == 2 ){
    ret.first = circle(p.first,r);
    ret.second = circle(p.second,r);
    if( !checkAll(ret.first, vc) ){ cc_ret--; ret.first = ret.second;
    }else if( !checkAll(ret.second, vc) ) cc_ret--;
    if( !checkAll(ret.first, vc) ) cc_ret--;
  }
  return cc_ret;
}

struct bc{
  int corr;
  point center;
  point corr_c;

  bc(int corr, point center, point corr_c):corr(corr),center(center),corr_c(corr_c){}
};

struct cmp{
  point center;
  cmp(point c):center(c){}
  bool operator()(const bc &a, const bc &b)const{
    assert(abs(a.corr_c-center)>0);
    assert(abs(b.corr_c-center)>0);

    elem tmp_a = arg(a.corr_c-center);
    elem tmp_b = arg(b.corr_c-center);
    if(!eq(tmp_a,tmp_b))return tmp_a<tmp_b;
    return false;
  }
};

int main()
{
  int n;
  elem R;

  while( cin >> n >> R ){

    if( n == 0 && eq(R,0) ) break;
    
    vector<circle> vc;
    elem res = 0;

    for(int i = 0; i < n; ++i){
      elem x,y,r;
      cin >> x >> y >> r;
      vc.push_back( circle(point(x,y),r) );
    }

    removeIncircles( vc );
    n = vc.size();
    
    if( n == 1 ){
      if( !lt(R,vc.front().r) ){
        res = 2*pi * (2*R - vc.front().r);
      }
    }else if( n >= 2 ){
      vector<bc> blueCircles;

      for(int i = 0; i < n; ++i){
        for(int j = i+1; j < n; ++j){
          pair<circle,circle> tmp;
          int ret = getEncirclingCircle(R,vc[i],vc[j],vc,tmp);
          if(ret>=1){
            point pc0 = (R/(abs(tmp.first.c-vc[i].c))) * (tmp.first.c-vc[i].c) + tmp.first.c;
            point pc1 = (R/(abs(tmp.first.c-vc[j].c))) * (tmp.first.c-vc[j].c) + tmp.first.c;
            blueCircles.push_back( bc(i,tmp.first.c,pc0) );
            blueCircles.push_back( bc(j,tmp.first.c, pc1));
          }
          if(ret>=2){
            point pc0 = (R/(abs(tmp.second.c-vc[i].c))) * (tmp.second.c-vc[i].c) + tmp.second.c;
            point pc1 = (R/(abs(tmp.second.c-vc[j].c))) * (tmp.second.c-vc[j].c) + tmp.second.c;
            blueCircles.push_back( bc(i,tmp.second.c,pc0) );
            blueCircles.push_back( bc(j,tmp.second.c,pc1) );
          }
        }
      }
      
      if( blueCircles.size() == 0 ){
        cout << 0 << endl;
        continue;
      }
      assert(blueCircles.size()>0);
      
      sort(blueCircles.begin(), blueCircles.end(), cmp(blueCircles.front().center));
            
      for(int i = 0; i < (int)blueCircles.size(); ++i){
        bc i0 = blueCircles[i];
        bc i1 = blueCircles[(i+1)%blueCircles.size()];
        if( i0.corr != i1.corr ){
          elem tmp=abs(arg( (i0.corr_c-i0.center)/(i1.corr_c-i1.center)));
          res += tmp * R;
        }
        else if( i0.corr == i1.corr ){            
          elem tmp = abs(arg((i0.corr_c-vc[i0.corr].c)/(i1.corr_c-vc[i0.corr].c)));
          res += tmp * (2*R-vc[i0.corr].r);
        }
      }
    }

    cout << fixed << setprecision(16) << res << endl;
  }
  return 0;
}