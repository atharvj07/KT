import javax.print.DocFlavor;
import javax.swing.text.html.HTMLDocument;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.Inet4Address;
import java.nio.charset.IllegalCharsetNameException;
import java.sql.SQLOutput;
import java.util.*;
import java.util.concurrent.locks.ReentrantReadWriteLock;


public class Main {
    static int[] parent;


    public static void main(String[] args) throws IOException{
        Reader.init(System.in);
        int t = Reader.nextInt();
        while (t-->0) {
            solve();
        }




    }


    static  int n ;
    static int m;
    static int k;
    static int[] arr;
    static int A;
    static  int B;
    static int C;
    static int min = Integer.MAX_VALUE;
    static void solve()throws IOException {
        int a = Reader.nextInt();
        int b = Reader.nextInt();
        int c = Reader.nextInt();
        int ans = Integer.MAX_VALUE;
        min = Integer.MAX_VALUE;
        for (int i = 1; i<=2*10000 ; i++){
            ans = Math.min(ans , fun(i,b,c,Math.abs(i-a)));
        }
        System.out.println(ans);
        System.out.println(A + " " + B + " "+ C);

    }

    static int fun(int a , int b , int c , int answer){
        int res = Integer.MAX_VALUE;
        for (int i = a ; i <= 2*10000 ; i+=a){
            res = Math.min(res , answer +Math.abs(i-b)+ fun1(a,i,c,answer + Math.abs(i-b)));
        }
        return res;
    }

    static int fun1(int a , int b  , int c,int answer){
        //System.out.println(a + " " + b + " " + c);
        int num = c;
        num-=c%b;
        num+=b;
        int tmp =  Math.min(Math.abs(num- c),c%b);
        if (Math.abs(num-c) > (c%b)){
            c-=c%b;
        }
        else{
            c = num;
        }
        int f = tmp + answer;
        if (f < min){
            min = f;
            A = a;
            B = b;
            C = c;
        }
        return tmp;
    }







    static int next(long[] arr, long target)
    {
        int start = 0, end = arr.length - 1;

        int ans = -1;
        while (start <= end) {
            int mid = (start + end) / 2;

            // Move to right side if target is
            // greater.
            if (arr[mid] <= target) {
                start = mid + 1;
            }

            // Move left side.
            else {
                ans = mid;
                end = mid - 1;
            }
        }
        return ans;
    }

    static int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }
    static boolean merge(int x, int y) {
        x = find(x);
        y = find(y);
        if (x==y){
            return false;
        }
        parent[x] = y;
        return true;
    }







    public static void sortbyColumn(int arr[][], int col)
    {
        // Using built-in sort function Arrays.sort
        Arrays.sort(arr, new Comparator<int[]>() {

            @Override
            // Compare values according to columns
            public int compare(final int[] entry1,
                               final int[] entry2) {

                // To sort in descending order revert
                // the '>' Operator
                if (entry1[col] > entry2[col])
                    return 1;
                else
                    return -1;
            }
        });  // End of function call sort().
    }


    static class Node{
        long a;
        int i;
        Node(long a, int i){
            this.a = a;
            this.i = i;
        }
    }

}


class Reader {
    static BufferedReader reader;
    static StringTokenizer tokenizer;

    /** call this method to initialize reader for InputStream */
    static void init(InputStream input) {
        reader = new BufferedReader(
                new InputStreamReader(input) );
        tokenizer = new StringTokenizer("");
    }
    /** get next word */
    static String next() throws IOException {
        while ( ! tokenizer.hasMoreTokens() ) {
            //TODO add check for eof if necessary
            tokenizer = new StringTokenizer(
                    reader.readLine() );
        }
        return tokenizer.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt( next() );
    }
    static long nextLong() throws IOException {
        return Long.parseLong( next() );
    }

    static double nextDouble() throws IOException {
        return Double.parseDouble( next() );
    }
}
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        // Find sizes of two subarrays to be merged
        int n1 = m - l + 1;
        int n2 = r - m;

        /* Create temp arrays */
        int L[] = new int [n1];
        int R[] = new int [n2];

        /*Copy data to temp arrays*/
        for (int i=0; i<n1; ++i)
            L[i] = arr[l + i];
        for (int j=0; j<n2; ++j)
            R[j] = arr[m + 1+ j];


        /* Merge the temp arrays */

        // Initial indexes of first and second subarrays
        int i = 0, j = 0;

        // Initial index of merged subarry array
        int k = l;
        while (i < n1 && j < n2)
        {
            if (L[i] <= R[j])
            {
                arr[k] = L[i];
                i++;
            }
            else
            {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        /* Copy remaining elements of L[] if any */
        while (i < n1)
        {
            arr[k] = L[i];
            i++;
            k++;
        }

        /* Copy remaining elements of R[] if any */
        while (j < n2)
        {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        if (l < r)
        {
            // Find the middle point
            int m = (l+r)/2;

            // Sort first and second halves
            sort(arr, l, m);
            sort(arr , m+1, r);

            // Merge the sorted halves
            merge(arr, l, m, r);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method

}

class Node implements Comparable<Node>{
    int a;
    int b;
    Node (int a , int b){
        this.a = a;
        this.b = b;
    }



    public int compareTo(Node o) {
        if ((this.a%2) == (o.a%2)){
            return (this.b - o.b);
        }
        else{
            return this.a - o.a;
        }
    }
}