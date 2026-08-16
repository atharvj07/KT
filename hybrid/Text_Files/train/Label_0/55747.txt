import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;


public class CodeC 
{
	static class Scanner
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer("");
		
		public String nextLine()
		{
			try
			{
				return br.readLine();
			}
			catch(Exception e)
			{
				throw(new RuntimeException());
			}
		}
		
		public String next()
		{
			while(!st.hasMoreTokens())
			{
				String l = nextLine();
				if(l == null)
					return null;
				st = new StringTokenizer(l);
			}
			return st.nextToken();
		}
		
		public int nextInt()
		{
			return Integer.parseInt(next());
		}
		
		public long nextLong()
		{
			return Long.parseLong(next());
		}
		
		public double nextDouble()
		{
			return Double.parseDouble(next());
		}
		
		public int[] nextIntArray(int n)
		{
			int[] res = new int[n];
			for(int i = 0; i < res.length; i++)
				res[i] = nextInt();
			return res;
		}
		
		public long[] nextLongArray(int n)
		{
			long[] res = new long[n];
			for(int i = 0; i < res.length; i++)
				res[i] = nextLong();
			return res;
		}
		
		public double[] nextDoubleArray(int n)
		{
			double[] res = new double[n];
			for(int i = 0; i < res.length; i++)
				res[i] = nextLong();
			return res;
		}
		
		public String[] nextStringArray(int n)
		{
			String[] res = new String[n];
			for(int i = 0; i < res.length; i++)
				res[i] = next();
			return res;
		}
		public void sortIntArray(int[] array)
		{
			Integer[] vals = new Integer[array.length];
			for(int i = 0; i < array.length; i++)
				vals[i] = array[i];
			Arrays.sort(vals);
			for(int i = 0; i < array.length; i++)
				array[i] = vals[i];
		}
		
		public void sortLongArray(long[] array)
		{
			Long[] vals = new Long[array.length];
			for(int i = 0; i < array.length; i++)
				vals[i] = array[i];
			Arrays.sort(vals);
			for(int i = 0; i < array.length; i++)
				array[i] = vals[i];
		}
		
		public void sortDoubleArray(double[] array)
		{
			Double[] vals = new Double[array.length];
			for(int i = 0; i < array.length; i++)
				vals[i] = array[i];
			Arrays.sort(vals);
			for(int i = 0; i < array.length; i++)
				array[i] = vals[i];
		}
	}
	
	static BigInteger two = BigInteger.ONE.add(BigInteger.ONE);
	static long mod = 1000000007;
	static BigInteger modulo = BigInteger.valueOf(mod);
	
	
	
	static long[] factorial;
	
	static void calcularFactorial()
	{
		factorial = new long[1010];
		factorial[0] = 1;
		for(int i = 1; i < 1010; i++)
			factorial[i] = (factorial[i - 1] * i) % mod;
	}
	
	static long combinatoria(int n, int k)
	{
		long res = factorial[n];
		res *= BigInteger.valueOf(factorial[k]).modInverse(modulo).longValue();
		res %= mod;
		res *= BigInteger.valueOf(factorial[n - k]).modInverse(modulo).longValue();
		res %= mod;
		return res;
	}
	
	public static void main(String[] args)
	{
		calcularFactorial();
		Scanner sc = new Scanner();
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] prendidas = sc.nextIntArray(m);
		sc.sortIntArray(prendidas);
		ArrayList <Integer> gapsDobles = new ArrayList <Integer> ();
		ArrayList <Integer> gapsSencillos = new ArrayList <Integer> ();
		if(prendidas[0] - 1 != 0)
			gapsSencillos.add(prendidas[0] - 1);
		if(n - prendidas[m - 1] != 0)
			gapsSencillos.add(n - prendidas[m - 1]);
		for(int i = 1; i < m; i++)
		{
			int gap = prendidas[i] - prendidas[i - 1] - 1;
			if(gap != 0)
				gapsDobles.add(gap);
		}
		int totalPoner = 0;
		for(int i : gapsSencillos)
			totalPoner += i;
		for(int i : gapsDobles)
			totalPoner += i;
		long acum = 1;
		for(int i : gapsDobles)
		{
			long res = combinatoria(totalPoner, i) % mod;
			res *= two.modPow(BigInteger.valueOf(i - 1), modulo).longValue() % mod;
			res %= mod;
			acum *= res;
			acum %= mod;
			totalPoner -= i;
		}
		for(int i : gapsSencillos)
		{
			long res = combinatoria(totalPoner, i) % mod;
			acum *= res;
			acum %= mod;
			totalPoner -= i;
		}
		System.out.println(acum);
	}

}
