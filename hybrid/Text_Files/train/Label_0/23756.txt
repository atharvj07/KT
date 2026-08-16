     #include <bits/stdc++.h>
                                            #include<iostream>
                                            #include<cstdio>
                                            #include<vector>
                                            #include<queue>
                                            #include<map>
                                            #include<cstring>
                                            #include<string>
                                            #include <math.h>
                                            #include<algorithm>
                                        //    #include <boost/multiprecision/cpp_int.hpp>
                                            #include<functional>
                                   #define int long long
                                            #define inf  1000000007
                                            #define pa pair<int,int>
                                            #define ll long long
                                            #define pal pair<double,double>
                                            #define ppap pair<pa,int>
                                    //  #define PI 3.14159265358979323846
                                            #define paa pair<int,char>
                                            #define  mp make_pair
                                            #define  pb push_back
                                            #define EPS (1e-10)
                                            #define equals(a,b) (fabs((a)-(b))<EPS)
    int dx[8]={0,-1,0,1,1,1,-1,-1};
    int dy[8]={1,0,-1,0,-1,1,1,-1};
                                            using namespace std;
                                   			class pa3{
                                            	public:
                                            	int x,y,z;
                                            	pa3(int x=0,int y=0,int z=0):x(x),y(y),z(z) {}
                                            	bool operator < (const pa3 &p) const{
                                            		if(x!=p.x) return x<p.x;
                                            		if(y!=p.y) return y<p.y;
                                            		 return z<p.z;
                                            		//return x != p.x ? x<p.x: y<p.y;
                                            	}
                                   				bool operator > (const pa3 &p) const{
                                            		if(x!=p.x) return x>p.x;
                                            		if(y!=p.y) return y>p.y;
                                            		 return z>p.z;
                                            		//return x != p.x ? x<p.x: y<p.y;
                                            	}
                                            	bool operator == (const pa3 &p) const{
                                            		return x==p.x && y==p.y && z==p.z;
                                            	}
                                            		bool operator != (const pa3 &p) const{
                                            			return !( x==p.x && y==p.y && z==p.z);
                                            	}
                                            
                                            };
                                            
                                            class pa4{
                                            	public:
                                            	double x;
                                            	int y,z,w;
                                            	pa4(double x=0,int y=0,int z=0,int w=0):x(x),y(y),z(z),w(w) {}
                                            	bool operator < (const pa4 &p) const{
                                            		if(x!=p.x) return x<p.x;
                                            		if(y!=p.y) return y<p.y;
                                            		if(z!=p.z)return z<p.z;
                                            		return w<p.w;
                                            		//return x != p.x ? x<p.x: y<p.y;
                                            	}
                                            	bool operator > (const pa4 &p) const{
                                            		if(x!=p.x) return x>p.x;
                                            		if(y!=p.y) return y>p.y;
                                            		if(z!=p.z)return z>p.z;
                                            		return w>p.w;
                                            		//return x != p.x ? x<p.x: y<p.y;
                                            	}
                                            	bool operator == (const pa4 &p) const{
                                            		return x==p.x && y==p.y && z==p.z &&w==p.w;
                                            	}
                                            		
                                            
                                            };
                                            class pa2{
                                            	public:
                                            	int x,y;
                                            	pa2(int x=0,int y=0):x(x),y(y) {}
                                            	pa2 operator + (pa2 p) {return pa2(x+p.x,y+p.y);}
                                            	pa2 operator - (pa2 p) {return pa2(x-p.x,y-p.y);}
                                            	bool operator < (const pa2 &p) const{
                                            		return y != p.y ? y<p.y: x<p.x;
                                            	}
                                            	bool operator > (const pa2 &p) const{
                                            		return x != p.x ? x<p.x: y<p.y;
                                            	}
                                            	bool operator == (const pa2 &p) const{
                                            		return abs(x-p.x)==0 && abs(y-p.y)==0;
                                            	}
                                            	bool operator != (const pa2 &p) const{
                                            		return !(abs(x-p.x)==0 && abs(y-p.y)==0);
                                            	}
                                            		
                                            
                                            };
                                            
                                                   #define ppa pair<int,pas>
                                            class Point{
                                            	public:
                                            	double x,y;
                                            	Point(double x=0,double y=0):x(x),y(y) {}
                                            	Point operator + (Point p) {return Point(x+p.x,y+p.y);}
                                            	Point operator - (Point p) {return Point(x-p.x,y-p.y);}
                                            	Point operator * (double a) {return Point(x*a,y*a);}
                                            	Point operator / (double a) {return Point(x/a,y/a);}
                                            	double absv() {return sqrt(norm());}
                                            	double norm() {return x*x+y*y;}
                                            	bool operator < (const Point &p) const{
                                            		return x != p.x ? x<p.x: y<p.y;
                                            	}
                                            	bool operator == (const Point &p) const{
                                            		return fabs(x-p.x)<EPS && fabs(y-p.y)<EPS;
                                            	}
                                            };
                                            typedef Point Vector;
                                     #define pl pair<int,pas>
                                            struct Segment{
                                            Point p1,p2;
                                            };
                                             double dot(Vector a,Vector b){
                                            	return a.x*b.x+a.y*b.y;
                                            }
                                            double cross(Vector a,Vector b){
                                            	return a.x*b.y-a.y*b.x;
                                            }
                                        
                bool parareru(Point a,Point b,Point c,Point d){
                //	if(abs(cross(a-b,d-c))<EPS)cout<<"dd "<<cross(a-b,d-c)<<endl;
                	return abs(cross(a-b,d-c))<EPS;
                }
                double distance_ls_p(Point a, Point b, Point c) {
                  if ( dot(b-a, c-a) < EPS ) return (c-a).absv();
                  if ( dot(a-b, c-b) < EPS ) return (c-b).absv();
                  return abs(cross(b-a, c-a)) / (b-a).absv();
                }
                bool is_intersected_ls(Segment a,Segment b) {
                	if(a.p1==b.p1||a.p2==b.p1||a.p1==b.p2||a.p2==b.p2) return false;
                	if(parareru((a.p2),(a.p1),(a.p1),(b.p2))&&parareru((a.p2),(a.p1),(a.p1),(b.p1))){
                //		cout<<"sss"<<endl;
                		if(dot(a.p1-b.p1,a.p1-b.p2)<EPS) return true;
                		if(dot(a.p2-b.p1,a.p2-b.p2)<EPS) return true;
                		if(dot(a.p1-b.p1,a.p2-b.p1)<EPS) return true;
                		if(dot(a.p1-b.p2,a.p2-b.p2)<EPS) return true;
                		return false;
                	}
                  else return ( cross(a.p2-a.p1, b.p1-a.p1) * cross(a.p2-a.p1, b.p2-a.p1) < EPS ) && ( cross(b.p2-b.p1, a.p1-b.p1) * cross(b.p2-b.p1, a.p2-b.p1) < EPS );
                }
                 
                double segment_dis(Segment a,Segment b){
                	if(is_intersected_ls(a,b))return 0;
                	double r=distance_ls_p(a.p1, a.p2, b.p1);
                	r=min(r,distance_ls_p(a.p1, a.p2, b.p2));
                	r=min(r,distance_ls_p(b.p1, b.p2, a.p2));
                	r=min(r,distance_ls_p(b.p1, b.p2, a.p1));
                	return r;
                }
                Point intersection_ls(Segment a, Segment b) {
                  Point ba = b.p2-b.p1;
                  double d1 = abs(cross(ba, a.p1-b.p1));
                  double d2 = abs(cross(ba, a.p2-b.p1));
                  double t = d1 / (d1 + d2);
                 
                  return a.p1 + (a.p2-a.p1) * t;
                }
                 
                                string itos( int i ) {
                                ostringstream s ;
                                s << i ;
                                return s.str() ;
                                }
                                 
                                int gcd(int v,int b){
                                	if(v>b) return gcd(b,v);
                                	if(v==b) return b;
                                	if(b%v==0) return v;
                                	return gcd(v,b%v);
                                }
                 
                                double distans(double x1,double y1,double x2,double y2){
                                	double rr=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
                                	return sqrt(rr);
                                	
                                }
                                int mod;
                                
                int pr[500010];
                int inv[500010];
                
                int beki(int wa,int rr,int warukazu){
                	if(rr==0) return 1%warukazu;
                	if(rr==1) return wa%warukazu;
                	if(rr%2==1) return (beki(wa,rr-1,warukazu)*wa)%warukazu;
                	int zx=beki(wa,rr/2,warukazu);
                	return (zx*zx)%warukazu;
                }
    double bekid(double w,int r){
    	if(r==0) return 1.0;
    	if(r==1) return w;
    	if(r%2) return bekid(w,r-1)*w;
    	double f=bekid(w,r/2);
    	return f*f;
    }
                
    			int comb(int nn,int rr){
    				int r=pr[nn]*inv[rr];
    				r%=mod;
    				r*=inv[nn-rr];
    				r%=mod;
    				return r;
    			}
                
                void gya(int ert){
                	pr[0]=1;
                	for(int i=1;i<ert;i++){
                		pr[i]=(pr[i-1]*i)%mod;
                	}
                	for(int i=0;i<ert;i++) inv[i]=beki(pr[i],mod-2,mod);
                	
                }
                
              //   cin.tie(0);
    		//	ios::sync_with_stdio(false);
    			//priority_queue<pa3,vector<pa3>,greater<pa3>> pq;            
                 //sort(ve.begin(),ve.end(),greater<int>());
                                         //----------------kokomade tenpure------------
                //vector<double> ans(100000000),ans2(100000000)

