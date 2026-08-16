import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class CodeJ 
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
	
	static int nFilas;
	static int nColumnas;

	static byte[][][][][] dp;
	
	static byte dp(int mascaraActual, int enviadosActual, int enviadosSiguiente, int filaActual, int columnaActual)
	{
		if(dp[mascaraActual][enviadosActual][enviadosSiguiente][filaActual][columnaActual] != Byte.MAX_VALUE)
			return dp[mascaraActual][enviadosActual][enviadosSiguiente][filaActual][columnaActual];
		if(filaActual == nFilas)
			return dp[mascaraActual][enviadosActual][enviadosSiguiente][filaActual][columnaActual] = 0;
		if(columnaActual == nColumnas)
		{
			int ambos = mascaraActual & enviadosSiguiente;
			int mascaraSiguiente = (1 << nColumnas) - 1;
			mascaraSiguiente ^= ambos;
			int mascaraEnviados = enviadosSiguiente;
			mascaraEnviados ^= ambos;
			return dp[mascaraActual][enviadosActual][enviadosSiguiente][filaActual][columnaActual] = (byte) (nColumnas - Integer.bitCount(mascaraActual) + dp(mascaraSiguiente, mascaraEnviados, 0, filaActual + 1, 0));
		}
		if(((mascaraActual & (1 << columnaActual)) == 0))
		{
			// me envian desde abajo
			byte a = dp(mascaraActual | (1 << columnaActual), enviadosActual, enviadosSiguiente | (1 << columnaActual), filaActual, columnaActual + 1);
			// normal
			byte b = dp(mascaraActual, enviadosActual, enviadosSiguiente, filaActual, columnaActual + 1);
			return dp[mascaraActual][enviadosActual][enviadosSiguiente][filaActual][columnaActual] = (byte) Math.max(a, b);
		}
		if((enviadosActual & (1 << columnaActual)) != 0)
		{
			byte a = dp(mascaraActual, enviadosActual, enviadosSiguiente | (1 << columnaActual), filaActual, columnaActual + 1);
			byte b = dp(mascaraActual, enviadosActual, enviadosSiguiente, filaActual, columnaActual + 1);
			return dp[mascaraActual][enviadosActual][enviadosSiguiente][filaActual][columnaActual] = (byte) Math.max(a, b);
		}
		// izquierda
		byte ans = 0;
		if(columnaActual != 0)
			ans = (byte) Math.max(ans, dp((mascaraActual ^ (1 << columnaActual)) | (1 << (columnaActual - 1)), enviadosActual, enviadosSiguiente, filaActual, columnaActual + 1));
		// derecha
		if(columnaActual != nColumnas - 1)	
			ans = (byte) Math.max(ans, dp((mascaraActual ^ (1 << columnaActual)) | (1 << (columnaActual + 1)), enviadosActual | (1 << (columnaActual + 1)), enviadosSiguiente, filaActual, columnaActual + 1));
		// abajo
		if(filaActual != nFilas - 1)
			ans = (byte) Math.max(ans, dp((mascaraActual ^ (1 << columnaActual)), enviadosActual, enviadosSiguiente | (1 << columnaActual), filaActual, columnaActual + 1));
		// quieto
		ans = (byte) Math.max(ans, dp(mascaraActual, enviadosActual, enviadosSiguiente, filaActual, columnaActual + 1));
		return dp[mascaraActual][enviadosActual][enviadosSiguiente][filaActual][columnaActual] = ans;
	}
	
	public static void main(String[] args)
	{
		Scanner sc = new Scanner();
		int a = sc.nextInt();
		int b = sc.nextInt();
		nFilas = Math.max(a, b);
		nColumnas = Math.min(a, b);
		dp = new byte[1 << nColumnas][1 << nColumnas][1 << nColumnas][nFilas + 1][nColumnas + 1];
		for(byte[][][][] i : dp)
			for(byte[][][] j : i)
				for(byte[][] k : j)
					for(byte[] l : k)
						Arrays.fill(l, Byte.MAX_VALUE);
		System.out.println(dp((1 << nColumnas) - 1, 0, 0, 0, 0));
	}
}