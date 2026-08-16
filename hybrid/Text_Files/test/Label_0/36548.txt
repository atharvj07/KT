import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class CodeB 
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
		ArrayList <Arista> aristas = new ArrayList <Arista> ();
		ArrayList <Integer> subArboles = new ArrayList <Integer> ();
		int totalParcial = 0;
		boolean termino = false;
		
		ArrayList <Integer> subArbolesMejor = new ArrayList <Integer> ();
		Integer mejorPrimero;
		Integer mejorSegundo;
		boolean terminoMejor = false;
		
		
		void procesarMejor(int valor)
		{
			if(mejorPrimero == null)
				mejorPrimero = valor;
			else if(mejorSegundo == null)
			{
				if(valor < mejorPrimero)
				{
					mejorSegundo = mejorPrimero;
					mejorPrimero = valor;
				}
				else
					mejorSegundo = valor;
			}
			else
			{
				if(valor < mejorPrimero)
				{
					mejorSegundo = mejorPrimero;
					mejorPrimero = valor;
				}
				else if(valor < mejorSegundo)
					mejorSegundo = valor;
			}
		}
		
		int calcularMejorEscogida(int idPadre)
		{
			if(subArbolesMejor.isEmpty())
			{
				procesarMejor(calcularCostoSubArbol(-1));
				for(int i = 0; i < aristas.size(); i++)
					subArbolesMejor.add(null);
				for(int i = 0; i < aristas.size(); i++)
				{
					if(i == idPadre)
						continue;
					Arista actual = aristas.get(i);
					subArbolesMejor.set(i, actual.otro.calcularMejorEscogida(actual.idOpuesto));
					procesarMejor(subArbolesMejor.get(i));
				}
				return mejorPrimero;
			}
			else
			{
				if(idPadre >= 0 && subArbolesMejor.get(idPadre) == null)
					return mejorPrimero;
				if(!terminoMejor)
				{
					for(int i = 0; i < aristas.size(); i++)
					{
						if(subArbolesMejor.get(i) == null)
						{
							Arista actual = aristas.get(i);
							subArbolesMejor.set(i, actual.otro.calcularMejorEscogida(actual.idOpuesto));
							procesarMejor(subArbolesMejor.get(i));
						}
					}
					terminoMejor = true;
				}
				return subArbolesMejor.get(idPadre).intValue() == mejorPrimero.intValue() ? mejorSegundo : mejorPrimero;
			}
		}
		
		int calcularCostoSubArbol(int idArista)
		{
			if(subArboles.isEmpty())
			{
				for(int i = 0; i < aristas.size(); i++)
					subArboles.add(null);
				for(int i = 0; i < aristas.size(); i++)
				{
					if(i == idArista)
						continue;
					Arista actual = aristas.get(i);
					subArboles.set(i, (actual.invertida ? 1 : 0) + actual.otro.calcularCostoSubArbol(actual.idOpuesto));
					totalParcial += subArboles.get(i);
				}
				return totalParcial;
			}
			else
			{
				if(idArista >= 0 && subArboles.get(idArista) == null)
					return totalParcial;
				if(!termino)
				{
					for(int i = 0; i < aristas.size(); i++)
					{
						if(subArboles.get(i) == null)
						{
							Arista actual = aristas.get(i);
							subArboles.set(i, (actual.invertida ? 1 : 0) + actual.otro.calcularCostoSubArbol(actual.idOpuesto));
							totalParcial += subArboles.get(i);
						}
					}
					termino = true;
				}
				return totalParcial - (idArista < 0 ? 0 : subArboles.get(idArista));
			}
		}

		int calcularSolucion()
		{
			if(aristas.size() <= 1)
				return Integer.MAX_VALUE;
			class Entrada implements Comparable <Entrada>
			{
				int costo;
				int ahorro;
				int escogiendo;
				boolean opuesta;
				
				@Override
				public int compareTo(Entrada o) 
				{
					if(ahorro == o.ahorro)
					{
						if(opuesta == o.opuesta)
							return 0;
						else if(!opuesta)
							return -1;
						else
							return 1;
					}
					return o.ahorro - ahorro;
				}
			}
			Entrada mejorUno = null;
			Entrada mejorDos = null;
			int totalCostos = 0;
			int id = 0;
			for(Arista a : aristas)
			{
				Entrada nueva = new Entrada();
				nueva.costo = (a.invertida ? 1 : 0) + a.otro.calcularCostoSubArbol(a.idOpuesto);
				nueva.escogiendo = a.otro.calcularMejorEscogida(a.idOpuesto) - calcularCostoSubArbol(id);
				nueva.ahorro = nueva.costo - nueva.escogiendo;
				nueva.opuesta = a.invertida;
				totalCostos += nueva.costo;
				if(mejorUno == null)
					mejorUno = nueva;
				else if(mejorDos == null)
				{
					if(nueva.compareTo(mejorUno) < 0)
					{
						mejorDos = mejorUno;
						mejorUno = nueva;
					}
					else
						mejorDos = nueva;
				}
				else
				{
					if(nueva.compareTo(mejorUno) < 0)
					{
						mejorDos = mejorUno;
						mejorUno = nueva;
					}
					else if(nueva.compareTo(mejorDos) < 0)
						mejorDos = nueva;
				}
				id++;
			}
			totalCostos -= mejorUno.ahorro;
			totalCostos -= mejorDos.ahorro;
			if(!mejorUno.opuesta || !mejorDos.opuesta)
				totalCostos--;
			return totalCostos;
		}
	}
	
	static class Arista
	{
		Nodo otro;
		boolean invertida;
		int idOpuesto;
		
		public Arista(Nodo o, boolean in, int id)
		{
			otro = o;
			invertida = in;
			idOpuesto = id;
		}
	}
	
	static Nodo[] nodos;
	
	static void agregarArista(int a, int b)
	{
		int idA = nodos[a].aristas.size();
		int idB = nodos[b].aristas.size();
		nodos[a].aristas.add(new Arista(nodos[b], false, idB));
		nodos[b].aristas.add(new Arista(nodos[a], true, idA));
	}
	
	public static void main(String[] args)
	{
		Scanner sc = new Scanner();
		int n = sc.nextInt();
		nodos = new Nodo[n];
		for(int i = 0; i < n; i++)
			nodos[i] = new Nodo();
		for(int i = 0; i < n - 1; i++)
			agregarArista(sc.nextInt() - 1, sc.nextInt() - 1);
		int mejor = Integer.MAX_VALUE;
		for(int i = 0; i < n; i++)
			mejor = Math.min(mejor, nodos[i].calcularSolucion());
		System.out.println(mejor == Integer.MAX_VALUE ? 0 : mejor);
	}
}