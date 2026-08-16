import java.io.*;
import java.util.*;

class Node {
    public int p, q, r, b, parent;
    Node(int p, int q, int r, int b) {
        this.p = p;
        this.q = q;
        this.r = r;
        this.b = b;
        this.parent = -1;
    }
}

public class Main {
    Scanner sc;
    int n;
    int root;
    Node[] tree;

    long gcd(long a, long b) {
        if (a > b) {
            long tmp = a;
            a = b;
            b = tmp;
        }
        if (a == 0) return b;
        return gcd(b % a, a);
    }

    long lcm(long a, long b) {
        return a / gcd(a, b) * b;
    }

    Main() {
        sc = new Scanner(System.in);
    }

    long lightest(int index) {
        int p = tree[index].p;
        int q = tree[index].q;
        int r = tree[index].r;
        int b = tree[index].b;
        if (r == -1 && b == -1) {
            return (p + q) / gcd(p, q);
        } else if (r == -1) {
            long b_weight = lcm(lightest(b), p);
            long r_weight = b_weight * q / p;
            return r_weight + b_weight;
        } else if (b == -1) {
            long r_weight = lcm(lightest(r), q);
            long b_weight = r_weight * p / q;
            return r_weight + b_weight;
        }
        long lcm_rb = lcm(lightest(r)*p, lightest(b)*q);
        long r_weight = lcm_rb / p;
        long b_weight = lcm_rb / q;
        return r_weight + b_weight;
    }

    boolean init() {
        n = sc.nextInt();
        if (n == 0) return false;

        tree = new Node[n];
        for (int i = 0; i < n; i++) {
            int p = sc.nextInt();
            int q = sc.nextInt();
            int r = sc.nextInt();
            int b = sc.nextInt();
            long gcd_pq = gcd(p, q);
            p /= gcd_pq;
            q /= gcd_pq;
            tree[i] = new Node(p, q, r-1, b-1);  // 0-originに
        }

        // 親を探す
        for (int i = 0; i < n; i++) {
            if (tree[i].r >= 0) tree[tree[i].r].parent = i;
            if (tree[i].b >= 0) tree[tree[i].b].parent = i;
        }

        // rootを探す
        for (int i = 0; i < n; i++) 
            if (tree[i].parent == -1) {
                root = i;
                break;
            }

        return true;
    }

    void debug() {
        for (int i = 0; i < n; i++) {
            System.out.printf("%d %d %d %d %d\n", tree[i].p, tree[i].q, tree[i].r, tree[i].b, tree[i].parent);
        }
    }

    void run() {
        while (init()) {
            System.out.printf("%d\n", lightest(root));
        }
    }

    public static void main(String[] args) {
        new Main().run();
    }
}