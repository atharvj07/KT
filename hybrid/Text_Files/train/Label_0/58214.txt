import java.io.IOException;
import java.io.FilterInputStream;
import java.util.Iterator;
import java.io.OutputStream;
import java.util.ArrayDeque;
import java.io.PrintWriter;
import java.io.BufferedInputStream;
import java.util.HashSet;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 * @author Zyflair Griffane
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputUtil in = new InputUtil(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		Task solver = new Task();
		solver.solve(1, in, out);
		out.close();
	}
}

class Task {
    public void solve(int testNumber, InputUtil in, PrintWriter out) {
        int n = in.nextInt() + 1;
        int m = in.nextInt();
        int k = in.nextInt();

        IntDeque[] adj = IntDeque.IntDeques(n);
        HashSet<Long> forbidden = new HashSet<>();

        adj[0].add(1);
        for (int i = 0; i < m; i++) {
            int u = in.nextInt();
            int v = in.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }
        for (int i = 0; i < k; i++) {
            forbidden.add(hash(in.nextInt(), in.nextInt(), in.nextInt()));
        }

        int[][] dp = new int[n][n];
        int[][] prev = new int[n][n];

        int u = 0, v = 0;
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[] {0, 1});
        while (!q.isEmpty()) {
            int[] p = q.poll();
            u = p[0];
            v = p[1];
            if (v == n - 1) {
                break;
            }
            for (int w: adj[v]) {
                if (dp[v][w] == 0 && !forbidden.contains(hash(u, v, w))) {
                    dp[v][w] = dp[u][v] + 1;
                    prev[v][w] = u;
                    q.add(new int[] {v, w});
                }
            }
        }

        if (v != n - 1) {
            out.println("-1");
            return;
        }

        IntDeque path = new IntDeque();
        path.push(n - 1);
        while (u != 0) {
            path.push(u);
            int t = prev[u][v];
            v = u;
            u = t;
        }

        out.println(path.size() - 1);
        out.println(path);
    }
    public long hash(long i, long j, long k) {
        return (i << 26) + (j << 13) + k;
    }
}

class InputUtil {

    JoltyScanner in;

    public InputUtil(InputStream istream) {
        in = new JoltyScanner(istream);
    }

    public String next() {
        return in.next();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

}

class IntDeque implements Iterable<Integer> {

    private int capacity;
    private int size = 0;
    private int front = 0;
    private int back = 0;
    private int[] deque;
    public IntDeque() {
        this(16);
    }
    public IntDeque(int capacity) {
        this.capacity = capacity;
        deque = new int[capacity];
    }
    public static IntDeque[] IntDeques(int length) {
        IntDeque[] arr = new IntDeque[length];
        for (int i = 0; i < length; i++) {
            arr[i] = new IntDeque();
        }
        return arr;
    }
    public <T extends Iterable<Integer>>IntDeque(T intList) {
        this(16);
        addAll(intList);
    }
    public void add(int x) {
        addLast(x);
    }
    public <T extends Iterable<Integer>>void addAll(T intList) {
        for (int i: intList) {
            addLast(i);
        }
    }
    public void addLast(int x) {
        ensureCapacity();
        size++;
        deque[back++] = x;
        if (back == capacity) {
            back = 0;
        }
    }
    public void addFirst(int x) {
        ensureCapacity();
        size++;
        if (front == 0) {
            front = capacity;
        }
        deque[--front] = x;
    }

    public void ensureCapacity() {
        if (size < capacity) {
            return;
        }
        int[] newDeque = new int[capacity << 1];
        for (int i = 0, j = front; i < size; i++, j++) {
            if (j == capacity) {
                j = 0;
            }
            newDeque[i] = deque[j];
        }
        deque = newDeque;
        capacity <<= 1;
        front = 0;
        back = size;
    }

    public Iterator<Integer> iterator() {
        return new Iterator<Integer>() {
            int done = 0;
            int curr = front;
            public boolean hasNext() {
                return done < size;
            }
            public Integer next() {
                Integer res = deque[curr++];
                if (curr == capacity) {
                    curr = 0;
                }
                done++;
                return res;
            }
            public void remove() {
                throw new UnsupportedOperationException();
            }
        };
    }

    public void push(int x) {
        addFirst(x);
    }
    public int size() {
        return size;
    }

    public String toString() {
        if (size == 0) {
            return "";
        }
        StringBuilder res = new StringBuilder();
        for (int i: this) {
            res.append(i);
            res.append(" ");
        }
        res.setLength(res.length() - 1);
        return res.toString();
    }
}

class JoltyScanner {
    public static final int BUFFER_SIZE = 1 << 16;
	public static final char NULL_CHAR = (char) -1;

	StringBuilder str = new StringBuilder();
	byte[] buffer = new byte[BUFFER_SIZE];
	boolean EOF_FLAG = false;
	int bufferIdx = 0, size = 0;
	char c = NULL_CHAR;
	BufferedInputStream in;

	public JoltyScanner(InputStream in) {
		this.in = new BufferedInputStream(in, BUFFER_SIZE);
	}

    public String next() {
		checkEOF();
		if (c == NULL_CHAR) {
			c = nextChar();
		}
		while (Character.isWhitespace(c)) {
			c = nextChar();
			checkEOF();
		}
		str.setLength(0);
		for (; !EOF_FLAG && !Character.isWhitespace(c); c = nextChar()) {
			str.append(c);
		}
		return str.toString();
	}

    public char nextChar() {
		if (EOF_FLAG) {
			return NULL_CHAR;
		}
		while (bufferIdx == size) {
			try {
				size = in.read(buffer);
				if (size == -1) {
					throw new Exception();
				}
			} catch (Exception e) {
				EOF_FLAG = true;
				return NULL_CHAR;
			}
			if (size == -1) {
				size = BUFFER_SIZE;
			}
			bufferIdx = 0;
		}
		return (char) buffer[bufferIdx++];
	}

    public void checkEOF() {
		if (EOF_FLAG) {
			throw new EndOfFileException();
		}
	}

	public class EndOfFileException extends RuntimeException {
	}
}

