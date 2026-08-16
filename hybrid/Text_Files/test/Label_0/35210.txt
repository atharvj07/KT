import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.*;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

public class First {

    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskA solver = new TaskA();
        int t;
        t = in.nextInt();
        //t = 1;
        while (t > 0) {
            solver.call(in,out);
            t--;
        }
        out.close();
    }

    static class TaskA {
        public void call(InputReader in, PrintWriter out) {
            int n, k, a=0, b=0 ,c=0 , d=0 , e =0 , f=0 ,  g= 0;
            n = in.nextInt();
            k = in.nextInt();
            
            int[] arr = new int[n];
            answer[] array = new answer[n];

            String s;
            s = in.next();

            for (int i = 0; i < n; i++) {
                if(s.charAt(i)=='W') {
                    arr[i] = 1;
                    e++;
                }
            }

            for (int i = 0; i < n; i++) {
                if(i==0){
                    if(arr[i]==1)
                        d++;
                }
                else {
                    if (arr[i]==1 && arr[i-1]==0)
                        d++;
                }

                if(arr[i]==0)
                {
                    if(a==0){
                        b = i;
                    }
                    a++;
                }

                else {
                    if(a!=0) {
                        array[b] = new answer(b, a);
                    }
                    a=0;
                }
            }

            if(a!=0){
                array[b] = new answer(b,a);

            }
            for (int i = 0; i < n; i++) {
                if(array[i]==null)
                {
                    array[i] = new answer(0, 0);
                    c++;
                }
            }


            Arrays.sort(array);


            if(e==0){
                if(k>0)
                    out.println(1+2*(k-1));
                else
                    out.println(0);

            }
            else {
                e -= d;


                for (int i = c; i < n; i++) {
                    if (k == 0)
                        break;

                    if (array[i].index != 0 && array[i].index+array[i].value!=n) {
                        if (array[i].value <= k) {
                            k -= array[i].value;

                            e += array[i].value + 1;
                            d--;


                        } else {
                            e += k;
                            k = 0;
                        }
                    } else {

                        if(array[i].index==0)
                            f = i;
                        else
                            g = i;
                    }
                }


                if (k != 0) {

                    if(array[g].value<k){
                        e+=array[g].value;
                        k-=array[g].value;
                    }
                    else {
                        e+=k;
                        k=0;
                    }


                    if (array[f].value < k) {
                        e += array[f].value;
                    } else {
                        e += k;
                    }
                }

                out.println(2 * e + d);


            }


        }

        static class answer implements Comparable<answer>{
            int index, value;

            public answer(int a, int b) {
                this.index = a;
                this.value = b;
            }


            @Override
            public int compareTo(answer o) {
                return this.value-o.value;
            }
        }


    }

    static int gcd(int a, int b)
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