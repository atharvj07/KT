import java.util.*;

public class Main {
	Scanner sc = new Scanner(System.in);
	int cnt(int s,int g,int cnt,int xy[][],int n){
		int result = 0;
		int c[] = new int [n+1];
		int d[] = new int [n+1];
		c[s] = 1;
		if(s == g && cnt > 0)result = 1;
		for(int i = 1;i < cnt;i++){
			for(int j = 1;j < n+1;j++){
				for(int k = 1;k < n+1;k++){
					if(xy[j][k] == 1 && c[j] == i){
						d[k] = i + 1;
					}
				}
			}
			for(int j = 1;j < n+1;j++){
				c[j] = d[j];
			}
			if(c[g] > 0){
				result = c[g];
				break;
			}
			if(i == 101){
				break;
			}
		}
		return result;
	}
	void doIt() { 
		int n = sc.nextInt();
		int xy[][] = new int [n+1][n+1];
		for(int i = 0;i < n;i++){
			int r1 = sc.nextInt();
			int k1 = sc.nextInt();
			for(int j = 0;j < k1;j++){
				int t = sc.nextInt();
				xy[r1][t] = 1;
			}
    	 }
		int p = sc.nextInt();
		for(int i = 0;i < p;i++){
			int s = sc.nextInt();
			int d = sc.nextInt();
			int TTL = sc.nextInt();
			int ans = cnt(s,d,TTL,xy,n);
			if(ans == 0){
				System.out.println("NA");
			}else{
				System.out.println(ans);
			}
		}
		/*
		//中身
		for(int i = 1;i <= n;i++){
			for(int j = 1;j <= n;j++){
				System.out.print(xy[i][j]);
			}
			System.out.println();
		}
		*/
     }
    public static void main(String[] args) {
    	// TODO Auto-generated method stub
    	new Main().doIt();
    }
}