//package com.kanari;

import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        InputReader in = new InputReader(System.in);
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));

        int n = in.nextInt(), m = in.nextInt();
        String[] map = new String[n];
        for (int i = 0; i < n; ++i)
            map[i] = in.nextToken();

        DisjointSet d = new DisjointSet(n + m);

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (map[i].charAt(j) == '#')
                    d.union(i, n + j);

        boolean answer = true;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (d.find(i) == d.find(n + j) && map[i].charAt(j) != '#')
                    answer = false;

        out.println(answer ? "Yes" : "No");
        out.close();
    }

    public static class DisjointSet {
        int[] parent;
        int n;

        DisjointSet(int n) {
            parent = new int[n];
            this.n = n;
            for (int i = 0; i < n; ++i)
                parent[i] = i;
        }

        int find(int x) {
            return parent[x] == x ? x : (parent[x] = find(parent[x]));
        }

        void union(int x, int y) {
            parent[find(x)] = find(y);
        }
    }

    static class InputReader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        InputReader(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
            tokenizer = null;
        }

        String nextToken() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return tokenizer.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(nextToken());
        }

        long nextLong() {
            return Long.parseLong(nextToken());
        }

        float nextFloat() {
            return Float.parseFloat(nextToken());
        }

        double nextDouble() {
            return Double.parseDouble(nextToken());
        }
    }
}
