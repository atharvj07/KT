import java.util.*;
public class Main {
	Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}

	public Main(){
		new AOJ0260().doIt();
	}
	
	class AOJ0260{
		long n;
		long[] p,j;
		void solve(){
			Arrays.sort(j);
//			System.out.println(Arrays.toString(j));
			long sum = 0;
			long cnt = n;
			for(int i=0;i<n;i++)sum+=p[i];
			long max = sum*cnt;
			for(int i=(int)n-2;i>=0;i--){
//				System.out.println(sum+" "+cnt+" "+max);
				sum = sum+j[i];
				cnt--;
				long calc = sum*cnt;
//				System.out.println(calc);
				max = Math.max(max, calc);
			}
			System.out.println(max);
		}
		
		void doIt(){
			while(in.hasNext()){
				n = in.nextInt();
				if(n==0)break;
				p = new long[(int)n];
				j = new long[(int)(n-1)];
				for(int i=0;i<n;i++)p[i] = in.nextInt();
				for(int i=0;i<n-1;i++)j[i] = in.nextInt();
				solve();
			}
		}
	}
	
}