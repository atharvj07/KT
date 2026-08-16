/*
    Aman Agarwal
    algo.java
*/

import java.util.*;
import java.io.*;

public class B1305
{
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
                    catch (IOException  e)
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


    static FastReader sc = new FastReader();
    static PrintWriter out = new PrintWriter(System.out);
    static int ni()throws IOException{return sc.nextInt();}
    static long nl()throws IOException{return sc.nextLong();}
    static int[] nai(int N,int start)throws IOException{int[]A=new int[N+start];for(int i=start;i!=(N+start);i++){A[i]=ni();}return A;}
    static long[] nal(int N)throws IOException{long[]A=new long[N];for(int i=0;i!=N;i++){A[i]=nl();}return A;}
    static void print(int arr[]){for(int i=0;i<arr.length;i++)out.print(arr[i]+" ");out.println();}
    static void print(long arr[]){for(int i=0;i<arr.length;i++)out.print(arr[i]+" ");out.println();}
    static long gcd(long a, long b)throws IOException{return (b==0)?a:gcd(b,a%b);}
    static int gcd(int a, int b)throws IOException{return (b==0)?a:gcd(b,a%b);}
    static int bit(long n)throws IOException{return (n==0)?0:(1+bit(n&(n-1)));} // return the number of set bits.
    static boolean isPrime(int number){if(number==1) return false;if (number == 2 || number == 3){return true;}if (number % 2 == 0) {return false;}int sqrt = (int) Math.sqrt(number) + 1;for(int i = 3; i < sqrt; i += 2){if (number % i == 0){return false;}}return true;}
    static boolean isPrime(long number){if(number==1) return false;if (number == 2 || number == 3){return true;}if (number % 2 == 0) {return false;}long sqrt = (long) Math.sqrt(number) + 1;for(int i = 3; i < sqrt; i += 2){if (number % i == 0){return false;}}return true;}
    static int power(int n,int p){if(p==0)return 1;int a = power(n,p/2);a = a*a;int b = p & 1;if(b!=0){a =  n*a;}return a;}
    static long power(long n,long p){if(p==0)return 1;long a = power(n,p/2);a = a*a;long b = p & 1;if(b!=0){a =  n*a;}return a;}
    static void reverse(int[] a) {int b;for (int i = 0, j = a.length - 1; i < j; i++, j--) {b = a[i];a[i] = a[j];a[j] = b;}}
    static void reverse(long[] a) {long b;for (int i = 0, j = a.length - 1; i < j; i++, j--) {b = a[i];a[i] = a[j];a[j] = b;}}
    static void swap(int a[],int i,int j){int temp = a[i];a[i] = a[j];a[j] = temp;}
    static void swap(long a[],int i,int j){long temp = a[i];a[i] = a[j];a[j] = temp;}
    static int count(int n){int c=0;while(n>0){c++;n = n/10;}return c;}
    static int[] prefix_sum(int a[],int n){int s[] = new int[n];s[0] = a[0];for(int i=1;i<n;i++){s[i] = a[i]+s[i-1];}return s;}
    static long[] prefix_sum(long a[],int n){long s[] = new long[n];s[0] = a[0];for(int i=1;i<n;i++){s[i] = a[i]+s[i-1];}return s;}
    static boolean isPerfectSquare(double x){double sr = Math.sqrt(x);return ((sr - Math.floor(sr)) == 0);}
    static ArrayList<Integer> sieve(int n) {int k=0; boolean prime[] = new boolean[n+1];ArrayList<Integer> p_arr = new ArrayList<>();for(int i=0;i<n;i++) prime[i] = true;for(int p = 2; p*p <=n; p++){ k=p;if(prime[p] == true) { p_arr.add(p);for(int i = p*2; i <= n; i += p) prime[i] = false; } }for(int i = k+1;i<=n;i++){if(prime[i]==true)p_arr.add(i);}return p_arr;} 
    static boolean[] seive_check(int n) {boolean prime[] = new boolean[n+1];for(int i=0;i<n;i++) prime[i] = true;for(int p = 2; p*p <=n; p++){ if(prime[p] == true) { for(int i = p*2; i <= n; i += p) prime[i] = false; } }prime[1]=false;return prime;} 
    static void close(){out.flush();}

    /*-------------------------Main Code Starts(algo.java)----------------------------------*/    

    public static void main(String[] args) throws IOException 
    {
        int t = 1;
        //t = sc.nextInt();
        while(t-- > 0)
        {
            /*String s = sc.next();
            int n = s.length();
            int l = s.indexOf('(');
            int r = s.lastIndexOf(')');
            ArrayList<Integer> lis = new ArrayList<>();
            while(l<r && l!=1)
            {
                lis.add(l+1);
                lis.add(r+1);
                l = s.indexOf('(',l+1);
                r = s.lastIndexOf(')',r-1);
            }
            if(lis.size()>0)
                out.println(1);
            out.println(lis.size());

            Collections.sort(lis);
            for(int i=0;i<lis.size();i++)
                out.print(lis.get(i)+" ");*/

            String s=sc.next();
            int n=s.length();
            int l=s.indexOf('(');
            int r=s.lastIndexOf(')');
            ArrayList<Integer> al=new ArrayList<>();
            
            while(l<r&&l!=-1)
            {
                al.add(l+1);
                al.add(r+1);  
                l=s.indexOf('(',l+1);
                r=s.lastIndexOf(')',r-1);
            }
            if(al.size()>0){
            System.out.println(1);}
            System.out.println(al.size());
            Collections.sort(al);
            for(int i=0;i<al.size();i++)
            System.out.print(al.get(i)+" ");
        }    
        close();
    }
}
