/**
 * ******* Created  on 19/12/19 2:44 AM*******
 */

import java.io.*;
import java.util.*;

public class D359_SparceTree implements Runnable {

    private static final int MAX = (int) (1E5 + 5);
    private static final int MOD = (int) (1E9 + 7);
    private static final long Inf = (long) (1E14 + 10);
    class Sparse{
        int n ;
        int[][] table ;
        int lgn ;
        Combiner ho;
        Sparse(int[] a, Combiner ho){
            this.ho = ho;
            build(a);
        }

        private void build(int[] a) {
            int te = a.length;
            n = a.length;
            while(te > 0){
                lgn++;
                te >>=1;
            }
            table =new int[lgn+1][n];
            for(int i =0;i<n;i++)
                table[0][i] = a[i];

            for(int j =1;j<=lgn;j++){
                for(int i =0;i +(1<<(j-1) )< n ; i++){
                    table[j] [i] = ho.combine(table[j-1][i] , table[j-1] [i+(1<<(j-1))] );
                }
            }
        }
        int query(int l, int r){
            int len = r- l +1;
            int te = len;
            int k =0;
            while(te >0){
                te >>=1;
                k++;
            }
            k--;
            return ho.combine(table[k][l], table[k][r+1- (1<<k)]);
        }
    }
    private void solve() throws IOException {
        int n = reader.nextInt();
        int[] a = reader.readIntArray(n);
        Sparse gcd = new Sparse(a, new Combiner() {
            @Override
            public int combine(int a, int b) {
                return gcd(a,b);
            }
        });
        int max = 0;
        TreeSet<Integer> res = new TreeSet<>();
        for(int i =0;i<n;i++){
            int l = i, r= n-1;
            int max1 =i+1, max2 =i;
            int mid1 = (l+r+1)/2;
            while(l < r){

                if(gcd.query(i, mid1) !=a[i])
                    r = mid1-1;
                else{
                    l = mid1;
                }
                mid1 =(l + r+1)/2;

            }
            l = 0; r = i;
            int mid2= (l+r)/2;
            while(l < r){

                if(gcd.query(mid2,i)!=a[i])
                    l =mid2+1;
                else{
                    r= mid2;
                }
                mid2 = (l+r)/2;
            }

            if(mid1-mid2> max){
                res.clear();
                max = mid1 - mid2;
            }
            if(mid1 - mid2 == max){
                res.add(mid2+1);
            }
        }
        writer.println(res.size() +" "+max);
        for(int an : res)
            writer.print(an+" ");
    }
    public int gcd(int a , int b){
        if( b  == 0)
            return a;
        return gcd(b, a%b);
    }
    public static void main(String[] args) throws IOException {
        try (Input reader = new StandardInput(); PrintWriter writer = new PrintWriter(System.out)) {
            new D359_SparceTree().run();
        }
    }
    interface Combiner{
        public int combine(int a,  int b);
    }
    StandardInput reader;
    PrintWriter writer;

    @Override
    public void run() {
        try {
            reader = new StandardInput();
            writer = new PrintWriter(System.out);
            solve();
            reader.close();
            writer.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    interface Input extends Closeable {
        String next() throws IOException;

        default int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        default long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        default double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        default int[] readIntArray() throws IOException {
            return readIntArray(nextInt());
        }

        default int[] readIntArray(int size) throws IOException {
            int[] array = new int[size];
            for (int i = 0; i < array.length; i++) {
                array[i] = nextInt();
            }
            return array;
        }

        default long[] readLongArray(int size) throws IOException {
            long[] array = new long[size];
            for (int i = 0; i < array.length; i++) {
                array[i] = nextLong();
            }
            return array;
        }
    }

    private static class StandardInput implements Input {
        private final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        private StringTokenizer stringTokenizer;

        @Override
        public void close() throws IOException {
            reader.close();
        }

        @Override
        public String next() throws IOException {
            if (stringTokenizer == null || !stringTokenizer.hasMoreTokens()) {
                stringTokenizer = new StringTokenizer(reader.readLine());
            }
            return stringTokenizer.nextToken();
        }
    }
}
