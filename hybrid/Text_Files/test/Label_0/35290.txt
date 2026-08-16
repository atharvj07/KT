import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader reader;
	static StringTokenizer tokenizer;
	static PrintWriter writer;
	static int[][] k = new int[3][3];
	static boolean[] wuz = new boolean[9];
	static int s,n;
	static int[] d;

	static int nextInt() throws IOException {
		return Integer.parseInt(nextToken());
	}

	static long nextLong() throws IOException {
		return Long.parseLong(nextToken());
	}

	static double nextDouble() throws IOException {
		return Double.parseDouble(nextToken());
	}

	static String nextToken() throws IOException {

		//
		while (tokenizer == null || !tokenizer.hasMoreTokens()) {
			tokenizer = new StringTokenizer(reader.readLine());
		}
		return tokenizer.nextToken();
	}

	public static void main(String[] args) throws IOException {
		// reader = new BufferedReader(new FileReader(new File("code.txt")));
		reader = new BufferedReader(new InputStreamReader(System.in));
		writer = new PrintWriter(System.out);
		tokenizer = null;
		// File file=new File("code.txt");
		// writer = new PrintWriter(file);
		solve();
		// File("new.odt")));
		// reader.close();
		writer.close();
	}

	

	public static void solve() throws IOException {
	int h = nextInt();
	int m= nextInt();
	int n= nextInt();
	int res=0;
	Map<Integer,Integer> ids=new HashMap<Integer,Integer>();
	boolean[] hash=new boolean[h];
	for(int i=0; i<n; i++){
		String c=nextToken();
		if(c.equals("+"))
		{
			int id=nextInt();
			int p=nextInt();
			while (hash[p])
			{
				res++;
				p+=m;
				p%=h;
			}
			ids.put(id,p);
			hash[p]=true;
		} else
		{
			int id=nextInt();
			hash[ids.get(id)]=false;
			ids.remove(id);
		}
	}
	writer.println(res);
	}
}
