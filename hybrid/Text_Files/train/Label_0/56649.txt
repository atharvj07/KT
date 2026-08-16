import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), k = sc.nextInt();
        UnionFind uf = new UnionFind(n);
        for (int i = 1; i <= k; i++) {
            //uf.debug();

            int num = sc.nextInt();
            if (num == 1) {
                int a = sc.nextInt() - 1;
                int b = sc.nextInt() - 1;
                int ba = uf.get_bukatu(a);
                int bb = uf.get_bukatu(b);
                if(ba == -1) {
                    uf.unite(a, b);
                    uf.setBukatu(a, bb);
                } else if(bb == -1) {
                    uf.unite(a, b);
                    uf.setBukatu(b, ba);
                } else {
                    if(ba == bb) {
                        uf.unite(a, b);
                    } else {
                        System.out.println(i);
                        return;
                    }
                }
            } else {
                int c = sc.nextInt() - 1;
                int x = sc.nextInt() - 1;
                int b = uf.get_bukatu(c);
                if(b == -1) {
                    uf.setBukatu(c, x);
                } else {
                    if(b != x) {
                        System.out.println(i);
                        return;
                    }
                }
            }
        }
        System.out.println(0);
    }
}

class UnionFind {
    int[] data;
    int[] bukatu;

    public UnionFind(int size) {
        data = new int[size];
        Arrays.fill(data, -1);
        bukatu = new int[size];
        Arrays.fill(bukatu,-1);
    }

    public boolean unite(int x, int y) {
        x = find(x);
        y = find(y);
        if(x == y) return false;
        if(data[x] > data[y]) {
            int temp = x;
            x = y;
            y = temp;
        }
        data[x] += data[y];
        data[y] = x;
        return true;
    }

    public int find(int k) {
        if(data[k] < 0) return k;
        return (data[k] = find(data[k]));
    }

    public int size(int k) {
        return -data[find(k)];
    }

    public void setBukatu(int c, int number) {
        bukatu[find(c)] = number;
    }

    public int get_bukatu(int x) {
        return bukatu[find(x)];
    }

    public void debug() {
        System.err.println(Arrays.toString(data));
        System.err.println(Arrays.toString(bukatu));
    }
}