///////////////////////////////////////////////////////////
struct segsumxor{
	//       1
	//   2        3
	// 4   5   6    7
	
	
	private:
	public:
	
	// 1<<10 = 1024
	// 1<<11 = 2048
	// 1<<12 = 4096
	// 1<<13 = 8192
	// 1<<14 = 16384
	// 1<<15 = 32768
	// 1<<16 = 65536
	// 1<<17 = 131072
	// 1<<18 = 262144
	
	int cor=(1<<17);
	
	vector<int> vec;
	int tani=0;
	int en(int x,int y){
		return x^y;	
	}
	void shoki1(){
		vec.resize(2*cor+3, tani);
	}
		void shoki2(){
			for(int i=cor-1;i>0;i--) vec[i]=en(vec[2*i],vec[2*i+1]);
		}
	
	
	
	// [a,b)
	// k-th node
	// k no kukanha [l,r)
	int sum(int a,int b,int k=1,int l=0,int r=-10){
		if(r<0)r=cor;
		
	//	cout<<a<<" "<<b<<" "<<k<<" "<<l<<" "<<r<<endl;
		
		if(a<=l && r<=b){
			return vec[k];
		}
		if(r<=a || b<=l){
			return tani;
		}
		
		int v1=sum(a,b,k*2,l,(l+r)/2),v2=sum(a,b,k*2+1,(l+r)/2,r);
		return en(v1,v2);
	}
	
};

