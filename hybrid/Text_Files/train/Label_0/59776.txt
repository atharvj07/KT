import java.util.*;
import java.io.*;
import java.math.*;
 
public class Solver {	
    public static void main(String args[]) throws IOException{
    	new Solver().run();
	}

	StreamTokenizer in;
	PrintWriter out;

	int nextInt() throws IOException{
		in.nextToken();
		return (int)in.nval;
	}
	void run() throws IOException{
		in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
		out = new PrintWriter(new OutputStreamWriter(System.out));
		solve();
		out.flush();
	}
	void solve() throws IOException{
		int n = nextInt();
    	int[][] G = new int[n][n];
    	if(n == 4)
    		out.println("-1");
    	else{
    		for(int i = 0; i < n; i++)
    			G[i][(i+1)%n] = 1;
    		for(int y = 0; y < n; y++){
    			for(int x = 0; x < n; x++){
    				if(G[y][x] + G[x][y] == 0 && x != y){
    					if(y % 2 == x % 2) G[y][x] = 1;
    					else G[x][y] = 1;
    				}
    			}
    		}
    		for(int y = 0; y < n; y++){
    			for(int x = 0; x < n-1; x++){
    				out.print(G[y][x]);
    				out.print(" ");
    			}
    			out.println(G[y][n-1]);
    		}
    	}
	}
}