import java.util.*;

public class Q4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long a[] = new long[n];
		int pos = 0 , neg = 0;
		Stack<Long> stk = new Stack<Long>();
		long sum = 0;
		
		for(int i=0;i<n;i++) {
			a[i] = sc.nextLong();
			if(a[i] >= 0)
				pos++;
			if(a[i] < 0)
				neg++;
			sum += Math.abs(a[i]);
		}
		if(n == 1)
			System.out.println(a[0]);
		else if(pos !=0  &&  neg != 0)
			System.out.println(sum);
		else {
			long min = Integer.MAX_VALUE;
			for(int i=0;i<n;i++)
				min = Math.min(min ,  Math.abs(a[i]));
			
			long ans = sum - (long)(2*min);
			System.out.println(ans);
		}
	}
}
