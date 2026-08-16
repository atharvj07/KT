import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class CodeG 
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
	
	static final int limite = 1000000000;
	
	static ArrayList <Long> luckys = new ArrayList <Long> ();
	
	static void generarLuckys(String acum)
	{
		if(acum.length() == 0 || Long.parseLong(acum) <= limite)
		{
			if(acum.length() != 0)
				luckys.add(Long.parseLong(acum));
			generarLuckys(acum + '4');
			generarLuckys(acum + '7');
		}
	}
	
	static long contar(int indiceA, int k, int pl, int pr, int vl, int vr)
	{
		if(indiceA + k - 1 >= luckys.size())
			return 0;
		long primero = luckys.get(indiceA);
		long segundo = luckys.get(indiceA + k - 1);
		long primeroAnt = indiceA == 0 ? 0L : luckys.get(indiceA - 1) + 1;
		long segundoSig = indiceA + k >= luckys.size() ? Integer.MAX_VALUE : luckys.get(indiceA + k) - 1;
		return cuantosHay(primeroAnt, primero, pl, pr) * cuantosHay(segundo, segundoSig, vl, vr) + cuantosHay(primeroAnt, primero, vl, vr) * cuantosHay(segundo, segundoSig, pl, pr);
	}
	
	private static long cuantosHay(long a, long b, long pl, long pr) 
	{
		long limiteSup = Math.min(b, pr);
		long limiteInf = Math.max(a, pl);
		if(limiteSup >= limiteInf)
			return limiteSup - limiteInf + 1;
		else
			return 0L;
	}

	public static void main(String[] args)
	{
		Scanner sc = new Scanner();
		generarLuckys("");
		Collections.sort(luckys);
		int pl = sc.nextInt();
		int pr = sc.nextInt();
		int vl = sc.nextInt();
		int vr = sc.nextInt();
		int k = sc.nextInt();
		long cuantos = 0;
		long cuantosTotal = ((long) ((pr - pl + 1))) * (vr - vl + 1);
		for(int i = 0; i < luckys.size(); i++)
			cuantos += contar(i, k, pl, pr, vl, vr);
		for(long l : luckys)
		{
			if(cuantosHay(l, l, pl, pr) == 1 && cuantosHay(l, l, vl, vr) == 1 && k == 1)
				cuantos--;
		}
		System.out.println((cuantos + 0.0d) / cuantosTotal);
		
	}
}