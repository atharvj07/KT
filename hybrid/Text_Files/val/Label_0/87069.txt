import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.Reader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputStreamReader in = new InputStreamReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskC solver = new TaskC();
		solver.solve(1, in, out);
		out.close();
	}
}

class TaskC {
    Long[] numbers;
    int[] primeSum;
    int n;

    boolean[] used;

    long MAX_VAL = (long) 1e15;
    long MAX_DIV = (long) ((long) 2 * 1e15);

    int[] parents;

    public void solve(int testNumber, InputStreamReader inSt, PrintWriter out) {
        InputReader in = new InputReader(inSt);
        n = in.nextInt();

        numbers = new Long[n];
        primeSum = new int[n];
        used = new boolean[n];

        for (int i = 0; i < n; i++) {
            numbers[i] = in.nextLong();
        }


        Comparator<Long> cmp = new Comparator<Long>() {
            @Override
            public int compare(Long o1, Long o2) {
                return -(o1.compareTo(o2));
            }
        };
        Arrays.sort(numbers, cmp);
        for (int i = 0; i < numbers.length; i++) {
            primeSum[i] = getPrimeSum(numbers[i]);
        }

        if (n == 1) {
            if (primeSum[0] == 1) {
                out.println(1);
            } else {
                out.println(primeSum[0] + 1);
            }
            return;
        }

        parents = new int[n];
        parents[0] = -1;
        int min = getAnswer(0, false);

        parents[0] = 0;
        int min2 = getAnswer(1, true);

        min = Math.min(min, min2);

        out.println(min);

    }

    long getChildProduct(int parVertex, int endVertex) {
        long product = 1;
        for (int i = parVertex + 1; i < endVertex; i++) {
            if (parents[i] == parVertex) {
                product = mult(product, numbers[i]);
            }

        }
        return product;
    }

    int calculateAnswer(boolean isFirstRoot) {
        int additionalLeafs = 0;
        for (int i = 0; i < n; i++) {
            int curSum = primeSum[i];
            if (curSum == 1) {
                continue;
            }
            for (int j = i + 1; j < n; j++) {
                if (parents[j] == i) {
                    curSum -= primeSum[j];
                }
            }
            additionalLeafs += curSum;
        }


        int result = n;
        result += additionalLeafs;
        if (!isFirstRoot) {
            result++;
        }

        return result;

    }

    int getAnswer(int curVertex, boolean isFirstRoot) {
        if (curVertex == n) {
            return calculateAnswer(isFirstRoot);
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < curVertex; i++) {
            long product = getChildProduct(i, curVertex);
            product = mult(product, numbers[curVertex]);
            if (isDiv(numbers[i], product)) {
                parents[curVertex] = i;
                min = Math.min(min, getAnswer(curVertex + 1, isFirstRoot));
            }
        }
        if (!isFirstRoot) {
            parents[curVertex] = -1;
            min = Math.min(min, getAnswer(curVertex + 1, isFirstRoot));
        }

        return min;
    }


    boolean isDiv(long a, long b) {
        if (a == MAX_DIV) {
            return true;
        }
        return a % b == 0;
    }


    long mult(long a, long b) {
        if (MAX_VAL / b < a) {
            return MAX_VAL;
        }

        return a * b;
    }

    private int getPrimeSum(long num) {
        int start = 2;
        int result = 0;
        while (start <= Math.sqrt(num)) {
            while (num % start == 0) {
                result++;
                num /= start;
            }
            start++;
        }

        if (num > 1) {
            result++;
        }
        return result;
    }

    class InputReader {
        public BufferedReader reader;
        private String[] currentArray;
        int curPointer;

        public InputReader(InputStreamReader inputStreamReader) {
            reader = new BufferedReader(inputStreamReader);
        }

        public String next() {
            try {
                currentArray = null;
                return reader.readLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        public void nextChars(char[] t) {
            try {
                currentArray = null;
                reader.read(t);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        public char nextChar() {
            try {
                currentArray = null;
                return (char) reader.read();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        public int nextInt() {
            if ((currentArray == null) || (curPointer >= currentArray.length)) {
                try {
                    currentArray = reader.readLine().split(" ");
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
                curPointer = 0;
            }
            return Integer.parseInt(currentArray[curPointer++]);
        }

        public long nextLong() {
            if ((currentArray == null) || (curPointer >= currentArray.length)) {
                try {
                    currentArray = reader.readLine().split(" ");
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
                curPointer = 0;
            }
            return Long.parseLong(currentArray[curPointer++]);
        }

    }
}

