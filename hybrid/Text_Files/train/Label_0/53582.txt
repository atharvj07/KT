import java.awt.Point;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.StreamTokenizer;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Random;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {
	public static void main(String[] args) throws Exception {
		//in = new BufferedReader(new InputStreamReader(System.in));
		//in = new BufferedReader(new FileReader("input.txt"));
		//out = new PrintWriter("output.txt");
		out = new PrintWriter(System.out);
		in = new StreamTokenizer(new InputStreamReader(System.in));
		//in = new StreamTokenizer(new FileReader("input.txt"));

		int n = nextInt();		
		src = new int[n];
		for (int i = 0; i < n; ++i) src[i] = nextInt();
		next = new int[n];
		HashMap<Integer, Integer> mp = new HashMap<Integer, Integer>();
		next[n - 1] = n;
		mp.put(src[n - 1], n - 1);
		for (int i = n - 2; i >= 0; --i) {
			if (mp.get(src[i]) == null)
				next[i] = n;
			else {
				next[i] = mp.get(src[i]);
			}
			mp.put(src[i], i);
		}
		
		Random rand = new Random();
		long mod = BigInteger.probablePrime(31, rand).longValue();
		long mul = BigInteger.probablePrime(11, rand).longValue(); //13?, rand? another
		
		long[] modinv = new long[n];
		long mulinv = BigInteger.valueOf(mul).modInverse(BigInteger.valueOf(mod)).longValue();		
		modinv[0] = 1;		
		for (int i = 1; i < n; ++i) modinv[i] = (modinv[i - 1] * mulinv) % mod;
		
		mul %= mod; //
		long[] hash = new long[n];
		hash[0] = src[0] % mod;
		for (int i = 1; i < n; ++i) hash[i] = ((hash[i - 1] * mul) % mod + src[i]) % mod;
		
		pair[] pv = new pair[n];
		
		for (int i = 0; i < n; ++i) {
			pv[i] = new pair();
			pv[i].pos = i;
			pv[i].len = 0;
			
			int loc = i;
			while (true) {					
				loc = next[loc];
				if (loc >= n) break;
				if (loc + (loc - i) - 1 >= n) break;
				
				long h1, h2;
				
				h1 = hash[loc - 1]; //loc > 0 ? 
				if (i > 0) {
					h1 = (h1 + mod - hash[i - 1]) % mod;
					h1 = (h1 * modinv[i]) % mod;
				}
				
				h2 = (hash[loc + loc - i - 1] + mod - hash[loc - 1]) % mod; //loc > 0 ? 
				h2 = (h2 * modinv[loc]) % mod; //loc?
				
				if (h1 == h2) {
					pv[i].len = loc - i; //!!
					break;
				}
			}
		}
		
		Arrays.sort(pv);
		
		int left = 0;
		for (int i = 0; i < n; ++i) {
			if (pv[i].len == 0) continue;
			if (pv[i].pos < left) continue;
			left = pv[i].pos + pv[i].len;			
		}
			
		out.println(n - left);
		for (int i = left; i < n; ++i) {
			out.print(src[i]);
			out.print(" ");
		}
		out.close();
	}
	
	static int[] src, next;
	
	static int 	nextInt() throws Exception {
		in.nextToken();
		return (int)in.nval;
	}
	
	static StreamTokenizer in;
	//static BufferedReader in;
	static PrintWriter out;
	
}

class pair implements Comparable<pair>{
	int pos, len;

	public int compareTo(pair arg) {
		if (len == arg.len) return pos - arg.pos;
		return len - arg.len;
	}
	
}