import java.util.*;import java.io.*;import java.math.*;
public class E
{
    public static void process()throws IOException
    {
    	int n=ni();
		int nTowers=ni();
		HashSet<Integer>[] towers=new HashSet[nTowers];
		for (int i=0; i<nTowers; i++) towers[i]=new HashSet<>();
		int potential=n-1;
		for (int i=0; i<n; i++) {
			int tower=ni()-1;
			if (towers[tower].contains(i-1)) potential--;
			towers[tower].add(i);
		}
		pn(potential);
		for (int qq=1; qq<nTowers; qq++) {
			int t1=ni()-1, t2=ni()-1;
			HashSet<Integer> smaller=towers[t1].size()<towers[t2].size()?towers[t1]:towers[t2];
			HashSet<Integer> bigger=smaller==towers[t1]?towers[t2]:towers[t1];
			int[] smallerValues=new int[smaller.size()];
			int smallerIndex=0;
			for (int i:smaller)
				smallerValues[smallerIndex++]=i;
			ruffleSort(smallerValues);
			for (int i=0; i<smallerValues.length; i++) {
				if (i<smallerValues.length-1 && smallerValues[i+1]==smallerValues[i]+1)
					potential++;
				bigger.add(smallerValues[i]);
				if (bigger.contains(smallerValues[i]-1)) potential--;
				if (bigger.contains(smallerValues[i]+1)) potential--;
			}
			
			towers[t1]=bigger;
			pn(potential);
		}
    }
    static void ruffleSort(int[] a) {
		Random get = new Random();
		for (int i = 0; i < a.length; i++) {
			int r = get.nextInt(a.length);
			int temp = a[i];
			a[i] = a[r];
			a[r] = temp;
		}
		Arrays.sort(a);
	}
    
    static AnotherReader sc;
    static PrintWriter out;
    public static void main(String[]args)throws IOException
    {
        boolean oj = true;
        if(oj){sc=new AnotherReader();out=new PrintWriter(System.out);}
        else{sc=new AnotherReader(100);out=new PrintWriter("output.txt");}
        int t=1;
//        t=ni();
        while(t-- > 0) {process();}
        out.flush();out.close();  
    }

    static void pn(Object o){out.println(o);}
    static void p(Object o){out.print(o);}
    static void pni(Object o){out.println(o);out.flush();}
    static int ni()throws IOException{return sc.nextInt();}
    static long nl()throws IOException{return sc.nextLong();}
    static double nd()throws IOException{return sc.nextDouble();}
    static String nln()throws IOException{return sc.nextLine();}
    static int[] nai(int N)throws IOException{int[]A=new int[N];for(int i=0;i!=N;i++){A[i]=ni();}return A;}
    static long[] nal(int N)throws IOException{long[]A=new long[N];for(int i=0;i!=N;i++){A[i]=nl();}return A;}
    static long gcd(long a, long b)throws IOException{return (b==0)?a:gcd(b,a%b);}
    static int gcd(int a, int b)throws IOException{return (b==0)?a:gcd(b,a%b);}
    static int bit(long n)throws IOException{return (n==0)?0:(1+bit(n&(n-1)));}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

    static class AnotherReader{BufferedReader br; StringTokenizer st;
    AnotherReader()throws FileNotFoundException{
    br=new BufferedReader(new InputStreamReader(System.in));}
    AnotherReader(int a)throws FileNotFoundException{
    br = new BufferedReader(new FileReader("input.txt"));}
    String next()throws IOException{
    while (st == null || !st.hasMoreElements()) {try{
    st = new StringTokenizer(br.readLine());}
    catch (IOException  e){ e.printStackTrace(); }}
    return st.nextToken(); } int nextInt() throws IOException{
    return Integer.parseInt(next());}
    long nextLong() throws IOException
    {return Long.parseLong(next());}
    double nextDouble()throws IOException { return Double.parseDouble(next()); }
    String nextLine() throws IOException{ String str = ""; try{
    str = br.readLine();} catch (IOException e){
    e.printStackTrace();} return str;}}
   
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
}