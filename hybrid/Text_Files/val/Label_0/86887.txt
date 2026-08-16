import java.util.*;
import java.awt.geom.Line2D;

public class Main{
    int n;
    int xa,ya,xb,yb;
    int xs,ys,xt,yt,o,l;
    Line2D a,b;
    Intersection[] inter;

    class Intersection{
	double dist;
	int owner,height;
	public Intersection(double dist,int owner,int height){
	    this.dist = dist;
	    this.owner = owner;
	    this.height = height;
	}
    }

    void solve(){
	Scanner sc = new Scanner(System.in);
	int T = sc.nextInt();
	while(T--!=0){
	    xa = sc.nextInt(); ya = sc.nextInt();
	    xb = sc.nextInt(); yb = sc.nextInt();
	    n = sc.nextInt();

	    inter = new Intersection[n];
	    for(int i=0; i<n; i++){
		xs = sc.nextInt(); ys = sc.nextInt();
		xt = sc.nextInt(); yt = sc.nextInt();
		o = sc.nextInt(); l = sc.nextInt();
		a = new Line2D.Double(xa,ya,xb,yb);
		b = new Line2D.Double(xs,ys,xt,yt);
		if(a.intersectsLine(b)){
		    double d = calcDist(xa,ya,xb,yb,xs,ys,xt,yt);
		    inter[i] = new Intersection(d,o,l);
		}else{
		    inter[i] = new Intersection(-1,-1,-1);
		}
	    }

	    Comparator<Intersection> cmp = new Comparator<Intersection>(){
		public int compare(Intersection i1, Intersection i2){
		    if(i1.dist<i2.dist) return -1;
		    if(i1.dist>i2.dist) return 1;
		    return 0;
		}
	    };
	    Arrays.sort(inter, cmp);
	    
	    int ans = Math.min(countGate(0),countGate(1));
	    
	    System.out.println(ans);
	}
    }
    
    double calcDist(int x1,int y1,int x2,int y2,int x3,int y3,int x4,int y4){
	double bx = x4-x3;
	double by = y4-y3;
	double d1 = Math.abs(bx*(y1-y3)-by*(x1-x3));
	double d2 = Math.abs(bx*(y2-y3)-by*(x2-x3));
	double t = d1/(d1+d2);	
	double x = x1+(x2-x1)*t;
	double y = y1+(y2-y1)*t;
	
	return (xa-x)*(xa-x)+(ya-y)*(ya-y);
    }
    
    int countGate(int nowHeight){
	int count = 0;
	for(int i=0; i<n; i++){
	    if(inter[i].dist==-1)continue;
	    if(inter[i].owner==0){
		if(inter[i].height==nowHeight){
		    nowHeight = 1 - nowHeight;
		    count++;
		}
	    }else{
		if(inter[i].height!=nowHeight){
		    nowHeight = 1 - nowHeight;
		    count++;
		}
	    }
	}
	return count;
    }
    
    public static void main(String[] args){
	new Main().solve();
    }
}