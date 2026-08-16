import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
	public static void main(String[] args) throws NumberFormatException,
			IOException {
		ContestScanner in = new ContestScanner();
		int n = in.nextInt();
		int[] dmax = new int[2];
		int oldx = 0;
		int oldy = 0;
		int[] fmin = new int[2];
		fmin[0] = 1000000;
		fmin[1] = 1000000;
		int oldt = -1;
		int olda = -1;
		int oldf = 0;
		for(int i=0; i<n; i++){
			int f = in.nextInt();
			int a = in.nextInt();
			int t = in.nextInt();
			int x = in.nextInt();
			int y = in.nextInt();
			int d = (x-oldx)*(x-oldx) + (y-oldy)*(y-oldy);
			if(oldt != t || olda == a){
				oldt = t;
				olda = a;
				oldf = f;
				oldx = x;
				oldy = y;
				continue;
			}
			oldt = t;
			olda = a;
			if(dmax[t] < d){
				dmax[t] = d;
				fmin[t] = f - oldf;
			}else if(dmax[t] == d){
				if(fmin[t] > f - oldf) fmin[t] = f - oldf;
			}
			oldf = f;
			oldx = x;
			oldy = y;
		}
		double[] d = new double[2];
		double[] f = new double[2];
		for(int i=0; i<2; i++){
			if(dmax[i] == 0){
				System.out.println("-1 -1");
			}else{
				d[i] = Math.sqrt(dmax[i]);
				f[i] = fmin[i]/60.0;
				System.out.println(d[i]+" "+f[i]);
			}
		}
	}
	
}

class MyComp implements Comparator<int[]> {
	public int compare(int[] a, int[] b) {
		return a[0] - b[0];
	}
}

class Reverse implements Comparator<Integer> {
	public int compare(Integer arg0, Integer arg1) {
		return arg1 - arg0;
	}
}

class Node {
	int id;
	List<Node> edge = new ArrayList<Node>();

	public Node(int id) {
		this.id = id;
	}

	public void createEdge(Node node) {
		edge.add(node);
	}
}

class ContestWriter {
	private PrintWriter out;

	public ContestWriter(String filename) throws IOException {
		out = new PrintWriter(new BufferedWriter(new FileWriter(filename)));
	}

	public ContestWriter() throws IOException {
		out = new PrintWriter(System.out);
	}

	public void println(String str) {
		out.println(str);
	}

	public void print(String str) {
		out.print(str);
	}

	public void close() {
		out.close();
	}
}

class ContestScanner {
	private BufferedReader reader;
	private String[] line;
	private int idx;

	public ContestScanner() throws FileNotFoundException {
		reader = new BufferedReader(new InputStreamReader(System.in));
	}

	public ContestScanner(String filename) throws FileNotFoundException {
		reader = new BufferedReader(new InputStreamReader(new FileInputStream(
				filename)));
	}

	public String nextToken() throws IOException {
		if (line == null || line.length <= idx) {
			line = reader.readLine().trim().split(" ");
			idx = 0;
		}
		return line[idx++];
	}

	public long nextLong() throws IOException, NumberFormatException {
		return Long.parseLong(nextToken());
	}

	public int nextInt() throws NumberFormatException, IOException {
		return (int) nextLong();
	}

	public double nextDouble() throws NumberFormatException, IOException {
		return Double.parseDouble(nextToken());
	}
}