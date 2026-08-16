import java.util.*;
import java.util.regex.*;
import static java.lang.Math.*;
import static java.lang.System.out;

// AOJ
public class Main {
	final Scanner sc=new Scanner(System.in);
	final int[] vx={0,1,0,-1}, vy={-1,0,1,0};
	final int INF=1<<24;
	static class Point{
		int x, y;
		Point(int x, int y){	this.x=x;	this.y=y;}
		Point(){	this.x=0; this.y=0;}
		@Override public String toString(){	return "("+this.x+","+this.y+")";}
		static boolean ok(int x,int y,int X,int Y,int min){	return (min<=x&&x<X)&&(min<=y&&y<Y);}
		static boolean ok(int x,int y,int X,int Y){	return ok(x,y,X,Y,0);}
	}
	public static void main(String[] args) {
		new Main().AOJ0231();
	}
	
	void AOJ0215(){
		while(sc.hasNext()){
			int X=sc.nextInt(),Y=sc.nextInt();
			if((X|Y)==0)	break;
			char[][] c=new char[X][Y];
			ArrayList<C0215> m=new ArrayList<C0215>();
			int sx=0,sy=0,gx=0,gy=0;
			for(int y=0; y<Y; y++){
				String line=sc.next();
				for(int x=0; x<X; x++){
					c[x][y]=line.charAt(x);
					if(Character.isDigit(c[x][y]))	m.add(new C0215(x,y,Character.digit(c[x][y],10)));
					else if(c[x][y]=='S'){	
						sx=x;	sy=y;
					}else if(c[x][y]=='G'){
						gx=x;	gy=y;
					}
				}
			}
			LinkedList<C02152> open=new LinkedList<C02152>();
			open.add(new C02152(-1,0,1<<1,1));
			open.add(new C02152(-1,0,1<<2,2));
			open.add(new C02152(-1,0,1<<3,3));
			open.add(new C02152(-1,0,1<<4,4));
			open.add(new C02152(-1,0,1<<5,5));
			int[] close=new int[1<<6];
			Arrays.fill(close, INF);
			close[1<<1]=0;	close[1<<2]=0;
			close[1<<3]=0;	close[1<<4]=0;	close[1<<5]=0;
			int ss=0,ans=INF;
			while(!open.isEmpty()){
				C02152 now=open.poll();
				int nx=(now.now<0?sx:m.get(now.now).x),ny=(now.now<0?sy:m.get(now.now).y);
				for(int i=0; i<m.size(); i++){
					if(!cat(now.m,m.get(i).type))	continue;
					if((now.m&(1<<m.get(i).type))>0)	continue;
					int step=now.step+abs(nx-m.get(i).x)+abs(ny-m.get(i).y);
					int mm=now.m|(1<<m.get(i).type);
					if(mm==((1<<6)-1)){
						ans=min(ans,now.step+abs(m.get(now.now).x-gx)+abs(m.get(now.now).y-gy));
						ss=now.s;
						continue;
					}
					if(close[mm]<=step)	continue;
					open.add(new C02152(i,step,mm,now.s));
					close[mm]=step;
				}
			}
			out.println(ans+" "+ss);
		}
	}
	class C0215{
		int x,y,type;
		C0215(int x,int y,int type){this.x=x; this.y=y; this.type=type;}
	}
	class C02152{
		int step,now,m,s;
		C02152(int now,int step,int m,int s){this.now=now; this.step=step; this.m=m; this.s=s;}
	}
	boolean cat(int a,int bb){
		int b=(bb-1>0?bb-1:5);
		return (a&(1<<b))>0;
	}
	
	int c;
	void AOJ0212(){
		while(sc.hasNext()){
			c=sc.nextInt();
			int n=sc.nextInt(),m=sc.nextInt(),s=sc.nextInt()-1,d=sc.nextInt()-1,ans=INF;
			if(c==0)	break;
			int[][] g=new int[n][n];
			for(int i=0; i<n; i++){
				for(int j=0; j<n; j++)	g[i][j]=INF;
			}
			for(int i=0; i<m; i++){
				int a=sc.nextInt()-1,b=sc.nextInt()-1,f=sc.nextInt();
				g[a][b]=f;	g[b][a]=f;
			}
			PriorityQueue<C0212> open=new PriorityQueue<C0212>();
			int[] close=new int[n];
			Arrays.fill(close, INF);
			int[] temp=new int[c];
			open.add(new C0212(s,0,temp,0));
			while(!open.isEmpty()){
				C0212 now=open.poll();
				//out.println("N"+now.now+" S"+now.sum);
				for(int i=0; i<n; i++){
					if(now.now==i)	continue;
					if(g[now.now][i]>=INF)	continue;
					C0212 tmp=new C0212(i,g[now.now][i],now.max.clone(),now.sum);
					if(close[i]<=tmp.sum)	continue;
					//out.println(now.now+" -> "+tmp.now+" S "+tmp.sum);
					if(i==d){
						//out.println("ANS2 "+tmp.sum);
						ans=min(ans,tmp.sum);
						continue;
					}
					open.add(new C0212(tmp));
					close[i]=tmp.sum;
				}
			}
			out.println(ans);
		}
	}
	class C0212 implements Comparable<C0212>{
		int now,sum;
		int[] max=new int[c];
		C0212(C0212 o){this.now=o.now; this.sum=o.sum; this.max=o.max;}
		C0212(int now,int nowc,int[] a,int sum){
			if(a[0]<nowc){
				sum+=a[0]/2;
				sum+=nowc/2;
				a[0]=nowc;
				Arrays.sort(a);
			}else	sum+=nowc;
			this.now=now;	this.max=a;	this.sum=sum;
		}
		@Override public int compareTo(C0212 o) {
			if(this.sum<o.sum)	return -1;
			if(this.sum>o.sum)	return 1;
			return 0;
		}
		@Override public String toString(){
			return "("+this.now+" , "+this.sum+")";
		}
	}
	
	void AOJ0231(){
		while(sc.hasNext()){
			int n=sc.nextInt();
			if(n==0)	break;
			C0231[] a=new C0231[n],b=new C0231[n];
			for(int i=0; i<n; i++){
				int m=sc.nextInt(),aa=sc.nextInt(),bb=sc.nextInt();
				a[i]=new C0231(m,aa);	b[i]=new C0231(m,bb);
			}
			Arrays.sort(a);	Arrays.sort(b);
			int i=0,j=0,w=0;
			while(i<n&&j<n){
				if(a[i].t>=b[j].t){
					w-=b[j].m;	j++;
				}
				if(a[i].t<b[j].t){
					w+=a[i].m;	i++;
				}
				//out.println("w"+w+" i"+i+" j"+j);
				if(w>150)	break;
			}
			out.println((w>150?"NG":"OK"));
		}
	}
	class C0231 implements Comparable<C0231>{
		int m,t;
		C0231(int m,int t){this.m=m; this.t=t;}
		@Override public int compareTo(C0231 o) {
			if(this.t<o.t)	return -1;
			if(this.t>o.t)	return 1;
			return 0;
		}
		
	}
}