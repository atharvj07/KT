import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Dictionary;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.Map;
import java.util.StringTokenizer;

import javax.print.attribute.DocAttributeSet;
import javax.print.attribute.HashDocAttributeSet;

import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputReader in = new InputReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskA solver = new TaskA();
		solver.solve(1, in, out);
		out.close();
	}
}

class TaskA {
	boolean[] is_prime;
	int max;
	public void sieve(){
		max = (1<<29)+(1<<27)+(1<<24)+(1<<23);
		//System.out.println(max);
		is_prime = new boolean[max+1];
		is_prime[0] = is_prime[1] = true;
		for(int i = 2; i*i < max; i++){
			if(!is_prime[i]){
				for(int j = i*i; j <= max; j+=i){
					is_prime[j] = true;
				}
			}
		}
	}	 
    
    public void solve(int testNumber, InputReader in, PrintWriter out) {
        int max = (int)(1e6+2);
    	int[] dp = new int[max];
        int n = in.nextInt();
        HashMap<Integer, Integer> set = new HashMap<>();
        for(int i = 0; i < n; i++)
        	set.put(in.nextInt(), in.nextInt());
        if(set.containsKey(0))
        	dp[0] = 1;
        int res = 0; 
        for(int i = 1; i < max ; i++){
        	if(set.containsKey(i) && set.get(i) < i)
        		dp[i] = dp[i-set.get(i)-1]+1;
        	else if(set.containsKey(i) && set.get(i) >= i)
        		dp[i] = 1;
        	else
        		dp[i] = dp[i-1];
        	res = Math.max(res, dp[i]);
        }
        out.println(n - res);
    }
}



    //||||||| UNION FIND ||||||||
  class uni_find{
	  int[] id , sz;
	  int count ;
	 
	  public uni_find(int N){
		  count = N;
	      id = new int[N];
	      sz = new int [N];
	      for (int i = 0; i < N; i++)
	         id[i] = i;
	      for (int i = 0; i < N; i++)
	    	  sz[i] = 1;
	  }
	  
	  private int find(int p) 
	  {  
	     while (p != id[p]) p = id[p];
	     return p; 
	  }
	  public void union(int p, int q)
	   {  
	      int i = find(p);
	      int j = find(q);
	      if (i == j) return;
	     // Make smaller root point to larger one.
	      if   (sz[i] < sz[j]) { id[i] = j; sz[j] += sz[i]; }
	      else                 { id[j] = i; sz[i] += sz[j]; }
	      count--;
	   }
	  
	  public int count() {
			return count;
		}
		public boolean connected(int p, int q) {
			return find(p) == find(q);
		}
  }
  
  
         //||||||| comparable pair ||||||||
 class pair implements Comparable<pair>{
	 public long first,second;
	 public pair(){
		 first = second = 0;
	 }
	@Override
	public int compareTo(pair arg0) {
		if(this.second > arg0.second)
			return 1;
		else if(this.second < arg0.second)
			return -1;
		else if(this.first > arg0.first)
			return 1;
		else if(this.first < arg0.first)
		     return -1;
		return 0;
	}
 }

 
   // ||||||| INPUT READER ||||||||
class InputReader {
    public BufferedReader reader;
    public StringTokenizer tokenizer;

    public InputReader(InputStream stream) {
        reader = new BufferedReader(new InputStreamReader(stream));
        tokenizer = null;
    }

    public String next() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken();
    }

    public Integer nextInt() {
        return Integer.parseInt(next());
    }
    
    public Long nextLong() {
    	return Long.parseLong(next());
    }
    
    public Double nextDouble() {
    	return Double.parseDouble(next());
    }
    
    public Float nextFloat() {
    	return Float.parseFloat(next());
    }
    
    public BigInteger nextBigInteger() {
    	return new BigInteger(next());
    }
    
    public String nextLine() {
    	try {
			return reader.readLine();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		}
    	
    }
    
    public Integer[] nextIntegerArray(int n) {
    	Integer[] a = new Integer[n];
    	for(Integer i = 0; i <  n; i++)
    		a[i] = nextInt();
    	
    	return a;
    }
    
    public Long[] nextLongArray(int n) {
    	Long[] a = new Long[n];
    	for(Integer i = 0; i <  n; i++)
    		a[i] = nextLong();
    	
    	return a;
    }
    
    public long[] nextlongArray(int n) {
    	long[] a = new long[n];
    	for(Integer i = 0; i <  n; i++)
    		a[i] = nextLong();
    	
    	return a;
    }
    
    public double[] nextdoubleArray(int n) {
    	double[] a = new double[n];
    	for(Integer i = 0; i <  n; i++)
    		a[i] = nextDouble();
    	
    	return a;
    }
    
    public String[] nextStringArray(int n){
    	String[] s = new String[n];
    	for(Integer i = 0; i < n; i++)
    		s[i] = next();
    	return s;
    }
    
    public String[] nextLineStringArray(int n){
    	String[] s = new String[n];
    	for(Integer i = 0; i < n; i++)
    		s[i] = next();
    	return s;
    }

    
    }