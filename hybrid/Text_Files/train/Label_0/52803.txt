import org.omg.CORBA.INTERNAL;

import java.io.*;
import java.util.*;

public class Main {



    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskA solver = new TaskA();
        solver.solve(in, out);
        out.close();
    }

    private static class TaskA {


        public void solve(InputReader in, PrintWriter out) {
            int n = in.nextInt();
            List<String> list = new ArrayList<>();
            for(int i = 0;i  < n; i ++){
                list.add(in.next());
            }

            for(int i = 0; i < list.size(); i++){
                String s1 = list.get(i);
                int[]a1 = new int[26];

                for(char c : s1.toCharArray()){
                    a1[c-'a']++;
                }

                boolean isOkay = true;
                boolean isStart = false;
                boolean first = true;
                int start = 0;
                for(int b = 0; b < 26; b++){
                    if(a1[b] > 1 ){
                        isOkay = false;
                        break;
                    }
                    if(a1[b] == 1 && first){
                        start++;
                        isStart = true;
                        first = false;
                        continue;
                    }
                    if(a1[b] == 1 && isStart){
                        start++;
                    }else {
                        isStart = false;
                    }
                }
                if(start != s1.length()) isOkay = false;
                if(isOkay){
                    out.println("Yes");
                } else{
                    out.println("NO");
                }
            }
        }
    }


    private static class TaskB {
        public void solve(InputReader in, PrintWriter out) {

        }
    }

    private static class TaskC {


        public void solve(InputReader in, PrintWriter out) {

        }


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

    }

}

