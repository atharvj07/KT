//package codeforces;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class E {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter writer = new PrintWriter(System.out);
    StringTokenizer stringTokenizer;

    String next() throws IOException {
        while (stringTokenizer == null || !stringTokenizer.hasMoreTokens()) {
            stringTokenizer = new StringTokenizer(reader.readLine());
        }
        return stringTokenizer.nextToken();
    }

    int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    long nextLong() throws IOException {
        return Long.parseLong(next());
    }

    void solve() throws IOException {
        final int n = nextInt();
        final int m = nextInt();
        List<Event> events = new ArrayList<>(2 * n);
        for(int i = 0; i < n; i++) {
            events.add(new Event(nextInt(), nextInt()));
        }
        int[] ans = new int[m];
        for(int k = 0; k < m; k++) {
            int prev = 0;
            for(int i = nextInt(); i > 0; i--) {
                int cur = nextInt();
                events.add(new Query(prev, cur, ans, k));
                prev = cur;
            }
            events.add(new Query(prev, 1000 * 1000 + 1, ans, k));
        }
        Collections.sort(events);
        SegmentTree segmentTree = new SegmentTree();
        for(Event event: events) {
            event.eventAction(segmentTree);
        }
        for(int x: ans) {
            writer.println(n - x);
        }
        writer.flush();
        writer.close();

    }

    class SegmentTree {
        int q = 1 << 20;
        int[] a = new int[2 * q];

        void add(int i, int x) {
            for(i += q; i > 0; i >>= 1) {
                a[i] += x;
            }
        }

        int sum(int l, int r) {
            int ret = 0;
            for(l += q, r += q; l < r; l >>= 1, r >>= 1) {
                if(l % 2 == 1) {
                    ret += a[l++];
                }
                if(r % 2 == 1) {
                    ret += a[--r];
                }
            }
            return ret;
        }
    }

    class Event implements Comparable<Event> {
        int l, r;
        int tier;

        Event(int l, int r) {
            this.l = l;
            this.r = r;
        }

        @Override
        public int compareTo(Event o) {
            if(r == o.r) {
                return tier - o.tier;
            }
            return r - o.r;
        }

        public void eventAction(SegmentTree segmentTree) {
            segmentTree.add(l, 1);
        }
    }

    class Query extends Event {
        int[] queryAnswers;
        int queryNumber;

        Query(int l, int r, int[] queryAnswers, int queryNumber) {
            super(l, r);
            this.queryAnswers = queryAnswers;
            this.queryNumber = queryNumber;
            tier = -1;
        }

        @Override
        public void eventAction(SegmentTree segmentTree) {
            queryAnswers[queryNumber] += segmentTree.sum(l + 1, r);
        }
    }

    public static void main(String[] args) throws IOException {
        new E().solve();
    }
}

