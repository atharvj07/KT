import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.StringTokenizer;

public class Solver {

	public static void main(String[] Args) throws NumberFormatException,
			IOException {
		new Solver().Run();
	}

	PrintWriter pw;
	StringTokenizer Stok;
	BufferedReader br;

	public String nextToken() throws IOException {
		while (Stok == null || !Stok.hasMoreTokens()) {
			Stok = new StringTokenizer(br.readLine());
		}
		return Stok.nextToken();
	}

	public int nextInt() throws NumberFormatException, IOException {
		return Integer.parseInt(nextToken());
	}

	public double nextDouble() throws NumberFormatException, IOException {
		return Double.parseDouble(nextToken());
	}

	public long nextLong() throws NumberFormatException, IOException {
		return Long.parseLong(nextToken());
	}

	int maxEdges;
	int n;
	TVertex[] verts;
	int maxLen;
	int[] kolByLen;
	ArrayList<TEdge> edges;
	
	class TVertex implements Comparable<TVertex>{

		int lenPath;
		int numVert;
		
		@Override
		public int compareTo(TVertex o) {
			return lenPath-o.lenPath;
		}
		
	}
	
	class TEdge{
		int v1, v2;
		
		public TEdge(int av1, int av2){
			v1=av1;
			v2=av2;
		}
	}
	
	public void shuffle(TVertex[] mas){
		int len=mas.length;
		Random rn=new Random();
		TVertex buf;
		int j;
		for (int i=0; i<len; i++){
			j=rn.nextInt(len);
			buf=mas[i];
			mas[i]=mas[j];
			mas[j]=buf;
		}
	}
	
	public boolean checkGraph(){
		if (kolByLen[0]!=1)
			return false;
		if (maxLen==0)
			return true;
		if (kolByLen[1]>maxEdges)
			return false;
		for (int i=2; i<=maxLen; i++){
			if ((long)kolByLen[i-1]*(maxEdges-1)<(long)kolByLen[i])
				return false;
		}
		return true;
	}
	
	public void Run() throws NumberFormatException, IOException {
		//br = new BufferedReader(new FileReader("input.txt")); pw = new PrintWriter("output.txt");
		br=new BufferedReader(new InputStreamReader(System.in));  pw=new PrintWriter(new OutputStreamWriter(System.out));
		
		n=nextInt();
		maxEdges=nextInt();
		verts=new TVertex[n];
		for (int i=0; i<n; i++){
			verts[i]=new TVertex();
			verts[i].lenPath=nextInt();
			verts[i].numVert=i+1;
		}
		shuffle(verts);
		Arrays.sort(verts);
		maxLen=verts[n-1].lenPath;
		kolByLen=new int[maxLen+1];
		for (int i=0; i<n; i++){
			kolByLen[verts[i].lenPath]++;
		}
		
		if (!checkGraph())
		{
			pw.println(-1);
			pw.flush();
			pw.close();
			return;
		}
		
		edges=new ArrayList<Solver.TEdge>();
		int lastConnected=0;
		int curLevel=0;
		int curParent=0;
		while (lastConnected<n-1){
			while (lastConnected+1<n && verts[lastConnected+1].lenPath==curLevel+1){
				int curPower=0;
				if (curParent>0)
					curPower=1;
				while (lastConnected+1<n && curPower<maxEdges && verts[lastConnected+1].lenPath==curLevel+1){
					lastConnected++;
					edges.add(new TEdge(verts[curParent].numVert, verts[lastConnected].numVert));
					curPower++;
				}
				curParent++;
			}
			while (curParent<n && verts[curParent].lenPath==curLevel)
				curParent++;
			curLevel++;
		}
		pw.println(edges.size());
		for (TEdge edge : edges) {
			pw.print(edge.v1);
			pw.print(' ');
			pw.println(edge.v2);
		}
		pw.flush();
		pw.close();
	}

}
