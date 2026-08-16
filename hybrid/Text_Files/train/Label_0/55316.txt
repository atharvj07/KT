import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class CodeSegment
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
	
	static class Nodo
	{
		int a;
		int b;
		int valor;
		int proximoEvento;
		int acumulado;
		int numeroLuckys;
		Nodo izquierdo;
		Nodo derecho;
		
		int darProximoEvento()
		{
			return proximoEvento - acumulado;
		}
		
		void actualizar()
		{
			if(a == b)
			{
				int l = siguienteLucky(valor);
				proximoEvento = l - valor;
				numeroLuckys = proximoEvento == 0 ? 1 : 0;
				acumulado = 0;
			}
			else
			{
				proximoEvento = Math.min(izquierdo.darProximoEvento(), derecho.darProximoEvento());
				numeroLuckys = izquierdo.numeroLuckys + derecho.numeroLuckys;
			}
		}
		
		Nodo(int i, int d, int[] iniciales)
		{
			a = i;
			b = d;
			acumulado = 0;
			if(a == b)
			{
				valor = iniciales[i];
				actualizar();
			}
			else
			{
				izquierdo = new Nodo(a, (a + b) / 2, iniciales);
				derecho = new Nodo((a + b) / 2 + 1, b, iniciales);
				actualizar();
			}
		}
		
		void update(int i, int j, int delta)
		{
			if(i > b || j < a)
				return;
			if(a >= i && a <= j && b <= j)
			{
				if(a == b)
				{
					valor += delta;
					actualizar();
				}
				else if(delta < darProximoEvento())
					acumulado += delta;
				else
				{
					izquierdo.update(i, j, delta + acumulado);
					derecho.update(i, j, delta + acumulado);
					acumulado = 0;
					actualizar();
				}
			}
			else
			{
				if(acumulado != 0)
				{
					izquierdo.update(izquierdo.a, izquierdo.b, acumulado);
					derecho.update(derecho.a, derecho.b, acumulado);
					acumulado = 0;
				}
				izquierdo.update(i, j, delta);
				derecho.update(i, j, delta);
				actualizar();
			}
		}
		
		int query(int i, int j)
		{
			if(i > b || j < a)
				return 0;
			if(a >= i && a <= j && b <= j)
				return numeroLuckys;
			else
				return izquierdo.query(i, j) + derecho.query(i, j);
		}
	}
	
	
	static Integer[] luckys = new Integer[44445];
	
	static boolean esLucky(int v)
	{
		for(char c : (v + "").toCharArray())
			if(c != '4' && c != '7')
				return false;
		return true;
	}
	static void llenarLuckys()
	{
		int luckyAnterior = -1;
		for(int i = luckys.length - 1; i >= 0; i--)
		{
			if(esLucky(i))
				luckyAnterior = i;
			luckys[i] = luckyAnterior;
		}
	}
	static int siguienteLucky(int v)
	{
		return luckys[v];
	}

	public static void main(String[] args)
	{
		llenarLuckys();
		Scanner sc = new Scanner();
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] iniciales = sc.nextIntArray(n);
		Nodo raiz = new Nodo(0, n - 1, iniciales);
		for(int q = 0; q < m; q++)
		{
			String orden = sc.next();
			if(orden.charAt(0) == 'c')
			{
				int a = sc.nextInt() - 1;
				int b = sc.nextInt() - 1;
				System.out.println(raiz.query(a, b));
			}
			else
			{
				int a = sc.nextInt() - 1;
				int b = sc.nextInt() - 1;
				int delta = sc.nextInt();
				raiz.update(a, b, delta);
			}
		}
	}
}
