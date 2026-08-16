import java.io.BufferedReader;
import java.io.Closeable;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class E {
	
	public static void main(String[] args) {
		try (final Scanner sc = new Scanner(System.in)) {
			final int N = sc.nextInt();
			final int E = sc.nextInt();
			
			ArrayList<HashSet<Integer>> no_adj = new ArrayList<HashSet<Integer>>();
			for(int i = 0; i < N; i++){ no_adj.add(new HashSet<Integer>()); }
			for(int i = 0; i < E; i++){
				final int s = sc.nextInt() - 1;
				final int t = sc.nextInt() - 1;
				
				no_adj.get(s).add(t);
				no_adj.get(t).add(s);
			}

			LinkedList<Integer> queue = new LinkedList<Integer>();
			HashSet<Integer> removed = new HashSet<Integer>();
			
			TreeSet<Integer> availables = new TreeSet<Integer>();
			HashSet<Integer> tmp_availables = new HashSet<Integer>();
			
			for(int i = 0; i < N; i++){ availables.add(i); }
			
			boolean[] had_queue = new boolean[N];
			
			ArrayList<Integer> comps = new ArrayList<Integer>();
			int glob_size = N;
			while(glob_size > 0){
				int comp_size = 0;
				
				queue.clear();
				{
					final int first = availables.first();
					queue.add(first);
					had_queue[first] = true;
				}
				
				while(!queue.isEmpty()){
					final int node = queue.poll();
					availables.remove(node);
					removed.clear();
					
					//System.out.println("used : " + node + " " + availables);
					comp_size++; glob_size--;
					
					
					for(final int no_next : no_adj.get(node)){
						if(availables.remove(no_next)){
							removed.add(no_next);
						}
					}
					
					//System.out.println(availables);
					
					if(availables.isEmpty()){
						for(final int no_next : removed){
							availables.add(no_next);
						}
					}else{
						tmp_availables.clear();
						tmp_availables.addAll(availables);
						
						for(final int next : tmp_availables){
							availables.remove(next);
							queue.add(next);
						}
						
						for(final int no_next : removed){
							availables.add(no_next);
						}
					}
				}
				
				comps.add(comp_size);
				//System.out.println(comp_size);
			}
			
			Collections.sort(comps);
			try(final PrintWriter pw = new PrintWriter(System.out)){
				final int comp = comps.size();
				pw.println(comp);
				for(int i = 0; i < comp; i++){
					pw.print((i == 0 ? "" : " ") + comps.get(i)); 
				}
				pw.println();
			}
		}
	}
	
	public static class Scanner implements Closeable {
		private BufferedReader br;
		private StringTokenizer tok;

		public Scanner(InputStream is) {
			br = new BufferedReader(new InputStreamReader(is));
		}

		private void getLine() {
			try {
				while (!hasNext()) {
					tok = new StringTokenizer(br.readLine());
				}
			} catch (IOException e) { /* ignore */
			}
		}

		private boolean hasNext() {
			return tok != null && tok.hasMoreTokens();
		}

		public String next() {
			getLine();
			return tok.nextToken();
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}
		
		public long nextLong() {
			return Long.parseLong(next());
		}

		public void close() {
			try {
				br.close();
			} catch (IOException e) { /* ignore */
			}
		}
	}
}