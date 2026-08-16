import java.util.*;
import static java.lang.Math.*;
public class Main {
	final Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		new Main().init();
	}
	void init(){
		new AOJ1156();
	}
	
	class AOJ1156{
		AOJ1156(){
			while(true){
				int w=sc.nextInt(),h=sc.nextInt();
				if((w|h)==0)	break;
				solve(w,h);
			}
		}
		final int INF=Integer.MAX_VALUE/4;
		void solve(int w,int h){
			int[][] b=new int[w][h];
			for(int y=0; y<h; ++y)for(int x=0; x<w; ++x)b[x][y]=sc.nextInt();
			int[] c={sc.nextInt(),sc.nextInt(),sc.nextInt(),sc.nextInt()};
			
//			LinkedList<State> open=new LinkedList<State>();
			PriorityQueue<State> open=new PriorityQueue<State>();
			open.add(new State(0,0,1,0));
			
			int[][][] closed=new int[w][h][4];
			for(int i=0; i<w; ++i)for(int j=0; j<h; ++j)for(int k=0; k<4; ++k)closed[i][j][k]=INF;
			closed[0][0][1]=0;
			
			final int[] vx={0,1,0,-1}, vy={-1,0,1,0};
			
			while(!open.isEmpty()){
				State now=open.poll();
//				System.out.println(now);
				if(now.x==w-1 && now.y==h-1){
					System.out.println(now.c);
					break;
				}
				
				for(int v=0; v<4; ++v){
					int tmp=(now.z+v)%4;
					int xx=now.x+vx[tmp];
					int yy=now.y+vy[tmp];
					if(0<=xx&&xx<w && 0<=yy&&yy<h){
						int nc=now.c + (b[now.x][now.y]==v?0:c[v]);
						if(closed[xx][yy][tmp]>nc){
							open.add(new State(xx,yy,tmp,nc));
							closed[xx][yy][tmp]=nc;
						}
					}
				}
			}
		}
		class State implements Comparable<State>{
			int x,y,z,c;
			State(int x,int y,int z,int c){
				this.x=x;
				this.y=y;
				this.z=z;
				this.c=c;
			}
			@Override public int compareTo(State o){
				return this.c-o.c;
			}
			@Override public String toString(){
				return x+","+y+" "+z+" "+c;
			}
		}
	}
	
	class AOJ1155{
		AOJ1155(){
			while(true){
				String str=sc.next();
				if(str.equals("."))	break;
				solve(str);
			}
		}
		void solve(String str){
			int cnt=0;
			str+="#";
			for(int p=0; p<=2; ++p)for(int q=0; q<=2; ++q)for(int r=0; r<=2; ++r){
				String tmp=str.replaceAll("P", ""+p).replaceAll("Q", ""+q).replaceAll("R", ""+r);
//				System.out.println(tmp);
				this.line=tmp.toCharArray();
				this.pos=0;
				int ret=expr();
//				System.out.println(ret);
				cnt += (ret==2?1:0);
			}
			System.out.println(cnt);
		}
		final int[][]	and={{0,0,0},{0,1,1},{0,1,2}},
				or={{0,1,2},{1,1,2},{2,2,2}};
		final int[] m={2,1,0};
		char[] line;
		int pos=0;
		private int expr(){
			int ret=term();
			while(true){
				char op=line[pos];
				if( op=='+' ){
					int old=ret;
					++pos;
					ret=term();
					ret=or[old][ret];
//					System.out.println(old+"+"+ret+" = "+or[old][ret]);
				}else	break;
			}
			return ret;
		}
		private int term(){
			int ret=fact();
			while(true){
				char op=line[pos];
				if( op=='*' ){
					int old=ret;
					++pos;
					ret=fact();
					ret=and[old][ret];
//					System.out.println(old+"*"+ret+" = "+and[old][ret]);
				}else	break;
			}
			return ret;
		}
		private int fact(){
			if(line[pos]=='-'){
				++pos;
				return m[fact()];
			}else if(Character.isDigit(line[pos])){
				int ret=line[pos]-'0';
				++pos;
				return ret;
			}else if(line[pos]=='('){
				++pos;
				int ret=expr();
				++pos;	// ")"テ」ツ?古ヲツ敖・テ」ツつ凝」ツ?ィテ、ツサツョテ・ツョツ?
				return ret;
			}
			return 0;
		}
	}
	
	class AOJ1153{
		AOJ1153(){
			while(true){
				int n=sc.nextInt(),m=sc.nextInt();
				if((n|m)==0)	break;
				solve(n,m);
			}
		}
		void solve(int n,int m){
			int[] nn=new int[n],
					mm=new int[m];
			int ns=0, ms=0;
			for(int i=0; i<n; ++i){
				nn[i]=sc.nextInt();
				ns+=nn[i];
			}
			for(int i=0; i<m; ++i){
				mm[i]=sc.nextInt();
				ms+=mm[i];
			}
			Arrays.sort(nn);
			Arrays.sort(mm);
			int cand1=-1,cand2=-1,sum=Integer.MAX_VALUE/4;
			for(int i=0; i<n; ++i){
				for(int j=0; j<m; ++j){
					if(ns-nn[i]+mm[j] == ms-mm[j]+nn[i] && sum>nn[i]+mm[j]){
						cand1=i;
						cand2=j;
						sum=nn[i]+mm[j];
					}
				}
			}
			System.out.println(cand1<0? "-1" : nn[cand1]+" "+mm[cand2]);
		}
	}
}