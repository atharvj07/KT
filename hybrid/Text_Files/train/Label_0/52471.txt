import java.util.*;
 
public class Main {
    Scanner sc = new Scanner(System.in);
 
    public static void main(String[] args) {
    	new Main(); 
    }
 
    public Main() {
    	new DPL5().doIt();
    }
    class DPL5{
    	int dpT(char ctra[],char ctrb[]){
    		int al = ctra.length;
    		int bl = ctrb.length;
    		int dp[][] = new int [al+1][bl+1];
    		int INF = 100000000;
    		for(int i = 0;i < al+1;i++){
    			for(int j = 0;j < bl+1;j++){
    				dp[i][j] = (i == 0 || j == 0 ? Math.max(i, j) : INF);
    			}
    		}
    		for(int i = 1;i < al+1;i++){
    			for(int j = 1;j < bl+1;j++){
    				dp[i][j] = Math.min(dp[i][j - 1] + 1, Math.min(dp[i - 1][j] + 1, dp[i - 1][j - 1] + (ctra[i - 1] == ctrb[j - 1] ? 0 : 1)));
    			}
    		}
    		return dp[al][bl];
    	}
    	void doIt(){
    		String stra = sc.next();
    		String strb = sc.next();
    		char ctra[] = stra.toCharArray();
    		char ctrb[] = strb.toCharArray();
    		System.out.println(dpT(ctra,ctrb));
    	}
    }
}