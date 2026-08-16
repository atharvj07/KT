import java.io.*;
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public  class Solution {

    static  class pair implements  Comparable<pair> {
        long a ;
        int b   ;
        pair(long a, int b  ){
            this.a = a;
            this.b = b ;
        }
        @Override
        public int compareTo(pair o) {
            if (this.a == o.a)
                return (int) (this.b - o.b);
            long diff = this.a - o.a ;
            if (diff < 0)return -1 ;
            else return 1 ;
         //   return (int) (this.a - o.a);
        }
    }

    public static void main(String[] args) {

            int n = fsca.nextInt() ;
            long a[] = fsca.readLongArray(n) ;
            PriorityQueue<pair> queue = new PriorityQueue<>() ;
        for (int i = 0; i <n ; i++) {
            queue.add(new pair(a[i] , i)) ;
        }


        for (int i = 0; i <2*n && queue.size() >=2 ; i++) {
            pair tt1 = queue.poll() ;
            pair tt2 = queue.poll() ;
            if (tt1.a != tt2.a){
               queue.add(tt2) ;
               continue;
            }

            a[Math.max(tt1.b , tt2.b)] = 2*tt1.a ;
            queue.add(  new pair(2*tt1.a , Math.max(tt1.b , tt2.b))) ;
            a[Math.min(tt1.b , tt2.b)] = -1 ;
        }

       int cnt = 0 ;
        StringBuilder sb = new StringBuilder() ;

        for (int i = 0; i <n ; i++) {
            if (a[i] != -1){
                cnt++ ;
                sb.append(a[i] + " ") ;
            }
        }
        System.out.println(cnt);
        System.out.println(sb);


        fop.flush();
        fop.close();
    }


    /*-----------------------------------------------------------------------------------------------------------------------------------------------*/

    static PrintWriter fop = new PrintWriter(System.out);
    static FastScanner fsca = new FastScanner();


    static long gcd(long a, long b) {
        return (b == 0) ? a : gcd(b, a % b);
    }
    static int gcd(int a, int b) {
        return (b == 0) ? a : gcd(b, a % b);
    }

   // Arrays.sort() takes o(n^2) time to sort when array is reverse sorted
   // so always shuffle the array before sorting
    static final Random random = new Random();
    static void ruffleSort(int[] a) {
        int n = a.length;
        for (int i = 0; i < n; i++) {
            int oi = random.nextInt(n), temp = a[oi];
            a[oi] = a[i]; a[i] = temp;
        }
        Arrays.sort(a);
    }
    static void ruffleSort(long[] a) {
        int n = a.length;
        for (int i = 0; i < n; i++) {
            int oi = random.nextInt(n);
            long temp = a[oi];
            a[oi] = a[i];
            a[i] = temp;
        }
        Arrays.sort(a);
    }
    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");

        String next() {
            while (!st.hasMoreTokens())
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        // int array input
        int[] readArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = nextInt();
            return a;
        }
        // long array input
        long[] readLongArray(int n) {
            long[] a = new long[n];
            for (int i = 0; i < n; i++)
                a[i] = nextLong();
            return a;
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }

}