
import java.util.*;
  
public class Main {
    Scanner sc = new Scanner(System.in);
  
    public static void main(String[] args) {
        new Main(); 
    }
  
    public Main() {
        new C().doIt();
    }
    class C{
    	double map[][];
    	double DP[][];
        void doIt(){
        	int n = sc.nextInt();
        	int m = sc.nextInt();
        	map = new double[n][401];
        	DP = new double[n][401];
        	for(int i = 0;i < n;i++){
        		int s = sc.nextInt();
        		double Hsum = 0;
        		double start = 1;
        		for(int j = 0;j < s;j++){
        			double S = sc.nextDouble();
        			double H = sc.nextDouble();
        			Hsum = Hsum + (H*S);
        			for(int k = (int)start;k <= Hsum;k++){
        				if(k > 400)break;
        				map[i][k] = map[i][k-1] + (1.0/S);
        			}
        			start = Hsum + 1;
        		}
        	}
        	for(int i = 1;i <= 400;i++){
        		DP[0][i] = map[0][i];
        		if(DP[0][i] == 0)DP[0][i] = DP[0][i-1];
        	}
        	for(int i = 1;i < n;i++){
        		for(int j = 1;j <= 400;j++){
        			for(int k = 0;k <= j;k++){
        				DP[i][j] = Math.max(DP[i][j],DP[i-1][j-k]+map[i][k]);
        			}
        		}
        	}
//        	for(int i = 0;i < n;i++){
//        		for(int j = 0;j <= 15;j++){
//        			System.out.printf("%.3f ",DP[i][j]);
//        		}
//        		System.out.println();
//        	}
//        	System.out.println();
//        	for(int i = 0;i < n;i++){
//        		for(int j = 0;j <= 15;j++){
//        			System.out.printf("%.3f ",map[i][j]);
//        		}
//        		System.out.println();
//        	}
        	System.out.println(DP[n-1][m]);
        }
    }
}