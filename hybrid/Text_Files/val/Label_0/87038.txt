import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;


import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.Random;
import java.util.TreeSet;


public final class CF_460_F{

	static boolean verb=true;
	static void log(Object X){if (verb) System.err.println(X);}
	static void log(Object[] X){if (verb) {for (Object U:X) System.err.print(U+" ");System.err.println("");}}
	static void log(int[] X){if (verb) {for (int U:X) System.err.print(U+" ");System.err.println("");}}
	static void log(int[] X,int L){if (verb) {for (int i=0;i<L;i++) System.err.print(X[i]+" ");System.err.println("");}}
	static void log(long[] X){if (verb) {for (long U:X) System.err.print(U+" ");System.err.println("");}}

	static void logWln(Object X){if (verb) System.err.print(X);}
	static void info(Object o){	System.out.println(o);}
	static void output(Object o){outputWln(""+o+"\n");	}
	static void outputWln(Object o){try {out.write(""+ o);} catch (Exception e) {}}


	static long mod=1000000007;
	static long MX=1000000000000000001L;

	// Global vars
	static BufferedWriter out;
	static InputReader reader;

	static long powerMod(long b,long e,long m){
		long x=1;
		while (e>0) {
			if (e%2==1)
				x=(b*x)%m;
			b=(b*b)%m;
			e=e/2;
		}
		return x; 
	}


	// -1 lose
	// 1 win
	// 2 neutral
	static void dfs(){


	}

	static int NX=8;
	static int ref=0;
	static int VX=5;



	static class Node {

		Node[] nodes;
		int index;

		int insert(ArrayList<Integer> list,int pos){
			if (pos==NX){
				if (index==-1)
					index=ref++;
				return index;
			}
			int x=list.get(pos);
			if (nodes[x]==null){
				nodes[x]=new Node();
			}
			return nodes[x].insert(list, pos+1);

		}

		int getIndex(ArrayList<Integer> list,int pos){
			if (pos==NX)
				return index;
			int x=list.get(pos);
			if (nodes[x]==null)
				return -1;
			return nodes[x].getIndex(list,pos+1);
		}

		public Node(){
			nodes=new Node[VX];
			index=-1;
		}


	}


