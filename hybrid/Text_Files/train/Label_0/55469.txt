import java.io.BufferedReader;
import java.util.Comparator;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Collection;
import java.util.List;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.math.BigInteger;
import java.util.Collections;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputReader in = new InputReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskE solver = new TaskE();
		solver.solve(1, in, out);
		out.close();
	}
}

class TaskE {
    Graph tree;
    DFSOrder dfsOrder;
    int[] parent;
    List<Event>[] events;

    public void solve(int testNumber, InputReader in, PrintWriter out) {
        int n = in.nextInt();
        int nQueries = in.nextInt();
        tree = new Graph();
        tree.initGraph(n, n-1);
        for (int i = 0; i < n-1; ++i) {
            int x = in.nextInt() - 1;
            int y = in.nextInt() - 1;
            tree.addEdge(x, y);
        }
        parent = Parent.run(tree, 0);
        dfsOrder = new DFSOrder(tree, 0, parent);
        int[] order = new int[n];
        for (int i = 0; i < n; ++i) {
            order[dfsOrder.start(i)] = i;
        }
        SegmentTree sTree = new SegmentTree(n + 1);
//        for (int i = 0; i < n; ++i) {
//            out.println(i + " " + dfsOrder.start(i) + " " + dfsOrder.end(i));
//        }
        events = new List[n+1];
        for (int i = 0; i <= n; ++i) {
            events[i] = new ArrayList<Event>();
        }
        while (nQueries-- > 0) {
            int v1 = in.nextInt() - 1;
            int v2 = in.nextInt() - 1;
            int left1 = dfsOrder.start(v1);
            int right1 = dfsOrder.end(v1);
            int left2 = dfsOrder.start(v2);
            int right2 = dfsOrder.end(v2);
            events[left1].add(new Event(1, left1, right1));
            events[left1].add(new Event(1, left2, right2));

            events[left2].add(new Event(1, left1, right1));
            events[left2].add(new Event(1, left2, right2));

            events[right1 + 1].add(new Event(0, left1, right1));
            events[right2 + 1].add(new Event(0, left1, right1));

            events[right1 + 1].add(new Event(0, left2, right2));
            events[right2 + 1].add(new Event(0, left2, right2));
        }
        int[] res = new int[n];
        for (int i = 0; i < n; ++i) {
            Collections.sort(events[i]);
            for (Event e : events[i]) {
                if (e.type == 0) {
                    sTree.delete(e.left, e.right);
                } else {
                    sTree.add(e.left, e.right);
                }
            }

            res[order[i]] = sTree.maxRight + 1 - sTree.get0();
            if (res[order[i]] > 0) --res[order[i]];
        }
        out.println(ArrayUtils.toString(res));
    }

    class Event implements Comparable<Event> {
        int type;
        int left, right;

        Event(int type, int left, int right) {
            this.type = type;
            this.left = left;
            this.right = right;
        }

        public int compareTo(Event event) {
            if (type != event.type) return type - event.type;
            if (left != event.left) return left - event.left;
            return right - event.right;
        }
    }

    class SegmentTree {
        int[] min;
        int[] cnt;
        int[] add;
        int maxTree, maxRight;

        SegmentTree(int size) {
            maxTree = 1;
            while (maxTree <= size) maxTree <<= 1;
            maxRight = maxTree - 1;
            maxTree <<= 1;
            min = new int[maxTree];
            cnt = new int[maxTree];
            add = new int[maxTree];
            initTree(1, 0, maxRight);
        }

        private void initTree(int v, int left, int right) {
            min[v] = 0;
            add[v] = 0;
            cnt[v] = right - left + 1;
            if (left != right) {
                int middle = (left + right) / 2;
                initTree(v * 2, left, middle);
                initTree(v * 2 + 1, middle + 1, right);
            }
        }

        void add(int left, int right) {
            internalUpdate(1, 0, maxRight, left, right, 1);
        }

        void delete(int left, int right) {
            internalUpdate(1, 0, maxRight, left, right, -1);
        }

