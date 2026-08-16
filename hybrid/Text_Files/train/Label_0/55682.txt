import java.awt.geom.*;
import java.io.*;
import java.util.*;


public class Main {
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			int n = sc.nextInt();
			int m = sc.nextInt();
			if((n|m) == 0) break;
			int [] data = new int[n];
			for(int i = 0; i < n; i++){
				data[i] = sc.nextInt();
			}
			ArrayList<Integer> list = new ArrayList<Integer>();
			for(int i = 0; i < (1 << n); i++){
				int sum = 0;
				for(int j = 0; j < n; j++){
					if((i & (1 << j)) == 0) continue;
					sum += data[j];
				}
				list.add(sum);
			}
			Collections.sort(list);
			int INF = 1 << 24;
			int [] dp = new int[m + 1];
			Arrays.fill(dp, INF);
			dp[0] = 0;
			for(int i = 0; i < m; i++){
				if(dp[i] == INF) continue;
				for(int j = 0; j < list.size(); j++){
					int nextind = i + list.get(j);
					if(nextind > m) break;
					int value = dp[i] + 1;
					dp[nextind] = Math.min(dp[nextind], value);
				}
			}
			System.out.println(dp[m]);
		}
	}
	
	

	public static void main(String [] args){
		new Main().doit();
	}
}