struct segsumor{
	//       1
	//   2        3
	// 4   5   6    7
	
	
	private:
	public:
	
	// 1<<10 = 1024
	// 1<<11 = 2048
	// 1<<12 = 4096
	// 1<<13 = 8192
	// 1<<14 = 16384
	// 1<<15 = 32768
	// 1<<16 = 65536
	// 1<<17 = 131072
	// 1<<18 = 262144
	
	int cor=(1<<17);
	
	vector<int> vec;
	int tani=0;
	int en(int x,int y){
		return x|y;	
	}
	void shoki1(){
		vec.resize(2*cor+3, tani);
	}
		void shoki2(){
			for(int i=cor-1;i>0;i--) vec[i]=en(vec[2*i],vec[2*i+1]);
		}
	
	
	
	// [a,b)
	// k-th node
	// k no kukanha [l,r)
	int sum(int a,int b,int k=1,int l=0,int r=-10){
		if(r<0)r=cor;
		
	//	cout<<a<<" "<<b<<" "<<k<<" "<<l<<" "<<r<<endl;
		
		if(a<=l && r<=b){
			return vec[k];
		}
		if(r<=a || b<=l){
			return tani;
		}
		
		int v1=sum(a,b,k*2,l,(l+r)/2),v2=sum(a,b,k*2+1,(l+r)/2,r);
		return en(v1,v2);
	}
	
};

struct segsumand{
	//       1
	//   2        3
	// 4   5   6    7
	
	
	private:
	public:
	
	// 1<<10 = 1024
	// 1<<11 = 2048
	// 1<<12 = 4096
	// 1<<13 = 8192
	// 1<<14 = 16384
	// 1<<15 = 32768
	// 1<<16 = 65536
	// 1<<17 = 131072
	// 1<<18 = 262144
	
	int cor=(1<<17);
	
	vector<int> vec;
	int tani=(1ll<<31)-1;
	int en(int x,int y){
		return x&y;	
	}
	void shoki1(){
		vec.resize(2*cor+3, tani);
	}
		void shoki2(){
			for(int i=cor-1;i>0;i--) vec[i]=en(vec[2*i],vec[2*i+1]);
		}
	
	
	
	// [a,b)
	// k-th node
	// k no kukanha [l,r)
	int sum(int a,int b,int k=1,int l=0,int r=-10){
		if(r<0)r=cor;
		
	//	cout<<a<<" "<<b<<" "<<k<<" "<<l<<" "<<r<<endl;
		
		if(a<=l && r<=b){
			return vec[k];
		}
		if(r<=a || b<=l){
			return tani;
		}
		
		int v1=sum(a,b,k*2,l,(l+r)/2),v2=sum(a,b,k*2+1,(l+r)/2,r);
		return en(v1,v2);
	}
	
};

