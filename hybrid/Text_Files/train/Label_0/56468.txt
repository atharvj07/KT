//package com.company;

import java.util.*;
import java.io.*;

public class Main {

    public static class Query {
        int aIdx;
        int qIdx;
        int from, to;

        public Query(int aIdx, int qIdx, int from, int to) {
            this.aIdx = aIdx;
            this.qIdx = qIdx;
            this.from = from;
            this.to = to;
        }
    }

    public static class SegmentTree {
        int[][] nodes;
        int baseSize;
        int maskFirst = (1 << 30) - 2;
        public SegmentTree(int n) {
            baseSize = 1;
            while (baseSize < n) baseSize *= 2;
            nodes = new int[baseSize * 2][100];
            for (int i = 0; i < nodes.length; i++) {
                for (int j = 0; j < 100; j++) {
                    nodes[i][j] = j;
                }
            }
        }

        public void mergeChildToParent(int child) {
            int parent = child >> 1;
            int first = child & maskFirst;
            int second = child | 1;
            for (int i = 0; i < 100; i++) {
                nodes[parent][i] = nodes[second][nodes[first][i]];
            }
        }

        public void update(Query q) {
            int nodeIdx = q.qIdx + baseSize;
            nodes[nodeIdx][q.from] = q.to;
            while (nodeIdx != 1) {
                mergeChildToParent(nodeIdx);
                nodeIdx >>= 1;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt() - 1;
        }
        int q = sc.nextInt();
        SegmentTree st = new SegmentTree(q);
        Query[] queries = new Query[2 * q];
        for (int i = 0; i < q; i++) {
            int l = sc.nextInt() - 1;
            int r = sc.nextInt();
            int x = sc.nextInt() - 1;
            int y = sc.nextInt() - 1;
            queries[i << 1] = new Query(l, i, x, y);
            queries[i << 1 | 1] = new Query(r, i, x, x);
        }
        Arrays.sort(queries, new Comparator<Query>() {
            @Override
            public int compare(Query o1, Query o2) {
                return o1.aIdx - o2.aIdx;
            }
        });
        int qIdx = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            while (qIdx < 2 * q && queries[qIdx].aIdx == i) {
                st.update(queries[qIdx++]);
            }
            sb.append(st.nodes[1][a[i]] + 1);
            sb.append(" ");
        }
        System.out.println(sb.toString());
    }

    // Java Fast IO.
    public static class Scanner {
        StringTokenizer st;
        BufferedReader br;

        public Scanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        public Scanner(FileReader s) throws FileNotFoundException {
            br = new BufferedReader(s);
        }

        public String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public String nextLine() throws IOException {
            return br.readLine();
        }

        public double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        public boolean ready() throws IOException {
            return br.ready();
        }
    }
}

			 		 	 	  	 	 		 	 	    			