	static void process() throws Exception {


		out = new BufferedWriter(new OutputStreamWriter(System.out));
		reader=new InputReader(System.in);

		long lastTime=System.currentTimeMillis();

		log("generating");
		ArrayList<ArrayList<Integer>> lst=new ArrayList<ArrayList<Integer>>();
		lst.add(new ArrayList<Integer>());
		for (int i=0;i<8;i++){
			ArrayList<ArrayList<Integer>> nxt=new ArrayList<ArrayList<Integer>>();

			for (int u=0;u<5;u++)
				for (ArrayList<Integer> ls:lst){

					ArrayList<Integer> tmp=new ArrayList<Integer>();
					tmp.addAll(ls);
					if (tmp.size()==0 || (tmp.size()>0 && tmp.get(tmp.size()-1)<=u)){
						tmp.add(u);
						nxt.add(tmp);
					}
				}
			lst=nxt;
		}


		log(lst.size());
		Node root=new Node();
		ref=0;
		for (ArrayList<Integer> list:lst){
			int id=root.insert(list, 0);
		}

		long curTime=System.currentTimeMillis();
		log(curTime-lastTime);
		lastTime=curTime;


		int L=lst.size();
		/*
		HashMap<String,Integer> hm=new HashMap<String,Integer>();
		for (int i=0;i<L;i++){
			String rs="";
			for (int x:lst.get(i))
				rs+=x;
			hm.put(rs, i);
		}
		 */

		ArrayList<int[]>[][] friends=new ArrayList[L][L];
		ArrayList<int[]>[][] next=new ArrayList[L][L];
		for (int i=0;i<L;i++)
			for (int j=0;j<L;j++){
				friends[i][j]=new ArrayList<int[]>();
				next[i][j]=new ArrayList<int[]>();
			}

		log("building friends");

		for (int i=0;i<L;i++)
			for (int j=0;j<L;j++){
				ArrayList<Integer> ls1=lst.get(i);
				ArrayList<Integer> ls2=lst.get(j);
				int lastv=0;
				for (int v=0;v<8;v++){
					if (ls1.get(v)!=lastv){
						lastv=ls1.get(v);
						int lastu=0;
						for (int u=0;u<8;u++){
							if (ls2.get(u)!=lastu){
								lastu=ls2.get(u);
								ArrayList<Integer> ls3=new ArrayList<Integer>();
								ls3.addAll(ls1);
								int x=ls3.get(v);
								x+=ls2.get(u);
								x%=5;
								ls3.set(v, x);
								Collections.sort(ls3);
								int k=root.getIndex(ls3,0);

								//String rs="";
								//for (int y:ls3)
								//	rs+=x;
								//int k=hm.get(rs);
								friends[j][k].add(new int[]{i,j});
								next[i][j].add(new int[]{j,k});
								// now need to map
							}
						}
					}
				}
			}


		curTime=System.currentTimeMillis();
		log(curTime-lastTime);
		lastTime=curTime;


		log("Exploring");
		// 0 xx win
		// xx 0 loses
		// 0 0 impossible

		int[][] stack=new int[L*L][];
		boolean[][] onstack=new boolean[L][L];
		boolean[][] visited=new boolean[L][L];
		//int r=0;
		//int w=0;

		int st=0;
		int[][] win=new int[L][L];
		for (int i=1;i<L;i++){
			win[0][i]=1;
			win[i][0]=-1;
			//onstack[0][i]=true;
			//onstack[i][0]=true;
			visited[0][i]=true;
			visited[i][0]=true;

		}

		int[][] ptr=new int[L][L];


		/*
		for (int i=0;i<L;i++)
			for (int j=0;j<L;j++){

				if (!visited[i][j]){
					visited[i][j]=true;
					if (win[i][j]==0){
						st=0;

						stack[st++]=new int[]{i,j};

						while (st>0){
							int[] star=stack[st-1];
							int u=star[0];
							int v=star[1];

							int id=ptr[u][v];
							if (id<next[u][v].size()){
								int[] tmp=next[u][v].get(id);
								ptr[u][v]++;
								int a=tmp[0];
								int b=tmp[1];
								if (win[a][b]==0 && !visited[a][b]){
									stack[st++]=new int[]{a,b};
									visited[a][b]=true;
								}
							} else {
								st--;
								boolean wn=true;
								loop:for (int[] tmp:next[u][v]){
									int a=tmp[0];
									int b=tmp[1];
									if (win[a][b]==-1){
										win[u][v]=1;
										break loop;
									}
									if (win[a][b]!=1)
										wn=false;
								}
								if (wn==true){
									win[u][v]=-1;
								}
								if (win[u][v]==0)
									win[u][v]=2;
							}


						}
					}
				}

			}

		 */

		int r=0;
		int w=0;

		for (int i=1;i<L;i++){
			stack[w++]=new int[]{i,0};
			stack[w++]=new int[]{0,i};


		}
		while (r<w){
			boolean vrb=false;
			int[] tmp=stack[r++];
			int i=tmp[0];
			int j=tmp[1];
			if (i==9 && j==45){
				//vrb=true;
			}
			if (vrb)
				log("Processing i:"+i+" j:"+j+" win[i][j]:"+win[i][j]);
			//onstack[i][j]=false;
			for (int[] bob:friends[i][j]){
				int u=bob[0];
				int v=bob[1];
				if (vrb)
					log("Processing u:"+u+" u:"+v+" win[u][v]:"+win[u][v]+" visited[u][v]:"+visited[u][v]);
				if (!visited[u][v]){
					
					if (win[i][j]==-1){
						win[u][v]=1;
						//win[v][u]=-1;


						//visited[v][u]=true;
						//stack[w++]=new int[]{v,u};
					} else {
						boolean wn=true;
						for (int[] bab:next[u][v]){
							int a=bab[0];
							int b=bab[1];
							if (win[a][b]!=1){
								wn=false;
							}
						}
						if (wn){
							win[u][v]=-1;
							//win[v][u]=1;
							//visited[v][u]=true;
						}

					}
					if (win[u][v]!=0) {
						visited[u][v]=true;

						stack[w++]=new int[]{u,v};
					}
				}
			}

		}
		curTime=System.currentTimeMillis();
		log(curTime-lastTime);
		lastTime=curTime;

		log("ok");

		int T=reader.readInt();
		for (int t=0;t<T;t++){
			int f=reader.readInt();

			/*
			int[] a=new int[8];
			for (int i=0;i<8;i++)
				a[i]=reader.readInt();
			Arrays.sort(a);

			int[] b=new int[8];
			for (int i=0;i<8;i++)
				b[i]=reader.readInt();
			Arrays.sort(b);
			 */

			/*
			String A="";
			for (int x:a)
				A+=x;
			String B="";
			for (int x:b)
				B+=x;
			int i=hm.get(A);
			int j=hm.get(B);
			 */

			ArrayList<Integer> a=new ArrayList<Integer>();
			for (int e=0;e<8;e++)
				a.add(reader.readInt());
			ArrayList<Integer> b=new ArrayList<Integer>();
			for (int e=0;e<8;e++)
				b.add(reader.readInt());

			Collections.sort(a);
			Collections.sort(b);


			int i=root.getIndex(a, 0);
			int j=root.getIndex(b, 0);
			int res=win[i][j];

			/*
			log("i:"+i+" j:"+j+" "+win[i][j]);
		
			int[] bob=new int[]{i,j};
			while (next[bob[0]][bob[1]].size()>0){
				log("---------------");
				log("size:"+next[bob[0]][bob[1]].size());
				bob=next[bob[0]][bob[1]].get(0);
				
				int u=bob[0];
				int v=bob[1];
				log(u+" "+v+" "+lst.get(u)+" "+lst.get(v)+" win:"+win[u][v]);
				
			}
			*/
			if (f==1)
				res=win[j][i];
			//log("res:"+res);
			String ans="Deal";
			if (res==1) {
				if (f==0)
					ans="Alice";
				else
					ans="Bob";
			}
			if (res==-1) {
				if (f==1)
					ans="Alice";
				else
					ans="Bob";	
			}
			output(ans);
		}

		try {
			out.close();
		}
		catch (Exception EX){}


	}