        private void internalUpdate(int v, int rangeLeft, int rangeRight, int left, int right, int value) {
            if (rangeLeft == left && rangeRight == right) {
                add[v] += value;
                return;
            }
            int middle = (rangeLeft + rangeRight) / 2;
            if (left <= middle) internalUpdate(v * 2, rangeLeft, middle, left, Math.min(right, middle), value);
            if (right > middle) internalUpdate(v * 2 + 1, middle + 1, rangeRight, Math.max(middle + 1, left), right, value);
            min[v] = Math.min(min[v * 2] + add[v * 2], min[v * 2 + 1] * add[v * 2 + 1]);
            cnt[v] = 0;
            if (min[v] == min[v * 2] + add[v * 2]) {
                cnt[v] += cnt[v * 2];
            }
            if (min[v] == min[v * 2 + 1] + add[v * 2 + 1]) {
                cnt[v] += cnt[v * 2 + 1];
            }
        }

        int get0() {
            int m = min[1] + add[1];
            if (m == 0) {
                return cnt[1];
            }
            return 0;
        }
    }
}

class Graph {
    public int[] from;
    public int[] to;
    public int[] first;
    public int[] next;
    public int nVertex;
    public int nEdges;
    public int curEdge;

    public Graph() {}

    public void initGraph(int n, int m) {
        curEdge = 0;
        nVertex = n;
        nEdges = m;
        from = new int[m * 2];
        to = new int[m * 2];
        first = new int[n];
        next = new int[m * 2];
        Arrays.fill(first, -1);
    }

    public void addEdge(int a, int b) {
        next[curEdge] = first[a];
        first[a] = curEdge;
        to[curEdge] = b;
        from[curEdge] = a;
        ++curEdge;

        next[curEdge] = first[b];
        first[b] = curEdge;
        to[curEdge] = a;
        from[curEdge] = b;
        ++curEdge;
    }

}

class DFSOrder {
    int[] start;
    int[] end;

    public DFSOrder(Graph tree, int root, int[] p) {
        start = new int[tree.nVertex];
        end = new int[tree.nVertex];
        buildDfsOrder(tree, root, p);
    }

    public int start(int v) {
        return start[v];
    }

    public int end(int v) {
        return end[v];
    }

    private void buildDfsOrder(Graph tree, int root, int[] p) {
        int[] stack = new int[2 * tree.nVertex];
        int top = 0;
        stack[top++] = (root + 1);
        int time = 0;
        while (top > 0) {
            --top;
            int v = stack[top];
            if (v < 0) {
                v = (-v) - 1;
                end[v] = time-1;
            } else {
                --v;
                start[v] = time++;
                stack[top++] = -(v+1);
                for (int i = tree.first[v]; i != -1; i = tree.next[i]) {
                    if (p[v] != tree.to[i]) {
                        stack[top++] = (tree.to[i] + 1);
                    }
                }
            }
        }
    }
}

class InputReader {
    private BufferedReader reader;
    private StringTokenizer stt;

    public InputReader(InputStream stream) {
        reader = new BufferedReader(new InputStreamReader(stream));
    }

    public String nextLine() {
        try {
            return reader.readLine().trim();
        } catch (IOException e) {
            return null;
        }
    }

    public String nextString() {
        while (stt == null || !stt.hasMoreTokens()) {
            stt = new StringTokenizer(nextLine());
        }
        return stt.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(nextString());
    }

}

class Parent {
    public static int[] run(Graph tree, int root) {
        int[] parent = new int[tree.nVertex];
        int[] queue = new int[tree.nVertex];
        int front = 0, back = 0;
        queue[back++] = root;
        parent[root] = -1;
        while (front < back) {
            int v = queue[front++];
            for (int i = tree.first[v]; i != -1; i = tree.next[i]) {
                if (parent[v] != tree.to[i]) {
                    queue[back++] = tree.to[i];
                    parent[tree.to[i]] = v;
                }
            }
        }
        return parent;
    }

}

class ArrayUtils {

    public static String toString(int[] a) {
        StringBuilder result = new StringBuilder("");
        for (int x : a) result.append(x).append(' ');
        return result.substring(0, result.length()-1);
    }

}

