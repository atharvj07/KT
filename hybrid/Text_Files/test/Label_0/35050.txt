import java.util.*;

public class Main {
    public static List<Integer> link[];
    public static int[] d;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        link = new ArrayList[N];
        for (int i=0; i<N; i++) {
            link[i] = new ArrayList<Integer>();
        }
        
        for (int i=0; i<N-1; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            link[a-1].add(b-1);
            link[b-1].add(a-1);
        }
        d = new int[N];
        for (int i=0; i<N; i++) d[i] = -1;
        dfs(0,0);
        // for (int i=0; i<N; i++) {
        //     System.out.println(d[i]);
        // }
        int maxD = -1;
        int maxI = -1;
        for(int i=0; i<N; i++) {
            if(maxD < d[i]) {
                maxD = d[i];
                maxI = i;
            }
        }
        for (int i=0; i<N; i++) d[i] = -1;
        dfs(maxI,0);
        for(int i=0; i<N; i++) {
            if(maxD < d[i]) {
                maxD = d[i];
            }
        }
        int longest = maxD+1;
        if(longest%3 == 2) {
            System.out.println("Second");
        } else {
            System.out.println("First");
        }
 


    }
    public static void dfs(int s, int value){
        d[s] = value;
        for (Integer w : link[s]) {
            if(d[w] != -1) continue;
            dfs(w, value+1);
        }

    }

}