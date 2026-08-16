import java.io.*;
import java.text.DecimalFormat;
import java.util.*;

public class Main {
	static int mod = (int)1e9+7;
	static int N = (int)2e3+10;
	static int ci[] = {1, 0, -1, 0};
	static int cj[] = {0, 1, 0, -1};
	int n, m;
	char[][] a = new char[N][N];
    int[][] deg = new int[N][N];
    void fill(int i, int j) {
        if (deg[i][j] != 1) return;

        deg[i][j] = -1;
        for (int k = 0; k < 4; k++)
            if (deg[i + ci[k]][j + cj[k]] != -1) {
                deg[i + ci[k]][j + cj[k]] = -1;

                if (k == 0) {
                    a[i][j] = '^';
                    a[i+1][j] = 'v';
                } else if (k == 1) {
                    a[i][j] = '<';
                    a[i][j+1] = '>';
                } else if (k == 2) {
                    a[i-1][j] = '^';
                    a[i][j] = 'v';
                } else {
                    a[i][j-1] = '<';
                    a[i][j] = '>';
                }

                for (int kk = 0; kk < 4; kk++) {
                    if (deg[i + ci[kk]][j + cj[kk]] != -1) 
                        deg[i + ci[kk]][j + cj[kk]]--;
                    if (deg[i + ci[k] + ci[kk]][j + cj[k] + cj[kk]] != -1) 
                        deg[i + ci[k] + ci[kk]][j + cj[k] + cj[kk]]--;
                }

                for (int kk = 0; kk < 4; kk++) {
                    fill(i + ci[kk], j + cj[kk]);
                    fill(i + ci[k] + ci[kk], j + cj[k] + cj[kk]);
                }

                return;
            }
    }
    void work() throws Exception {
    	//in = new BufferedReader(new InputStreamReader(System.in));
    	out = new PrintWriter(System.out);
    	//
    	Scanner cin = new Scanner(System.in);
    	/////////////////////////////////////////
    	for(int i = 0; i < N; i ++) {
    		for(int j = 0; j < N; j ++) {
    			deg[i][j] = -1;
    		}
    	}
    	
    	n = cin.nextInt();
    	m = cin.nextInt();
        for (int i = 1; i <= n; i++) {
            String s = cin.next();
            for (int j = 1; j <= m; j++){
            	a[i][j] = s.charAt(j-1);
                if (a[i][j] == '*') 
                    deg[i][j] = -1;
                else 
                    deg[i][j] = 0;
            }
        }

        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) 
                if (deg[i][j] == 0)
                    for (int k = 0; k < 4; k++){
                    	if(deg[i + ci[k]][j + cj[k]] != -1) 
                    		deg[i][j] += 1;
                    }
                        

        for (int i = 1; i <= n; i++) 
            for (int j = 1; j <= m; j++) 
                fill(i, j);         

        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                if (a[i][j] == '.') {
                	out.println("Not unique");
                    return ;
                }

        for (int i = 1; i <= n; i ++){
        	for(int j = 1; j <= m; j ++) {
        		out.print(a[i][j]);
        	}
        	out.println();  
        }
             	
    }
  //  BufferedReader in;
  //  StringTokenizer str = null;
    static PrintWriter out;
//    private String next() throws Exception{
//    	while (str == null || !str.hasMoreElements())
//    	    str = new StringTokenizer(in.readLine());
//    	return str.nextToken();
//    } 
//    private int nextInt() throws Exception{
//    	return Integer.parseInt(next());
//    }
//    private long nextLong() throws Exception{
//    	return Long.parseLong(next());
//    }
    static int dx[] = {0,1,0,-1};
    static int dy[] = {1,0,-1,0};
    class pair implements Comparable<pair>{
    	int first, second;
    	pair(int x, int y) {
    		first = x;
    		second = y;
    	}
		public int compareTo(pair o) {
			// TODO auto-generated method stub
			if(first != o.first) return ((Integer)first).compareTo(o.first);
			else return ((Integer)second).compareTo(o.second); 
		}
    }
    DecimalFormat df=new DecimalFormat("0.00");
    public static void main(String[] args) throws Exception{
        Main wo = new Main();
        wo.work();
        out.close();
    }
}