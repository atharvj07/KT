

import java.io.*;
import java.util.*;


public class G {

    static class Pair<U extends Comparable<U>, V extends Comparable<V>>
            implements Comparable<Pair<U,V>>{

        final public U a;
        final public V b;

        private Pair(U a, V b) {
            this.a = a;
            this.b = b;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (o == null || getClass() != o.getClass())
                return false;

            Pair<?, ?> pair = (Pair<?, ?>) o;
            if (!a.equals(pair.a))
                return false;
            return b.equals(pair.b);
        }

        @Override
        public int hashCode() {
            return 31 * a.hashCode() + b.hashCode();
        }

        @Override
        public String toString() {
            return "(" + a + ", " + b + ")";
        }

        @Override
        public int compareTo(Pair<U, V> o) {
            if(this.a.equals(o.a)){
                return getV().compareTo(o.getV());
            }
            return getU().compareTo(o.getU());
        }
        private U getU() {
            return a;
        }
        private V getV() {
            return b;
        }
        static void print(Pair[] pairs){
            for(int i=0;i<pairs.length;i++){
                System.out.print(pairs[i]+" ");
            }
            System.out.println();
        }
        static void print(Pair[][] pairs){

            for(int i=0;i<pairs.length;i++){
                for(int j=0;j<pairs[0].length;j++) {
                    System.out.print(pairs[i][j] + " ");
                }
                System.out.println();
            }
        }
    }


    static BufferedReader inp = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));


    public static void main(String[] args) throws IOException {

        int size = Integer.parseInt(inp.readLine());
        int[] given = new int[size];
        int[] capacity = new int[size];

        String[] s1 = inp.readLine().split(" ");
        String[] s2 = inp.readLine().split(" ");

        int sum = 0;

        for(int i=0;i<size;i++){
            given[i] = Integer.parseInt(s1[i]);
            capacity[i] = Integer.parseInt(s2[i]);
            sum+= given[i];
        }

        Pair<Integer,Integer>[][] dp = new Pair[size+1][sum+1];
        for(int i=0;i<=size;i++) {
            Arrays.fill(dp[i], new Pair<>(100000,-1));
        }
        //Pair.print(dp);

        for(int i=1;i<=size;i++){
            int a = capacity[i-1];
            for(int j=1;j<=sum;j++){
                if(j<=a){
                    if(dp[i-1][j].a>1){
                        dp[i][j] = new Pair<>(1, given[i-1]);
                    }
                    else{
                        dp[i][j]= new Pair<>(1, Math.max(given[i-1],dp[i-1][j].b));
                    }

                }
                else {
                    if(dp[i-1][j-a].a+1>dp[i-1][j].a){
                        dp[i][j] = dp[i-1][j];
                    }
                    else if(dp[i-1][j-a].a+1==dp[i-1][j].a){
                        dp[i][j] = new Pair<>(dp[i-1][j-a].a+1,Math.max(given[i-1]+dp[i-1][j-a].b,dp[i-1][j].b));
                    }
                    else{
                        dp[i][j] = new Pair<>(dp[i-1][j-a].a+1,given[i-1]+dp[i-1][j-a].b);
                    }
                }
            }
        }

        //Pair.print(dp);

        int a = dp[size][sum].a;
        int b = sum-dp[size][sum].b;
        out.write(a+" "+b);


        out.flush();


    }
    static void print(int[] array){
        for(int j=0;j<array.length;j++){
            System.out.print(array[j]+" ");
        }
        System.out.println();
    }
    static void print(int[][] array){
        for(int i=0;i< array.length;i++) {
            for (int j = 0; j < array[0].length; j++) {
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
    }
    static void print(boolean[] array){
        for(int j=0;j<array.length;j++){
            System.out.print(array[j]+" ");
        }
        System.out.println();
    }
    static void print(boolean[][] array){
        for(int i=0;i< array.length;i++) {
            for (int j = 0; j < array[0].length; j++) {
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
    }
    static void print(long[] array){
        for(int j=0;j<array.length;j++){
            System.out.print(array[j]+" ");
        }
        System.out.println();
    }
    static void print(long[][] array){
        for(int i=0;i< array.length;i++) {
            for (int j = 0; j < array[0].length; j++) {
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
    }
    static void print(String[] array){
        for(int j=0;j<array.length;j++){
            System.out.print(array[j]+" ");
        }
        System.out.println();
    }
    static void print(String[][] array){
        for(int i=0;i< array.length;i++) {
            for (int j = 0; j < array[0].length; j++) {
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
    }
}

