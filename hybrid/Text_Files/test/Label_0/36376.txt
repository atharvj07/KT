import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int N = sc.nextInt();
        Node[] nodes = new Node[N];
        for (int i = 0; i < N; i++) {
            int parent = sc.nextInt() - 1;
            String v = sc.next();
            nodes[i] = new Node(v);
            if (i > 0) nodes[parent].children.add(nodes[i]);
        }
        nodes[0].print(0);
    }

    static class Node {
        ArrayList<Node> children = new ArrayList<>();
        String v;

        public Node(String v) {
            this.v = v;
        }

        void print(int depth) {
            for (int i = 0; i < depth; i++) {
                System.out.print(".");
            }
            System.out.println(v);
            for (Node c : children) {
                c.print(depth + 1);
            }
        }
    }
}