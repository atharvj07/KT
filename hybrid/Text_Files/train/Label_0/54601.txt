import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		HashSet<String> hs = new HashSet<>();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			long K = sc.nextLong();
			long N = sc.nextLong();
			long a = sc.nextLong();
			long b = sc.nextLong();
			
			long res = -1;
			long l = 0, h = 2 * N, mid;
			while(l <= h)
			{
				mid = (l + h) / 2;
				if(mid > N) 
				{
					h = mid - 1;
					continue;
				}
				long num = a * mid;
				
				if(K - num > b * (N - mid))
				{
					res = mid;
					l = mid + 1;
				}
				else h = mid - 1;
			}
			System.out.println(res);
		}
	}
}