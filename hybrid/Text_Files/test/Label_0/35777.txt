import static java.lang.Math.*;
import static java.lang.System.*;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Collection;
import java.util.LinkedList;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Queue;
import java.util.Random;
import java.util.Scanner;

class Main {
    public static Random rand=new Random();
    static  final  int INF=1<<29;


    class P{
    	int x,y;
    	P(int _x,int _y){
    		x=_x;y=_y;
    	}
    }

    int[] dirx=new int[]{1,0,-1,0};
    int[] diry=new int[]{0,1,0,-1};

    int getDist(int i,int j){
    	P _p=new P(dx[i],dy[i]);
    	Queue<P> que=new LinkedList<P>();
    	que.add(_p);
    	int d=0;
    	boolean[][] passed=new boolean[h][w];
		passed[_p.y][_p.x]=true;
    	while(!que.isEmpty()){
    		Queue<P> tmp=new LinkedList<P>();
    	   	while(!que.isEmpty()){
        		P p=que.poll();
        		for(int k=0;k<4;k++){
        			int nx=p.x+dirx[k],ny=p.y+diry[k];
        			if(0<=nx && nx<w && 0<=ny && ny<h){
        				if(map[ny][nx]=='x')continue;
        				if(nx==dx[j] && ny==dy[j])return d+1;
        				if(!passed[ny][nx]){
        					tmp.add(new P(nx,ny));
        					passed[ny][nx]=true;
        				}
        			}
        		}
    	   	}
    		que=tmp;
    		d++;
    	}
    	return INF;
    }

    // O(n^3) n≦100
 	static void warshall_floyd(int[][] d){
 		int n=d.length;
 	    for(int k=0;k<n;k++)
 	    	for(int i=0;i<n;i++)for(int j=0;j<n;j++)
 	    		d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
 	}


	char[][] map;
	int[] dx,dy;
	int h,w;
    public void run() {
        Case:while(true){
        	w=sc.nextInt();h=sc.nextInt();
        	if(h==0 && w==0)return;

        	map=new char[h][w];
        	for(int y=0;y<h;y++)
        		map[y]=sc.next().toCharArray();

        	int D=0;
        	for(int y=0;y<h;y++)for(int x=0;x<w;x++)
        		if(map[y][x]=='*')D++;
        	dx=new int[D+1];dy=new int[D+1];
        	int ind=0;
        	for(int y=0;y<h;y++)for(int x=0;x<w;x++)if(map[y][x]=='o'){
    			dx[ind]=x;
    			dy[ind]=y;
    			ind++;
        	}
        	for(int y=0;y<h;y++)for(int x=0;x<w;x++)if(map[y][x]=='*'){
    			dx[ind]=x;
    			dy[ind]=y;
    			ind++;
        	}
        	int[][] ds=new int[D+1][D+1];
        	for(int i=0;i<D+1;i++)Arrays.fill(ds[i],INF);
        	for(int i=0;i<D+1;i++)ds[i][i]=0;
        	for(int i=0;i<D+1;i++)for(int j=0;j<D+1;j++)
        		if(i!=j)ds[i][j]=getDist(i,j);

        	warshall_floyd(ds);

        	int[][] dp=new int[D+1][1<<(D+1)];
        	for(int i=0;i<D+1;i++)
        		Arrays.fill(dp[i],INF);
        	dp[0][1]=0;
        	for(int i=1;i<(1<<(D+1));i++){
        		for(int pos=1;pos<D+1;pos++){
        			if(((i>>pos) & 1) ==0)continue;
        			int mv=INF;
        			for(int prev=0;prev<D+1;prev++){
        				if(((i>>prev) & 1)==1 && pos!=prev)
        					if(mv>dp[prev][i-(1<<pos)]+ds[prev][pos])
        						mv=dp[prev][i-(1<<pos)]+ds[prev][pos];
         			}
        			dp[pos][i]=mv;
        		}
        	}
        	int mv=INF;
        	for(int i=1;i<D+1;i++)mv=min(mv,dp[i][(1<<(D+1))-1]);
        	if(mv<INF)
        		ln(mv);
        	else
        		ln(-1);
        }
    }
    public static void main(String[] args) {
        new Main().run();
    }

	static Scanner sc=new Scanner(in);


	//output lib
	static final String br=System.getProperty("line.separator");
	static final String[] asep=new String[]{""," ",br,br+br};
	static String str(Boolean o){
		return o?"YES":"NO";
	}
//	static String str(Double o){
//		return String.format("%.8f",o);
//	}
	static <K,V> String str(Map<K, V> map){
		StringBuilder sb=new StringBuilder();
		boolean isFirst=true;
		for(Entry<K,V> set:map.entrySet()){
			if(!isFirst)sb.append(br);
			sb.append(str(set.getKey())).append(":").append(str(set.getValue()));
			isFirst=false;
		}
		return sb.toString();
	}
	static <E> String str(Collection<E> list){
		StringBuilder sb=new StringBuilder();
		boolean isFirst=true;
		for(E e:list){
			if(!isFirst)sb.append(" ");
			sb.append(str(e));
			isFirst=false;
		}
		return sb.toString();
	}

	static String str(Object o){
		int depth=_getArrayDepth(o);
		if(depth>0)return _strArray(o,depth);
		Class<?> c=o.getClass();
		if(c.equals(Boolean.class))return str((Boolean)o);
		//if(c.equals(Double.class))return str((Double)o);

		return o.toString();
	}
	static int _getArrayDepth(Object o){
		if(!o.getClass().isArray() || Array.getLength(o)==0) return 0;
		return 	1+_getArrayDepth(Array.get(o,0));
	}
	static String _strArray(Object o,int depth){
		if(depth==0) return str(o);
		StringBuilder sb=new StringBuilder();
		for(int i=0,len=Array.getLength(o);i<len;i++){
			if(i!=0)sb.append(asep[depth]);
			sb.append(_strArray(Array.get(o,i),depth-1));
		}
		return sb.toString();
	}
	static void pr(Object... os){
		boolean isFirst=true;
		for(Object o:os){
			if(!isFirst)out.print(" ");
			out.print(o);
			isFirst=false;
		}
	}
	static void ln(){
		out.println();
	}
	static void ln(Object... os){
		for(Object o:os){
			pr(o);ln();
		}
	}
}