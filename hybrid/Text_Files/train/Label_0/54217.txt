import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Constructor;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.StringTokenizer;

public class CodeF 
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
				res[i] = nextDouble();
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

		public String[] nextStringArray(int n) 
		{	
			String[] vals = new String[n];
			for(int i = 0; i < n; i++)
				vals[i] = next();
			return vals;
		}
		
		public Integer nextInteger()
		{
			String s = next();
			if(s == null)
				return null;
			return Integer.parseInt(s);
		}
		
		public int[][] nextIntMatrix(int n, int m)
		{
			int[][] ans = new int[n][];
			for(int i = 0; i < n; i++)
				ans[i] = nextIntArray(m);
			return ans;
		}
		
		public char[][] nextGrid(int r) 
		{
			char[][] grid = new char[r][];
			for(int i = 0; i < r; i++)
				grid[i] = next().toCharArray();
			return grid;
		}
		
		public static <T> T fill(T arreglo, int val)
		{
			if(arreglo instanceof Object[])
			{
				Object[] a = (Object[]) arreglo;
				for(Object x : a)
					fill(x, val);
			}
			else if(arreglo instanceof int[])
				Arrays.fill((int[]) arreglo, val);
			else if(arreglo instanceof double[])
				Arrays.fill((double[]) arreglo, val);
			else if(arreglo instanceof long[])
				Arrays.fill((long[]) arreglo, val);
			return arreglo;
		}
		
		<T> T[] nextObjectArray(Class <T> clazz, int size)
		{
			@SuppressWarnings("unchecked")
			T[] result = (T[]) java.lang.reflect.Array.newInstance(clazz, size);
			for(int c = 0; c < 3; c++)
			{
				Constructor <T> constructor;
				try 
				{
					if(c == 0)
						constructor = clazz.getDeclaredConstructor(Scanner.class, Integer.TYPE);
					else if(c == 1)
						constructor = clazz.getDeclaredConstructor(Scanner.class);
					else
						constructor = clazz.getDeclaredConstructor();
				} 
				catch(Exception e)
				{
					continue;
				}
				try
				{
					for(int i = 0; i < result.length; i++)
					{
						if(c == 0)
							result[i] = constructor.newInstance(this, i);
						else if(c == 1)
							result[i] = constructor.newInstance(this);
						else
							result[i] = constructor.newInstance();	
					}
				}
				catch(Exception e)
				{
					throw new RuntimeException(e);
				}
				return result;
			}
			throw new RuntimeException("Constructor not found");
		}
		
		public void printLine(int... vals)
		{
			if(vals.length == 0)
				System.out.println();
			else
			{
				System.out.print(vals[0]);
				for(int i = 1; i < vals.length; i++)
					System.out.print(" ".concat(String.valueOf(vals[i])));
				System.out.println();
			}
		}
		
		public void printLine(long... vals)
		{
			if(vals.length == 0)
				System.out.println();
			else
			{
				System.out.print(vals[0]);
				for(int i = 1; i < vals.length; i++)
					System.out.print(" ".concat(String.valueOf(vals[i])));
				System.out.println();
			}
		}
		
		public void printLine(double... vals)
		{
			if(vals.length == 0)
				System.out.println();
			else
			{
				System.out.print(vals[0]);
				for(int i = 1; i < vals.length; i++)
					System.out.print(" ".concat(String.valueOf(vals[i])));
				System.out.println();
			}
		}
		
		public void printLine(int prec, double... vals)
		{
			if(vals.length == 0)
				System.out.println();
			else
			{
				System.out.printf("%." + prec + "f", vals[0]);
				for(int i = 1; i < vals.length; i++)
					System.out.printf(" %." + prec + "f", vals[i]);
				System.out.println();
			}
		}
		
		public Collection <Integer> wrap(int[] as)
		{
			ArrayList <Integer> ans = new ArrayList <Integer> ();
			for(int i : as)
				ans.add(i);
			return ans;
		}
		
		public int[] unwrap(Collection <Integer> collection)
		{
			int[] vals = new int[collection.size()];
			int index = 0;
			for(int i : collection) vals[index++] = i;
			return vals;
		}
	}
	
	public static class Fenwick
	{
		long[] fenwickTree;
		int tam;
		
		public Fenwick(int t)
		{
			fenwickTree = new long[t];
			tam = t;
		}
		
		long query(int a, int b) 
		{
		    if (a == 0)
		    {
		        long sum = 0;
		        for (; b >= 0; b = (b & (b + 1)) - 1)
		          sum += fenwickTree[b];
		        return sum;
		    } 
		    else 
		    {
		        return (query(0, b) - query(0, a - 1));
		    }
		}
	
		void increase(int k, long inc)
		{
		    for (; k < tam; k |= k + 1)
		        fenwickTree[k] += inc;
		}
		
		void increaseRange(int a, int b, long val)
		{
			increase(a, val);
			increase(b + 1, -val);
		}
		
		long queryRangePoint(int a)
		{
			return query(0, a);
		}
	}
	
	static class Query
	{
		int from;
		int to;
		int answer = 0;
		
		public Query(Scanner sc)
		{
			from = sc.nextInt() - 1;
			to = sc.nextInt() - 1;
		}
	}
	
	static class EfficientSortedQueries
	{
		static final Query[] emptyArray = new Query[0];
		Query[][] map = new Query[array.length][];
		int[] count = new int[array.length];
		
		Query[] getAt(int index)
		{
			return map[index];
		}
		
		void addQuery(int index, Query query)
		{
			map[index][--count[index]] = query;
		}
		
		void addCount(int index)
		{
			count[index]++;
		}
		
		void prepareCount()
		{
			for(int i = 0; i < map.length; i++)
				map[i] = new Query[count[i]];
		}
	}
	
	static class Number
	{
		int first = -1;
		int second = -1;
		int last = -1;
		int outside = -1;
		
		int addRight(int index)
		{
			boolean wasGood = outside == 0;
			if(first == -1)
			{
				first = index;
				last = index;
				second = -1;
				outside = 0;
			}
			else if(second == -1)
			{
				second = first;
				first = index;
				last = second;
				outside = 0;
			}
			else
			{
				int difference = first - second;
				if(index - first == difference)
				{
					second = first;
					first = index;
				}
				else
				{
					int count = (first - last) / difference;
					outside = count;
					second = last = first;
					first = index;
				}
			}
			boolean isGood = outside == 0;
			if(wasGood && isGood) return 0;
			else if(wasGood && !isGood) return -1;
			else if(!wasGood && isGood) return 1;
			else return 0;
		}
		
		int removeLeft(int index)
		{
			boolean wasGood = outside == 0;
			if(index == first)
				first = second = last = outside = -1;
			else if(index == second)
			{
				last = first;
				second = -1;
				outside = 0;
			}
			else if(index == last)
			{
				int difference = first - second;
				last += difference;
			}
			else
				outside--;
			boolean isGood = outside == 0;
			if(wasGood && isGood) return 0;
			else if(wasGood && !isGood) return -1;
			else if(!wasGood && isGood) return 1;
			else return 0;
		}
		
		int addLeft(int index)
		{
			boolean wasGood = outside == 0;
			if(first == -1)
			{
				first = last = index;
				second = -1;
				outside = 0;
			}
			else if(outside > 0)
				outside++;
			else if(second == -1)
			{
				second = last = index;
				outside = 0;
			}
			else
			{
				int difference = first - second;
				if(index == last - difference)
					last -= difference;
				else
					outside++;
			}
			boolean isGood = outside == 0;
			if(wasGood && isGood) return 0;
			else if(wasGood && !isGood) return -1;
			else if(!wasGood && isGood) return 1;
			else return 0;
		}

		public void clear()
		{
			first = -1;
			second = -1;
			last = -1;
			outside = -1;
		}
	}
	
	static int[] array;
	
	static class NumberSegmentEfficient
	{
		Number[] numbers = new Number[100000];
		int left, right, count = 0;
		
		NumberSegmentEfficient(int start)
		{
			left = start;
			right = start - 1;
			for(int i = 0; i < numbers.length; i++)
				numbers[i] = new Number();
			addRight();
		}
		
		void removeLeft()
		{
			Number affected = numbers[array[left]];
			count += affected.removeLeft(left);
			left++;
		}
		
		void addLeft()
		{
			int next = left - 1;
			Number affected = numbers[array[next]];
			count += affected.addLeft(next);
			left = next;
		}
		
		void addRight()
		{
			int next = right + 1;
			Number affected = numbers[array[next]];
			count += affected.addRight(next);
			right = next;
		}
		
		boolean isArithmetic()
		{
			return count > 0;
		}

		public void clear(int start) 
		{
			for(int i = 0; i < numbers.length; i++)
				numbers[i].clear();
			count = 0;
			left = start;
			right = start - 1;
			addRight();
		}
		
		public void clear(int start, int from, int to)
		{
			for(int i = from; i <= to; i++)
				numbers[array[i]].clear();
			count = 0;
			left = start;
			right = start - 1;
			addRight();
		}
	}
	
	static boolean solveManual(int from, int to, NumberSegmentEfficient segment)
	{
		while(segment.left != from)
			segment.addLeft();
		return segment.isArithmetic();
	}
	
	static void solveQueryManual(Query q, NumberSegmentEfficient segment)
	{
		if(!solveManual(q.from, q.to, segment))
			q.answer++;
	}

	static void solveQuery(Query query, NumberSegmentEfficient segment)
	{
		int startingIndex = segment.left;
		while(segment.left != query.from)
			segment.addLeft();
		if(!segment.isArithmetic())
			query.answer++;
		while(segment.left != startingIndex)
			segment.removeLeft();
	}
	
	static Query[] allQueries;
	
	static void solveInitial()
	{
		for(int i = 0; i < array.length; i++)
			array[i]--;
		EfficientSortedQueries hash = new EfficientSortedQueries();
		for(Query q : allQueries)
			hash.addCount(q.to);
		hash.prepareCount();
		for(Query q : allQueries)
			hash.addQuery(q.to, q);
		Fenwick fenwick = new Fenwick(array.length);
		int[] last = new int[100000];
		Arrays.fill(last, -1);
		for(int i = 0; i < array.length; i++)
		{
			int current = array[i];
			if(last[current] == -1)
			{
				last[current] = i;
				fenwick.increase(i, 1);
			}
			else
			{
				fenwick.increase(last[current], -1);
				fenwick.increase(i, 1);
				last[current] = i;
			}
			for(Query q : hash.getAt(i))
				q.answer = (int) fenwick.query(q.from, i);
		}
	}
	
	static void solveEfficient()
	{
		solveInitial();
		EfficientSortedQueries startingQueries = new EfficientSortedQueries();
		for(Query q : allQueries)
			startingQueries.addCount(q.from);
		startingQueries.prepareCount();
		for(Query q : allQueries)
			startingQueries.addQuery(q.from, q);
		EfficientSortedQueries endingQueries = new EfficientSortedQueries();
		for(int j = 0; j < array.length; j++)
			for(Query q : startingQueries.getAt(j))
				endingQueries.addCount(q.to);
		endingQueries.prepareCount();
		for(int j = 0; j < array.length; j++)
			for(Query q : startingQueries.getAt(j))
				endingQueries.addQuery(q.to, q);
		NumberSegmentEfficient segment = new NumberSegmentEfficient(0);
		for(int i = 0; i < array.length; i += 316)
		{
			int last = i + 316 - 1;
			last = Math.min(last, array.length - 1);
			for(int j = i; j <= last; j++)
				for(Query q : endingQueries.getAt(j))
					if(q.from >= i && q.from <= last)
					{
						segment.clear(q.to, i, j);
						solveQueryManual(q, segment);
					}
			if(last == array.length - 1) continue;
			segment.clear(last + 1);
			for(int j = last + 1; j < array.length; j++)
			{
				if(j != last + 1)
					segment.addRight();
				for(Query q : endingQueries.getAt(j))
					if(q.from >= i && q.from <= last)
						solveQuery(q, segment);
			}
		}
	}

	public static void main(String[] args)
	{
		Scanner sc = new Scanner();
		int m = sc.nextInt();
		array = sc.nextIntArray(m);
		int q = sc.nextInt();
		allQueries = sc.nextObjectArray(Query.class, q);
		solveEfficient();
		StringBuilder sb = new StringBuilder();
		for(Query query : allQueries)
			sb.append(query.answer).append('\n');
		System.out.print(sb.toString());
		System.out.flush(); 
	}
}