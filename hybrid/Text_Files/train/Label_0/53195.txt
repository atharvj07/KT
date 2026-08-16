import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

//Compress Files
public class Main{

	int INF = 1<<29;
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt(), m = sc.nextInt();
			if((n|m)==0)break;
			int[] a = new int[n], b = new int[n];
			for(int i=0;i<n;i++){
				b[i] = sc.nextInt(); a[i] = sc.nextInt();
			}
			int[] dp = new int[1<<n];
			Arrays.fill(dp, INF);
			dp[(1<<n)-1] = 0;
			List<Integer> l = new ArrayList<Integer>();
			l.add((1<<n)-1);
			while(!l.isEmpty()&&dp[0]==INF){
				List<Integer> next = new ArrayList<Integer>();
				for(int S:l){
					int e = m, s = (S-1)&S;
					for(int k=0;k<n;k++)if(((S>>k)&1)==0)e+=b[k]-a[k];
					while(s!=S){
						if(dp[s]==INF){
							int r = 0;
							for(int k=0;k<n;k++)if(((S>>k)&1)>0&&((s>>k)&1)==0)r+=a[k];
							if(r<=e){
								dp[s] = dp[S]+1; next.add(s);
							}
						}
						s = (s-1)&S;
					}
				}
				l = next;
			}
			System.out.println(dp[0]==INF?"Impossible":dp[0]);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}