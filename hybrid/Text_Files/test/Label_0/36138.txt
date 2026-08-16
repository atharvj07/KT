import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Stack;
import java.util.Comparator;
import java.util.StringTokenizer;
import static java.lang.Math.max;
import static java.lang.Math.min;
import static java.lang.Math.abs;

public class A
{
    static int n;
    static int[] arr;
    static char[] s;
    public static void main(String[] args) throws IOException
    {
        f = new Flash();
        out = new PrintWriter(System.out);
        
        int T = 1; //ni();
        for(int tc = 1; tc <= T; tc++){
            n = ni(); arr = arr(n); sop(fn());
        }
        
        out.flush(); out.close();
    }
    
    //similar to
    //https://codeforces.com/contest/1359/problem/D
    static long fn()
    {
        long[] max = new long[n];
        Stack<Integer> st = new Stack<Integer>();
        for(int i = 0; i < n; i++) {
        	while(!st.isEmpty() && arr[st.peek()] <= arr[i]) st.pop();
        	if(st.isEmpty()) max[i] = i+1;
        	else max[i] = i-st.peek();
        	st.push(i);
        }
        while(!st.isEmpty()) st.pop();
        for(int i = n-1; i >= 0; i--) {
        	while(!st.isEmpty() && arr[i] > arr[st.peek()]) st.pop();
        	if(st.isEmpty()) max[i] *= (n-i);
        	else max[i] *= st.peek()-i;
        	
        	max[i] *= arr[i];
        	st.push(i);
        }
        
        while(!st.isEmpty()) st.pop();
        
        long[] min = new long[n];
        for(int i = 0; i < n; i++) {
        	while(!st.isEmpty() && arr[st.peek()] >= arr[i]) st.pop();
        	if(st.isEmpty()) min[i] = i+1;
        	else min[i] = i-st.peek();
        	st.push(i);
        }
        while(!st.isEmpty()) st.pop();
        for(int i = n-1; i >= 0; i--) {
        	while(!st.isEmpty() && arr[i] < arr[st.peek()]) st.pop();
        	if(st.isEmpty()) min[i] *= (n-i);
        	else min[i] *= st.peek()-i;
        	
        	min[i] *= arr[i];
        	st.push(i);
        }
        
        long MAX = 0L, MIN = 0L;
        for(long v : max) MAX += v;
        for(long v : min) MIN += v;
        return MAX-MIN;
    }
    
    static Flash f;
    static PrintWriter out;
    static final long mod = (long)1e9+7;
    static final long inf = Long.MAX_VALUE;
    static final int _inf = Integer.MAX_VALUE;
    static final int maxN = (int)5e5+5;
    static long[] fact, inv;
    
    static void sort(int[] a){
        List<Integer> A = new ArrayList<>();
        for(int i : a) A.add(i);
        Collections.sort(A);
        for(int i = 0; i < A.size(); i++) a[i] = A.get(i);
    }
    
    static void sort(long[] a){
        List<Long> A = new ArrayList<>();
        for(long i : a) A.add(i);
        Collections.sort(A);
        for(int i = 0; i < A.size(); i++) a[i] = A.get(i);
    }
    
    static void print(int[] a){
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < a.length; i++) sb.append(a[i] + " ");
        sop(sb);
    }
    
    static void print(long[] a){
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < a.length; i++) sb.append(a[i] + " ");
        sop(sb);
    }
    
    static int swap(int itself, int dummy){return itself;}
    static long swap(long itself, long dummy){return itself;}
    static void sop(Object o){out.println(o);}
    static int ni(){return f.ni();}
    static long nl(){return f.nl();}
    static double nd(){return f.nd();}
    static String next(){return f.next();}
    static String ns(){return f.ns();}
    static char[] nc(){return f.nc();}
    static int[] arr(int len){return f.arr(len);}
    static int gcd(int a, int b){if(b == 0) return a; return gcd(b, a%b);}
    static long gcd(long a, long b){if(b == 0) return a; return gcd(b, a%b);}
    static int lcm(int a, int b){return (a*b)/gcd(a, b);}
    static long lcm(long a, long b){return (a*b)/gcd(a, b);}
    
    static class Flash
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        
        String next(){
            while(!st.hasMoreTokens()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch(IOException e){
                    e.printStackTrace();
                }
            }
            
            return st.nextToken();
        }
        
        String ns(){
            String s = new String();
            try{
                s = br.readLine().trim();
            }catch(IOException e){
                e.printStackTrace();
            }
            
            return s;
        }
        
        int[] arr(int n){
            int[] a = new int[n];
            for(int i = 0; i < n; i++) a[i] = ni();
            return a;
        }
        
        char[] nc(){return ns().toCharArray();}
        int ni(){return Integer.parseInt(next());}
        long nl(){return Long.parseLong(next());}
        double nd(){return Double.parseDouble(next());}
    }
}