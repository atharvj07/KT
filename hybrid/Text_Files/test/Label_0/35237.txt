import java.util.*;

public class Code {
	
    public static void main(String args[]) {
    	Scanner in = new Scanner(System.in);
    	
    	int n = in.nextInt();
    	
    	int a[][] = new int[n][6];
    	boolean vis[] = new boolean[100];
    	for(int i=0; i<n; i++) {
    		for(int j=0; j<6; j++) a[i][j] = in.nextInt();
    	}
    	
    	if(n==1) {
    		for(int i=0; i<6; i++) {
    			vis[a[0][i]] = true;
    		}
    	}
    	
    	else if(n==2) {
    		for(int i=0; i<6; i++) {
    			for(int j=0; j<6; j++) {
    				vis[a[0][i]] = true;
    				vis[a[1][j]] = true;
    				int p = 10*a[0][i] + a[1][j];
    				int q = 10*a[1][j] + a[0][i];
    				vis[p] = true;
    				vis[q] = true;
    			}
    		}
    	}
    	
    	else {
    		for(int i=0; i<6; i++) {
    			for(int j=0; j<6; j++) {
    				for(int k=0; k<6; k++) {
    					vis[a[0][i]] = true;
        				vis[a[1][j]] = true;
        				vis[a[2][k]] = true;
        				int p1 = 10*a[0][i] + a[1][j];
        				int p2 = 10*a[1][j] + a[2][k];
        				int p3 = 10*a[0][i] + a[2][k];
        				int p4 = a[0][i] + 10*a[1][j];
        				int p5 = a[1][j] + 10*a[2][k];
        				int p6 = a[0][i] + 10*a[2][k];
        				vis[p1] = vis[p2] = vis[p3] = vis[p4] = vis[p5] = vis[p6] = true;
    				}
    			}
    		}
    	}
    	int ans = 0;
    	for(int i=1; i<1000; i++) {
    		if(!vis[i]) {
    			ans = i-1; break;
    		}
    	}
    	System.out.println(ans);
    }
}