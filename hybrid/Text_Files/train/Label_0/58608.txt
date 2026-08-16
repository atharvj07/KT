import java.util.ArrayList;
import java.util.Scanner;

public class Main 
{
	static int MAX = 222220;
	static boolean[] sieve = new boolean[MAX+1];
	static int[] primes = new int[5637];
	
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		sieve[0] = true;
		sieve[1] = true;
		for(long i = 2; i <= MAX; i++)
		{
			if(!sieve[(int)i])
				for(long j = i*i; j <= MAX; j+=i)
				{
					sieve[(int)j] = true;
				}
		}
		int f = 55555;
		int pr = 0;
		for(int i = 2; i <= f; i++)
		{
			if(pr >=5637)break;
			if(!sieve[i])
			{
				primes[pr] = i;
				pr++;
			}
		}
//		System.out.println(Arrays.toString(primes));
//		System.out.println(pr);
		
		ArrayList<Integer> l = new ArrayList<>();
		
		StringBuilder sb = new StringBuilder();
		int cur = 0;
		while(l.size()<n)
		{
			long curp = primes[cur];
			while(primes[cur]%5!=1)cur++;
			curp = primes[cur];
			l.add(primes[cur]);
			if(l.size()>1)sb.append(' ');
			sb.append(primes[cur]);
			cur++;
		}
		
		System.out.println(sb);
			
	}

}