segsumor Sor;
segsumand Sand;
segsumxor Sxor;
///////////////////////////////
int a[4][100200]={0};

int val[4][100200]={0};

vector<pa> ve[4];

int sxor(int l,int r){
	return Sxor.sum(l,r);
}

int sand(int l,int r){
return	Sand.sum(l,r);
}

int sor(int l,int r){
return	Sor.sum(l,r);
}
string s;
int solve4(int l,int r){
	int ans=0;
	for(int i=l;i<=r;i++){
	ans*=10;
		ans+=s[i]-'0';
	}
//	cout<<"solve4 "<<l<<" "<<r<<" "<<ans<<endl;
	return ans;
}

int solve3(int l,int r){
	int ans;
	if(a[3][l]==a[3][r]) ans= solve4(l,r);
	else  ans=sxor(a[3][l]+1,a[3][r])^solve4(ve[3][a[3][r]].first,r)^solve4(l,ve[3][a[3][l]].second);
//	cout<<"solve3 "<<l<<" "<<r<<" "<<ans<<endl;
	return ans;
}

int solve2(int l,int r) {// 0~9, ^,&
	int ans;
	if(a[2][l]==a[2][r]) ans= solve3(l,r);
	else ans=sand(a[2][l]+1,a[2][r])&solve3(ve[2][a[2][r]].first,r)&solve3(l,ve[2][a[2][l]].second);
//	cout<<"solve2 "<<l<<" "<<r<<" "<<ans<<endl;
	return ans;
}

int solve(int l,int r){
	int ans;
	if(a[1][l]==a[1][r]) ans= solve2(l,r);
	else  ans=sor(a[1][l]+1,a[1][r])|solve2(ve[1][a[1][r]].first,r)|solve2(l,ve[1][a[1][l]].second);
//	cout<<"solve1 "<<l<<" "<<r<<" "<<ans<<endl;
	return ans;
}

    signed main(){
     
    	       cin.tie(0);
    			ios::sync_with_stdio(false);
int n,q;
    	cin>>n;
    	
    	
    	n++;
    	cin>>s;
    	s+="|";
    	for(int i=0;i<100200;i++)val[1][i]=(1ll<<31)-1;
    	int ima=0;
    	int si=0;
    	for(int i=0;i<n;i++){
    		if(s[i]>='0' && s[i]<='9'){
    			a[3][i]=ima;
    			val[3][ima]*=10;
    			val[3][ima]+=s[i]-'0';
    		}
    		else{
    			
    			ve[3].pb(mp(si,i-1));
    			si=i+1;
    			ima++;
    		}
    	}
    	
    	ima=0;
    	si=0;
    	for(int i=0;i<n;i++){
    		
    		if(s[i]!='&' && s[i]!='|'){
    			a[2][i]=ima;
    			if(s[i]=='^'){
    				val[2][ima]^= val[3][a[3][i-1]];
    			}
    		}
    		else{
    			
    			ve[2].pb(mp(si,i-1));
    			si=i+1;
    			val[2][ima]^= val[3][a[3][i-1]];
    			
    			ima++;
    		}
    	}
    
    	ima=0;
    	si=0;
    	for(int i=0;i<n;i++){
    		if( s[i]!='|'){
    			a[1][i]=ima;
    			if(s[i]=='&'){
    	
    				val[1][ima]&= val[2][a[2][i-1]];
   
    			}
    		}
    		else {
    			ve[1].pb(mp(si,i-1));
    			si=i+1;
    				val[1][ima]&= val[2][a[2][i-1]];

    			ima++;
    		}
    	}
    	
    	Sor.shoki1();
    	Sxor.shoki1();
    	Sand.shoki1();
    	for(int i=0;i<=100000;i++)Sxor.vec[Sxor.cor+i]=val[3][i];
    	for(int i=0;i<=100000;i++)Sand.vec[Sxor.cor+i]=val[2][i];
    	for(int i=0;i<=100000;i++)Sor.vec[Sxor.cor+i]=val[1][i];
    	Sor.shoki2();
    	Sxor.shoki2();
    	Sand.shoki2();
    	cin>>q;
    	
    	for(int i=0;i<q;i++){
    		int l,r;
    		cin>>l>>r;
    		cout<<solve(l,r)<<endl;
    	}
   
  	return 0;
    }

