import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;


public class CodeA 
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
	
	
	static void generarSolucion(String entradaS) throws IOException
	{
		entradaS = "000" + entradaS;
		char[] entrada = new StringBuilder(entradaS).reverse().toString().toCharArray();
		int estado = 0;
		int indiceS1 = 0;
		int indiceS2 = 0;
		char[] operaciones = new char[entradaS.length() + 3];
		Arrays.fill(operaciones, '.');
		for(int actual = 0; actual < entrada.length; actual++)
		{
			if(estado == 0)
			{
				if(entrada[actual] == '0')
					continue;
				else
				{
					estado = 1;
					indiceS1 = actual;
				}
			}
			else if(estado == 1)
			{
				if(entrada[actual] == '0')
				{
					operaciones[indiceS1] = '+';
					estado = 0;
				}
				else
				{
					estado = 2;
					indiceS2 = actual;
				}
			}
			else if(estado == 2)
			{
				if(entrada[actual] == '0')
				{
					estado = 3;
					operaciones[actual] = '-';
				}
				else
					indiceS2 = actual;
			}
			else
			{
				if(entrada[actual] == '0')
				{
					estado = 0;
					operaciones[actual - 1] = '.';
					operaciones[indiceS2 + 1] = '+';
					operaciones[indiceS1] = '-';
				}
				else
				{
					indiceS2 = actual;
					estado = 2;
				}
			}
		}
		ArrayList <String> salida = new ArrayList <String> ();
		for(int i = 0; i < operaciones.length; i++)
		{
			if(operaciones[i] == '+')
				salida.add("+2^" + i);
			else if(operaciones[i] == '-')
				salida.add("-2^" + i);
		}
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(salida.size() + "\n");
		for(String s : salida)
		{
			bw.write(s);
			bw.write('\n');
		}
		bw.flush();
		bw.close();
	}
	
	public static void main(String[] args) throws IOException
	{
		Scanner sc = new Scanner();
		generarSolucion(sc.nextLine());
	}

}
