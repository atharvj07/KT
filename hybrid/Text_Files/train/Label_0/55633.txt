import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Task6 {
    boolean[] ancestorsAreSwapped;
    Node root;

    private static class Node {
        long sum;
        Node left;
        Node right;
    }

    public static void main(String[] args) throws IOException {
        new Task6().solve();
    }

    private void solve() throws IOException {
        BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        StringTokenizer tokenizer = new StringTokenizer(f.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        int q = Integer.parseInt(tokenizer.nextToken());
        tokenizer = new StringTokenizer(f.readLine());
        int[] ar = new int[1 << n];
        for (int i = 0; i < ar.length; i++) ar[i] = Integer.parseInt(tokenizer.nextToken());
        root = new Node();
        makeChildren(root, n, ar, 0);
        ancestorsAreSwapped = new boolean[n + 1];

        for (int q1 = 0; q1 < q; q1++) {
            tokenizer = new StringTokenizer(f.readLine());
            int query = Integer.parseInt(tokenizer.nextToken());
            if (query == 1) {
                replace(root, 0, Integer.parseInt(tokenizer.nextToken()) - 1, Integer.parseInt(tokenizer.nextToken()), n);
            } else if (query == 2) {
                int k = Integer.parseInt(tokenizer.nextToken());
                for (int i = k; i >= 0; i--) {
                    ancestorsAreSwapped[i] = !ancestorsAreSwapped[i];
                }
            } else if (query == 3) {
                int k = Integer.parseInt(tokenizer.nextToken());
                ancestorsAreSwapped[k + 1] = !ancestorsAreSwapped[k + 1];
            } else {
                int l = Integer.parseInt(tokenizer.nextToken()) - 1;
                int r = Integer.parseInt(tokenizer.nextToken()) - 1;
                out.println(getSum(root, n, l, r, 0, (1 << n) - 1));
            }
        }

        out.close();
    }

    private long getSum(Node node, int n, int from, int to, int a, int b) {
        //System.out.println(a + " " + b + " " + ancestorsAreSwapped[n]) ;
        if (from <= a && b <= to) {
            //System.out.println(a + " " + b ) ;
            return node.sum;
        }

        Node left;
        Node right;
        if (ancestorsAreSwapped[n]) {
            left = node.right;
            right = node.left;
        } else {
            left = node.left;
            right = node.right;
        }

        int mid = (a + b) / 2;
        long sum = 0;

        if (from <= mid) sum += getSum(left, n - 1, from, to, a, mid );
        if (to > mid) sum += getSum(right,n - 1, from, to, mid + 1, b);

        return sum;
    }

    private long makeChildren(Node node, int n, int[] ar, int index) {
        if (n == 0) {
            node.sum = ar[index];
            return node.sum;
        }

        node.left = new Node();
        node.sum = makeChildren(node.left, n - 1, ar, index);
        node.right = new Node();
        node.sum += makeChildren(node.right, n - 1, ar, index + (1 << (n - 1)));

        return node.sum;
    }

    private void replace(Node node, int index, int targetIndex, int num, int n) {
        if (n == 0) {
            node.sum = num;
            return;
        }

        Node left;
        Node right;
        if (ancestorsAreSwapped[n]) {
            left = node.right;
            right = node.left;
        } else {
            left = node.left;
            right = node.right;
        }

        if (targetIndex >= (index + (1 << (n - 1)))) {
            replace(right, index + (1 << (n - 1)), targetIndex, num, n - 1);
        } else {
            replace(left, index, targetIndex, num, n - 1);
        }

        node.sum = node.left.sum + node.right.sum;
    }
}
