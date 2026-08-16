#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0,i##_cond=(n);i<i##_cond;++i)
#define all(a) (a).begin(),(a).end()

const double EPS = 1e-8;
// 点
typedef complex<double> P;
namespace std {
  bool isnan(const P&p){
    return isnan(p.real()) or isnan(p.imag());
  }
}

// 円
struct C {
  P p; double r;
  C(const P &p_, double r_) : p(p_), r(r_) { }
};

// 点同士
double distancePP(const P &p, const P &q){
  return abs(p-q);
}
// 円同士の交点
// 1点または2点で交わることを要求する
// 交わらない時はnanを返す
pair<P, P> crosspointCC(const C& c1, const C& c2) {
    double d = abs(c1.p - c2.p);
    double rc = (d*d + c1.r*c1.r - c2.r*c2.r) / (2*d);
    double rs = sqrt(c1.r*c1.r - rc*rc);
    P diff = (c2.p - c1.p) / d;
    return make_pair(c1.p + diff * P(rc, rs), c1.p + diff * P(rc, -rs));
}

// 入力
int n;
vector<C> cs;

// 点が全ての円に含まれないか
bool notInclude(const P &p){
  bool f = true;
  rep(j,n)
    if(distancePP(cs[j].p,p) + EPS < cs[j].r) // 内部にある
      f = false;
  return f;
}

// i番目の円について
double calc(int i){
  double res = 0;

  // 交点を列挙
  vector<P> ps; // 交点
  rep(j,n){
    if(i == j) continue;

    auto pp = crosspointCC(cs[i],cs[j]);
    if(not isnan(pp.first))
      ps.push_back(pp.first);
    if((not isnan(pp.second)) and pp.first != pp.second)
      ps.push_back(pp.second);
  }

  // 半時計回りにソート
  auto g = [&](const P &p, const P &q){
    P tmpp = p - cs[i].p, tmpq = q - cs[i].p;
    return arg(tmpp) < arg(tmpq);
  };
  sort(all(ps),g);

  // 各区間がカウントされるかチェック
  if(ps.size() == 0){
    // 交点がなければどこでもいい
    P tmp{cs[i].p.real(), cs[i].p.imag()+cs[i].r};
    if(notInclude(tmp))
      res += 2 * M_PI * cs[i].r;
    
  }else if(ps.size() == 1){
    // どこかで接していたら反対側をとる
    P op = ps[0] - P(2,0)*(ps[0]-cs[i].p);
    if(notInclude(op))
      res += 2 * M_PI * cs[i].r;
    
  }else{
    rep(k,ps.size()){
      P a = ps[k]-cs[i].p, b = ps[(k+1)%ps.size()]-cs[i].p;

      double midd = (arg(a)+arg(b))/2;
      P midp = cs[i].p + P(cs[i].r*cos(midd),cs[i].r*sin(midd));
      if(arg(a) > arg(b)) 
	midp = midp - P(2,0)*(midp-cs[i].p);

      if(notInclude(midp)){
	if(arg(a) < arg(b)){
	  double tmp = (arg(b)-arg(a)) * cs[i].r;
	  res += tmp;
	}else{
	  double tmp = (2*M_PI + arg(b)-arg(a)) * cs[i].r;
	  res += tmp;
	}
      }
    }
  }
  
  return res;
}

signed main(){
  while(cin >> n, n){
    cs.clear();
    rep(i,n){
      double x,y,r; cin >> x >> y >> r;
      P tmp(x,y);
      cs.emplace_back(tmp,r);
    }
    double ans = 0;
    rep(i,n){
      double tmp = calc(i);
      ans += tmp;
    }
    printf("%.10lf\n",ans);
  }
}
