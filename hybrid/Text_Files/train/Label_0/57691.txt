import java.util.*;

public class file {

    private static final Scanner sc = new Scanner(System.in);
    private static String s;
    private static int[] arr;
    private static HashSet<Long> set;
    private static HashMap<Character, Integer> cmap;
    private static HashMap<Integer, Integer> map;
    private static Stack<Integer> stk;
    private static ArrayList<Integer>[] graph;
    private static boolean[] visited;



    private static void dfs(int b) {
        visited[b] = true;
        for (int x : graph[b]) {
            if (!visited[x]) dfs(x);
        }
        stk.push(b);
    }


    private static void foo(int testCase){

        int n = sc.nextInt(), m = sc.nextInt();
        //int[] arr = new int[n];
        //int max = Integer.MIN_VALUE;
        /*for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            //max = Math.max(max, arr[i]);
        }
        */
        int x, a, b;
        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            x = sc.nextInt();
            a = sc.nextInt();
            b = sc.nextInt();
            a--;
            b--;
            if (x == 1) {
                graph[a].add(b);
            }
            edges[i][0] = a;
            edges[i][1] = b;
        }
        visited = new boolean[n];
        stk = new Stack<>();
        for (int i = 0; i < n; i++) {
            if (!visited[i]) dfs(i);
        }
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) {
            pos[stk.pop()] = i;
        }
        boolean notPossible = false;
        for (int i = 0; i < n; i++) {
            for (int j : graph[i]) {
                if (pos[i] > pos[j]) notPossible = true;
            }
        }
        if (notPossible){
            System.out.println("NO");
            return;
        }
        System.out.println("YES");
        for (int i = 0; i < edges.length; i++) {

            if (pos[edges[i][0]] < pos[edges[i][1]]) {
                System.out.println((edges[i][0] + 1) + " " + (edges[i][1] + 1));
            } else {
                System.out.println((edges[i][1]+1) + " " + (edges[i][0]+1));
            }
        }

    }


    public static void main(String[] args) {

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            foo(i);
        }
    }
}