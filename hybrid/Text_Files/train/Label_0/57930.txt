
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.StringTokenizer;


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Gerasimov
 */
public class Main {

    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader inp = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(inp.readLine());
        int n = Integer.parseInt(st.nextToken());
        HashMap<Long, Long> h1 = new HashMap<>();
        HashMap<Long, Long> h2 = new HashMap<>();
        HashMap<String, Long> h3 = new HashMap<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(inp.readLine());
            long[] m = new long[2];
            m[0] = Long.parseLong(st.nextToken());
            m[1] = Long.parseLong(st.nextToken());
            if (!h1.containsKey(m[0])) {
                h1.put(m[0], 0l);
            }
            if (!h2.containsKey(m[1])) {
                h2.put(m[1], 0l);
            }
            if (!h3.containsKey(m[0]+"_"+m[1])) {
                h3.put(m[0]+"_"+m[1], 0l);
            }
            h1.replace(m[0], h1.get(m[0]) + 1);
            h2.replace(m[1], h2.get(m[1]) + 1);
            h3.replace(m[0]+"_"+m[1], h3.get(m[0]+"_"+m[1]) + 1);

        }
        long res = 0l;
        res = h1.entrySet().stream().map((entry) -> entry.getValue() * (entry.getValue() - 1) / 2).reduce(res, (accumulator, _item) -> accumulator + _item);
        res = h2.entrySet().stream().map((entry) -> entry.getValue() * (entry.getValue() - 1) / 2).reduce(res, (accumulator, _item) -> accumulator + _item);
        res = h3.entrySet().stream().map((entry) -> entry.getValue() * (entry.getValue() - 1) / 2).reduce(res, (accumulator, _item) -> accumulator - _item);
        out.print(res);
        out.close();
    }

}
