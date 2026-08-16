import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.*;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

import static java.lang.Math.log;
import static java.lang.Math.min;

public class First {

    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskA solver = new TaskA();
        int t;
        //t = in.nextInt();
        t = 1;
        while (t > 0) {
            solver.call(in,out);
            t--;
        }
        out.close();
    }

    static class TaskA {
        public void call(InputReader in, PrintWriter out) {
            int index , a = 0;
            long t = 0 , ans = 0 , l , r;
            l = in.nextInt();
            r = in.nextInt();

            ArrayList<Long> arrayList = new ArrayList<>();
            arrayList.add(4L);
            arrayList.add(7L);

            index = 0;
            while(t<10000000000L){
                t = arrayList.get(index)*10;
                arrayList.add(t+4);
                arrayList.add(t+7);
                index++;
            }
            index = 0;
            while(arrayList.get(index)<l){
                index++;
            }
            while(arrayList.get(a)<r){
                a++;
            }

            for (int i = index; i <= a; i++) {
                if (arrayList.get(i) < r) {
                    ans += arrayList.get(i) * (arrayList.get(i) - l + 1);
                    l = arrayList.get(i) + 1;
                }
                else{
                    ans+= arrayList.get(i)*((r-l) +1);
                }
            }
            out.println(ans);

        }
    }

    static class answer implements Comparable<answer> {
        int a, b;

        public answer(int a, int b) {
            this.a = a;
            this.b = b;
        }

        @Override
        public int compareTo(answer o) {
            return this.a - o.a;
        }
    }


    static long gcd(long a, long b)
    {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

    static void sort(int[] a) {
        ArrayList<Integer> l=new ArrayList<>();
        for (int i:a) l.add(i);
        Collections.sort(l);
        for (int i=0; i<a.length; i++) a[i]=l.get(i);
    }

    static final Random random=new Random();

    static void shuffleSort(int[] arr) {
        int n=arr.length;
        for (int i=0; i<n; i++) {
            int a=random.nextInt(n), temp=arr[a];
            arr[a]=arr[i];
            arr[i]=temp;
        }
        Arrays.sort(arr);
    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }
        public long nextLong(){
            return Long.parseLong(next());
        }
        public double nextDouble() {
            return Double.parseDouble(next());
        }

    }
}