	public static void main(String[] args) throws Exception {
		process();

	}

	static final class InputReader {
		private final InputStream stream;
		private final byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;

		public InputReader(InputStream stream) {
			this.stream = stream;
		}

		private int read() throws IOException {
			if (curChar >= numChars) {
				curChar = 0;
				numChars = stream.read(buf);
				if (numChars <= 0) {
					return -1;
				}
			}
			return buf[curChar++];
		}


		public final String readString() throws IOException {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			StringBuilder res=new StringBuilder();
			do {
				res.append((char)c);
				c = read();
			} while (!isSpaceChar(c));
			return res.toString();
		}

		public final int readInt() throws IOException {
			int c = read();
			boolean neg=false;
			while (isSpaceChar(c)) {
				c = read();
			}
			char d=(char)c;
			//log("d:"+d);
			if (d=='-') {
				neg=true;
				c = read();
			}
			int res = 0;
			do {
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			//log("res:"+res);
			if (neg)
				return -res;
			return res;

		}

		public final long readLong() throws IOException {
			int c = read();
			boolean neg=false;
			while (isSpaceChar(c)) {
				c = read();
			}
			char d=(char)c;
			//log("d:"+d);
			if (d=='-') {
				neg=true;
				c = read();
			}
			long res = 0;
			do {
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			//log("res:"+res);
			if (neg)
				return -res;
			return res;

		}




		private boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}
	}


}