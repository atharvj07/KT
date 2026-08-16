//package com.vishal;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.Map.Entry;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;


public class LevekoAndSets {
	
	static enum Sign{
		ZERO, POS, NEG;
		
		Sign applySign(Sign sign) {
			if(this==ZERO)
				return sign;
			if(sign==ZERO)
				return this;
			if(this!=sign)
				return ZERO;
			return sign;
		}

		public Sign reverseSign() {
			if(this==POS)
				return NEG;
			if(this==NEG)
				return POS;
			return ZERO;
		}
	}
	
	static List<Long>factors = new ArrayList<>();
	
	static boolean[] isNotPrime;
	
	static Map<Long, Integer> posOfFactors = new HashMap<>();
	
	static void populateFactors(long n) {
		long sqrt = (long) Math.sqrt(n);
		for(long i=1; i<=sqrt; i++) {
			if(n%i==0)
				factors.add(i);
		}
		
		for(int i=factors.size()-1; i>=0; i--)
			factors.add(n/factors.get(i));
		
		for(int i=0; i<factors.size(); i++)
			posOfFactors.put(factors.get(i), i);
	}
	
	static long pow(long base, long pow, long prime) {
		if(pow==0)
			return 1;
		long half = pow(base, pow/2, prime);
		if(pow%2!=0)
			return (((half*half)%prime)*base)%prime;
		return (half*half)%prime;
	}
	
	static void reduce(Long[] a, long gcd, long prime) {
		IntStream.range(0, a.length).forEach(idx->{a[idx] = pow(a[idx], gcd, prime);});
	}
	
	/*static void setPrimes(int val) {
		IntStream.range(0, val+1).forEach(idx->isNotPrime[idx]=false);
		
		IntStream.range(2, (int)Math.sqrt(val)).forEach(idx->{
			if(isNotPrime[idx]) {
				IntStream.iterate(2*idx, i->i<=val, i->i+idx).forEach(i->isNotPrime[i]=true);
			}
		});
	}*/
	
	static long find_first(long base, long prime) {
		for(long factor:factors) {
			if(pow(base, factor, prime)==1)
				return factor;
		}
		
		return -1;
	}
	
	static void reduce(Long[]a, long prime) {
		IntStream.range(0, a.length).forEach(idx->{ a[idx] = (prime-1)/find_first(a[idx], prime);});
	}
	
	static long gcd(long a, long b) {
			return (a%b==0)?b:gcd(b,a%b);
	}
	
	static long lcm(long a, long b) {
		return (a*b)/gcd(a,b);
	}
	
	static long ans(Set<Long> a, long primeMinueOne) {
		final Integer[] cntofFactors = new Integer[factors.size()];
		IntStream.range(0, cntofFactors.length).forEach(i->cntofFactors[i]=0);
		long ans = 0;
		a.forEach(val->{
			Integer[] savedCnt = Arrays.copyOf(cntofFactors, cntofFactors.length);
			int idx = posOfFactors.get(val);
			if(savedCnt[idx]==0) {
				IntStream.range(0, cntofFactors.length).forEach(i->{
					long factor = factors.get(i);
					long lcm = lcm(factor, val);
					int j = posOfFactors.get(lcm);
					savedCnt[j] = savedCnt[j]-cntofFactors[i];
				});
				savedCnt[idx] = savedCnt[idx]+1;
		  }
		  copy(cntofFactors, savedCnt);
		});
		
		for(int i = 0; i<cntofFactors.length; i++) {
			int cntOfFactor = cntofFactors[i];
			long factor = factors.get(i);
			if(cntOfFactor>0)
				ans += primeMinueOne/factor;
			else if(cntOfFactor < 0)
				ans -= primeMinueOne/factor;
		}
		
		return ans;
	}

	private static <T> void copy(final T[] cntofFactors, T[] savedCnt) {
		for(int i=0; i<cntofFactors.length; i++)
			cntofFactors[i] = savedCnt[i];
	}

	public static void main(String[] args) {
		boolean flag = false;
		Scanner scanner = null;
		if (!flag)
			scanner = new Scanner(System.in);
		else
			try {
				scanner = new Scanner(new File("D:\\file.txt"));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		
		int n = scanner.nextInt();
		int m = scanner.nextInt();
		long p = scanner.nextLong();
		long primeMinusOne = p-1;
		long sqrt = (long)Math.sqrt(primeMinusOne);
		isNotPrime = new boolean[(int) (sqrt+1)];
		
		Long[] a = new Long[n];
		
		for(int i=0; i<n; i++) 
			a[i] = scanner.nextLong();

		long gcd = scanner.nextLong();
		for(int i=1; i<m; i++)
			gcd = gcd(gcd, scanner.nextLong());
		
		//setPrimes((int) sqrt);
		populateFactors(primeMinusOne);
		reduce(a, gcd, p);
		reduce(a, p);
		//print(factors.stream());
		Set<Long> set = convertArrayToSet(a);
		//only for test purpose
		//Long[] k = new Long[] {1170L, 299910L, 99970L, 390L, 99070270L, 891632430L, 297210810L, 899730L, 386490L, 1159470L, 128830L};
		//set = convertArrayToSet(k);
		//primeMinusOne = 891632430L;
		//print(set.stream());
		System.out.println(ans(set, primeMinusOne));
	}

	private static void print(Stream<Long> a) {
		a.forEach(b->System.out.printf("%d ", b));
		System.out.println();
	}

	public static <T> Set<T> convertArrayToSet(T [] a) {
		return Arrays.stream(a).collect(Collectors.toSet());
	}

}
