import java.util.*;
import java.io.*;
public class Main{
	static class node{
		int x,y,d;
		 node(int x1, int y1,int d1){x=x1;y=y1;d=d1;}
	}

public static long gcd(long a,long b){
	if(b==0){return a;}
	return gcd(b,a%b);
}

static int bfs(int[][] arr, int sx,int sy,int dx,int dy){
	int n=arr.length,m=arr[0].length;
	Queue<node> q=new LinkedList<>();
	boolean[][] b=new boolean[n][m];
	if(arr[sx][sy]!=0)q.add(new node(sx,sy,0));
	b[sx][sy]=true;
	while(!q.isEmpty()){
		node curr=q.poll();
		int x=curr.x,y=curr.y,d=curr.d;
		if(x==dx&&y==dy){return d;}
		if(y+1<m&&arr[x][y+1]!=0&&!b[x][y+1]){q.add(new node(x,y+1,d+1));b[x][y+1]=true;}
		if(y-1>=0&&arr[x][y-1]!=0&&!b[x][y-1]){q.add(new node(x,y-1,d+1));b[x][y-1]=true;}
		if(x+1<n&&arr[x+1][y]!=0&&!b[x+1][y]){q.add(new node(x+1,y,d+1));b[x+1][y]=true;}
		if(x-1>=0&&arr[x-1][y]!=0&&!b[x-1][y]){q.add(new node(x-1,y,d+1));b[x-1][y]=true;}
	}
	return -1;
}
public static void main(String[] args) throws FileNotFoundException, IOException{
       Scanner s=new Scanner(System.in);
       BufferedWriter out=new BufferedWriter(new OutputStreamWriter(System.out));
       int n=s.nextInt(),m=s.nextInt();
       s.nextLine();
       int[][] arr=new int[n][m];
       int[][][][] dp=new int[n][m][n][m];
       for(int i=0;i<n;i++){
       	String ss= s.nextLine();
       	for(int j=0;j<m;j++){
       		if(ss.charAt(j)=='.'){arr[i][j]=1;}
       	}
       }
       int res=0;
        for(int i=0;i<n;i++){
        	for(int j=0;j<m;j++){
        		for(int k=0;k<n;k++){
        			for(int l=0;l<m;l++){
        				if(arr[i][j]==0||dp[k][l][i][j]!=0){continue;}
        				dp[i][j][k][l]=bfs(arr,i,j,k,l);
        				res=Math.max(res,dp[i][j][k][l]);
        			}
        		}
        	}
        }
                out.write(res+" ");
        
        out.flush();
  }
}
