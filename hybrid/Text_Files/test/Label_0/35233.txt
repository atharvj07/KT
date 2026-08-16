import java.awt.Point;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;
import java.util.Vector;
import java.util.TreeSet;

import java.math.BigInteger;

public class Main {
	
	public static boolean debug = false;
	
	public static void main(String[] args) {
		Reader in = null;
		Writer out = null;
		
		if(debug) {
			in = new Reader(args[0]);
			out = new Writer(args[1]);
		} else {
			in = new Reader();
			out = new Writer();
		}
		
		int n = in.nextInt();
		int k = in.nextInt();
		int[] nums = new int[n+1];
		if(fillNums(nums, n, k)) {
			for(int i=1; i<=n; i++)
				out.print(nums[i]+" ");
		} else out.print(-1);
		/*
		Vector<Integer> nums = new Vector<Integer>();
		boolean[] used = new boolean[n+1];
		for(int i=1; i<=k; i++) {
			if(((1<<i)&((1<<i)-1))==0) {
				if((1<<i)>n) {
					nums.clear();
					break;
				}
				nums.add(1<<i);
				used[nums.lastElement()] = true;
			} else {
				used[i] = true;
				nums.add(i);
			}
		}
		int tempC = 0;
		int tempNum = 1;
		while(k<n) {
			//out.println(nums);
			while(used[tempNum+tempC]) tempC++;
			nums.add(tempNum+tempC);
			if(nums.lastElement()>n) {
				nums.clear();
				break;
			}
			tempNum++;
			k++;
		}
		
		if(nums.size()==0) out.print(-1);
		else 
			for(Integer num: nums)
				out.print(num+" ");*/
		out.close();
	}
	
	static boolean fillNums(int[] nums, int n, int k) {
		if(n==k) return false;
		nums[1] = 1;
		for(int i=2; i<=k+1; i++)
			nums[i] = i;
		for(int i=k+2; i<=n; i+=2) {
			//System.out.println(i+" "+Arrays.toString(nums));
			if(i<n) {
				nums[i] = i+1;
				nums[i+1] = i;
			} else {
				/*for(int j=k+2; j<n; j++) {
					System.out.println(i+" "+j+" "+nums[j]);
					if(gcd(i, j)==1 && gcd(i, nums[j])==1) {
						nums[i] = nums[j];
						nums[j] = i;
						return true;
					}
				}*/
				nums[i] = 1;
				nums[1] = i;
				return true;//false;
			}
		}
		return true;
	}
	
	static int gcd(int a, int b) {
		if(b==0) return a;
		return gcd(b, a%b);
	}
}

class Writer {
	
	private BufferedWriter output;
	
	public Writer() {
		output = new BufferedWriter(new OutputStreamWriter(System.out));
	}
	
	public Writer(String s) {
		try {
			output = new BufferedWriter(new FileWriter(s));
		} catch(Exception ex) { ex.printStackTrace(); System.exit(0);}
	}
	
	public void println() {
		try {
			output.append("\n");
		} catch(IOException io) { io.printStackTrace(); System.exit(0);}
	}

	public void print(Object o) {
		try {
			output.append(o.toString());
		} catch(IOException io) { io.printStackTrace(); System.exit(0);}
	}
	
	public void println(Object o) {
		try {
			output.append(o.toString()+"\n");
		} catch(IOException io) { io.printStackTrace(); System.exit(0);}
	}

	public void printf(String format, Object... args) {
		try {
			output.append(String.format(format, args));
		} catch(IOException io) { io.printStackTrace(); System.exit(0);}
	}
	
	public void printfln(String format, Object... args) {
		try {
			output.append(String.format(format, args)+"\n");
		} catch(IOException io) { io.printStackTrace(); System.exit(0);}
	}
	
	public void flush() {
		try {
			output.flush();
		} catch(IOException io) { io.printStackTrace(); System.exit(0);}
	}
	
	public void close() {
		try {
			output.close();
		} catch(IOException io) { io.printStackTrace(); System.exit(0);}
	}
}

class Reader {
	private BufferedReader input;
	private StringTokenizer line = new StringTokenizer("");
	
	public Reader() {
		input = new BufferedReader(new InputStreamReader(System.in));
	}

	public Reader(String s) {
		try {
			input = new BufferedReader(new FileReader(s));
		} catch(IOException io) { io.printStackTrace(); System.exit(0);}
	}
	
	public void fill() {
		try {
			if(!line.hasMoreTokens()) line = new StringTokenizer(input.readLine());
		} catch(IOException io) { io.printStackTrace(); System.exit(0);}
	}
	
	public double nextDouble() {
		fill();
		return Double.parseDouble(line.nextToken());
	}
	
	public String nextWord() {
		fill();
		return line.nextToken();
	}
	
	public int nextInt() {
		fill();
		return Integer.parseInt(line.nextToken());
	}

	public long nextLong() {
		fill();
		return Long.parseLong(line.nextToken());
	}
	
	public double readDouble() {
		double d = 0;
		try {
			d = Double.parseDouble(input.readLine());
		} catch(IOException io) {io.printStackTrace(); System.exit(0);}
		return d;
	}
	
	public int readInt() {
		int i = 0;
		try {
			i = Integer.parseInt(input.readLine());
		} catch(IOException io) {io.printStackTrace(); System.exit(0);}
		return i;
	}
	
	public int[] readInts(int n) {
		int[] a = new int[n];
		for(int i=0; i<n; i++)
			a[i] = nextInt();
		return a;
	}
	
	public void fillInts(int[] a) {
		for(int i=0; i<a.length; i++)
			a[i] = nextInt();
	}
	
	public long readLong() {
		long l = 0;
		try {
			l = Long.parseLong(input.readLine());
		} catch(IOException io) {io.printStackTrace(); System.exit(0);}
		return l;
	}
	
	public String readLine() {
		String s = "";
		try {
			s = input.readLine();
		} catch(IOException io) {io.printStackTrace(); System.exit(0);}
		return s;
	}
}