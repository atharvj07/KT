import com.sun.org.apache.xpath.internal.operations.Bool;

import java.io.*;
import java.math.BigInteger;
import java.util.*;
import java.io.IOException;
import java.io.InputStream;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {

        File file = new File("in.txt");
        File fileOut = new File("out.txt");
        InputStream inputStream = null;
        OutputStream outputStream = null;
        // try {inputStream= new FileInputStream(file);} catch (FileNotFoundException ex){return;};
        // try {outputStream= new FileOutputStream(fileOut);} catch (FileNotFoundException ex){return;};
        inputStream = System.in;
        outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskB solver = new TaskB();
        solver.solve(1, in, out);
        out.close();
    }
}





class TaskB {



    Integer nodes;
    Map<Integer, Set<Integer>> edges;
    Map<Integer, Integer> color;
    Map<Integer, Integer> neigboringColors;
    Integer max;
    Integer indexOfMax;
    Set<Integer> ones;
    Set<Integer> biggerThanOnes;
    public void solve(int testNumber, InputReader in, PrintWriter out) {
        nodes = in.nextInt();
        color = new HashMap<>();
        neigboringColors = new HashMap<>();
        edges = new HashMap<>();
        ones = new HashSet<>();
        biggerThanOnes = new HashSet<>();

        for(int i=1; i<=nodes; i++){
            edges.put(i,new HashSet<>());
        }
        for(int i=1; i<nodes; i++){
            Integer source = in.nextInt();
            Integer target = in.nextInt();
            edges.get(source).add(target);
            edges.get(target).add(source);
        }
        for(int i=1; i<=nodes; i++){
            color.put(i,in.nextInt());
        }
        dfs(null, 1);

        if(biggerThanOnes.size()>1){
            out.println("NO");
            return;
        }

        if(biggerThanOnes.isEmpty() && ones.size()>2){
            out.println("NO");
            return;
        }

        Integer root = null;
        if(!biggerThanOnes.isEmpty()){
            root = biggerThanOnes.iterator().next();
        }
        else if(!ones.isEmpty()){
            root = ones.iterator().next();
            ones.remove(root);
        }
        else{
            root = 1;
        }

        for(Integer neighbor : edges.get(root)){
            ones.remove(neighbor);
        }

        if(!ones.isEmpty()){
            out.println("NO");
            return;
        }
        else{
            out.println("YES");
            out.println(root);
        }


    }

    public void dfs(Integer parent, Integer target){
        Integer differentlyColoredNeighbors = 0;
        for(Integer neighbor: edges.get(target)){
            if(!color.get(target).equals(color.get(neighbor))){
                differentlyColoredNeighbors++;
            }
        }
        neigboringColors.put(target,differentlyColoredNeighbors);
        if(differentlyColoredNeighbors>1){
            biggerThanOnes.add(target);
        }
        else if(differentlyColoredNeighbors==1){
            ones.add(target);
        }
        for(Integer neighbor : edges.get(target)){
            if(!neighbor.equals(parent)){
                dfs(target, neighbor);
            }
        }

    }



}





class InputReader {
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

    public String nextLine(){
        try {
            return reader.readLine();
        } catch (IOException e){
            throw new RuntimeException(e);
        }
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }
    public long nextLong() { return Long.parseLong(next()); }

}



class Pair<F, S> {
    public final F first;
    public final S second;




    public Pair(F first, S second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Pair)) {
            return false;
        }
        Pair<?, ?> p = (Pair<?, ?>) o;
        return Objects.equals(p.first, first) && Objects.equals(p.second, second);
    }

    @Override
    public int hashCode() {
        return (first == null ? 0 : first.hashCode()) ^ (second == null ? 0 : second.hashCode());
    }

    @Override
    public String toString() {
        return "(" + first + ", " + second + ')';
    }
}
