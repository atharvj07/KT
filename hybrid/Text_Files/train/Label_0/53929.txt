import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			int n = sc.nextInt();
			int k = sc.nextInt();
			if(n==0 && k==0) break;
			
			int[][] cost = new int[n+1][n+1];
			for(int i=1;i<=n;i++){
				Arrays.fill(cost[i], Integer.MAX_VALUE);
				cost[i][i] = 0;
			}
			
			int p, a, b ,c, d, e;
			for(int z=0;z<k;z++){
				p = sc.nextInt();
				if(p==0){
					a = sc.nextInt();
					b = sc.nextInt();
					if(cost[a][b]==Integer.MAX_VALUE) System.out.println(-1);
					else System.out.println(cost[a][b]);
				}else{
					c = sc.nextInt();
					d = sc.nextInt();
					e = sc.nextInt();
					if(e<cost[c][d]){
						cost[c][d] = e;
						cost[d][c] = e;
						for(int i=1;i<=n;i++){
							for(int j=1;j<=n;j++){	
								if(cost[i][c]!=Integer.MAX_VALUE && cost[d][j]!=Integer.MAX_VALUE){
									cost[i][j] = Math.min(cost[i][j], cost[i][c]+cost[c][d]+cost[d][j]);
								}
								if(cost[i][d]!=Integer.MAX_VALUE && cost[c][j]!=Integer.MAX_VALUE){
									cost[i][j] = Math.min(cost[i][j], cost[i][d]+cost[d][c]+cost[c][j]);
								}
								cost[j][i] = cost[i][j];
							}
						}
					}
				}
			}
		}	
	}	
}