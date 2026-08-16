/**
 * @author vivek
 * programming is thinking, not typing
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static void solveTC(int __) {

        /* For Google */
//		ans.append("Case #").append(__).append(": ");

        //code start

        int n = scn.nextInt();

        long[] array=scn.nextLongArray(n);

        int[] bit=new int[21];
        for(long ele:array){
            addToBit(ele,bit);
        }

        long ans=0;

        for (int i = 0; i < n; i++) {
            long num=genNum(bit);
            ans+=num*num;
        }

        print(ans);

        //code end

        print("\n");
    }

    private static long genNum(int[] bit) {
        long ans=0;
        for (int i = 0; i < 21; i++) {
            if (bit[i]>0){
                ans += (1 << i);
                bit[i]--;
            }
        }
        return ans;
    }

    private static void addToBit(long ele, int[] bit) {
        int i=0;
        while (ele>0){
            bit[i]+=ele&1;
            ele>>=1;
            i++;
        }
    }

    /**
     * Don't copy other's templates, make your own <br>
     * It would be much more beneficial
     */

    public static void main(String[] args) {

//        int limit=               ;
//        sieve(limit);

        scn = new Scanner();
        ans = new StringBuilder();
//        int t = scn.nextInt();
        int t = 1;
        for (int i = 1; i <= t; i++) {
            solveTC(i);
        }
        System.out.print(ans);
    }
    //Stuff for prime start
    /**
     * List containing prime numbers <br>
     * <b>i<sup>th</sup></b> position contains <b>i<sup>th</sup></b> prime number <br>
     * 0th index is <b>null</b>
     */
    private static ArrayList<Integer> listOfPrimes;

    /**
     * query <b>i<sup>th</sup></b> element to get if its prime of not
     */
    private static boolean[] isPrime;

    /**
     * Performs Sieve of Erathosnesis and initialise isPrime array and listOfPrimes list
     *
     * @param limit the number till which sieve is to be performed
     */
    private static void sieve(int limit) {
        listOfPrimes = new ArrayList<>();
        listOfPrimes.add(null);
        boolean[] array = new boolean[limit + 1];

        Arrays.fill(array, true);
        array[0] = false;
        array[1] = false;

        for (int i = 2; i <= limit; i++) {
            if (array[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    array[j] = false;
                }
            }
        }
        isPrime = array;
        for (int i = 0; i <= limit; i++) {
            if (array[i]) {
                listOfPrimes.add(i);
            }
        }
    }
    //stuff for prime end

    /**
     * Calculates the Least Common Multiple of two numbers
     *
     * @param a First number
     * @param b Second Number
     * @return Least Common Multiple of <b>a</b> and <b>b</b>
     */
    private static long lcm(long a, long b) {
        return a * b / gcd(a, b);
    }

    /**
     * Calculates the Greatest Common Divisor of two numbers
     *
     * @param a First number
     * @param b Second Number
     * @return Greatest Common Divisor of <b>a</b> and <b>b</b>
     */
    private static long gcd(long a, long b) {
        return (b == 0) ? a : gcd(b, a % b);
    }

    static void print(Object obj) {
        ans.append(obj.toString());
    }


    static Scanner scn;
    static StringBuilder ans;

    //Fast Scanner
    static class Scanner {
        BufferedReader br;
        StringTokenizer st;

        public Scanner() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }

        int[] nextIntArray(int n) {
            int[] array = new int[n];
            for (int i = 0; i < n; i++) {
                array[i] = nextInt();
            }
            return array;
        }

        Integer[] nextIntegerArray(int n) {
            Integer[] array = new Integer[n];
            for (int i = 0; i < n; i++) {
                array[i] = nextInt();
            }
            return array;
        }

        long[] nextLongArray(int n) {
            long[] array = new long[n];
            for (int i = 0; i < n; i++) {
                array[i] = nextLong();
            }
            return array;
        }

        String[] nextStringArray() {
            return nextLine().split(" ");
        }

        String[] nextStringArray(int n) {
            String[] array = new String[n];
            for (int i = 0; i < n; i++) {
                array[i] = next();
            }
            return array;
        }
    }
}