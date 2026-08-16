/*input
100 40021

*/
import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{
	static PrintWriter out;
	static int MOD = 1000000007;
	static FastReader scan;

    /*-------- I/O using short named function ---------*/
	public static String ns(){return scan.next();}
	public static int ni(){return scan.nextInt();}
	public static long nl(){return scan.nextLong();}
	public static double nd(){return scan.nextDouble();}
	public static String nln(){return scan.nextLine();}
	public static void p(Object o){out.print(o);}
	public static void ps(Object o){out.print(o + " ");}
	public static void pn(Object o){out.println(o);}
    /*-------- for output of an array ---------------------*/
     static void iPA(int arr []){
     	 StringBuilder output = new StringBuilder();
	     for(int i=0; i<arr.length; i++)output.append(arr[i] + " ");out.println(output);
	}
	static void lPA(long arr []){
	     StringBuilder output = new StringBuilder();
	     for(int i=0; i<arr.length; i++)output.append(arr[i] + " ");out.println(output);
	}
	static void sPA(String arr []){
	     StringBuilder output = new StringBuilder();
	     for(int i=0; i<arr.length; i++)output.append(arr[i] + " ");out.println(output);
	}
	static void dPA(double arr []){
	     StringBuilder output = new StringBuilder();
	     for(int i=0; i<arr.length; i++)output.append(arr[i] + " ");out.println(output);
	}
    /*-------------- for input in an array ---------------------*/
	static void iIA(int arr[]){
	     for(int i=0; i<arr.length; i++)arr[i] = ni();
	}
	static void lIA(long arr[]){
	     for(int i=0; i<arr.length; i++)arr[i] = nl(); 
	}
	static void sIA(String arr[]){
	     for(int i=0; i<arr.length; i++)arr[i] = ns(); 
	}
	static void dIA(double arr[]){
	     for(int i=0; i<arr.length; i++)arr[i] = nd();
	}
	/*------------ for taking input faster ----------------*/
     static class FastReader
	{
		BufferedReader br;
		StringTokenizer st;

		public FastReader()
		{
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next()
		{
			while (st == null || !st.hasMoreElements())
			{
				try
				{
					st = new StringTokenizer(br.readLine());
				}
				catch (IOException e)
				{
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt()
		{
			return Integer.parseInt(next());
		}

		long nextLong()
		{
			return Long.parseLong(next());
		}

		double nextDouble()
		{
			return Double.parseDouble(next());
		}

		String nextLine()
		{
			String str = "";
			try
			{
				str = br.readLine();
			}
			catch (IOException e)
			{
				e.printStackTrace();
			}
			return str;
		}
	}

	// Method to check if x is power of 2
    static boolean isPowerOfTwo (int x) { return x!=0 && ((x&(x-1)) == 0);}
    //Method to return lcm of two numbers
    static int gcd(int a, int b){return a==0?b:gcd(b % a, a); }
    // method to return LCM of two numbers
    static int lcm(int a, int b){return (a / gcd(a, b)) * b;}
    //Method to count digit of a number
    static int countDigit(long n){return (int)Math.floor(Math.log10(n) + 1);}

    //Method to find the max in an array
    static int getMax(int arr[]){
    	int max = arr[0];
    	for(int i=0; i<arr.length; i++){
    		max = arr[i]>max?arr[i]:max;
    	}
    	return max;
    }
    //Method to find the min in an array
    static int getMin(int arr[]){
    	int min = arr[0];
    	for(int i=0; i<arr.length; i++){
    		min = min>arr[i]?arr[i]:min;
    	}
    	return min;
    }
    //Method for sorting
	static void ruffle_sort(int[] a) {
		//shandom_ruffle
		Random r=new Random();
		int n=a.length;
		for (int i=0; i<n; i++) {
			int oi=r.nextInt(n);
			int temp=a[i];
			a[i]=a[oi];
			a[oi]=temp;
		}
		
		//sort
		Arrays.sort(a);
	}
	static ArrayList<Long> list;
	public static void main (String[] args) throws java.lang.Exception
	{
		OutputStream outputStream =System.out;
        out =new PrintWriter(outputStream);
        scan =new FastReader();
		//for fast output sometimes
		StringBuilder sb = new StringBuilder();
		list = new ArrayList<Long>();
		long a = ni(), b = ni();
		boolean check = false;
		while(true){
			//pn(b);
			list.add(b);
			if(b<a){
				break;
			}
			if(b==a){
				check = true;
				break;
			}
			if(b%2==0){
				b/=2;
			}
			else 
			if(b%10==1){
				b/=10;
			}else{
				break;
			}
		}
		if(check){
			pn("YES");
			pn(list.size());
			for(int i = list.size()-1; i>=0; i--){
				ps(list.get(i));
			}
		}else{
			pn("NO");
		}
        out.flush();
		out.close();
	}
	
	
}
